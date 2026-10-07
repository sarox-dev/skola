def sorting(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste


while True:
    skaitli = input("Ievadi skaitļus, kurus kārtot (piemēram, 5, 2, 8, 1): ")

    try:
        skaitli = skaitli.split(",")
        skaitli = [float(skaitlis.strip()) for skaitlis in skaitli]
        if len(skaitli) == 0:
            print("Kļūda! Ievadi vismaz vienu skaitli.")
            continue
        break

    except ValueError:
        print("Kļūda! Lūdzu, ievadi tikai skaitļus, atdalot tos ar komatu.")
        print("Piemērs: 5, 2, 8, 1, 3")


print("Sākuma secība:", skaitli)
print("Kārtībā:", sorting(skaitli))