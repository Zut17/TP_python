import matplotlib.pyplot as plt

semaines = list(range(1, 13))
notes = [11.5, 11.6, 9.9, 9.7, 10, 10.4, 9.5, 9.4, 8.9, 8.5, 9.7, 9.3]
presence = [88, 95, 83, 87, 89, 89, 78, 89, 98, 76, 94, 89]

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True,
                         gridspec_kw={"height_ratios": [2, 1]})
axes[0].plot(semaines, notes, color="#1f4e79")
axes[0].set_ylabel("Note (/20)")
axes[1].bar(semaines, presence, color="#2e75b6")
axes[1].set_ylabel("Présence (%)")
axes[1].set_xlabel("Semaine")
plt.tight_layout()
plt.show()