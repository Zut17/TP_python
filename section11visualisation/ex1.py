import matplotlib.pyplot as plt

evaluations = [f"Éval {i}" for i in range(1, 11)]
notes = [12, 13.5, 11, 14, 15, 13, 16, 14.5, 15.5, 17]

plt.plot(evaluations, notes)
plt.title("Évolution des notes")
plt.xlabel("Évaluation")
plt.ylabel("Note (/20)")
plt.show()