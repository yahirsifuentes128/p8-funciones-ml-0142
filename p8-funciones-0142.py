# yahir sifuentes NC = 0142 

def es_palindromo(texto):
    # Limpiamos el texto: quitamos espacios y pasamos a minúsculas
    texto_limpio = ""
    for caracter in texto.lower():
        if caracter != " ":
            texto_limpio += caracter
            
    # Comparamos la cadena con su versión invertida [::-1]
    return texto_limpio == texto_limpio[::-1]


# Pruebas
print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("Python"))              # False

def es_primo(numero):
    if numero <= 1:
        return False
    
    # Revisamos si algún número desde el 2 hasta antes del número lo divide exactamente
    for i in range(2, numero):
        if numero % i == 0:
            return False  # Si se puede dividir, no es primo
            
    return True


# Pruebas
print(es_primo(7))   # True
print(es_primo(10))  # False

def aplanar_lista(lista_con_listas):
    lista_plana = []
    
    for elemento in lista_con_listas:
        # Si el elemento es una lista, iteramos sobre sus valores
        if type(elemento) == list:
            for sub_elemento in elemento:
                lista_plana.append(sub_elemento)
        else:
            lista_plana.append(elemento)
            
    return lista_plana


# Prueba
datos = [1, [2, 3], 4, [5, 6, 7]]
print(aplanar_lista(datos))  # Resultado: [1, 2, 3, 4, 5, 6, 7]

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
            
    return conteo


# Prueba
frase = "hola mundo hola python mundo mundo"
print(contar_palabras(frase))  # Resultado: {'hola': 2, 'mundo': 3, 'python': 1}

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    secuencia = [0, 1]
    
    # Generamos los números restantes hasta completar 'n'
    for _ in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        
    return secuencia


# Prueba
print(fibonacci(8))  # Resultado: [0, 1, 1, 2, 3, 5, 8, 13]

print("programa realizado por yahir sifuentes NC = 0142 ")