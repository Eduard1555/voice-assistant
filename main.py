import os
import eel
import random
import pyttsx3
import openai
from datetime import datetime

OPENAI_API_KEY = ("sk-SM3Pjh_wBJWWC4Bd0Sw0Ok_WBjIppgeyKywKKp8lZVQ4GNDUkJ-mId7TTLq-"
                  "n6FeklrjKdAPsOT3BlbkFJLy4SKW20Y3xRic5Xb451WWg6jBdZAxiXQnll3rmRzz8AGrJj_nM7u7slAd2fzmxPKT7Vz4_IUA")
openai.api_key = OPENAI_API_KEY

# functie pt text to speech
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    romanian_voice = next((voice for voice in voices if "ro_RO" in voice.id or "Romanian" in voice.name), None)

    if romanian_voice:
        engine.setProperty('voice', romanian_voice.id)
    else:
        print("Romanian voice not found. Using default voice.")
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', 175)
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

#eel frontend
eel.init("FEnd")

# raspunsurile predefinite
responses = {
    "Cine a făcut acest Asistent Virtual?": [
        "Am fost creat de Manea Mihai Eduard.",
        "Manea Mihai Eduard m-a creat!",
    ],
    "Care este numele profesorului meu de Micro Procesoare?": [
        "Numele profesorului tău este Mircea Giurgiu.",
        "Nu este cumva Mircea Giurgiu?",
        "Cred că este Mircea Giurgiu"
    ],
    "Care este capitala României?": [
        "Capitala României este București!",
        "București!!",
    ],
    "Cum este vremea astăzi?": [
        "Vremea este foarte frumoasă astăzi!",
        "Astăzi va ploua, să nu îți uiți umbrela!",
    ],
    "Care este viteza luminii?": [
        "Viteza luminii este de 299,792 kilometri pe secundă.",
    ],
    "Care este numele tău?": [
        "Eduard nu mi-a dat un nume așa că spune-mi cum vrei!",
        "Nu am un nume dar poți să mă numești cum vrei!",
    ],
}

DAYS_RO = {
    "Monday": "Luni", "Tuesday": "Marți", "Wednesday": "Miercuri",
    "Thursday": "Joi", "Friday": "Vineri", "Saturday": "Sâmbătă", "Sunday": "Duminică"
}
MONTHS_RO = {
    "January": "Ianuarie", "February": "Februarie", "March": "Martie", "April": "Aprilie",
    "May": "Mai", "June": "Iunie", "July": "Iulie", "August": "August",
    "September": "Septembrie", "October": "Octombrie", "November": "Noiembrie", "December": "Decembrie"
}

# functia pt a lua raspunsurile predefinite
@eel.expose
def get_response(question):
    if question == "În ce dată suntem?":
        now = datetime.now()
        day_ro = DAYS_RO[now.strftime("%A")]
        month_ro = MONTHS_RO[now.strftime("%B")]
        return f"Astăzi este ziua de {day_ro}, {now.day} {month_ro} {now.year}."
    elif question == "Cât este ceasul?":
        now = datetime.now()
        return f"Este {now.strftime('%H:%M')}."
    elif question in responses:
        return random.choice(responses[question])
    else:
        return "Nu sunt sigur. Întreabă-mă altceva!"

# functie pt response chatgpt
@eel.expose
def get_chatgpt_response(question):
    try:
        print(f"Received question for ChatGPT: {question}")
        response = openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that answers in Romanian."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        print(f"ChatGPT Response: {answer}")
        return answer
    except openai.error.OpenAIError as e:
        print(f"Error with OpenAI API: {e}")
        return "Ne pare rău, dar nu am putut obține un răspuns de la ChatGPT."

# functia pt tts
@eel.expose
def speak_response(response_text):
    """Read the response aloud."""
    speak(response_text)

if __name__ == "__main__":
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
