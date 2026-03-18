"""
Google Gemini client module.
Provides a helper function to call the Google Gemini model.
"""

import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the Gemini API client
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Use the recommended Gemini model for general text tasks
MODEL_ID = "gemini-2.5-flash"

def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Google Gemini and return the generated text.

    Args:
        prompt: The user prompt to send to the model.

    Returns:
        The model's response text, or an error message on failure.
    """
    try:
        model = genai.GenerativeModel(MODEL_ID)
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=4096,
                temperature=0.7,
                top_p=0.9,
            )
        )
        
        if response.text:
            return response.text
        return "No response generated."

    except Exception as e:
        return f"[Error] Failed to get response from Gemini: {str(e)}"
