import random
import seaborn as sns
import matplotlib.pyplot as plt

random.seed(1)
notes = [round(random.gauss(11, 3), 1) for _ in range(150)]

sns.set_theme(style="whitegrid")
sns.histplot(notes, bins=10, kde=True, color="#2e75b6")
plt.title("Distribution des notes de la classe")
plt.xlabel("Note (/20)")
plt.show()