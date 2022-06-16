""""Ejercicio Bimestral Teoría-Práctica"""


#input

valor_del_cheque = int (input ("Ingresa el valor del cheque "))

#processing
if valor_del_cheque<100:
    print("Error")
else:
    moneda_de_100=valor_del_cheque
    billete_de_10000=(moneda_de_100-moneda_de_100%10000)//10000
    moneda_de_100=moneda_de_100%10000
    billete_de_2000=(moneda_de_100-moneda_de_100%2000)//2000
    moneda_de_100=moneda_de_100%2000
    moneda_100=(moneda_de_100-moneda_de_100%100)//100
    moneda_de_100=moneda_de_100%100

#ouput

print ("cantidad de billetes de 2000: " + repr (billete_de_2000))
print ("cantidad de billetes de 10000: " + repr (billete_de_10000))
print ("cantidad de monedas de 100: " + repr (moneda_100))
print("Eso era...")