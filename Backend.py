def diagnose_disease(symptoms):
    """
    Diagnose the disease based on symptoms.
    
    Args:
        symptoms (list): List of symptoms entered by the user.
    
    Returns:
        str: Predicted disease and recommendation.
    """
    # Define symptom patterns for diseases
    common_cold_symptoms = {
        "runny nose", "sneezing", "sore throat", "mild cough", "headache", "low-grade fever"
    }
    chest_infection_symptoms = {
        "persistent cough", "shortness of breath", "chest pain", "high fever", "fatigue", "wheezing"
    }
    
    # Convert user symptoms to lowercase for consistency
    symptoms = set(symptom.lower() for symptom in symptoms)

    # Check symptom overlap with defined patterns
    cold_match = len(symptoms & common_cold_symptoms)
    chest_infection_match = len(symptoms & chest_infection_symptoms)

    # Determine the most likely condition
    if cold_match > chest_infection_match:
        return "Common Cold", (
            "You are likely experiencing a common cold. Rest, stay hydrated, and use over-the-counter medications if needed."
        )
    elif chest_infection_match > cold_match:
        return "Chest Infection", (
            "You might have a chest infection. Please consider consulting a doctor for proper diagnosis and treatment."
        )
    elif cold_match == chest_infection_match and cold_match > 0:
        return "Mixed Symptoms", (
            "Your symptoms overlap between a common cold and a chest infection. It's best to consult a doctor for an accurate diagnosis."
        )
    else:
        return "No Diagnosis", (
            "The symptoms provided do not match common cold or chest infection patterns. Please recheck your symptoms or consult a doctor."
        )
