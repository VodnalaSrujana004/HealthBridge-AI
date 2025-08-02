import streamlit as st
import pandas as pd

def display():
    st.header("🤰 Maternal Guidance")
    st.markdown("Get personalized tips for nutrition, pregnancy, and breastfeeding.")

    guidance_type = st.selectbox(
        "What kind of guidance do you need?",
        ("Nutrition by Trimester", "Breastfeeding Tips", "General Pregnancy Advice")
    )

    if guidance_type == "Nutrition by Trimester":
        trimester = st.selectbox("Select Trimester:", ("First Trimester", "Second Trimester", "Third Trimester"))
        if st.button("Get Nutritional Chart"):
            # This would typically fetch data from a reliable source or a fine-tuned model
            data = {
                "First Trimester": ["Folate-rich foods (lentils, spinach)", "Lean proteins", "Whole grains"],
                "Second Trimester": ["Calcium-rich foods (yogurt, milk)", "Iron sources (lean meat, beans)", "Vitamin D"],
                "Third Trimester": ["Omega-3 fatty acids (salmon)", "High-fiber foods", "Plenty of fluids"]
            }
            st.subheader(f"Nutritional Focus for the {trimester}")
            for item in data[trimester]:
                st.markdown(f"- {item}")

    elif guidance_type == "Breastfeeding Tips":
        st.subheader("General Breastfeeding Tips")
        st.markdown("""
        - **Ensure a good latch:** This prevents soreness and ensures the baby gets enough milk.
        - **Stay hydrated:** Drink plenty of water throughout the day.
        - **Eat a balanced diet:** Your body needs extra calories to produce milk.
        - **Find a comfortable position:** Use pillows for support.
        """)

    elif guidance_type == "General Pregnancy Advice":
        st.subheader("General Pregnancy Wellness Tips")
        st.markdown("""
        - **Get regular, gentle exercise:** Walking and swimming are great options.
        - **Get plenty of rest:** Listen to your body and rest when you feel tired.
        - **Avoid certain foods:** Such as unpasteurized dairy and raw meat.
        - **Attend all prenatal appointments:** Regular check-ups are crucial for monitoring your and your baby's health.
        """)