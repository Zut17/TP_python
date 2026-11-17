import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
base = rng.normal(12, 3, 10)  # niveau général de chaque étudiant
notes_df = pd.DataFrame({
    "Maths": base + rng.normal(0, 1, 10),
    "Algo": base + rng.normal(0, 1.5, 10),
    "Anglais": rng.normal(12, 3, 10),
})

corr = notes_df.corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", vmin=-1, vmax=1, square=True)
plt.title("Corrélation entre les notes des matières")
plt.show()