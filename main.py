from bs4 import BeautifulSoup
import pandas as pd

# Загружаем html файл
with open("table.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Находим таблицу
table = soup.find("table", {"id": "multiposition_table"})

# Заголовки
headers = [th.get_text(strip=True) for th in table.find("thead").find_all("td")]

# Данные
rows = []
for tr in table.find("tbody").find_all("tr"):
    cells = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
    rows.append(cells)

# Создаем DataFrame
df = pd.DataFrame(rows, columns=headers)

# Сохраняем в Excel
df.to_excel("output.xlsx", index=False, engine="openpyxl")

print("Готово! Данные сохранены в output.xlsx")