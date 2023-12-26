import requests
import json
import gradio as gr
import logging


url = "http://localhost:11434/api/generate"
url_tr = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
logging.basicConfig(filename='/Users/emily/Documents/Github/ollama-test/example.log', filemode='w',encoding='utf-8',  level=logging.INFO)



headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def generate_response(prompt):
    conversation_history.append(prompt)

    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "mistral",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        logging.info("here")   
        res = translate_response(actual_response)

        print(res)
        return res
    else:   
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)


def translate_response(prompt):
    querystring = {"langpair":"en|ko","q":prompt,"mt":"1","onlyprivate":"0","de":"a@b.c"}
    headers_tr = {
	"X-RapidAPI-Key": "131606fe64msh0d82f39e4f36c6fp19bc98jsndc3994603d7b",
	"X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }
    response = requests.get(url_tr, headers=headers_tr, params=querystring) 
    return response.json()['responseData']['translatedText']

logging.info("hello world?")
iface.launch()