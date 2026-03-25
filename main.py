import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='--', color='b')
plt.title("Wykres liniowy (Kwadraty liczb)")
plt.show()

#--------------------------------------------------------------

import matplotlib.pyplot as plt

kategorie = ['Jabłka', 'Banany', 'Pomarańcze']
wartosci = [10, 15, 7]

plt.bar(kategorie, wartosci, color='orange')
plt.title("Sprzedaż owoców")
plt.show()

#--------------------------------------------------------------

import matplotlib.pyplot as plt

wzrost = [160, 170, 180, 155, 190]
waga = [55, 70, 85, 50, 95]

plt.scatter(wzrost, waga, color='red')
plt.title("Zależność wagi od wzrostu")
plt.xlabel("Wzrost (cm)")
plt.ylabel("Waga (kg)")
plt.show()
