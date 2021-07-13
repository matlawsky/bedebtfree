import requests
from datetime import date

global saved 

saved = []


### function so not ot waste api requests

###
def save_debts() -> None:
    try:
        file = open("quote.txt", "w")
        for item in saved:
            file.write(f"{str(item)}\n")
    except:
        print("error: saving the quote")

###
def load_quote() -> list:
    try:
        file = open("quote.txt", "r")
        quote_list = file.readlines()     
        print("succesfully loaded")
        return quote_list
    except:
        print("error: load the quote")

###
def get_saved():
    loaded = load_quote() 
    truec = saved   
    if str(truec[2]) == str(date.today()):
        return [saved[0], saved[1]]
    elif str(loaded[2]) == str(date.today()):
        saved = loaded
        return saved
    else:
        saved = []
        part = get_all()
        saved[0] = part[0]
        saved[1] = part[1]
        saved[2] = date.today()
        return saved 

def get_all():
    url = 'https://quotes.rest/qod?category=management'
    api_token = "YOUR API KEY HERE"
    headers = {'content-type': 'application/json',
	   'X-TheySaidSo-Api-Secret': format(api_token)}

    response = requests.get(url, headers=headers)
    #print(response)
    quotes=response.json()['contents']['quotes'][0]
    author = quotes["author"]
    quote = quotes["quote"]
    quote = quote.replace(".",".\n") 

    return [author, quote]


