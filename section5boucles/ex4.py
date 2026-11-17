notes_cc = [10, 12, 14, 9]
notes_examen = [12, 11, 15, 9]
for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print(f"Étudiant {i + 1} : PROGRESSION")
    else:
        print(f"Étudiant {i + 1} : PAS DE PROGRESSION")