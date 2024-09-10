print("mas sobre funciones")
#aqui se escriben las funciones
def sumaab(n1,n2):
    s=n1+n2
    return (f"la suma de {n1} + {n2} es:{s}")
#llamadas a funciones
print("calculando suma")
n1 = int(input("que numero quieres sumar?:"))
#"int" funciona como un indicador de que tipo de datos debe ser ingresado y como este debe ser tratado
n2 = int(input("que otro numero quieres sumar?:"))
#nuevamente se llama la funcion enviando los datos ingresados por el usuario
print(sumaab(n1,n2))

def restaab(r1,r2):
    r=r1-r2
    return (f"la resta de {r1} - {r2} es:{r}")
#llamadas a funciones
print("calculando resta")
r1 = int(input("que numero quieres restar?:"))
#"int" funciona como un indicador de que tipo de datos debe ser ingresado y como este debe ser tratado
r2 = int(input("que otro numero quieres restar?:"))
#nuevamente se llama la funcion enviando los datos ingresados por el usuario
print(restaab(r1,r2))

def multiplicacionab(m1, m2):
    m = m1 * m2
    return f"La multiplicacion de {m1} * {m2} es: {m}"
print("Calculando multiplicacion")
m1 = int(input("¿Qué número quieres multiplicar?: "))
m2 = int(input("¿Qué otro número quieres multiplicar?: "))
print(multiplicacionab(m1, m2))

def divisionab(d1, d2):
    d = d1 / d2
    return f"La división de {d1} / {d2} es: {d}"
print("Calculando división")
d1 = int(input("¿Qué número quieres dividir?: "))
d2 = int(input("¿Por qué número quieres dividir?: "))
print(divisionab(d1, d2))