from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import json
import random
import requests
from typing import List, Dict
from medical_database import MEDICAL_CONDITIONS, MEDICAL_SPECIALTIES, SYMPTOM_CHECKER

# FREE AI OPTIONS - No API costs!
USE_FREE_AI = True

# FREE OPTION 1: Ollama (Local AI - Completely Free!)
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama2"

# FREE OPTION 2: Hugging Face Inference API (Free tier available)
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HUGGINGFACE_TOKEN = ""

app = FastAPI()

# Allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Professional medical greetings (no emojis)
MEDICAL_GREETINGS = [
    "Welcome to MedConsult. I'm your AI medical assistant. Please describe your symptoms or health concerns, and I'll provide professional medical guidance.",
    "Hello, I'm here to help with your health questions. Please tell me about your symptoms or medical concerns so I can provide appropriate guidance.",
    "Good day. I'm your medical consultation assistant. Please describe your health issue or symptoms, and I'll offer professional medical advice.",
    "Welcome to our medical consultation service. I'm ready to help with your health concerns. Please describe your symptoms or condition."
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
        self.current_symptoms = []

def get_or_create_context(session_id: str) -> ConversationContext:
    if session_id not in conversation_memory:
        conversation_memory[session_id] = ConversationContext()
    return conversation_memory[session_id]

# Enhanced medical search function
def search_medical_condition(query: str) -> Dict:
    """Search for medical conditions based on symptoms or condition names"""
    query_lower = query.lower()
    
    # Enhanced keyword mapping for medical conditions
    medical_keywords = {
        # Pain-related
        "stomach pain": "gastritis",
        "abdominal pain": "gastritis", 
        "belly pain": "gastritis",
        "chest pain": "heart_disease",
        "heart pain": "heart_disease",
        "headache": "migraine",
        "head pain": "migraine",
        "joint pain": "arthritis",
        "back pain": "arthritis",
        "muscle pain": "arthritis",
        
        # Respiratory
        "shortness of breath": "asthma",
        "difficulty breathing": "asthma",
        "wheezing": "asthma",
        "persistent cough": "bronchitis",
        "chronic cough": "bronchitis",
        "chest congestion": "bronchitis",
        
        # Cardiovascular
        "high blood pressure": "hypertension",
        "blood pressure": "hypertension",
        "heart palpitations": "heart_disease",
        "irregular heartbeat": "heart_disease",
        
        # Digestive
        "nausea": "gastritis",
        "vomiting": "gastritis",
        "indigestion": "gastritis",
        "heartburn": "gastritis",
        "diarrhea": "ibs",
        "constipation": "ibs",
        "bloating": "ibs",
        
        # Neurological
        "migraine": "migraine",
        "severe headache": "migraine",
        "seizure": "epilepsy",
        "epilepsy": "epilepsy",
        
        # Mental Health
        "depression": "depression",
        "anxiety": "anxiety_disorders",
        "panic": "anxiety_disorders",
        "sad": "depression",
        "worried": "anxiety_disorders",
        
        # Endocrine
        "diabetes": "diabetes_type2",
        "blood sugar": "diabetes_type2",
        "frequent urination": "diabetes_type2",
        "thyroid": "thyroid_disorders",
        
        # Skin
        "rash": "eczema",
        "itchy skin": "eczema",
        "skin irritation": "eczema",
        "psoriasis": "psoriasis",
        
        # Infections
        "cold": "common_cold",
        "flu": "influenza",
        "fever": "influenza",
        "sore throat": "common_cold",
        "runny nose": "common_cold",
        
        # Urinary
        "urinary tract infection": "urinary_tract_infection",
        "uti": "urinary_tract_infection",
        "burning urination": "urinary_tract_infection",
        
        # Women's Health
        "menstrual": "menstrual_disorders",
        "period": "menstrual_disorders",
        "cramps": "menstrual_disorders",
        
        # Men's Health
        "prostate": "prostate_problems",
        
        # Eye Health
        "vision": "glaucoma",
        "eye pain": "glaucoma",
        
        # ENT
        "sinus": "sinusitis",
        "nasal congestion": "sinusitis"
    }
    
    # First check for direct keyword matches
    for keyword, condition_key in medical_keywords.items():
        if keyword in query_lower:
            if condition_key in MEDICAL_CONDITIONS:
                return MEDICAL_CONDITIONS[condition_key]
    
    # Then check medical conditions database
    for condition_key, condition_info in MEDICAL_CONDITIONS.items():
        # Check condition name
        if condition_info["name"].lower() in query_lower or condition_key.replace("_", " ") in query_lower:
            return condition_info
        
        # Check symptoms
        for symptom in condition_info["symptoms"]:
            if symptom.lower() in query_lower:
                return condition_info
                
        # Check causes
        for cause in condition_info["causes"]:
            if cause.lower() in query_lower:
                return condition_info
    
    return None

def format_medical_response(condition_info: Dict, user_query: str) -> str:
    """Format a professional medical response"""
    condition_name = condition_info['name']
    category = condition_info['category']
    specialty = MEDICAL_SPECIALTIES.get(category, "General Medicine")
    
    response = f"**Medical Consultation: {condition_name}**\n\n"
    response += f"**Medical Specialty:** {specialty}\n"
    response += f"**Condition Category:** {category}\n\n"
    
    # Symptoms section
    response += f"**Common Symptoms:**\n"
    for symptom in condition_info['symptoms'][:6]:
        response += f"• {symptom.title()}\n"
    response += "\n"
    
    # Causes section
    response += f"**Possible Causes:**\n"
    for cause in condition_info['causes'][:5]:
        response += f"• {cause.title()}\n"
    response += "\n"
    
    # Treatment section
    response += f"**Treatment Options:**\n"
    for treatment in condition_info['treatments'][:6]:
        response += f"• {treatment.title()}\n"
    response += "\n"
    
    # Prevention section
    response += f"**Prevention Measures:**\n"
    for prevention in condition_info['prevention'][:5]:
        response += f"• {prevention.title()}\n"
    response += "\n"
    
    # When to see doctor
    if 'when_to_see_doctor' in condition_info:
        response += f"**When to Seek Medical Care:**\n"
        response += f"• {condition_info['when_to_see_doctor']}\n\n"
    
    # Severity warning
    if condition_info['severity'] == 'serious':
        response += "**⚠️ IMPORTANT MEDICAL NOTICE:**\n"
        response += "This is a serious medical condition that requires professional medical evaluation and treatment. Please consult with a qualified healthcare provider immediately.\n\n"
    elif condition_info['severity'] == 'moderate':
        response += "**Medical Recommendation:**\n"
        response += "Please consider consulting with a healthcare professional for proper evaluation and treatment planning.\n\n"
    
    response += "**Medical Disclaimer:** This information is for educational purposes only and should not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns."
    
    return response

# FREE AI FUNCTIONS
def call_ollama_ai(prompt: str) -> str:
    """Call Ollama local AI (completely free!)"""
    try:
        test_response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if test_response.status_code != 200:
            return None
            
        medical_prompt = f"""You are a professional medical AI assistant. Provide accurate, helpful medical information while being professional and empathetic. Always recommend consulting healthcare professionals for serious conditions.

Patient Query: {prompt}

Please provide a comprehensive medical response including symptoms, possible causes, treatment options, and when to seek professional medical care."""

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": medical_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json().get("response", "").strip()
            return result if result else None
        return None
    except Exception as e:
        print(f"Ollama error: {e}")
        return None

def call_huggingface_ai(prompt: str) -> str:
    """Call Hugging Face Inference API (free tier available)"""
    try:
        if not HUGGINGFACE_TOKEN:
            return None
        
        headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
        payload = {"inputs": f"Medical consultation: {prompt}"}
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated = result[0].get("generated_text", "")
                return generated.replace(f"Medical consultation: {prompt}", "").strip()
        return None
    except:
        return None

def generate_professional_medical_response(query: str) -> str:
    """Generate professional medical responses based on symptoms and conditions"""
    query_lower = query.lower()
    
    # Comprehensive medical response system
    if any(word in query_lower for word in ["stomach", "abdominal", "belly", "nausea", "vomiting"]):
        return """**Medical Consultation: Gastrointestinal Symptoms**

**Symptoms Assessment:**
Based on your description of stomach/abdominal discomfort, this could indicate several conditions including gastritis, gastroenteritis, or functional dyspepsia.

**Immediate Care Recommendations:**
• Rest and avoid solid foods temporarily
• Maintain hydration with clear fluids (water, clear broths, electrolyte solutions)
• Consider ginger tea for nausea relief
• Apply gentle heat to the abdomen if comfortable
• Avoid dairy, caffeine, alcohol, and spicy foods

**Dietary Management:**
• When ready to eat, start with bland foods (rice, toast, bananas, applesauce)
• Eat small, frequent meals rather than large portions
• Chew food thoroughly and eat slowly
• Avoid foods that may irritate the stomach

**When to Seek Immediate Medical Care:**
• Severe, persistent abdominal pain
• High fever (over 101°F/38.3°C)
• Signs of dehydration (dizziness, dry mouth, decreased urination)
• Vomiting blood or coffee-ground material
• Black, tarry stools
• Severe dehydration or inability to keep fluids down

**Follow-up Care:**
If symptoms persist beyond 24-48 hours or worsen, please consult with a healthcare provider for proper evaluation and treatment.

**Medical Disclaimer:** This information is for educational purposes only. For persistent or severe symptoms, please seek professional medical evaluation."""

    elif any(word in query_lower for word in ["headache", "head pain", "migraine"]):
        return """**Medical Consultation: Headache Assessment**

**Symptom Evaluation:**
Headaches can range from tension-type headaches to migraines or secondary headaches due to underlying conditions.

**Immediate Relief Measures:**
• Rest in a quiet, dark environment
• Apply cold compress to forehead or warm compress to neck/shoulders
• Ensure adequate hydration (drink water regularly)
• Gentle neck and shoulder massage
• Practice relaxation techniques or deep breathing

**Pain Management:**
• Over-the-counter pain relievers (acetaminophen, ibuprofen) as directed
• Avoid overuse of pain medications (rebound headaches)
• Consider caffeine in moderation if you regularly consume it

**Lifestyle Modifications:**
• Maintain regular sleep schedule (7-9 hours nightly)
• Eat regular, balanced meals
• Manage stress through relaxation techniques
• Stay hydrated throughout the day
• Limit screen time and take regular breaks

**Seek Immediate Medical Attention If:**
• Sudden, severe headache unlike any previous headache
• Headache with fever, stiff neck, confusion, or vision changes
• Headache after head injury
• Progressive worsening of headache pattern
• Headache with weakness, numbness, or difficulty speaking

**Preventive Measures:**
• Identify and avoid personal headache triggers
• Maintain consistent daily routines
• Regular moderate exercise
• Stress management techniques

**Medical Disclaimer:** Persistent or severe headaches require professional medical evaluation to rule out underlying conditions."""

    elif any(word in query_lower for word in ["chest pain", "heart", "shortness of breath"]):
        return """**Medical Consultation: Chest Pain/Cardiac Symptoms**

**⚠️ URGENT MEDICAL NOTICE:**
Chest pain and shortness of breath can indicate serious cardiac conditions requiring immediate medical evaluation.

**Immediate Actions:**
• If experiencing severe chest pain, call emergency services immediately
• Sit upright and try to remain calm
• Loosen tight clothing
• If prescribed, take nitroglycerin as directed
• Chew aspirin if not allergic and no contraindications

**Symptom Assessment:**
Chest pain can be cardiac (heart-related) or non-cardiac in origin. Associated symptoms help determine urgency.

**Cardiac Warning Signs (SEEK EMERGENCY CARE):**
• Crushing, squeezing, or pressure-like chest pain
• Pain radiating to arm, jaw, neck, or back
• Shortness of breath with chest pain
• Sweating, nausea, or lightheadedness with chest pain
• Irregular heartbeat or palpitations

**Non-Cardiac Causes May Include:**
• Muscle strain or inflammation
• Gastroesophageal reflux (heartburn)
• Anxiety or panic attacks
• Respiratory conditions

**When to Seek Immediate Medical Care:**
• Any chest pain with concerning features
• Shortness of breath at rest
• Chest pain lasting more than a few minutes
• Any doubt about the cause of symptoms

**Risk Factor Assessment:**
Consider cardiovascular risk factors: family history, smoking, diabetes, high blood pressure, high cholesterol, obesity, sedentary lifestyle.

**IMPORTANT:** Do not delay seeking medical care for chest pain. When in doubt, seek emergency medical evaluation immediately.

**Medical Disclaimer:** This is not a substitute for emergency medical care. Chest pain requires professional medical evaluation."""

    elif any(word in query_lower for word in ["cough", "breathing", "respiratory"]):
        return """**Medical Consultation: Respiratory Symptoms**

**Symptom Assessment:**
Respiratory symptoms including cough and breathing difficulties can indicate various conditions from common colds to more serious respiratory disorders.

**Immediate Care for Cough:**
• Stay well hydrated with warm liquids
• Use humidifier or breathe steam from hot shower
• Honey (for adults) can soothe throat irritation
• Avoid irritants (smoke, strong odors, dust)
• Elevate head while sleeping

**Breathing Support:**
• Sit upright to ease breathing
• Practice slow, deep breathing exercises
• Use pursed-lip breathing technique
• Ensure good air circulation in living spaces

**When Cough May Indicate Serious Condition:**
• Cough producing blood or pink frothy sputum
• Persistent cough lasting more than 3 weeks
• Cough with high fever and chills
• Severe shortness of breath
• Chest pain with coughing

**Seek Immediate Medical Care If:**
• Severe difficulty breathing or shortness of breath at rest
• Bluish lips or fingernails (cyanosis)
• High fever with respiratory symptoms
• Chest pain with breathing
• Coughing up blood

**Common Causes:**
• Viral upper respiratory infections (common cold)
• Bacterial infections (pneumonia, bronchitis)
• Allergies or asthma
• Gastroesophageal reflux
• Environmental irritants

**Prevention Measures:**
• Hand hygiene and avoid close contact with sick individuals
• Stay up to date with vaccinations
• Avoid smoking and secondhand smoke
• Manage underlying conditions (asthma, allergies)

**Medical Disclaimer:** Persistent or severe respiratory symptoms require professional medical evaluation for proper diagnosis and treatment."""

    elif any(word in query_lower for word in ["fever", "temperature", "chills"]):
        return """**Medical Consultation: Fever Management**

**Fever Assessment:**
Fever is a natural immune response but requires monitoring and appropriate management.

**Temperature Guidelines:**
• Normal: 97°F-99°F (36.1°C-37.2°C)
• Low-grade fever: 99.1°F-100.4°F (37.3°C-38°C)
• Fever: Above 100.4°F (38°C)
• High fever: Above 103°F (39.4°C)

**Immediate Management:**
• Rest and avoid strenuous activities
• Increase fluid intake (water, clear broths, electrolyte solutions)
• Dress in light, breathable clothing
• Use lukewarm sponge baths or cool compresses
• Monitor temperature regularly

**Medication Management:**
• Acetaminophen or ibuprofen as directed for comfort
• Follow dosing instructions carefully
• Avoid aspirin in children and teenagers
• Do not exceed recommended doses

**Supportive Care:**
• Maintain comfortable room temperature
• Use fans for air circulation
• Consume easily digestible foods when appetite returns
• Get adequate rest and sleep

**Seek Immediate Medical Care If:**
• Temperature above 103°F (39.4°C)
• Fever with severe headache and stiff neck
• Difficulty breathing or chest pain
• Persistent vomiting preventing fluid intake
• Signs of dehydration
• Fever in infants under 3 months
• Fever lasting more than 3 days in adults

**Red Flag Symptoms:**
• Confusion or altered mental state
• Severe abdominal pain
• Difficulty breathing
• Persistent high fever despite treatment
• Signs of serious infection

**Recovery Expectations:**
Most fevers resolve within 3-5 days with appropriate care and rest.

**Medical Disclaimer:** High fevers or fevers with concerning symptoms require professional medical evaluation."""

    elif any(word in query_lower for word in ["joint", "arthritis", "stiffness", "muscle"]):
        return """**Medical Consultation: Joint and Musculoskeletal Symptoms**

**Symptom Assessment:**
Joint pain and stiffness can indicate various conditions including arthritis, muscle strain, or inflammatory disorders.

**Immediate Pain Management:**
• Rest affected joints and avoid aggravating activities
• Apply ice for acute injuries (first 24-48 hours)
• Apply heat for chronic stiffness and muscle tension
• Gentle range-of-motion exercises as tolerated
• Over-the-counter anti-inflammatory medications as directed

**Activity Modification:**
• Avoid high-impact activities during acute symptoms
• Use supportive devices (braces, ergonomic tools) if needed
• Maintain gentle movement to prevent stiffness
• Balance activity with adequate rest

**Self-Care Measures:**
• Maintain healthy weight to reduce joint stress
• Regular low-impact exercise (swimming, walking)
• Proper posture and ergonomics
• Adequate sleep for tissue repair
• Stress management techniques

**Types of Joint Conditions:**
• Osteoarthritis: wear-and-tear arthritis
• Rheumatoid arthritis: autoimmune condition
• Gout: crystal arthritis
• Fibromyalgia: widespread muscle pain
• Bursitis: inflammation of joint cushions

**When to Seek Medical Care:**
• Severe joint pain limiting daily activities
• Joint swelling, warmth, or redness
• Morning stiffness lasting more than 1 hour
• Fever with joint pain
• Inability to bear weight or use affected joint
• Symptoms not improving with self-care

**Diagnostic Considerations:**
Healthcare providers may recommend blood tests, imaging studies, or joint fluid analysis for proper diagnosis.

**Long-term Management:**
• Physical therapy for strength and flexibility
• Occupational therapy for daily living adaptations
• Medication management as prescribed
• Regular monitoring by healthcare providers

**Medical Disclaimer:** Persistent joint symptoms require professional evaluation for accurate diagnosis and appropriate treatment planning."""

    # Greetings
    elif any(word in query_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return random.choice(MEDICAL_GREETINGS)
    
    # General medical response
    else:
        return """**Medical Consultation Service**

Thank you for reaching out for medical guidance. To provide you with the most accurate and helpful information, please describe your specific symptoms or health concerns in detail.

**Information That Helps:**
• Specific symptoms you're experiencing
• Duration of symptoms
• Severity level (mild, moderate, severe)
• Any associated symptoms
• Factors that make symptoms better or worse
• Your age range and general health status
• Any current medications or treatments

**Our Medical Coverage Includes:**
• General medicine and internal medicine
• Cardiovascular health
• Respiratory conditions
• Gastrointestinal disorders
• Neurological symptoms
• Musculoskeletal problems
• Dermatological conditions
• Mental health support
• Endocrine disorders
• Infectious diseases

**Professional Medical Guidance:**
I provide evidence-based medical information and recommendations while always emphasizing the importance of professional medical care when appropriate.

Please describe your specific health concern or symptoms, and I'll provide comprehensive medical guidance tailored to your situation.

**Medical Disclaimer:** This consultation service provides general medical information and should not replace professional medical advice, diagnosis, or treatment."""

def get_ai_response(prompt: str) -> str:
    """Try different AI providers in order of preference"""
    
    # Try Ollama first (local, completely free)
    if USE_FREE_AI:
        response = call_ollama_ai(prompt)
        if response and len(response) > 50:
            return response
    
    # Try Hugging Face API (free tier)
    if USE_FREE_AI and HUGGINGFACE_TOKEN:
        response = call_huggingface_ai(prompt)
        if response and len(response) > 50:
            return response
    
    # Fallback to professional medical response system (always works, always free)
    return generate_professional_medical_response(prompt)

@app.get("/")
def home():
    return FileResponse("health_website.html")

@app.get("/test-ai")
def test_ai():
    """Test which AI services are available"""
    status = {
        "ollama": False,
        "huggingface": False,
        "medical_database": True,
        "conditions_count": len(MEDICAL_CONDITIONS)
    }
    
    # Test Ollama
    try:
        test_response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if test_response.status_code == 200:
            models = test_response.json().get("models", [])
            status["ollama"] = len(models) > 0
            status["ollama_models"] = [m.get("name", "") for m in models]
    except:
        pass
    
    # Test Hugging Face
    status["huggingface"] = bool(HUGGINGFACE_TOKEN)
    
    return {
        "message": "Medical AI Service Status",
        "services": status,
        "medical_specialties": list(MEDICAL_SPECIALTIES.values()),
        "recommendation": "Professional medical database with AI enhancement" + (" + Ollama local AI" if status["ollama"] else "")
    }

@app.post("/chat")
def chat(query: UserQuery):
    try:
        context = get_or_create_context(query.session_id)
        user_message = query.question.lower().strip()
        
        # Handle greetings
        if any(greeting in user_message for greeting in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            response_text = random.choice(MEDICAL_GREETINGS)
            context.messages.append({"role": "user", "content": query.question})
            context.messages.append({"role": "assistant", "content": response_text})
            return {"answer": response_text}
        
        # Check for specific medical conditions in database
        condition_info = search_medical_condition(user_message)
        if condition_info:
            response_text = format_medical_response(condition_info, user_message)
            context.messages.append({"role": "user", "content": query.question})
            context.messages.append({"role": "assistant", "content": response_text})
            return {"answer": response_text}
        
        # Use AI response system (free alternatives + professional medical responses)
        response_text = get_ai_response(query.question)
        
        # Store in conversation memory
        context.messages.append({"role": "user", "content": query.question})
        context.messages.append({"role": "assistant", "content": response_text})
        
        return {"answer": response_text}
        
    except Exception as e:
        print(f"Error in medical consultation: {str(e)}")
        
        error_responses = [
            "I apologize for the technical difficulty. Please try rephrasing your medical question, and I'll provide professional guidance.",
            "I'm experiencing a temporary issue. Please describe your symptoms again, and I'll offer comprehensive medical information.",
            "Technical error encountered. Please restate your health concern, and I'll provide detailed medical consultation."
        ]
        return {"answer": random.choice(error_responses)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
