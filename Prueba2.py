import pandas as pd
a = input("¿Quieres ver la lista de datos completa? \n(si o no): ")
print("")

if a.lower() == "si":
    #Se imprime la tabla completa
    df = pd.read_csv('presenciaredes.csv')
    print(df)
    print("Bueno, ahora te presento los demas datos")
    print(" ")
else:
    print("Bueno, te presento los demas datos")
    print(" ")

df = pd.read_csv('presenciaredes.csv')
#Calcular la diferencia de seguidores
a = df["ENERO"][7]
a = a.replace(",", "")
b = df["JUNIO"][7]
b = b.replace(",", "")
print("La diferencia de seguidores(followers) en twitter entre el mes de Enero y Junio es de:",int(b) - int(a),"seguidores")
print(" ")

#Calcular la diferencia de visualizaciones
print("Ahora dime, entre que meses quieres ver la diferencia de visualizaciones de youtube:  \n(Entre Enero y Julio)")
m1 = input("Mes 1: ")
m2 = input("Mes 2: ")
if m1.upper() == "ENERO" and m2.upper() == "FEBRERO" or m1.upper() == "FEBRERO" and m2.upper() == "ENERO":
    en = df["ENERO"][15]
    en = en.replace(",","")
    fb = df["FEBRERO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ENERO" and m2.upper() == "MARZO" or m1.upper() == "MARZO" and m2.upper() == "ENERO":
    en = df["ENERO"][15]
    en = en.replace(",","")
    fb = df["MARZO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ENERO" and m2.upper() == "ABRIL" or m1.upper() == "ABRIL" and m2.upper() == "ENERO":
    en = df["ENERO"][15]
    en = en.replace(",","")
    fb = df["ABRIL"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ENERO" and m2.upper() == "MAYO" or m1.upper() == "MAYO" and m2.upper() == "ENERO":
    en = df["ENERO"][15]
    en = en.replace(",","")
    fb = df["MAYO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ENERO" and m2.upper() == "JUNIO" or m1.upper() == "JUNIO" and m2.upper() == "ENERO":
    en = df["ENERO"][15]
    en = en.replace(",","")
    fb = df["JUNIO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "FEBRERO" and m2.upper() == "MARZO" or m1.upper() == "MARZO" and m2.upper() == "FEBRERO":
    en = df["FEBRERO"][15]
    en = en.replace(",","")
    fb = df["MARZO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "FEBRERO" and m2.upper() == "ABRIL" or m1.upper() == "ABRIL" and m2.upper() == "FEBRERO":
    en = df["FEBRERO"][15]
    en = en.replace(",","")
    fb = df["ABRIL"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "FEBRERO" and m2.upper() == "MAYO" or m1.upper() == "MAYO" and m2.upper() == "FEBRERO":
    en = df["FEBRERO"][15]
    en = en.replace(",","")
    fb = df["MAYO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "FEBRERO" and m2.upper() == "JUNIO" or m1.upper() == "JUNIO" and m2.upper() == "FEBRERO":
    en = df["FEBRERO"][15]
    en = en.replace(",","")
    fb = df["JUNIO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "MARZO" and m2.upper() == "ABRIL" or m1.upper() == "ABRIL" and m2.upper() == "MARZO":
    en = df["MARZO"][15]
    en = en.replace(",","")
    fb = df["ABRIL"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "MARZO" and m2.upper() == "MAYO" or m1.upper() == "MAYO" and m2.upper() == "MARZO":
    en = df["MARZO"][15]
    en = en.replace(",","")
    fb = df["MAYO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "MARZO" and m2.upper() == "JUNIO" or m1.upper() == "JUNIO" and m2.upper() == "MARZO":
    en = df["MARZO"][15]
    en = en.replace(",","")
    fb = df["JUNIO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ABRIL" and m2.upper() == "MAYO" or m1.upper() == "MAYO" and m2.upper() == "ABRIL":
    en = df["ABRIL"][15]
    en = en.replace(",","")
    fb = df["MAYO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "ABRIL" and m2.upper() == "JUNIO" or m1.upper() == "JUNIO" and m2.upper() == "ABRIL":
    en = df["ABRIL"][15]
    en = en.replace(",","")
    fb = df["JUNIO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")

if m1.upper() == "MAYO" and m2.upper() == "JUNIO" or m1.upper() == "JUNIO" and m2.upper() == "MAYO":
    en = df["MAYO"][15]
    en = en.replace(",","")
    fb = df["JUNIO"][15]
    fb = fb.replace(",","")
    print("La diferencia de visualizaciones de youtube entre ",m1," y ",m2," es de:",int(fb)-int(en),"visualizaciones")
print("")
#Calcular promedio de crecimiento
# Twitter
en = df["ENERO"][9]
en = en.replace("%", "")
fb = df["FEBRERO"][9]
fb = fb.replace("%", "")
mr = df["MARZO"][9]
mr = mr.replace("%", "")
ab = df["ABRIL"][9]
ab = ab.replace("%", "")
my = df["MAYO"][9]
my = my.replace("%", "")
jn = df["JUNIO"][9]
jn = jn.replace("%", "")
promedio_1 = (int(en) + int(fb) + int(mr) + int(ab) + int(my) + int(jn)) / 6
#Facebbok
Fen = df["ENERO"][2]
Fen = Fen.replace("%", "")
Fen = float(Fen)
Ffb = df["FEBRERO"][2]
Ffb = Ffb.replace("%", "")
Fmr = df["MARZO"][2]
Fmr = Fmr.replace("%", "")
Fab = df["ABRIL"][2]
Fab = Fab.replace("%", "")
Fmy = df["MAYO"][2]
Fmy = Fmy.replace("%", "")
Fjn = df["JUNIO"][2]
Fjn = Fjn.replace("%", "")
promedio_2 = (int(Fen) + int(Ffb) + int(Fmr) + int(Fab) + int(Fmy) + int(Fjn)) / 6
print("El promedio de crecimiento de Twitter y Facebook entre los meses de Enero a Junio es de\nTwitter:",promedio_1,"% \nFacebook:",promedio_2,"%")
print(" ")
print('"Gracias pos su atención"')


