from openai import OpenAI
import os
from pydantic import BaseModel
import json
from pylabeador import syllabify

class Pregunta(BaseModel):
    pregunta: str
    respuestas: list[str]
    correcta: str

class Test(BaseModel):
    preguntas: list[Pregunta]

class OpenAIGpt:
    def __init__(self):
        self.client = OpenAI(os.getenv("OPENAI_API_KEY"))

    def format_message(self, message: str) -> str:
        
        formatted_message = ""

        for word in message.split():
            clean_word = ''.join(e for e in word if e.isalnum())
            syllables = syllabify(clean_word)
            if len(syllables) > 3:
                formatted_message += f"**{syllables[0]}{syllables[1]}**{word[len(syllables[0] + syllables[1]):]} "
            elif len(syllables) <= 3 and len(syllables) > 1:
                formatted_message += f"**{syllables[0]}**{word[len(syllables[0]):]} "
            else:
                formatted_message += f"{word} "
        return formatted_message

    def emoji(self, message: str) -> str:

        prompt = f"Sobre este texto necesito que lo adaptes para personas con dislexia de la siguiente manera, las palabras que tengan un emoticono conocido (por ejemplo en vez de agua pones 💧) por un emoji que signifique lo mismo en caso de que sea posible: {message}"

        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Cambia palabras clave conocidas por emoticonos"},
                {"role": "user", "content": prompt},
            ]
        )
        message = completion.choices[0].message.content
        return message
    
    def empathy(self, message: str) -> str:
        prompt = f"Modifica este texto cambiando el orden de algunas letras o palabras para que los alumnos sin problemas de dislexia puedan entender mejor lo que sienten las personas con dislexia (Algunas, NO TODAS): {message}"

        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Cambia el orden de las letras o palabras para simular dislexia moderada"},
                {"role": "user", "content": prompt},
            ]
        )
        message = completion.choices[0].message.content
        return message
    
    def absurdity(self, subject: str) -> str:
        prompt = f"Genera 5 preguntas tipo test, las 3 primeras correctas (con sus respectivas respuetas) y las 2 últimas absurdas (que el enunciado de x datos y pregunté por z dato, con todo posibles respuestas, para liar mas) sobre el tema de {subject}"

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Genera preguntas tipo test sobre el tema dado para niños como una historia, con ejemplos y planteamiento para niños"},
                {"role": "user", "content": prompt},
            ],
            response_format=Test
        )
        message = completion.choices[0].message.parsed
        message = message.json()
        message = json.loads(message)
        return message