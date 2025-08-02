import streamlit as st
import google.generativeai as genai

def display():
    st.header("💚 Mental Health Support")
    st.markdown("Your mental well-being is important. Share how you're feeling, and we'll provide personalized support and guidance. Remember, seeking help is a sign of strength.")
    
    # Configuration for Gemini API
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "AIzaSyDf5NK3kYz1OITVovJmn4awerHwiMHpK1M")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Could not configure API: {str(e)}")
        model = None

    # User context for better personalization
    col1, col2 = st.columns(2)
    
    with col1:
        user_role = st.selectbox(
            "I am a:",
            ["New mother", "Expecting mother", "Mother with young children", 
             "Mother with teenagers", "Partner/Support person", "Other"]
        )
    
    with col2:
        concern_type = st.selectbox(
            "Primary concern:",
            ["General stress/anxiety", "Postpartum feelings", "Sleep deprivation", 
             "Relationship concerns", "Work-life balance", "Parenting challenges", 
             "Depression/sadness", "Other"]
        )

    user_feeling = st.text_area(
        "Please share what you're experiencing. The more details you provide, the better I can support you:",
        height=150,
        placeholder="e.g., 'I feel overwhelmed since my baby was born. I'm not sleeping well and feel like I'm not doing anything right as a mother...'"
    )

    if st.button("💬 Get Personalized Support", type="primary"):
        if not user_feeling:
            st.warning("Please share how you're feeling so I can provide relevant support.")
        else:
            if model:
                try:
                    prompt = f"""
                    You are a compassionate, trained mental health AI assistant specializing in maternal and family mental health. 
                    
                    User context:
                    - Role: {user_role}
                    - Primary concern: {concern_type}
                    - What they shared: '{user_feeling}'
                    
                    Provide a comprehensive, empathetic response in this format:
                    
                    **ACKNOWLEDGMENT & VALIDATION:**
                    - Validate their feelings and normalize their experience
                    - Show understanding and empathy
                    
                    **UNDERSTANDING YOUR EXPERIENCE:**
                    - Provide insight into why they might be feeling this way
                    - Relate to common experiences for their situation
                    
                    **IMMEDIATE COPING STRATEGIES:**
                    - Give 3-4 practical, actionable strategies they can try today
                    - Include breathing exercises, grounding techniques, or self-care tips
                    
                    **LONGER-TERM SUPPORT IDEAS:**
                    - Suggest ongoing strategies for their specific situation
                    - Include lifestyle adjustments, support systems, or resources
                    
                    **WHEN TO SEEK PROFESSIONAL HELP:**
                    - Clearly outline warning signs that indicate need for professional support
                    - Be specific about when to contact healthcare providers
                    
                    **SUPPORT RESOURCES:**
                    - Suggest relevant support groups, apps, or resources
                    - Include specific recommendations based on their role and concerns
                    
                    Keep the tone warm, non-judgmental, and hopeful. Emphasize that they're not alone and that seeking help is normal and healthy.
                    """
                    
                    with st.spinner("💭 Providing personalized mental health support..."):
                        response = model.generate_content(prompt)
                        
                        st.success("💚 Support & Guidance Ready")
                        
                        # Display the response in a nice format
                        st.markdown("---")
                        st.markdown("### 🤗 Your Personalized Mental Health Support")
                        st.markdown(response.text)
                        
                        # Crisis support reminder
                        st.markdown("---")
                        st.error("🚨 **CRISIS SUPPORT:** If you're having thoughts of self-harm or suicide, please reach out for immediate help!")

                except Exception as e:
                    st.error(f"Sorry, I encountered an error while processing your request: {str(e)}")
                    st.info("Please try again or reach out to a mental health professional directly.")
            else:
                st.error("API not configured. Please reach out to mental health resources directly.")
    
    # Crisis and support resources
    st.markdown("---")
    st.markdown("### 📞 Immediate Support Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🆘 CRISIS SUPPORT:**
        - **Suicide & Crisis Lifeline:** 988
        - **Crisis Text Line:** Text HOME to 741741
        - **Emergency Services:** 911
        """)
    
    with col2:
        st.markdown("""
        **🤱 MATERNAL MENTAL HEALTH:**
        - **Postpartum Support International:** 1-800-944-4773
        - **PSI HelpLine:** Text 800-944-4773
        - **SAMHSA National Helpline:** 1-800-662-4357
        """)
    
    # Self-care tools
    with st.expander("🧘‍♀️ Quick Self-Care Tools"):
        tab1, tab2, tab3 = st.tabs(["Breathing Exercise", "Grounding Technique", "Positive Affirmations"])
        
        with tab1:
            st.markdown("""
            **4-7-8 Breathing Technique:**
            1. Exhale completely through your mouth
            2. Close your mouth, inhale through nose for 4 counts
            3. Hold your breath for 7 counts
            4. Exhale through mouth for 8 counts
            5. Repeat 3-4 times
            """)
        
        with tab2:
            st.markdown("""
            **5-4-3-2-1 Grounding:**
            - **5 things** you can see
            - **4 things** you can touch
            - **3 things** you can hear
            - **2 things** you can smell
            - **1 thing** you can taste
            """)
        
        with tab3:
            st.markdown("""
            **Daily Affirmations:**
            - "I am doing the best I can with what I have"
            - "It's okay to not be perfect"
            - "I deserve care and compassion"
            - "This feeling is temporary"
            - "I am stronger than I know"
            """)
    
    # Mental health screening
    with st.expander("📋 Self-Assessment Tools"):
        st.markdown("""
        **Consider professional help if you experience:**
        - Persistent sadness or anxiety for more than 2 weeks
        - Difficulty bonding with your baby
        - Thoughts of harming yourself or your baby
        - Extreme mood swings
        - Difficulty sleeping when baby sleeps
        - Loss of interest in activities you used to enjoy
        - Feeling overwhelmed most of the time
        
        **Remember:** Postpartum depression and anxiety are medical conditions, not personal failures.
        """)
    
    # Disclaimer
    st.info("💡 **Note:** This support is for informational purposes and doesn't replace professional mental health care. If you're experiencing a mental health crisis, please contact emergency services or a mental health professional immediately.")