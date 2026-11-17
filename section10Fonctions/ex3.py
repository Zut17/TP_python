def statistiques(notes):
    return sum(notes) / len(notes), min(notes), max(notes)

moyenne, minimum, maximum = statistiques([12.5, 14.0, 13.5, 16.0, 15.5])
print(f"Moyenne : {moyenne:.2f} | Min : {minimum} | Max : {maximum}")