from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import json
import random
import requests
from typing import List, Dict

# 🆓 FREE AI OPTIONS - No API costs!
USE_FREE_AI = True  # Set to True to use free alternatives

# FREE OPTION 1: Ollama (Local AI - Completely Free!)
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama2"  # Download with: ollama pull llama2

# FREE OPTION 2: Hugging Face Inference API (Free tier available)
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HUGGINGFACE_TOKEN = ""  # Get free token from huggingface.co/settings/tokens

app = FastAPI()

# Allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Comprehensive disease database
DISEASE_DATABASE = {
    "common_cold": {
        "name": "Common Cold",
        "symptoms": ["runny nose", "sneezing", "cough", "sore throat", "mild fever"],
        "treatments": ["rest", "fluids", "warm salt water gargle", "honey", "vitamin C"],
        "prevention": ["wash hands frequently", "avoid close contact with sick people", "boost immunity"],
        "severity": "mild"
    },
    "stomach_pain": {
        "name": "Stomach Pain/Abdominal Pain",
        "symptoms": ["abdominal cramping", "sharp pain", "dull ache", "bloating", "nausea"],
        "treatments": ["rest", "clear fluids", "bland diet", "antacids", "heat therapy"],
        "prevention": ["eat slowly", "avoid spicy foods", "manage stress", "stay hydrated"],
        "severity": "mild"
    },
    "headache": {
        "name": "Headache",
        "symptoms": ["head pain", "pressure", "throbbing", "sensitivity to light"],
        "treatments": ["rest", "hydration", "pain relievers", "cold compress", "massage"],
        "prevention": ["regular sleep", "stay hydrated", "manage stress", "limit screen time"],
        "severity": "mild"
    },
    "back_pain": {
        "name": "Back Pain",
        "symptoms": ["lower back ache", "muscle spasms", "stiffness", "shooting pain"],
        "treatments": ["rest", "ice/heat therapy", "gentle stretching", "pain relievers"],
        "prevention": ["good posture", "regular exercise", "proper lifting", "ergonomic workspace"],
        "severity": "mild"
    },
    "sore_throat": {
        "name": "Sore Throat",
        "symptoms": ["throat pain", "scratchiness", "difficulty swallowing", "swollen glands"],
        "treatments": ["warm salt water gargle", "throat lozenges", "honey", "warm liquids"],
        "prevention": ["hand hygiene", "avoid sick people", "stay hydrated"],
        "severity": "mild"
    }
}

# Friendly greeting responses
GREETINGS = [
    "Hello there! 😊 I'm Healthship, your friendly AI health companion. I'm running on FREE AI - no costs involved! How can I help you today?",
    "Hi! 🌟 Great to see you! I'm here to help with health questions using completely free AI technology. What's on your mind?",
    "Hey! 👋 I'm Healthship, powered by free AI! I can help with health topics, symptoms, treatments, and general wellness advice.",
    "Hello! 💙 I'm your caring health assistant running on free AI. Whether it's about symptoms, treatments, or prevention - I'm here for you!"
]

# Conversation memory
conversation_memory = {}

class UserQuery(BaseModel):
    question: str
    session_id: str = "default"

class ConversationContext:
    def __init__(self):
        self.messages = []
        self.user_name = None
        self.health_concerns = []

def get_or_create_context(session_id: str) -> ConversationContext:
    if session_id not in conversation_memory:
        conversation_memory[session_id] = ConversationContext()
    return conversation_memory[session_id]

# 🆓 FREE AI FUNCTIONS

def call_ollama_ai(prompt: str) -> str:
    """Call Ollama local AI (completely free!)"""
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        return None
    except:
        return None

def call_huggingface_ai(prompt: str) -> str:
    """Call Hugging Face Inference API (free tier available)"""
    try:
        if not HUGGINGFACE_TOKEN:
            return None
        
        headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
        payload = {"inputs": prompt}
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated = result[0].get("generated_text", "")
                return generated.replace(prompt, "").strip()
        return None
    except:
        return None

