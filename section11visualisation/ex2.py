import matplotlib.pyplot as plt

evaluations = [f"Éval {i}" for i in range(1, 11)]
notes = [12, 13.5, 11, 14, 15, 13, 16, 14.5, 15.5, 17]

glissante = []
for i in range(2, len(notes)):
    glissante.append(sum(notes[i - 2:i + 1]) / 3)

plt.plot(evaluations, notes, label="Notes", color="#1f4e79")
plt.plot(evaluations[2:], glissante, label="Moyenne glissante (3)", color="#e07a1f", linestyle="--")
plt.title("Notes et moyenne glissante")
plt.xlabel("Évaluation")
plt.ylabel("Note (/20)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()