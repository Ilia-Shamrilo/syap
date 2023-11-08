import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv("price_prepared.csv", delimiter=";", nrows=1000)
df = pd.read_csv("price_prepared.csv", delimiter=";", nrows=1000)

df.fillna(False, inplace=True)

if ds.any().empty:
    print("Все данные заполнены")
else:
    print("Некоторые данные пустые")

fig, ax = plt.subplots()
ax.set_yscale("log")
ax.boxplot(ds["Square"], vert=False)
ax.set_title("Логарифмическая шкала")

fig, ax = plt.subplots()
ax.hist(ds["Square"], bins=50)
ax.set_title("Гистограмма")
plt.show()

ds.to_csv("result_data.csv", index=False)