import matplotlib.pyplot as plt

minutes = 7
seconds = 8

years = [2022, 2023, 2024, 2025, 2026]
results = [84, 64, 291, 185, 60 * minutes + seconds]

plt.bar(years, results)
plt.xticks(years)
plt.xlabel("År")
plt.ylabel("Sekunder")
plt.title("Antall sekunder før noen turte å si ifra om at det var feil kræsjkurs")
plt.savefig("stats.png")
plt.show()
