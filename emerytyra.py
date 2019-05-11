brutto=input("Wpisz emeryturę brutto: ")
#emerytura brutto
brutto=float(brutto)

skladka_zdrowotna = brutto * 0.09
#print(skladka_zdrowotna)

zaliczka_na_podatek_dochodowy = brutto * 0.18
#print(zaliczka_na_podatek_dochodowy)

stala_kwota_zmnieniajszająca_podatek = 556.02
#print(stala_kwota_zmnieniajszająca_podatek)

pomniejszamy_o_1_12 = stala_kwota_zmnieniajszająca_podatek / 12 + brutto * 0.0775
#print(pomniejszamy_o_1_12)

zaliczka_na_podatek_dochodowy_po_zmniejszeniu = zaliczka_na_podatek_dochodowy - pomniejszamy_o_1_12
#print(zaliczka_na_podatek_dochodowy_po_zmniejszeniu)

netto = brutto - skladka_zdrowotna - zaliczka_na_podatek_dochodowy_po_zmniejszeniu
print(round(netto, 2))
