import os
import google.generativeai as genai
from meta_ai_api import MetaAI



genai.configure(api_key="xxx")

model = genai.GenerativeModel("gemini-pro")

ai = MetaAI()

def META_PROMPT(messagePROMPT):
    try:
        responseMeta = ai.prompt(message=messagePROMPT)
        print("[Meta]: \t")
        print(responseMeta)
    except Exception as e:
        print(f"[MetaAI Error]: {e}")
    print("<--------END OF PROMPT-------->")



# def GOOGLE_PROMPT(messagePROMPT):
#     try:
#         response = model.generate_content(messagePROMPT)  
#         output = response.text if hasattr(response, 'text') else "No response received."
#         print("[Google]: \t"+output)
#     except Exception as e:
#         print(f"[Google AI Error]: {e}")
#     print("<--------END OF PROMPT-------->")

