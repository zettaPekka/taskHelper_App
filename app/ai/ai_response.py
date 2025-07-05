from os import getenv

import openai
from dotenv import load_dotenv

from ai.image_processing import encode_image


load_dotenv()

client = openai.AsyncOpenAI(
    base_url="https://api.llm7.io/v1",
    api_key=getenv("AI_TOKEN")
)
model = 'gpt-o3-2025-04-16'


async def answer_to_photo(image: str, action: str) -> str:
    base64_image = encode_image(image)
    
    task = 'Просто дать подсказку как решить задачу, но не решать полностью' if action == 'help' else 'Решить задачу полностью с обьяснением'
    
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {
                'role':'system',
                'content':f'Ты помощник который решает разные задачи от пользователя, твоя задача {task}. Не стилизуй ответ никак (нельзя использовать latex и markdown). Отвечай на русском языке'
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )
    
    response = response.choices[0].message.content.replace('\n', '<br>')
    return response


async def answer_to_text(text: str, action: str) -> str:
    task = 'Просто дать подсказку как решить задачу, но не решать полностью' if action == 'help' else 'Решить задачу полностью с обьяснением'
    
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {
                'role':'system',
                'content':f'Ты помощник который решает разные задачи от пользователя, твоя задача {task}. Не стилизуй ответ никак (нельзя использовать latex и markdown). Отвечай на русском языке'
            },
            {
                "role": "user",
                "content": text
            }
        ],
    )
    
    response = response.choices[0].message.content.replace('\n', '<br>')
    return response