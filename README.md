# 💙 Healthship - Your Caring Health Companion

A modern, AI-powered health assistant bot that provides friendly, humanized conversations about health topics, diseases, symptoms, and treatments.

## ✨ Features

### 🤖 **Intelligent Health Assistant**
- **Comprehensive Disease Database**: Information on common conditions like flu, diabetes, hypertension, asthma, migraines, depression, and anxiety
- **Symptom Analysis**: Helps identify potential conditions based on symptoms
- **Treatment Suggestions**: Provides evidence-based treatment options and home remedies
- **Prevention Tips**: Offers practical advice for preventing various health conditions

### 💙 **Humanized & Friendly**
- **Warm Personality**: Speaks like a caring friend who happens to be a health expert
- **Empathetic Responses**: Shows genuine concern and understanding
- **Natural Conversations**: Uses emojis and encouraging language appropriately
- **Personalized Care**: Remembers conversation context for better assistance

### 🎨 **Modern UI/UX**
- **Beautiful Design**: Gradient backgrounds, smooth animations, and modern styling
- **Responsive Layout**: Works perfectly on desktop and mobile devices
- **Typing Indicators**: Shows when the bot is thinking/responding
- **Quick Questions**: Pre-made buttons for common health queries
- **Smooth Animations**: Message slides, hover effects, and transitions

### 🧠 **Smart Features**
- **Conversation Memory**: Maintains context throughout the chat session
- **Session Management**: Each user gets their own conversation thread
- **Error Handling**: Friendly error messages with retry suggestions
- **Safety First**: Always recommends professional medical care for serious conditions

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Healthship
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your OpenAI API key**
   - Go to [https://platform.openai.com](https://platform.openai.com)
   - Sign up or log in to your account
   - Navigate to "API Keys" in your account settings
   - Click "Create new secret key" and copy it
   - Add billing information at [https://platform.openai.com/account/billing](https://platform.openai.com/account/billing)

4. **Set up your API key**
   - Open `app.py`
   - Replace `"your_api_key_here"` with your actual OpenAI API key
   ```python
   os.environ["OPENAI_API_KEY"] = "your_actual_api_key_here"
   ```

5. **Run the application**
   ```bash
   uvicorn app:app --reload --host 127.0.0.1 --port 8000
   ```

6. **Open your browser**
   - Navigate to `http://127.0.0.1:8000`
   - Start chatting with Healthship!

## 💬 How to Use

### Quick Start Questions
Click on any of the quick question buttons to get started:
- "Flu symptoms" - Learn about influenza symptoms
- "Diabetes prevention" - Get diabetes prevention tips
- "Anxiety help" - Find anxiety management strategies
- "Cold treatment" - Discover cold treatment options

### Natural Conversations
Simply type your health questions naturally:
- "I have a headache and feel nauseous"
- "How can I prevent high blood pressure?"
- "What are the symptoms of diabetes?"
- "I'm feeling anxious, what can help?"

### Features You Can Try
- Ask about specific diseases and conditions
- Inquire about symptoms you're experiencing
- Request treatment and prevention advice
- Have follow-up conversations (the bot remembers context)
- Get friendly, encouraging responses

## 🏥 Health Topics Covered

### Common Conditions
- **Common Cold**: Symptoms, treatments, prevention
- **Influenza (Flu)**: Comprehensive flu information
- **Diabetes**: Management and prevention strategies
- **Hypertension**: Blood pressure management
- **Asthma**: Breathing condition guidance
- **Migraines**: Headache management
- **Depression**: Mental health support
- **Anxiety**: Stress and anxiety management

### General Health Areas
- Symptom analysis and guidance
- Treatment recommendations
- Prevention strategies
- Lifestyle advice
- When to see a doctor
- Emergency situations

## ⚠️ Important Disclaimers

- **Not a Medical Diagnosis Tool**: Healthship provides general information only
- **Consult Healthcare Professionals**: Always see a doctor for serious symptoms
- **Emergency Situations**: Call emergency services for urgent medical needs
- **Personal Medical Advice**: This bot cannot replace personalized medical care

## 🛠️ Technical Details

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **AI Model**: OpenAI GPT-3.5-turbo
- **Database**: In-memory conversation storage (expandable to persistent DB)
- **API**: RESTful endpoints for chat functionality

### Frontend (Vanilla JS)
- **Styling**: Modern CSS with gradients and animations
- **Responsive**: Mobile-first design approach
- **Interactive**: Real-time chat with typing indicators
- **Accessibility**: Keyboard navigation and focus management

### Key Files
- `app.py` - Main FastAPI application with health logic
- `index.html` - Beautiful, responsive chat interface
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## 🔧 Customization

### Adding New Diseases
Edit the `DISEASE_DATABASE` in `app.py`:
```python
"new_condition": {
    "name": "Condition Name",
    "symptoms": ["symptom1", "symptom2"],
    "causes": ["cause1", "cause2"],
    "treatments": ["treatment1", "treatment2"],
    "prevention": ["prevention1", "prevention2"],
    "severity": "mild|moderate|serious"
}
```

### Modifying Bot Personality
Update the system prompt in the `chat()` function to change how the bot responds.

### UI Customization
Modify the CSS in `index.html` to change colors, fonts, or layout.

## 📱 Mobile Support

Healthship is fully responsive and works great on:
- Desktop computers
- Tablets
- Mobile phones
- Different screen orientations

## 🔒 Privacy & Security

- Conversations are stored temporarily in memory
- No personal data is permanently stored
- OpenAI API calls follow their privacy policies
- Session IDs are randomly generated

## 🤝 Contributing

Feel free to contribute by:
- Adding new health conditions to the database
- Improving the UI/UX design
- Enhancing the bot's personality
- Adding new features
- Fixing bugs or issues

## 📞 Support

If you need help or have questions:
1. Check this README for common issues
2. Review the code comments for technical details
3. Test with different health questions
4. Ensure your OpenAI API key is valid

---

**Made with 💙 by [Your Name]**

*Healthship - Because your health deserves a caring companion!*