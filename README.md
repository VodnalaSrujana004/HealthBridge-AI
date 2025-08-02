# Team : Beta_Coders 

### Team Members: V.Srujana, D.Devika, A.Hansika, J.Likithanjali, I.Srimai, M.Vardhan, B.Umesh

# HealthBridge – AI Chatbot for Mothers & Children

🎯 **Focus:** Child & Maternal Health | SDG 3: Good Health and Well-being

---

## 🧠 Project Idea

**HealthBridge** is an AI-powered Streamlit chatbot built to:

- Provide real-time maternal and child health guidance  
- Answer health queries using advanced NLP  
- Suggest early interventions based on symptoms  
- Educate women on vaccination, nutrition, reproductive health & childcare  
- Monitor and support mental health via sentiment-aware conversations  

No sensors required – just text or (optionally) voice input.

---

## 📦 Modules Overview

**Symptom Checker (Mother/Baby)**  
- Input: `My child has a fever and rash.`  
- Output: `This could be a sign of measles or viral infection. Please ensure hydration. Visit your nearest clinic if rash persists beyond 3 days.`

**Maternal Guidance**  
- Covers antenatal care, pregnancy nutrition, vaccine reminders, breastfeeding tips.  
- Example: `What should I eat during second trimester?` → Nutritional plan via AI.

**Mental Health Assistant (Simple Sentiment Bot)**  
- Detects distress or postnatal depression from user language  
- Example: `I feel like crying every day.` → Suggests talking to someone, supportive advice, helpline links.

**Immunization & Health Tips Educator**  
- Based on WHO/UNICEF schedules  
- Explains vaccine due dates, common childhood diseases, hygiene education.

**AI-Powered Response System**  
- LLMs (Mistral, LLaMA-2, BERT) + fine-tuned domain prompts  
- Multilingual queries, responds in plain language

---

## 💻 Streamlit Interface Flow

- **Home:** Introduction + Select Topic (Chat, Vaccination, Nutrition, Mental Health)
- **Chat UI:** Text input box + voice input (optional)
- **Responses:** Displayed in chat bubbles with relevant emojis & icons
- **Backend:** AI model (HuggingFace or Gemini) processes input
- **Extras:** Health tips carousel, offline mode using SQLite

---

## 📊 Tech Stack

| Component        | Tech Used                                  |
|------------------|--------------------------------------------|
| Frontend         | Streamlit, streamlit-chat, HTML/CSS        |
| NLP Engine       | HuggingFace Transformers, Gemini Pro       |
| Mental Health Bot| Sentiment Analysis (RoBERTa)               |
| DB (optional)    | Firebase (online) / SQLite (offline)       |
| Hosting          | Streamlit Cloud / GCP / LocalHost          |

---

## 🧠 Unique Features

- No external hardware/sensors needed
- Offline/low-bandwidth compatible
- Designed for rural mothers & children
- Multilingual support via translation APIs
- Emotion-aware, empathetic responses
- Visuals for common health practices

---

## 🚀 Future Scope

- Integration with government health records (vaccination databases)
- WhatsApp/Telegram integration
- Voice AI for illiterate users
- AI diagnosis assistance via X-ray report images (Phase 2)

---

## 🏁 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VodnalaSrujana004/HealthBridge-AI.git
   cd HealthBridge-AI
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

## 🤝 Contributing

Contributions and suggestions are welcome! Please open issues or submit pull requests.

---

**HealthBridge-AI** is committed to supporting maternal and child health for communities worldwide.

