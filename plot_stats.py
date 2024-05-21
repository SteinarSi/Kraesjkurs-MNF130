
import matplotlib.pyplot as plt

result = 1000

years = [2022, 2023, 2024]
results = [84, 64, result]

plt.bar(years, results)
plt.xticks(years)
plt.xlabel("År")
plt.ylabel("Sekunder")
plt.title("Antall sekunder før noen turte å si ifra om at det var feil kræsjkurs")
plt.show()
