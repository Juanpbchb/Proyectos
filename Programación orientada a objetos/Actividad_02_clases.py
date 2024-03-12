#CAPÍTULO 3

#Ejercicio propuesto 18:

class Empleado:
    def __init__(self):
        self.codigo = input("Ingrese el código del empleado: ")
        self.nombres = input("Ingrese los nombres del empleado: ")
        self.horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
        self.valor_hora = float(input("Ingrese el valor de la hora trabajada: "))
        self.retencion_fuente = float(input("Ingrese el porcentaje de retención en la fuente (%): "))

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = (self.retencion_fuente / 100) * salario_bruto
        return salario_bruto - retencion

    def mostrar_informacion(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        print("Código del empleado:", self.codigo)
        print("Nombres del empleado:", self.nombres)
        print("Salario bruto:", salario_bruto)
        print("Salario neto:", salario_neto)

empleado = Empleado()
empleado.mostrar_informacion()

#Ejercicio propuesto 19:

import math

class TrianguloEquilatero:
    def __init__(self):
        self.lado = float(input("Ingrese el valor del lado del triángulo equilátero: "))

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return math.sqrt(3) / 2 * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def mostrar_resultados(self):
        perimetro = self.calcular_perimetro()
        altura = self.calcular_altura()
        area = self.calcular_area()
        print("Perímetro del triángulo:", perimetro)
        print("Altura del triángulo:", altura)
        print("Área del triángulo:", area)


triangulo = TrianguloEquilatero()
triangulo.mostrar_resultados()

#Ejercicio 21:

import math

class Triangulo:
    def __init__(self):
        self.lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        self.lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        self.lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_semiperimetro(self):
        return self.calcular_perimetro() / 2

    def calcular_area(self):
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def mostrar_resultados(self):
        perimetro = self.calcular_perimetro()
        semiperimetro = self.calcular_semiperimetro()
        area = self.calcular_area()
        print("Perímetro del triángulo:", perimetro)
        print("Semiperímetro del triángulo:", semiperimetro)
        print("Área del triángulo:", area)

triangulo = Triangulo()
triangulo.mostrar_resultados()

#Capitulo 4:

#Ejercicio resuelto 7:

class Comparador:
    def __init__(self):
        self.valor_a = float(input("Ingrese el valor de A: "))
        self.valor_b = float(input("Ingrese el valor de B: "))

    def comparar_valores(self):
        if self.valor_a > self.valor_b:
            return "A es mayor que B."
        elif self.valor_a < self.valor_b:
            return "A es menor que B."
        else:
            return "A es igual a B."

    def mostrar_resultado(self):
        resultado = self.comparar_valores()
        print(resultado)


comparador = Comparador()
comparador.mostrar_resultado()

#Ejercicio resuelto 10:

class Estudiante:
    def __init__(self):
        self.numero_inscripcion = input("Ingrese el número de inscripción del estudiante: ")
        self.nombres = input("Ingrese los nombres del estudiante: ")
        self.patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
        self.estrato_social = int(input("Ingrese el estrato social del estudiante: "))

    def calcular_pago_matricula(self):
        pago_base = 50000  
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            aumento = self.patrimonio * 0.03
            return pago_base + aumento
        else:
            return pago_base

    def mostrar_informacion(self):
        pago_matricula = self.calcular_pago_matricula()
        print("Número de inscripción:", self.numero_inscripcion)
        print("Nombres:", self.nombres)
        print("Pago de matrícula: $", pago_matricula)


estudiante = Estudiante()
estudiante.mostrar_informacion()

#Ejercicio resuelto 11:

class MayorNumero:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))
        self.num3 = int(input("Ingrese el tercer número entero: "))

    def encontrar_mayor(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            return self.num1
        elif self.num2 > self.num1 and self.num2 > self.num3:
            return self.num2
        else:
            return self.num3

    def mostrar_resultado(self):
        mayor = self.encontrar_mayor()
        print("El mayor número es:", mayor)

mayor_numero = MayorNumero()
mayor_numero.mostrar_resultado()

#Ejercicio resuelto 12:

class Trabajador:
    def __init__(self):
        self.nombres = input("Ingrese los nombres del trabajador: ")
        self.horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
        self.valor_hora = float(input("Ingrese el valor recibido por una hora normal de trabajo: "))

    def calcular_salario(self):
        if self.horas_trabajadas <= 40:
            salario = self.horas_trabajadas * self.valor_hora
        elif self.horas_trabajadas > 40 and self.horas_trabajadas <= 48:
            horas_normales = 40
            horas_extra = self.horas_trabajadas - horas_normales
            salario = (horas_normales * self.valor_hora) + (horas_extra * self.valor_hora * 2)
        else:
            horas_normales = 40
            horas_extra = self.horas_trabajadas - horas_normales
            horas_extra_doble = 8
            horas_extra_triple = horas_extra - horas_extra_doble
            salario = (horas_normales * self.valor_hora) + (horas_extra_doble * self.valor_hora * 2) + (horas_extra_triple * self.valor_hora * 3)
        return salario

    def mostrar_informacion(self):
        salario_devengado = self.calcular_salario()
        print("Nombre del trabajador:", self.nombres)
        print("Salario devengado: $", salario_devengado)


trabajador = Trabajador()
trabajador.mostrar_informacion()

#Ejercicio resuelto 13:

class Almacen:
    def __init__(self):
        self.valor_compra = float(input("Ingrese el valor de la compra: "))
        self.color_bolita = input("Ingrese el color de la bolita (blanca, verde, amarilla, azul, roja): ").lower()

    def calcular_descuento(self):
        if self.color_bolita == "blanca":
            descuento = 0
        elif self.color_bolita == "verde":
            descuento = 0.1
        elif self.color_bolita == "amarilla":
            descuento = 0.25
        elif self.color_bolita == "azul":
            descuento = 0.5
        elif self.color_bolita == "roja":
            descuento = 1
        else:
            print("Color de bolita no válido.")
            descuento = 0
        return descuento

    def calcular_valor_final(self):
        descuento = self.calcular_descuento()
        valor_final = self.valor_compra * (1 - descuento)
        return valor_final

    def mostrar_valor_final(self):
        valor_final = self.calcular_valor_final()
        print("Valor a pagar teniendo en cuenta los posibles descuentos:", valor_final)


almacen = Almacen()
almacen.mostrar_valor_final()

#Ejercicio resuelto 14:

class Empresa:
    def __init__(self):
        self.ventas_departamento1 = float(input("Ingrese el importe de ventas del departamento 1: "))
        self.ventas_departamento2 = float(input("Ingrese el importe de ventas del departamento 2: "))
        self.ventas_departamento3 = float(input("Ingrese el importe de ventas del departamento 3: "))
        self.salario_vendedores = float(input("Ingrese el salario de los vendedores de cada departamento: "))

    def calcular_incentivos(self):
        ventas_totales = self.ventas_departamento1 + self.ventas_departamento2 + self.ventas_departamento3
        incentivos = 0
        if self.ventas_departamento1 > 0.33 * ventas_totales:
            incentivos += 0.2 * self.salario_vendedores
        if self.ventas_departamento2 > 0.33 * ventas_totales:
            incentivos += 0.2 * self.salario_vendedores
        if self.ventas_departamento3 > 0.33 * ventas_totales:
            incentivos += 0.2 * self.salario_vendedores
        return incentivos

    def calcular_pago_final(self):
        incentivos = self.calcular_incentivos()
        salario_final = self.salario_vendedores + incentivos
        return salario_final

    def mostrar_salario_final(self):
        salario_final = self.calcular_pago_final()
        print("Valor recibido por salario en el departamento 1:", salario_final)
        print("Valor recibido por salario en el departamento 2:", salario_final)
        print("Valor recibido por salario en el departamento 3:", salario_final)

empresa = Empresa()
empresa.mostrar_salario_final()

#Ejercicio resuelto 15:

class Esferas:
    def __init__(self):
        self.peso_esfera_a = float(input("Ingrese el peso de la esfera A: "))
        self.peso_esfera_b = float(input("Ingrese el peso de la esfera B: "))
        self.peso_esfera_c = float(input("Ingrese el peso de la esfera C: "))
        self.peso_esfera_d = float(input("Ingrese el peso de la esfera D: "))

    def determinar_esfera_diferente(self):
        pesos = [self.peso_esfera_a, self.peso_esfera_b, self.peso_esfera_c, self.peso_esfera_d]
        pesos_unicos = set(pesos)
        for peso in pesos_unicos:
            if pesos.count(peso) == 1:
                esfera_diferente = peso
                break
        return esfera_diferente

    def comparar_peso_esfera_diferente(self, esfera_diferente):
        if esfera_diferente == self.peso_esfera_a:
            mensaje = "La esfera diferente es la A y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_b:
            mensaje = "La esfera diferente es la B y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_c:
            mensaje = "La esfera diferente es la C y es de menor peso que las otras tres."
        elif esfera_diferente == self.peso_esfera_d:
            mensaje = "La esfera diferente es la D y es de menor peso que las otras tres."
        else:
            mensaje = "No se encontró una esfera diferente."
        return mensaje

esferas = Esferas()
esfera_diferente = esferas.determinar_esfera_diferente()
mensaje = esferas.comparar_peso_esfera_diferente(esfera_diferente)
print(mensaje)

#Ejercicio propuesto 22:

class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.salario_hora = float(input("Ingrese el salario básico por hora del empleado: "))
        self.horas_trabajadas = int(input("Ingrese el número de horas trabajadas en el mes: "))

    def calcular_salario_mensual(self):
        salario_mensual = self.salario_hora * self.horas_trabajadas
        return salario_mensual

    def mostrar_resultado(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            print(f"Nombre del empleado: {self.nombre}")
            print(f"Salario mensual: ${salario_mensual}")
        else:
            print(f"Nombre del empleado: {self.nombre}")

empleado = Empleado()
empleado.mostrar_resultado()

#Ejercicio propuesto 23:

import math

class EcuacionSegundoGrado:
    def __init__(self):
        self.a = float(input("Ingrese el coeficiente 'A': "))
        self.b = float(input("Ingrese el coeficiente 'B': "))
        self.c = float(input("Ingrese el coeficiente 'C': "))

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz_discriminante = math.sqrt(discriminante)
            solucion1 = (-self.b + raiz_discriminante) / (2 * self.a)
            solucion2 = (-self.b - raiz_discriminante) / (2 * self.a)
            return solucion1, solucion2
        elif discriminante == 0:
            solucion_unica = -self.b / (2 * self.a)
            return solucion_unica,
        else:
            return "No tiene soluciones reales."

    def mostrar_soluciones(self):
        soluciones = self.calcular_soluciones()
        print("Soluciones de la ecuación de segundo grado:")
        for solucion in soluciones:
            print(solucion)

ecuacion = EcuacionSegundoGrado()
ecuacion.mostrar_soluciones()

#Ejercicio propuesto 24:

class Esferas:
    def __init__(self):
        self.peso_esfera_a = float(input("A continuación suministre el diferente peso para 3 esferas, Ingrese el peso de la esfera A: "))
        self.peso_esfera_b = float(input("Ingrese el peso de la esfera B: "))
        self.peso_esfera_c = float(input("Ingrese el peso de la esfera C: "))

    def determinar_esfera_mayor(self):
        if self.peso_esfera_a > self.peso_esfera_b and self.peso_esfera_a > self.peso_esfera_c:
            return "A"
        elif self.peso_esfera_b > self.peso_esfera_a and self.peso_esfera_b > self.peso_esfera_c:
            return "B"
        elif self.peso_esfera_c > self.peso_esfera_a and self.peso_esfera_c > self.peso_esfera_b:
            return "C"
        else:
            return "No se puede determinar"

    def mostrar_esfera_mayor(self):
        esfera_mayor = self.determinar_esfera_mayor()
        print(f"La esfera de mayor peso es la {esfera_mayor}")

esferas = Esferas()
esferas.mostrar_esfera_mayor()
