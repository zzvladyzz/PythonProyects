def fibonacci(numero):
    if numero==1:
        return 1
    else :
        return numero*fibonacci(numero-1)

numero =5
resultado=fibonacci(numero)
print(f"el resultado de{numero}es{resultado}")
