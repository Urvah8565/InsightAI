from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

client = Groq(api_key=api_key)


response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {'role':'user','content':'how are u'}
    ]
)

ai_reply = response.choices[0].message.content

print(ai_reply)
