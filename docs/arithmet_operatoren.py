strompreis = 0.4

verbrauch_tv=3*1*3*365
verbrauch_herd=4*2*2*52
verbrauch_router=2*4*365
Verbrauch_heizung=8*20*170 

gesamtverbrauch=verbrauch_herd+verbrauch_router+Verbrauch_heizung+verbrauch_tv

gesamtkosten=strompreis*gesamtverbrauch

print(f"Gesamtkosten des Haushalts im Jahr beträgt {gesamtkosten:.2f}")#empfehlung
print(10/2)
print("das Ergebnis lautet ",gesamtkosten)