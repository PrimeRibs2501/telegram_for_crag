import telebot
import requests
import json
from settings import settings

bot = telebot.TeleBot(settings.API_KEY)
url = f'{settings.HOST}:{settings.API_PORT}/{settings.CHAT_URL}'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    texto = """
    Olá, eu sou o bot do ICMC! Estarei aqui para te ajudar 
a encontrar informações sobre o Instituto de Ciências Matemáticas e de Computação da USP.

Me diga, como posso te ajudar?  
    """
    bot.reply_to(message, texto)

def chat_response(message: str, user_id: str) -> str:
    user_input = message
    payload = {
        "message": user_input, 
        "user_id": str(user_id)
    }
    llm_response = requests.post(url, json=payload)
    response_json = llm_response.json()
    
    # Verifica se o campo "response" existe
    ai_content = response_json.get("response", "")
    if isinstance(ai_content, str):
        # Tenta interpretar o JSON dentro do campo "response"
        try:
            parsed_response = json.loads(ai_content)
            # Aqui você pode processar o conteúdo do JSON como desejar
            return f"Tool: {parsed_response.get('name', 'N/A')}, Query: {parsed_response.get('arguments', {}).get('query', 'N/A')}"
        except json.JSONDecodeError:
            # Se não for um JSON válido, retorna o texto bruto
            return ai_content
    else:
        return "Desculpe, não consegui processar sua solicitação no momento."

@bot.message_handler(func=lambda message: True)
def send_noticias(message):

    response = chat_response(message.text, message.from_user.id)
    bot.reply_to(message, response)

bot.polling(none_stop=True, interval=0, timeout=60)