import google.generativeai as genai

# Initialize Gemini model
def configure_gemini(api_key: str, model_name: str = 'gemini-1.5-flash'):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def generate_question(model, field_label: str, lang: str = "en") -> str:
    prompt = f"Generate a only a polite question in {lang} asking the user to provide input for the field '{field_label}'."
    response = model.generate_content(prompt)
    return response.text.strip()
