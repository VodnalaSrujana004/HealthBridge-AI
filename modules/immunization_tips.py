
import streamlit as st
import pandas as pd

def display():
    st.header("💉 Immunization & Health Tips")
    st.markdown("Based on data from WHO and UNICEF. **Always consult your pediatrician for your child's specific needs.**")

    # Example data - in a real app, this would be from a database or API
    immunization_data = {
        "Age": ["Birth", "2 Months", "4 Months", "6 Months", "12-15 Months"],
        "Vaccine": ["BCG, OPV 0, Hep B 1", "DTwP 1, IPV 1, Hib 1, Hep B 2", "DTwP 2, IPV 2, Hib 2", "DTwP 3, IPV 3, Hib 3", "MMR 1, Varicella 1"]
    }
    df = pd.DataFrame(immunization_data)

    st.subheader("Recommended Immunization Schedule")
    st.table(df)

    st.subheader("Key Health & Hygiene Tips")
    st.markdown("""
    - **Handwashing:** Wash hands with soap and water frequently, especially before feeding.
    - **Safe Water:** Always use boiled or purified water for drinking and preparing formula.
    - **Proper Nutrition:** Ensure a balanced diet for your child's growth and development.
    - **Safe Sleep:** Place your baby on their back to sleep to reduce the risk of SIDS.
    """)