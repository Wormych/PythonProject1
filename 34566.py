from bs4 import BeautifulSoup
import requests
response = requests.get("https://pogoda.unian.ua/86787-nikopol")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="forecastCalendar__dayOfWeek")
    res = soup_list[0]
    print("The time -",res.text)
    print(type(res.text))
    soup_list = soup.find_all(class_="forecastCalendar__number")
    res1 = soup_list[0]
    print("The weather in city -", res1.text)
    print(type(res1.text))