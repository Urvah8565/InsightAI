from data_loader import load_dataset
from profiler import profile_dataset
from data_processor import detect_column_types
from data_processor import check_data_quality
from data_processor import analyze_dataset
from data_processor import calculate_category
from data_processor import calculate_average
from data_processor import date_time
from groq import Groq
import os
from dotenv import load_dotenv
import json
import pandas as pd


load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

client = Groq(api_key=api_key)





tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_average",
            'description':'Calculate the average of a specified numeric column.',
            "parameters": {
                "type": "object",
                "properties": {
                    "column_name": {
                        'type':'string',
                        'description':'The name of the numeric column to analyze'
                    },
                },
                "required": ["column_name"]
            }
        }
    }
]

response = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[
        {"role":'system','content':'you are one of the best data analyst and u calculate the most accurate calculations'},
        {'role':'user','content':'What is the average Revenue of column_name '}
    ],
    tools=tools,
    tool_choice='auto',
)

ai_reply = response.choices[0].message.tool_calls[0]

print(ai_reply)

 
tool_name = ai_reply.function.name

tool_args_string = ai_reply.function.arguments

print(tool_name)
print(tool_args_string)

tool_load = json.loads(tool_args_string)

print(tool_load)

df = load_dataset(file_path='data/sales.csv')
result = calculate_average(df, tool_load['column_name'])
print(result)

final_response = client.chat.completions.create(
   model='openai/gpt-oss-120b',
   messages=[
      {'role':'user','content':'what is the average revenue give me the detail natural answer'},

      response.choices[0].message,

      {'role':'tool','content':str(result),'tool_call_id':ai_reply.id}
   ]
)


final_reply = final_response.choices[0].message.content

print(final_reply)




