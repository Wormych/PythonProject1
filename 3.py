import requests
from datetime import datetime


current_date = datetime.now().strftime('%Y%m%d')


url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={current_date}&json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data:
        usd_to_uah = data[0]['rate']
        print(f"Курс доллара США на {current_date}: {usd_to_uah} UAH")

        class CurrencyConverter:
            def __init__(self, rate):
                self.rate = rate

            def convert_to_usd(self, amount_uah):
                return amount_uah / self.rate

        amount = float(input("Введите количество гривен: "))
        converter = CurrencyConverter(usd_to_uah)
        converted_amount = converter.convert_to_usd(amount)
        print(f"Это составляет {converted_amount:.2f} USD")
    else:
        print("Не удалось получить данные о курсе валют.")
else:
    print("Ошибка при получении данных с сайта НБУ.")
