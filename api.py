# imports
import os
from dotenv import load_dotenv
import logging
from openai import OpenAI

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# loading environmental variables to access api key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No API key found!")

# initializing the client
client = OpenAI()

def get_response(instruction, code):
    logging.info("Get response started...")
    response = client.chat.completions.create(
        # model="gpt-4o",
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": instruction
            },
            {
            "role": "user",
            "content": code
            }
        ],
        response_format={"type": "text"},
        temperature=0.0,
        # temperature=0.3,
        # temperature=1.0,
        max_tokens=2048,
        top_p=1
    )
    return response.choices[0].message.content

def analyze_error(code):
    logging.info("Analyzing error...")
    return get_response("Egy programkódot fogsz kapni. Keresd meg benne a hibákat, és foglald össze őket tömören és lényegre törően, programozók számára.", code)

def analyze_opt(code):
    logging.info("Analyzing optimalization...")
    return get_response("Egy programkódot fogsz kapni. Keresd meg benne az optimalizálási lehetőségeket, és foglald össze őket tömören és lényegre törően, programozók számára.", code)

def analyze_sec(code):
    logging.info("Analyzing security...")
    return get_response("Egy programkódot fogsz kapni. Keresd meg, milyen biztonsági rések vannak benne, és foglald össze őket tömören és lényegre törően, programozók számára.", code)