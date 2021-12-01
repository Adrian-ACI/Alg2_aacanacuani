def funcion(x):
    return (((-x) ** 4) + (30 * (x ** 3)) + (15 * (x ** 2)) + (34 * x) + 540) #O(1)


def biseccion(x0, x1): #O(1)
    exactitud = 0.001 #O(1)
    m = (x0 + x1) / 2 #O(1)
    if abs((funcion(m) - funcion(x0)) / funcion(m)) < exactitud: #O(1)
        print("La aproximacion de la raiz es: ", m)
        return 0 #O(1)

    if (funcion(x0) * funcion(m)) <= 0: #O(1)
        biseccion(x0, m) #O(log(n))
    else: #O(1)
        biseccion(m, x1) #O(log(n))

if __name__ == '__main__':
    while (True): #O(log(n))
        print("Ingrese el valor de x0:")
        x0 = int(input()) #O(1)
        print("Ingrese el valor de x1:")
        x1 = int(input()) #O(1)
        if ((funcion(x0) * funcion(x1)) < 0):
            break #O(1)
        else:
            print("Los intervalos no son validos, ingrese los valores nuevamente") 
    biseccion(x0, x1)
# 0(biseccion) = O(log(n))