def generate_intelligent_health_response(query: str) -> str:
    """Generate intelligent rule-based health responses (always free!)"""
    query_lower = query.lower()
    
    # Detailed health-specific responses
    if "stomach" in query_lower or "belly" in query_lower or "abdominal" in query_lower:
        return """I understand you're experiencing stomach discomfort. 💙 Here's what I recommend:

**Immediate Relief:**
• Rest and avoid solid foods temporarily
• Drink clear fluids (water, herbal tea, clear broth)
• Try ginger tea or ginger ale for nausea
• Apply gentle heat to your abdomen
• Sit upright or walk gently to help with gas

**When to eat again:**
• Start with bland foods: rice, toast, bananas, applesauce
• Avoid dairy, spicy, or fatty foods initially
• Eat small, frequent meals

**See a doctor if:**
• Severe pain that doesn't improve
• High fever (over 101°F)
• Vomiting that prevents keeping fluids down
• Signs of dehydration
• Pain lasts more than 24 hours

Feel better soon! 🤗"""

    elif "head" in query_lower and ("ache" in query_lower or "pain" in query_lower):
        return """I'm sorry you're dealing with a headache. 😔 Here are some effective remedies:

**Immediate Relief:**
• Rest in a quiet, dark room
• Apply a cold compress to your forehead or neck
• Drink plenty of water (dehydration is a common cause)
• Gently massage your temples and neck
• Try deep breathing or relaxation techniques

**Prevention Tips:**
• Maintain regular sleep schedule
• Stay hydrated throughout the day
• Take breaks from screens every hour
• Manage stress with relaxation techniques
• Eat regular meals

**See a doctor if:**
• Sudden, severe headache unlike any before
• Headache with fever, stiff neck, or vision changes
• Frequent headaches that interfere with daily life
• Headache after a head injury

Take care! 💙"""

    elif "back" in query_lower and ("pain" in query_lower or "ache" in query_lower):
        return """Back pain can be really uncomfortable! 😣 Here's how to find relief:

**Immediate Care:**
• Apply ice for first 24-48 hours, then switch to heat
• Rest, but avoid bed rest for more than 1-2 days
• Try gentle stretching and walking
• Over-the-counter pain relievers as directed
• Sleep on your side with a pillow between your knees

**Gentle Exercises:**
• Knee-to-chest stretches
• Cat-cow stretches
• Gentle walking
• Avoid heavy lifting

**See a doctor if:**
• Pain radiates down your leg
• Numbness or tingling in legs
• Loss of bladder/bowel control
• Severe pain that doesn't improve with rest

Hope you feel better soon! 💪"""

    elif "throat" in query_lower and ("sore" in query_lower or "pain" in query_lower):
        return """A sore throat is no fun! 😷 Here are some soothing remedies:

**Immediate Relief:**
• Gargle with warm salt water (1/2 tsp salt in warm water)
• Drink warm liquids: tea with honey, warm broth
• Use throat lozenges or hard candy
• Stay well hydrated
• Rest your voice
• Use a humidifier or breathe steam from hot shower

**Avoid:**
• Smoking or secondhand smoke
• Alcohol
• Spicy or acidic foods

**See a doctor if:**
• High fever (over 101°F)
• Difficulty swallowing or breathing
• White patches on throat
• Severe pain lasting more than a few days
• Swollen lymph nodes

Get well soon! 🍯"""

    elif "sleep" in query_lower or "insomnia" in query_lower or "tired" in query_lower:
        return """Sleep troubles can be frustrating! 😴 Here are proven strategies:

**Sleep Hygiene:**
• Keep consistent bedtime and wake time
• Create a relaxing bedtime routine
• Keep bedroom cool, dark, and quiet
• Avoid screens 1 hour before bed
• Use your bed only for sleep

**Lifestyle Tips:**
• Limit caffeine after 2 PM
• Avoid large meals before bedtime
• Get regular exercise (but not close to bedtime)
• Try relaxation techniques: deep breathing, meditation
• Write down worries to clear your mind

**Natural Remedies:**
• Chamomile tea
• Warm milk
• Gentle stretching
• Reading a book

**See a doctor if:**
• Chronic insomnia lasting weeks
• Loud snoring or breathing interruptions
• Excessive daytime sleepiness

Sweet dreams! 🌙"""

    elif "fever" in query_lower or "temperature" in query_lower:
        return """Fever can make you feel awful! 🌡️ Here's how to manage it:

**Immediate Care:**
• Rest and stay hydrated
• Take fever reducers (acetaminophen/ibuprofen) as directed
• Use cool, damp cloths on forehead
• Wear light, breathable clothing
• Take lukewarm baths or showers

**Stay Hydrated:**
• Water, herbal teas, clear broths
• Avoid alcohol and caffeine
• Popsicles or ice chips if nauseous

**Monitor Temperature:**
• Check every few hours
• Keep a record of readings

**Seek immediate medical care if:**
• Fever over 103°F (39.4°C)
• Difficulty breathing
• Severe headache or stiff neck
• Persistent vomiting
• Signs of dehydration
• Fever in infants under 3 months

Take care! 💙"""

    # General health advice
    elif any(word in query_lower for word in ["sick", "ill", "unwell", "pain", "hurt"]):
        return """I understand you're not feeling well. 💙 While I can provide general health information, it's important to listen to your body. 

**General Self-Care:**
• Rest and get plenty of sleep
• Stay hydrated with water and clear fluids
• Eat nutritious foods when you feel up to it
• Avoid stress when possible
• Monitor your symptoms

**When to see a healthcare provider:**
• Symptoms are severe or getting worse
• You have a high fever
• Symptoms persist for several days
• You're concerned about your condition

What specific symptoms are you experiencing? I can provide more targeted advice! 🤗"""

    # Greetings
    elif any(word in query_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return random.choice(GREETINGS)
    
    # General responses
    else:
        return """I'm here to help with your health questions! 😊 I specialize in providing advice about:

• Common symptoms (headaches, stomach pain, sore throat, etc.)
• Home remedies and self-care tips
• When to see a healthcare provider
• Prevention and wellness advice
• General health information

What specific health topic would you like to know about? Feel free to describe any symptoms you're experiencing! 💙"""

def get_ai_response(prompt: str) -> str:
    """Try different AI providers in order of preference"""
    
    # Try Ollama first (local, completely free)
    if USE_FREE_AI:
        response = call_ollama_ai(prompt)
        if response and len(response) > 10:
            return f"🤖 {response}"
    
    # Try Hugging Face API (free tier)
    if USE_FREE_AI and HUGGINGFACE_TOKEN:
        response = call_huggingface_ai(prompt)
        if response and len(response) > 10:
            return f"🤗 {response}"
    
    # Fallback to intelligent rule-based (always works, always free)
    return generate_intelligent_health_response(prompt)

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/chat")
def chat(query: UserQuery):
    try:
        context = get_or_create_context(query.session_id)
        user_message = query.question.lower().strip()
        
        # Handle greetings
        if any(greeting in user_message for greeting in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            response_text = random.choice(GREETINGS)
            context.messages.append({"role": "user", "content": query.question})
            context.messages.append({"role": "assistant", "content": response_text})
            return {"answer": response_text}
        
        # Check for specific disease information
        for disease_key, disease_info in DISEASE_DATABASE.items():
            if disease_key.replace("_", " ") in user_message or disease_info["name"].lower() in user_message:
                response_text = f"I'd be happy to help with {disease_info['name']}! 😊\n\n"
                response_text += f"**Common symptoms:** {', '.join(disease_info['symptoms'][:4])}\n\n"
                response_text += f"**Treatment options:** {', '.join(disease_info['treatments'][:4])}\n\n"
                response_text += f"**Prevention tips:** {', '.join(disease_info['prevention'][:3])}\n\n"
                if disease_info['severity'] == 'serious':
                    response_text += "⚠️ **Important:** This is a serious condition that requires professional medical care.\n\n"
                response_text += "Remember, I provide general information. For personalized advice, please consult a healthcare professional! 💙"
                
                context.messages.append({"role": "user", "content": query.question})
                context.messages.append({"role": "assistant", "content": response_text})
                return {"answer": response_text}
        
        # Use AI response (free alternatives)
        response_text = get_ai_response(query.question)
        
        # Store in conversation memory
        context.messages.append({"role": "user", "content": query.question})
        context.messages.append({"role": "assistant", "content": response_text})
        
        return {"answer": response_text}
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        
        error_responses = [
            "I'm having a small hiccup, but I'm still here to help! 😊 Could you try asking your question again?",
            "Something went wrong, but don't worry! 💙 I'm powered by free AI and ready to assist you. Please try again!",
            "Oops! I encountered an issue, but I'm back online! 🤗 Please ask me your health question once more."
        ]
        return {"answer": random.choice(error_responses)}
