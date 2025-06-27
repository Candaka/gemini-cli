import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# --- Configuration ---
MODEL_NAME = "gemini-2.5-flash-lite-preview-06-17" # More common and stable model

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Initialization ---
if not api_key:
    print("Error: GEMINI_API_KEY not found. Please set it in your .env file.")
    sys.exit(1)

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(MODEL_NAME)

# Main Q&A loop
def ask_gemini():
    print("🔍 Gemini Q&A Tool (type 'exit' to quit)\n")
    print(f"Using model: {MODEL_NAME}\n")
    while True:
        prompt = input("Your question: ")
        if prompt.lower() == "exit":
            break
        try:
            response = model.generate_content(prompt)
            print("Gemini:", response.text.strip(), "\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    ask_gemini()
