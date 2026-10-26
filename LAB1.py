# Zadanie 1
#a)
print("Zad. 1:")
print("a)")
print(type(1 + 2))
print(type(1 + 4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10))
print(type(8 ** (1/3)))
print()

#b)
print("b)")
print(int(3.0))      # Zamienia liczbę float na int, czyli 3.0 na 3
print(float(3))      # Zamienia liczbę całkowitą na float, czyli 3 na 3.0
print(float("3"))    # Zamienia tekst "3" na liczbę 3.0
print(str(12.4))     # Zamienia liczbę 12.4 na tekst "12.4"
print(bool(0))       # Zamienia 0 na false (fałsz)
print()

# Zadanie 2
print("Zad. 2:")
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)
print()

# Zadanie 3
print("Zad. 3:")
imie = "Jan"
wiek = 20
wzrost = 178

print("Nazywam się", imie, "i mam", wiek, "lat.")
print("Mój wzrost to", wzrost, "cm.")
print()

# Zadanie 4
print("Zad. 4:")
cena = 39.99
rabat = 0.2
cena_po_rabacie = cena * (1 - rabat)

print("Cena produktu po rabacie:", round(cena_po_rabacie, 2), "PLN")
print()

# Zadanie 5
print("Zad. 5:")
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))

pole = a * b
obwod = 2 * (a + b)

print("Pole prostokąta wynosi:", pole)
print("Obwód prostokąta wynosi:", obwod)
print()

# Zadanie 6
print("Zad. 6:")
przejechana_droga = float(input("Podaj przejechaną drogę w km: "))
srednie_spalanie_paliwa = float(input("Podaj średnie spalanie w literach na 100 km: "))
cena_paliwa = 6.5
zuzycie_paliwa = przejechana_droga * srednie_spalanie_paliwa / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print("Przewidywane zużycie paliwa:", zuzycie_paliwa, "l")
print("Szacowany koszt podróży:", koszt_podrozy, "zł")
print()

# Zadanie 6A
print("Zad. 6A:")
import random
przejechana_droga = random.randint(100, 1000)
print("Wylosowana droga:", przejechana_droga, "km")

srednie_spalanie_paliwa = float(input("Podaj średnie spalanie w litrach na 100 km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))
zuzycie_paliwa = przejechana_droga * srednie_spalanie_paliwa / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print("Przewidywane zużycie paliwa:", zuzycie_paliwa, "l")
print("Szacowany koszt podróży:", koszt_podrozy, "zł")
print()

# Zadanie 6B
print("Zad. 6B:")
import random
przejechana_droga = random.randint(100, 1000)
print(f"Wylosowana droga: {przejechana_droga} km")

srednie_spalanie_paliwa = float(input("Podaj średnie spalanie w litrach na 100 km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))
zuzycie_paliwa = przejechana_droga * srednie_spalanie_paliwa / 100
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa} l")
