import os
import sys
import json
import requests
import time
import wikipedia

from lxml import html
from lxml import etree
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
page = requests.get('http://inspirationalshit.com/quotes')
tree = html.fromstring(page.content)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  if data['text'] == 'Stinky Bot':
    msg = 'Howdy, {}!'.format(data['name'])
    send_message(msg)

  if data['text'] == 'Send an inspirational quote':
    getQuote();

  if data['text'][:6] == 'Who is':
    name = data['text'][7:-1]
    send_message(wikipedia.summary(name, sentences=2))
  return "ok", 200
def log(msg):
  print(str(msg))
  sys.stdout.flush()
def getQuote():
    quote = tree.xpath('//blockquote/p/text()')
    send_message(quote[0].strip())

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
