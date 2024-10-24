from openai import OpenAI
import os
from pydantic import BaseModel
import json
from pylabeador import syllabify
from dotenv import load_dotenv

class Pregunta(BaseModel):
    pregunta: str
    respuestas: list[str]
    correcta: str

class Test(BaseModel):
    preguntas: list[Pregunta]

class Course(BaseModel):
    normal: list[str]
    emoji: list[str]

class OpenAIGpt:
    def __init__(self):
        load_dotenv(os.path.join(os.getcwd(), "generation-api/.env"))
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def format_message(self, message: str) -> str:

        formatted_message = ""

        for word in message.split():
            clean_word = ''.join(e for e in word if e.isalnum())
            try:
                syllables = syllabify(clean_word)
            except:
                formatted_message += f"**{word}** "
            # 2 o menos la primera silaba, 3 o mas las dos primeras
            if len(syllables) > 2:
                formatted_message += f"**{syllables[0]}{syllables[1]}**{word[len(syllables[0] + syllables[1]):]} "
            else:
                formatted_message += f"**{syllables[0]}**{word[len(syllables[0]):]} "
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

    def course(self, message: str) -> str:
        prompt = f"Genera un curso sobre {message}"

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Genera un curso sobre el tema dado para niños (6 elementos), tienes que devolver: en 'normal' un array con 6 textos de 3-4 lineas sobre el tema SIN EMOJIS. En 'emoji' un array que contenga los mismos textos pero SUSTITUYENDO algunas palabras por emojis que signifiquen lo mismo (QUITANDO las palabras que ya sean emojis)"},
                {"role": "user", "content": prompt},
            ],
            response_format=Course
        )
        message = completion.choices[0].message.parsed
        message = message.json()
        message = json.loads(message)
        message["resaltado"] = [self.format_message(m) for m in message["normal"]]
        return message

    def absurdity_final(self, subject: str) -> str:
        data =  {
            "message": {
            "preguntas": [
                {
                "text": "Si María tiene 3 cajas y en cada caja hay 5 manzanas, ¿cuántas manzanas tiene en total?",
                "options": [
                    "15 manzanas",
                    "8 manzanas",
                    "10 manzanas",
                    "7 manzanas",
                ],
                "correctAnswer": "15 manzanas",
                },
                {
                "text": "Si un tren tiene 6 vagones y en cada vagón caben 20 personas, ¿cuántas personas caben en todo el tren?",
                "options": [
                    "120 personas",
                    "100 personas",
                    "60 personas",
                    "80 personas",
                ],
                "correctAnswer": "120 personas",
                },
                {
                "text": "Si tengo 10 botas y me quitan 10 sombreros, ¿cuántas gafas me quedan?",
                "options": ["1", "5", "10", "3"],
                "correctAnswer": " ",
                },
                {
                "text": "Pedro tiene 3 gatos, 2 perros y le regalaron 7 peces. ¿Cuántas animales tiene Pedro?",
                "options": ["14 ", "12", "8", "7"],
                "correctAnswer": "12",
                },
                {
                "text": "En Numerolandia, los números tienen colores mágicos. Si el número 5 es azul, el número 7 es amarillo y el número 9 es rojo, ¿cuál es el color del número elefante?",
                "options": ["azul", "amarillo", "rojo", "morado"],
                "correctAnswer": " ",
                },
            ],
            },
        }

        return data
