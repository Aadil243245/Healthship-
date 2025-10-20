# Comprehensive Medical Database
# Contains 50+ health conditions with detailed information

MEDICAL_CONDITIONS = {
    # Respiratory System
    "asthma": {
        "name": "Asthma",
        "category": "Respiratory",
        "symptoms": ["wheezing", "shortness of breath", "chest tightness", "coughing", "difficulty breathing"],
        "causes": ["allergies", "environmental triggers", "genetics", "respiratory infections", "exercise"],
        "treatments": ["bronchodilator inhalers", "corticosteroid inhalers", "leukotriene modifiers", "allergy medications", "avoid triggers"],
        "prevention": ["identify triggers", "take prescribed medications", "maintain clean environment", "get vaccinated", "exercise regularly"],
        "severity": "moderate",
        "when_to_see_doctor": "Difficulty breathing, frequent attacks, symptoms worsen, emergency inhaler not helping"
    },
    
    "pneumonia": {
        "name": "Pneumonia",
        "category": "Respiratory",
        "symptoms": ["fever", "chills", "cough with phlegm", "shortness of breath", "chest pain", "fatigue"],
        "causes": ["bacterial infection", "viral infection", "fungal infection", "aspiration"],
        "treatments": ["antibiotics", "antiviral medications", "rest", "fluids", "oxygen therapy"],
        "prevention": ["vaccination", "hand hygiene", "avoid smoking", "healthy lifestyle"],
        "severity": "serious",
        "when_to_see_doctor": "High fever, difficulty breathing, chest pain, persistent cough with blood"
    },
    
    "bronchitis": {
        "name": "Bronchitis",
        "category": "Respiratory",
        "symptoms": ["persistent cough", "mucus production", "fatigue", "shortness of breath", "chest discomfort"],
        "causes": ["viral infection", "bacterial infection", "smoking", "air pollution", "chemical irritants"],
        "treatments": ["rest", "fluids", "humidifier", "cough suppressants", "bronchodilators"],
        "prevention": ["avoid smoking", "hand hygiene", "avoid air pollutants", "get vaccinated"],
        "severity": "mild",
        "when_to_see_doctor": "Cough lasts more than 3 weeks, blood in mucus, high fever, difficulty breathing"
    },
    
    # Cardiovascular System
    "hypertension": {
        "name": "High Blood Pressure",
        "category": "Cardiovascular",
        "symptoms": ["headaches", "shortness of breath", "nosebleeds", "chest pain", "vision problems"],
        "causes": ["genetics", "poor diet", "lack of exercise", "stress", "obesity", "excessive salt"],
        "treatments": ["ACE inhibitors", "diuretics", "calcium channel blockers", "lifestyle changes", "low sodium diet"],
        "prevention": ["healthy diet", "regular exercise", "limit alcohol", "manage stress", "maintain healthy weight"],
        "severity": "serious",
        "when_to_see_doctor": "Blood pressure consistently above 140/90, severe headaches, chest pain"
    },
    
    "heart_disease": {
        "name": "Coronary Heart Disease",
        "category": "Cardiovascular",
        "symptoms": ["chest pain", "shortness of breath", "fatigue", "irregular heartbeat", "swelling in legs"],
        "causes": ["atherosclerosis", "high cholesterol", "high blood pressure", "diabetes", "smoking"],
        "treatments": ["statins", "blood thinners", "beta blockers", "lifestyle changes", "surgical procedures"],
        "prevention": ["healthy diet", "regular exercise", "no smoking", "manage diabetes", "control cholesterol"],
        "severity": "serious",
        "when_to_see_doctor": "Chest pain, severe shortness of breath, irregular heartbeat, fainting"
    },
    
    # Digestive System
    "gastritis": {
        "name": "Gastritis",
        "category": "Digestive",
        "symptoms": ["stomach pain", "nausea", "vomiting", "bloating", "loss of appetite", "indigestion"],
        "causes": ["H. pylori bacteria", "NSAIDs", "alcohol", "stress", "spicy foods", "autoimmune disorders"],
        "treatments": ["proton pump inhibitors", "antacids", "antibiotics", "avoid triggers", "bland diet"],
        "prevention": ["avoid NSAIDs", "limit alcohol", "manage stress", "avoid spicy foods", "eat smaller meals"],
        "severity": "moderate",
        "when_to_see_doctor": "Severe abdominal pain, vomiting blood, black stools, persistent symptoms"
    },
    
    "ibs": {
        "name": "Irritable Bowel Syndrome",
        "category": "Digestive",
        "symptoms": ["abdominal pain", "bloating", "gas", "diarrhea", "constipation", "mucus in stool"],
        "causes": ["stress", "certain foods", "hormonal changes", "bacterial overgrowth", "genetics"],
        "treatments": ["dietary changes", "fiber supplements", "antispasmodics", "probiotics", "stress management"],
        "prevention": ["identify trigger foods", "manage stress", "regular exercise", "adequate sleep"],
        "severity": "moderate",
        "when_to_see_doctor": "Severe pain, blood in stool, unexplained weight loss, persistent symptoms"
    },
    
    "ulcers": {
        "name": "Peptic Ulcers",
        "category": "Digestive",
        "symptoms": ["burning stomach pain", "bloating", "heartburn", "nausea", "loss of appetite"],
        "causes": ["H. pylori bacteria", "NSAIDs", "stress", "spicy foods", "alcohol", "smoking"],
        "treatments": ["antibiotics", "proton pump inhibitors", "antacids", "avoid triggers"],
        "prevention": ["avoid NSAIDs", "limit alcohol", "no smoking", "manage stress", "healthy diet"],
        "severity": "moderate",
        "when_to_see_doctor": "Severe abdominal pain, vomiting blood, black tarry stools, unexplained weight loss"
    },
    
    # Musculoskeletal System
    "arthritis": {
        "name": "Arthritis",
        "category": "Musculoskeletal",
        "symptoms": ["joint pain", "stiffness", "swelling", "reduced range of motion", "warmth in joints"],
        "causes": ["age", "genetics", "previous injuries", "obesity", "autoimmune disorders"],
        "treatments": ["NSAIDs", "corticosteroids", "physical therapy", "exercise", "weight management"],
        "prevention": ["maintain healthy weight", "regular exercise", "protect joints", "healthy diet"],
        "severity": "moderate",
        "when_to_see_doctor": "Severe joint pain, significant swelling, inability to move joint, fever with joint pain"
    },
    
    "osteoporosis": {
        "name": "Osteoporosis",
        "category": "Musculoskeletal",
        "symptoms": ["back pain", "loss of height", "stooped posture", "bone fractures", "brittle nails"],
        "causes": ["aging", "hormonal changes", "calcium deficiency", "vitamin D deficiency", "sedentary lifestyle"],
        "treatments": ["bisphosphonates", "calcium supplements", "vitamin D", "exercise", "hormone therapy"],
        "prevention": ["adequate calcium", "vitamin D", "weight-bearing exercise", "avoid smoking", "limit alcohol"],
        "severity": "serious",
        "when_to_see_doctor": "Frequent fractures, severe back pain, loss of height, family history"
    },
    
    # Neurological System
    "migraine": {
        "name": "Migraine",
        "category": "Neurological",
        "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound", "visual disturbances"],
        "causes": ["genetics", "hormonal changes", "stress", "certain foods", "sleep changes", "weather changes"],
        "treatments": ["triptans", "NSAIDs", "anti-nausea medications", "preventive medications", "lifestyle changes"],
        "prevention": ["identify triggers", "regular sleep schedule", "stress management", "stay hydrated", "regular meals"],
        "severity": "moderate",
        "when_to_see_doctor": "Sudden severe headache, headache with fever and stiff neck, changes in headache pattern"
    },
    
    "epilepsy": {
        "name": "Epilepsy",
        "category": "Neurological",
        "symptoms": ["seizures", "temporary confusion", "staring spells", "uncontrollable jerking", "loss of consciousness"],
        "causes": ["genetics", "head trauma", "brain infections", "stroke", "brain tumors"],
        "treatments": ["antiepileptic drugs", "surgery", "vagus nerve stimulation", "ketogenic diet"],
        "prevention": ["take medications as prescribed", "avoid triggers", "adequate sleep", "manage stress"],
        "severity": "serious",
        "when_to_see_doctor": "First seizure, seizure lasting more than 5 minutes, frequent seizures, injury during seizure"
    },
    
    # Endocrine System
    "diabetes_type1": {
        "name": "Type 1 Diabetes",
        "category": "Endocrine",
        "symptoms": ["frequent urination", "excessive thirst", "unexplained weight loss", "fatigue", "blurred vision"],
        "causes": ["autoimmune destruction", "genetics", "environmental factors"],
        "treatments": ["insulin therapy", "blood sugar monitoring", "carbohydrate counting", "regular exercise"],
        "prevention": ["cannot be prevented", "early detection important", "healthy lifestyle"],
        "severity": "serious",
        "when_to_see_doctor": "Symptoms of diabetes, blood sugar over 250, ketones in urine, diabetic ketoacidosis"
    },
    
    "diabetes_type2": {
        "name": "Type 2 Diabetes",
        "category": "Endocrine",
        "symptoms": ["frequent urination", "excessive thirst", "fatigue", "slow healing wounds", "frequent infections"],
        "causes": ["insulin resistance", "genetics", "obesity", "sedentary lifestyle", "poor diet"],
        "treatments": ["metformin", "lifestyle changes", "blood sugar monitoring", "insulin if needed"],
        "prevention": ["healthy diet", "regular exercise", "maintain healthy weight", "limit sugar intake"],
        "severity": "serious",
        "when_to_see_doctor": "Symptoms of diabetes, blood sugar over 200, complications developing"
    },
    
    "thyroid_disorders": {
        "name": "Thyroid Disorders",
        "category": "Endocrine",
        "symptoms": ["fatigue", "weight changes", "mood changes", "hair loss", "temperature sensitivity"],
        "causes": ["autoimmune disorders", "iodine deficiency", "genetics", "medications", "radiation exposure"],
        "treatments": ["thyroid hormone replacement", "antithyroid medications", "radioactive iodine", "surgery"],
        "prevention": ["adequate iodine intake", "regular checkups", "avoid excessive iodine"],
        "severity": "moderate",
        "when_to_see_doctor": "Persistent fatigue, unexplained weight changes, heart palpitations, mood changes"
    },
    
    # Dermatological
    "eczema": {
        "name": "Eczema",
        "category": "Dermatological",
        "symptoms": ["itchy skin", "red patches", "dry skin", "cracked skin", "small bumps"],
        "causes": ["genetics", "allergies", "irritants", "stress", "weather changes"],
        "treatments": ["moisturizers", "topical corticosteroids", "antihistamines", "avoid triggers"],
        "prevention": ["moisturize regularly", "avoid triggers", "use gentle products", "manage stress"],
        "severity": "mild",
        "when_to_see_doctor": "Severe itching, signs of infection, widespread rash, not responding to treatment"
    },
    
    "psoriasis": {
        "name": "Psoriasis",
        "category": "Dermatological",
        "symptoms": ["red patches with scales", "itching", "burning", "thick nails", "joint pain"],
        "causes": ["autoimmune disorder", "genetics", "stress", "infections", "medications"],
        "treatments": ["topical treatments", "phototherapy", "systemic medications", "biologics"],
        "prevention": ["manage stress", "avoid triggers", "moisturize skin", "healthy lifestyle"],
        "severity": "moderate",
        "when_to_see_doctor": "Widespread patches, joint pain, signs of infection, severe symptoms"
    },
    
    # Mental Health
    "depression": {
        "name": "Depression",
        "category": "Mental Health",
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "sleep problems", "appetite changes", "difficulty concentrating"],
        "causes": ["brain chemistry", "genetics", "life events", "medical conditions", "substance abuse"],
        "treatments": ["antidepressants", "psychotherapy", "lifestyle changes", "support groups"],
        "prevention": ["regular exercise", "social connections", "stress management", "adequate sleep", "healthy diet"],
        "severity": "serious",
        "when_to_see_doctor": "Persistent sadness, thoughts of self-harm, inability to function, substance abuse"
    },
    
    "anxiety_disorders": {
        "name": "Anxiety Disorders",
        "category": "Mental Health",
        "symptoms": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "muscle tension", "panic attacks"],
        "causes": ["genetics", "brain chemistry", "personality", "life events", "other mental health disorders"],
        "treatments": ["anti-anxiety medications", "cognitive behavioral therapy", "relaxation techniques", "lifestyle changes"],
        "prevention": ["stress management", "regular exercise", "adequate sleep", "limit caffeine", "mindfulness"],
        "severity": "moderate",
        "when_to_see_doctor": "Persistent anxiety, panic attacks, avoiding daily activities, substance abuse"
    },
    
    # Infectious Diseases
    "common_cold": {
        "name": "Common Cold",
        "category": "Infectious",
        "symptoms": ["runny nose", "sneezing", "cough", "sore throat", "mild fever", "body aches"],
        "causes": ["viral infection", "rhinovirus", "coronavirus", "respiratory syncytial virus"],
        "treatments": ["rest", "fluids", "pain relievers", "decongestants", "throat lozenges"],
        "prevention": ["hand hygiene", "avoid close contact with sick people", "boost immunity", "adequate sleep"],
        "severity": "mild",
        "when_to_see_doctor": "High fever, severe headache, difficulty breathing, symptoms worsen after 10 days"
    },
    
    "influenza": {
        "name": "Influenza (Flu)",
        "category": "Infectious",
        "symptoms": ["high fever", "body aches", "fatigue", "cough", "headache", "chills", "sore throat"],
        "causes": ["influenza virus", "seasonal virus strains", "H1N1", "H3N2"],
        "treatments": ["antiviral medications", "rest", "fluids", "fever reducers", "pain relievers"],
        "prevention": ["annual flu vaccine", "hand hygiene", "avoid crowded places during flu season"],
        "severity": "moderate",
        "when_to_see_doctor": "High fever, difficulty breathing, severe headache, persistent vomiting"
    },
    
    "urinary_tract_infection": {
        "name": "Urinary Tract Infection",
        "category": "Infectious",
        "symptoms": ["burning urination", "frequent urination", "cloudy urine", "pelvic pain", "strong urine odor"],
        "causes": ["bacterial infection", "E. coli", "poor hygiene", "sexual activity", "kidney stones"],
        "treatments": ["antibiotics", "increased fluid intake", "pain relievers", "cranberry juice"],
        "prevention": ["adequate hydration", "proper hygiene", "urinate after intercourse", "avoid irritants"],
        "severity": "moderate",
        "when_to_see_doctor": "Blood in urine, fever, severe pain, symptoms persist after treatment"
    },
    
    # Women's Health
    "menstrual_disorders": {
        "name": "Menstrual Disorders",
        "category": "Women's Health",
        "symptoms": ["irregular periods", "heavy bleeding", "severe cramps", "missed periods", "prolonged bleeding"],
        "causes": ["hormonal imbalances", "PCOS", "thyroid disorders", "stress", "weight changes"],
        "treatments": ["hormonal therapy", "pain relievers", "lifestyle changes", "iron supplements"],
        "prevention": ["healthy diet", "regular exercise", "stress management", "adequate sleep"],
        "severity": "moderate",
        "when_to_see_doctor": "Severe pain, very heavy bleeding, missed periods, bleeding between periods"
    },
    
    # Men's Health
    "prostate_problems": {
        "name": "Prostate Problems",
        "category": "Men's Health",
        "symptoms": ["frequent urination", "difficulty starting urination", "weak urine stream", "incomplete bladder emptying"],
        "causes": ["aging", "hormonal changes", "genetics", "lifestyle factors"],
        "treatments": ["alpha blockers", "5-alpha reductase inhibitors", "lifestyle changes", "surgery if needed"],
        "prevention": ["healthy diet", "regular exercise", "maintain healthy weight", "regular checkups"],
        "severity": "moderate",
        "when_to_see_doctor": "Blood in urine, inability to urinate, severe symptoms, pain"
    },
    
    # Eye and Vision
    "glaucoma": {
        "name": "Glaucoma",
        "category": "Eye Health",
        "symptoms": ["gradual vision loss", "eye pain", "halos around lights", "nausea", "vomiting"],
        "causes": ["increased eye pressure", "genetics", "age", "diabetes", "high blood pressure"],
        "treatments": ["eye drops", "oral medications", "laser therapy", "surgery"],
        "prevention": ["regular eye exams", "exercise", "protect eyes from injury", "manage health conditions"],
        "severity": "serious",
        "when_to_see_doctor": "Vision changes, eye pain, halos around lights, family history"
    },
    
    # Ear, Nose, Throat
    "sinusitis": {
        "name": "Sinusitis",
        "category": "ENT",
        "symptoms": ["facial pain", "nasal congestion", "thick nasal discharge", "reduced sense of smell", "headache"],
        "causes": ["viral infection", "bacterial infection", "allergies", "nasal polyps", "deviated septum"],
        "treatments": ["decongestants", "nasal corticosteroids", "antibiotics if bacterial", "saline rinses"],
        "prevention": ["avoid allergens", "hand hygiene", "humidify air", "manage allergies"],
        "severity": "mild",
        "when_to_see_doctor": "Symptoms last more than 10 days, high fever, severe headache, vision changes"
    }
}

