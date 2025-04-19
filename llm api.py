import requests

OLLAMA_URL = "http://localhost:11434/api/generate"  
MODEL_NAME = "llama2"   

def generate_response(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    
    if response.status_code == 200:
        result = response.json()
        reply = result.get("response", "I'm here for you. Can you tell me more?")
        print("AI:", reply)
        return reply
