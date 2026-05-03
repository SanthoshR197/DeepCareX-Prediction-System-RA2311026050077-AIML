import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv("secret.env")
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

print("\n--- INFERENCE ENGINE TEST ---")
print("Engine: Groq LPU (Language Processing Unit)")
print("Model: llama-3.1-8b-instant")

start_time = time.time()

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Explain why early diagnosis is important."}],
    model="llama-3.1-8b-instant",
)

end_time = time.time()

print("\n[INFERENCE RESPONSE]:")
print(chat_completion.choices[0].message.content[:200] + "...")
print(f"\n[INFERENCE TIME]: {end_time - start_time:.2f} seconds")
print("-----------------------------\n")
