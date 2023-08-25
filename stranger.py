import requests

def advice():
  url_advice = "https://api.adviceslip.com/advice" #Api to capture random advice
  data = requests.get(url_advice)
  response_advice = data.json()
  print("\t","'",response_advice["slip"]["advice"],"'")

url_name = "https://names.drycodes.com/1?nameOptions=boy_names&separator=space" #Api to capture random stranger names
load = requests.get(url_name)
response = load.json()
stranger_names = response[0]
head, sep, tail = stranger_names.partition(" ") #Since we only need the first name of the stranger, we will split the result and display only the first name
print(f"Hi I am {head.capitalize()}, I have some advice for you!")
advice()