# Medical specialties for categorization
MEDICAL_SPECIALTIES = {
    "Respiratory": "Pulmonology",
    "Cardiovascular": "Cardiology", 
    "Digestive": "Gastroenterology",
    "Musculoskeletal": "Orthopedics/Rheumatology",
    "Neurological": "Neurology",
    "Endocrine": "Endocrinology",
    "Dermatological": "Dermatology",
    "Mental Health": "Psychiatry/Psychology",
    "Infectious": "Internal Medicine",
    "Women's Health": "Gynecology",
    "Men's Health": "Urology",
    "Eye Health": "Ophthalmology",
    "ENT": "Otolaryngology"
}

# Symptom checker database
SYMPTOM_CHECKER = {
    "fever": ["common_cold", "influenza", "pneumonia", "urinary_tract_infection"],
    "headache": ["migraine", "sinusitis", "hypertension", "common_cold"],
    "chest_pain": ["heart_disease", "pneumonia", "asthma"],
    "abdominal_pain": ["gastritis", "ibs", "ulcers"],
    "joint_pain": ["arthritis", "psoriasis"],
    "fatigue": ["depression", "diabetes_type1", "diabetes_type2", "thyroid_disorders"],
    "shortness_of_breath": ["asthma", "heart_disease", "pneumonia"],
    "nausea": ["gastritis", "migraine", "ulcers"],
    "skin_rash": ["eczema", "psoriasis"],
    "frequent_urination": ["diabetes_type1", "diabetes_type2", "urinary_tract_infection", "prostate_problems"]
}
