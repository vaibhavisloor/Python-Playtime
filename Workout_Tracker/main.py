import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
xaid=os.environ.get('x-app-id')
xakey=os.environ.get('x-app-key')
sheety=os.environ.get('sheety')


header = {
'Content-Type':'application/json',
'x-app-id' :xaid,
'x-app-key':xakey,
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_input = str(input("What exercise did you do today ?"))

params={
    'query':user_input,

}
response=requests.post(url=exercise_endpoint, headers=header, json=params)

response=response.json()


sheety_endpoint='https://api.sheety.co/6973e26540b3a36aa97c35ee78ae915e/myWorkout/workouts'

date=str(datetime.now())[0:10]
time=str(datetime.now())[11:19]

body={
'workout':{
'date':date,
'time':time,
'exercise':(response['exercises'][0]['user_input']).title(),
'duration':response['exercises'][0]['duration_min'],
'calories':response['exercises'][0]['nf_calories']
}
}

header={
'Authorization':f'Basic {sheety}'
}

sheety_response = requests.post(url=sheety_endpoint,json=body,headers=header)
print(sheety_response.text)
  