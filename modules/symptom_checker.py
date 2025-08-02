import streamlit as st
import google.generativeai as genai

def display():
    st.header("🩺 Symptom Checker")
    st.markdown("Describe the symptoms, and our AI assistant will provide friendly guidance with suggestions and recommendations. **This is not a substitute for professional medical advice.**")
    
    # Configuration for Gemini API
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "AIzaSyDf5NK3kYz1OITVovJmn4awerHwiMHpK1M")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Could not configure API: {str(e)}")
        model = None

    # Age selection for better recommendations
    age_group = st.selectbox(
        "Select age group:",
        ["Newborn (0-1 month)", "Infant (1-12 months)", "Toddler (1-3 years)", 
         "Child (3-12 years)", "Teenager (12-18 years)", "Adult (18+ years)"]
    )

    symptoms = st.text_area(
        "Describe the symptoms in detail (e.g., 'My child has a fever of 101°F, cough, and runny nose for 2 days'):", 
        height=150,
        placeholder="Include details like duration, severity, any patterns you've noticed..."
    )

    if st.button("🔍 Analyze Symptoms", type="primary"):
        if not symptoms:
            st.warning("Please enter symptoms to analyze.")
        else:
            if model:
                try:
                    prompt = f"""
                    You are an experienced pediatric and family health AI assistant. A {age_group.lower()} has the following symptoms: '{symptoms}'.
                    
                    Please provide a comprehensive response in the following format:
                    
                    **POSSIBLE CONDITIONS:**
                    List 2-3 most likely conditions based on symptoms (emphasize these are possibilities, not diagnoses)
                    
                    **IMMEDIATE CARE SUGGESTIONS:**
                    - Provide 3-4 immediate home care tips
                    - Include comfort measures and symptom relief
                    
                    **OVER-THE-COUNTER OPTIONS:**
                    - Suggest appropriate OTC medications with proper dosing considerations for the age group
                    - Include natural remedies where applicable
                    - Always mention to check with pharmacist or doctor before giving any medication
                    
                    **WARNING SIGNS - CONTACT DOCTOR IMMEDIATELY IF:**
                    - List 4-5 red flag symptoms that require immediate medical attention
                    - Be specific about when to call emergency services
                    
                    **WHEN TO SEE A DOCTOR:**
                    - Provide clear timeline (e.g., "if symptoms persist beyond X days")
                    - Mention worsening symptoms to watch for
                    
                    **PREVENTION TIPS:**
                    - Suggest ways to prevent similar issues in the future
                    
                    Keep the tone caring, informative but not alarming. Emphasize that this is guidance only and professional medical advice should always be sought for serious concerns.
                    """
                    
                    with st.spinner("🔍 Analyzing symptoms and generating recommendations..."):
                        response = model.generate_content(prompt)
                        
                        st.success("✅ Analysis Complete!")
                        
                        # Display the response in a nice format
                        st.markdown("---")
                        st.markdown("### 📋 Symptom Analysis & Recommendations")
                        st.markdown(response.text)
                        
                        # Emergency contact reminder
                        st.markdown("---")
                        st.error("🚨 **EMERGENCY:** If this is a medical emergency, call emergency services immediately!")
                        
                        # Disclaimer
                        st.info("ℹ️ **Disclaimer:** This analysis is for informational purposes only and should not replace professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.")

                except Exception as e:
                    st.error(f"Sorry, I encountered an error while analyzing the symptoms: {str(e)}")
                    st.info("Please try again or consult with a healthcare professional directly.")
            else:
                st.error("API not configured. Please check the API configuration.")
    
    # Additional resources section
    st.markdown("---")
    st.markdown("### 📞 Emergency Contacts")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Emergency Services:** 911
        **Poison Control:** 1-800-222-1222
        """)
    
    with col2:
        st.markdown("""
        **Pediatric Nurse Line:** Contact your healthcare provider
        **Telehealth Options:** Available through most insurance providers
        """)
    
    # Common symptoms quick reference
    with st.expander("📚 Quick Reference - Common Symptoms"):
        st.markdown("""
        **Fever Management:**
        - Under 3 months: Contact doctor immediately for any fever
        - 3-36 months: Contact doctor if fever >102.2°F (39°C)
        - Over 36 months: Contact doctor if fever >104°F (40°C) or persists >3 days
        
        **Hydration Signs:**
        - Good: Regular urination, moist mouth, tears when crying
        - Concerning: Dry mouth, no tears, decreased urination
        
        **Breathing Concerns:**
        - Normal: Easy, quiet breathing
        - Concerning: Rapid breathing, wheezing, difficulty speaking
        """)