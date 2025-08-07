import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from a .env file
load_dotenv()

# It's good practice to check if the key was loaded successfully
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in a .env file.")

def main():
    # --- FIX 1: Configure the library with your API key ---
    # The genai library is configured directly, not through a Client object.
    genai.configure(api_key=api_key)

    # --- FIX 2: Create a GenerativeModel instance ---
    # You specify the model you want to use here.
    # 'gemini-1.5-flash-latest' is a great, fast choice.
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    # --- FIX 3: Removed typo 'U>' from the end of the string ---
    mystr = "Why is Boot.dev such a great place to learn backend development?"

    # The generate_content method is called on the model object
    response = model.generate_content(mystr)
    
    # The response object has a .text attribute for the model's output
    print(response.text)
    
    # Print usage metadata
    print("-" * 20) # A separator for clarity
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    
    # --- FIX 4: Corrected typo 'canidates' to 'candidates' and removed trailing '>' ---
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
