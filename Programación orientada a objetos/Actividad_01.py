#Ejercicio resuelto N°4:

Edad_Juan = int(input('Ingrese la edad de Juan: '))
Edad_Alberto = int((2/3)*Edad_Juan)
Edad_Ana = int((4/3)*Edad_Juan)
Edad_Madre = Edad_Juan + Edad_Alberto + Edad_Ana

print('La edad de Juan es:',Edad_Juan, '\n' 'La edad de Alberto es:', Edad_Alberto, '\n' 'La edad de Ana es:', 
      Edad_Ana, '\n' 'La edad de la mamá de Juan es:', Edad_Madre)

#Ejercicio resuelto N°5:

suma = 0
x = 20
suma += x
y = 40
x += y**2
suma += (x/y)
print('El valor de la suma es:', suma)

#Ejercicio propuesto N°12:

Horas_semana = 48
Valor_hora = 5000
Salario_bruto = float(48*5000)
Retencion_fuente = float(0.125*Salario_bruto)
Salario_neto = float(Salario_bruto - Retencion_fuente)

print('El salario bruto del trabajador es:', Salario_bruto,'\n''La retención en la fuente es:', Retencion_fuente,
      '\n''El salario neto del trabajador es:', Salario_neto)

#Ejercicio propuesto N°14:

x = float(input('Ingrese el número: '))

print('El cuadrado del número ingresado es:',(x)**2,'\n''El cubo del número ingresado es:',(x)**3)

#Ejercicio propuesto N°17:
import math as mt

Radio_circulo = float(input('Ingrese el radio del círculo:'))
Area_circulo =  mt.pi*(Radio_circulo)**2
Longitud_circunferencia = 2*mt.pi*Radio_circulo

print('El área del círculo es:',Area_circulo,'\n''La longitud de la circunferencia es:',Longitud_circunferencia)


    
