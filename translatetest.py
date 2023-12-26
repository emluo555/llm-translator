import requests
import json

url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"

querystring = {"langpair":"en|ko","q":"Friend, Hello, Boyfriend, Mom, Dad","mt":"1","onlyprivate":"0","de":"a@b.c"}

headers = {
	"X-RapidAPI-Key": "131606fe64msh0d82f39e4f36c6fp19bc98jsndc3994603d7b",
	"X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()['responseData']['translatedText'])