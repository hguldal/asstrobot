import re, string, unicodedata,time,datetime,csv,random,json

def chatbot_answer(question):
    

    returnAnswer=''
    
    csvLogdata = [datetime.datetime.now(), question, returnAnswer]

    with open('chatbotlog.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f,delimiter ='|')
        writer.writerow(csvLogdata)
    
    return returnAnswer
