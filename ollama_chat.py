# Ollama Chat Assistant
# A simple tool to chat with local AI models
# Built by Cody - March 2026

import requests
def chat_with_ollama(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    return result["response"]

def main():
    print("Welcome to your Local AI Assistant!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        response = chat_with_ollama(user_input)
        print(f"\nAI: {response}\n")

if __name__ == "__main__":
    main()