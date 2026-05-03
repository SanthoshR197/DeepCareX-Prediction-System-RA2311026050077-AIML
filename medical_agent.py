import os
from groq import Groq
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), "secret.env")
load_dotenv(env_path)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    client = None
else:
    client = Groq(api_key=api_key)

def get_medical_advice(diagnosis):
    if client is None:
        return "System Error: AI client not initialized."

    prompt = f"""
    You are a professional Medical AI Assistant. 
    The diagnostic model has detected: {diagnosis}.
    
    Tasks:
    1. Explain what {diagnosis} is in simple terms for a non-medical person.
    2. Provide 3 actionable health tips (lifestyle/precaution) for a patient.
    3. Include this exact disclaimer: "DISCLAIMER: This is an AI-generated summary for informational purposes and not a formal medical diagnosis."
    
    Keep the tone professional, clear, and empathetic.
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.5,
            max_tokens=500
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def chat_with_agent(diagnosis, messages):
    if client is None:
        return "System Error: AI client not initialized."

    system_prompt = {
        "role": "system",
        "content": f"You are a professional Medical AI Specialist. The patient has been diagnosed with: {diagnosis}. You must provide specific, concise, and professional advice. Do not repeat your introduction if you have already greeted the patient. Always maintain context of the conversation."
    }
    
    full_messages = [system_prompt] + messages

    try:
        chat_completion = client.chat.completions.create(
            messages=full_messages,
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=800
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    result = get_medical_advice("Pneumonia")
    print(result)