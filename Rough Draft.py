import json, requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
base_url1 = "https://api.openweathermap.org/data/2.5/weather?zip=94040&appid={appid}"
appid = "1e6a0df3fc613aef7e36d522089838cd"
J = 0
while J == 0:
  City = input("What city would you like weather information from? Enter   C for city, Z for zip code. To exit the program, enter 'E':")
  
  if City == "C":
    print(input("please enter the city name:"))
    url = f"{base_url}?q={City}&units=imperial&APPID={appid}"
    print(url)
    print()
    response = requests.get(url)
    unformated_data = response.json()
    
    temp = unformated_data["main"]["temp"]
    print(f"The current temp is: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
    temp_min = unformated_data["main"]["temp_min"]
    print(f"The minimum temp is: {temp_min}")
    feels_like = unformated_data["main"]["feels_like"]
    print(f"The feels like temp is: {feels_like}")
    pressure = unformated_data["main"]["pressure"]
    print(f"The pressure currently is: {pressure}")
    humidity = unformated_data["main"]["humidity"]
    print(f"The humidity is: {humidity}")
    wind_speed = unformated_data["wind"]["speed"]
    print(f"The wind speed is: {wind_speed}")
    wind_deg = unformated_data["wind"]["deg"]
    print(f"The wind degree is: {wind_deg}")
    
    #print(unformated_data)
  if City == "Z":
    print(input("Please enter the zip code:"))
    url = f"{base_url1}?q={City}&units=imperial&APPID={appid}"
    print(url)
    print()
    response = requests.get(url)
    unformated_data = response.json()
    
    temp = unformated_data["main"]["temp"]
    print(f"The current temp is: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
    temp_min = unformated_data["main"]["temp_min"]
    print(f"The minimum temp is: {temp_min}")
    feels_like = unformated_data["main"]["feels_like"]
    print(f"The feels like temp is: {feels_like}")
    pressure = unformated_data["main"]["pressure"]
    print(f"The pressure currently is: {pressure}")
    humidity = unformated_data["main"]["humidity"]
    print(f"The humidity is: {humidity}")
    wind_speed = unformated_data["wind"]["speed"]
    print(f"The wind speed is: {wind_speed}")
    wind_deg = unformated_data["wind"]["deg"]
    print(f"The wind degree is: {wind_deg}")

    
    response = requests.get(url)
    unformated_data = response.json()

  
  else:
    print("There was an error in getting the data from this city")
    
  
  
    
  