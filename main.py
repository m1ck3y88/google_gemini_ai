from datetime import datetime as dt
from pytz import timezone as tz
from env.api_key import api_key
import google.generativeai as genai
import time

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# print("Google Generative AI Setup Completed Successfully!")


def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text


def chat():
    try:
        chatting = True
        prompt = input('What would you like to know?\nType "quit" to quit.\n').lower()

        while chatting:

            if prompt != 'quit':

                print(get_response(prompt))
                keep_going = input('Anything else? (y/n)\n').lower()
                with open('chat_history.txt', 'a') as file:
                    date_created = dt.fromtimestamp(time.time(), tz=tz('US/Arizona'))
                    file.write('------------------------------\n')
                    file.write(date_created.strftime("%b/%d/%Y %I:%M %p")+'\n')
                    file.write(f'Prompt:\n{prompt}\n')
                    file.write(f'Response:\n{get_response(prompt)}\n')

                if keep_going in ['y', 'yes']:

                    prompt = input('What would you like to know?\nType "quit" to quit.\n').lower()

                elif keep_going in ['n', 'no', 'quit']:

                    chatting = False
                    print('Goodbye!')

                else:

                    print('Invalid input. Please try again.')
                    prompt = input('What would you like to know?\nType "quit" to quit.\n').lower()
            else:

                chatting = False
                print('Goodbye!')

    except Exception as e:
        print('Invalid input. Please try again.')
        print('Error: {}'.format(e))


chat()
