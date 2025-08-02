import streamlit as st
from streamlit_chat import message
import google.generativeai as genai
import pandas as pd
from modules import maternal_guidance, mental_health, symptom_checker, immunization_tips

# --- Page Configuration ---
st.set_page_config(
    page_title="HealthBridge – AI Chatbot for Mothers & Children",
    page_icon="assets/icon.png",  # Update with your icon path
    layout="wide",
)

# --- API Configuration ---
try:
    # Use Streamlit secrets for deployment, fallback to direct key for local development
    api_key = st.secrets.get("GEMINI_API_KEY", "AIzaSyDf5NK3kYz1OITVovJmn4awerHwiMHpK1M")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

except Exception as e:
    st.error(f"Could not configure Google Gemini API: {str(e)}")
    model = None

# --- UI Customization ---
st.markdown("""
<style>
    .st-emotion-cache-1y4p8pa {
        padding-top: 2rem;
    }
    .st-chat-message {
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.image("assets/logo.png", width=150) # Update with your logo path
st.sidebar.title("HealthBridge Modules")

page = st.sidebar.radio(
    "Navigate to a module:",
    ("Chat Assistant", "Symptom Checker", "Maternal Guidance", "Mental Health Support", "Immunization & Health Tips"),
    label_visibility="collapsed"
)

# --- Main Application Logic ---
if page == "Chat Assistant":
    st.header("🤖 General Health Chat")
    st.markdown("Ask me anything about maternal and child health!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        if model:
            try:
                response = model.generate_content(f"You are a helpful AI assistant for mothers. Respond to: {user_input}")
                st.session_state.chat_history.append({"role": "assistant", "text": response.text})
            except Exception as e:
                st.session_state.chat_history.append({"role": "assistant", "text": f"Sorry, I encountered an error: {str(e)}"})
        else:
            st.session_state.chat_history.append({"role": "assistant", "text": "API not configured."})


    for i, chat in enumerate(st.session_state.chat_history):
        if chat["role"] == "user":
            message(chat["text"], is_user=True, key=f"user_{i}")
        else:
            message(chat["text"], key=f"assistant_{i}")

elif page == "Symptom Checker":
    symptom_checker.display()

elif page == "Maternal Guidance":
    maternal_guidance.display()

elif page == "Mental Health Support":
    mental_health.display()

elif page == "Immunization & Health Tips":
    immunization_tips.display()

# --- Example Prompts ---
st.sidebar.markdown("---")
st.sidebar.header("Example Prompts")
if page == "Symptom Checker":
    st.sidebar.info("e.g., 'My baby has a high fever and a red rash.'")
elif page == "Maternal Guidance":
    st.sidebar.info("e.g., 'What should I eat during my first trimester?'")
elif page == "Mental Health Support":
    st.sidebar.info("e.g., 'I feel overwhelmed and anxious since my baby was born.'")
elif page == "Immunization & Health Tips":
    st.sidebar.info("e.g., 'What is the vaccination schedule for a newborn?'")