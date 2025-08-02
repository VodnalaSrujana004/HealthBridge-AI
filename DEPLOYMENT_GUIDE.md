# HealthBridge AI - Streamlit Deployment Guide

## 🚀 How to Deploy Your HealthBridge AI to Streamlit Cloud

### Prerequisites
- GitHub account
- Your Google Gemini API key
- All project files ready

### Step 1: Prepare Your Project
✅ All files have been updated for deployment
✅ requirements.txt contains all dependencies
✅ API keys are configured to use Streamlit secrets
✅ .gitignore file created to protect sensitive data

### Step 2: Push to GitHub

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - HealthBridge AI"
   ```

2. **Create GitHub Repository**:
   - Go to GitHub.com
   - Click "New Repository"
   - Name it "HealthBridge-AI" or similar
   - Don't initialize with README (since you already have files)
   - Click "Create Repository"

3. **Push Your Code**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/HealthBridge-AI.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create New App**:
   - Click "New app"
   - Select your GitHub repository: "HealthBridge-AI"
   - Main file path: `app.py`
   - App URL: Choose a custom URL or use default

3. **Configure Secrets**:
   - In the deployment settings, click "Advanced settings"
   - In the "Secrets" section, add:
   ```toml
   GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
   ```

4. **Deploy**:
   - Click "Deploy!"
   - Wait for deployment to complete (usually 2-5 minutes)

### Step 4: Test Your Deployed App

Once deployed, test all features:
- ✅ General Chat Assistant
- ✅ Symptom Checker
- ✅ Mental Health Support
- ✅ Maternal Guidance
- ✅ Immunization & Health Tips

### Troubleshooting

**Common Issues:**

1. **API Key Error**:
   - Double-check the secrets configuration in Streamlit Cloud
   - Ensure the key name is exactly: `GEMINI_API_KEY`

2. **Module Import Errors**:
   - Verify all files are in the correct directory structure
   - Check that requirements.txt includes all dependencies

3. **File Not Found Errors**:
   - Ensure assets/logo.png and assets/icon.png exist
   - Or remove/comment out those lines if you don't have the image files

### Your App Structure
```
HealthBridge-AI/
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── README.md             # This file
├── .gitignore            # Git ignore file
├── .streamlit/
│   ├── config.toml       # Streamlit config
│   └── secrets.toml      # Local secrets (not pushed to GitHub)
├── modules/
│   ├── __init__.py
│   ├── symptom_checker.py
│   ├── mental_health.py
│   ├── maternal_guidance.py
│   └── immunization_tips.py
└── assets/
    ├── logo.png          # Your logo
    └── icon.png          # Your icon
```

### Post-Deployment

1. **Share Your App**: Your app will be available at: `https://your-app-name.streamlit.app/`
2. **Monitor Usage**: Check Streamlit Cloud dashboard for analytics
3. **Update Code**: Push changes to GitHub - they'll auto-deploy to Streamlit

### Security Notes
- ✅ API keys are stored securely in Streamlit secrets
- ✅ .gitignore prevents sensitive files from being uploaded
- ✅ Local secrets.toml is excluded from version control

### Support
If you encounter issues:
- Check Streamlit Cloud logs in the deployment dashboard
- Verify GitHub repository has all files
- Ensure secrets are properly configured

Good luck with your deployment! 🎉
