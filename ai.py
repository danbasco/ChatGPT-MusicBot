import openai
import os



def open_ai(texto):

    question = str(texto)
    response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=2049)
    answer = response['choices'][0]['text']

    return str(answer)
            



def write(username, question, awnser, date):
    f = open("log.txt", "a")

    data = str(date)

    f.write(f"{data[:-7]}\nUsername: {username}\n\nQuestion: {question}\nAnswer: {awnser}")
    f.close()
    