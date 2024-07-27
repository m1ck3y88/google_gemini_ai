from env.api_key import api_key
import google.generativeai as genai

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

print("Google Generative AI Setup Completed Successfully!")

