from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import requests

# Create your views here.
count=0
name,age,gender='','',''
@csrf_exempt
def bot(request):
    try:
        data = JSONParser().parse(request)
        from_no = data['contacts'][0]['wa_id']
        msg = data['messages'][0]['text']['body']
        global count,name,age,gender
        headers = {
                'D360-API-KEY': 'IiUJIKRMCDoR6T7UWJVPc77qAK',
                'Content-Type': 'application/json'
            }
        url = "https://waba.360dialog.io/v1/messages"
        if count==0:
            body = {
    "recipient_type": "individual",
    "to": from_no,
    "type": "text",
    "text": {
        "body": "Hello user! May I know your full name?"
            }
                }
            r = requests.post(url = url, headers=headers, json=body)
            count+=1
        elif count==1:
            name = msg
            body = {
    "recipient_type": "individual",
    "to": from_no,
    "type": "text",
    "text": {
        "body": "Your age?"
            }
                }
            r = requests.post(url = url, headers=headers, json=body)
            count+=1
        elif count==2:
            age = msg
            body = {
    "recipient_type": "individual",
    "to": from_no,
    "type": "text",
    "text": {
        "body": "Your Gender?"
            }
                }
            r = requests.post(url = url, headers=headers, json=body)
            count+=1
        elif count==3:
            gender = msg
            body = {
    "recipient_type": "individual",
    "to": from_no,
    "type": "text",
    "text": {
        "body": "Okay , thank you for your responses"
            }
                }
            r = requests.post(url = url, headers=headers, json=body)
            count=0
            nbody = {
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Phone number': from_no
            }
            print(nbody)
            nr = requests.post(url = 'https://hook.integromat.com/k2l6fs2rbhsybb2bwg9dpoege0e7gjl1', data=nbody)
            print(nr.text)
        pass
    except Exception:
        pass
    return HttpResponse('The bot is working')
