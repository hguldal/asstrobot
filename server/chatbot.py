import re, string, unicodedata,time,datetime,csv,random,json

from openai import OpenAI
client = OpenAI()

def chatbot_answer(question):
    
    returnAnswer=''

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "AsstroBot"},
            {"role": "user", "content": question}
        ]
    )

    returnAnswer=completion.choices[0].message
    
    csvLogdata = [datetime.datetime.now(), question, returnAnswer]

    with open('chatbotlog.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f,delimiter ='|')
        writer.writerow(csvLogdata)
    
    return returnAnswer
