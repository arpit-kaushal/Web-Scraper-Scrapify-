import requests
from bs4 import BeautifulSoup
from groq import Groq

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

MODELS = {
    'Gemma2 💎': 'gemma2-9b-it',
    'Mixtral 🚀': 'mixtral-8x7b-32768' 
}


SELECTED_MODEL = MODELS['Mixtral 🚀']  

def scrape_website(url):
    """
    Scrape text content from a website.
    """
    try:
      
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')
        text_content = " ".join([p.get_text() for p in paragraphs])

        return text_content
    except Exception as e:
        return f"Error scraping website: {e}"

def summarize_text(text, model=SELECTED_MODEL, max_tokens=30000):
    """
    Summarize text using the selected Groq model.
    """
    try:
 
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error summarizing text: {e}"

def chat_with_llm(message, context="", model=SELECTED_MODEL,max_tokens=30000):
    """
    Generate a response using the selected Groq model.
    """
    try:
 
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{context}\n\nUser: {message}\nAI:"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"

def select_model(model_name):
    """
    Select the model for summarization and chatbot.
    """
    global SELECTED_MODEL
    if model_name in MODELS:
        SELECTED_MODEL = MODELS[model_name]
        return f"Model changed to {model_name}"
    else:
        return "Invalid model selected"