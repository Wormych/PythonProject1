from bs4 import BeautifulSoup
import requests
import sqlite3
response = requests.get("https://pogoda.unian.ua/86787-nikopol")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="forecastCalendar__dayOfWeek")
    res = soup_list[0]
    data = (res.text)
    print("The time -",res.text)
    print(type(res.text))
    soup_list = soup.find_all(class_="forecastCalendar__number")
    res1 = soup_list[0]
    temp = (res1.text)
    print("The weather in city -", res1.text)
    print(type(res1.text))


connection = sqlite3.connect("itsteps_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE Nikopol2 (dataandtime TEXT,temp TEXT)")
cur.execute("INSERT INTO Nikopol2 (dataandtime) VALUES (?)",(data,))
cur.execute("INSERT INTO Nikopol2 (temp) VALUES (?)",(temp,))
# cur.execute("ALTER TABLE ")
connection.commit()
res = cur.fetchall()
print(res)
connection.commit()
connection.close()