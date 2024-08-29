import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("API key for Google Generative AI is not set in the environment variables.")
   

genai.configure(api_key=api_key)

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def process_image_with_gemini(file_path):
    """Process the image and get a response from Gemini."""
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    
    # Upload the image
    uploaded_file = upload_to_gemini(file_path, mime_type="image/jpeg")

    # Create a chat session and get a response
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    uploaded_file,
                    "Describe the image."
                ],
            }
        ]
    )

    response = chat_session.send_message("Analyze the image and provide details.")
    return response.text
