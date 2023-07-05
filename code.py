import requests

def obtener_distancia(origen, destino):
    api_key = "AlzaSyA0dJYLisOyf2GUmvoh1yFldOXhnxCA7P4"
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origen}&destinations={destino}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    try:
        distancia = data['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convertir de metros a kilómetros
        duracion = data['rows'][0]['elements'][0]['duration']['value']  # Duración en segundos
        return distancia, duracion
    except (KeyError, IndexError):
        print("No se pudo obtener la distancia y la duración del viaje.")
        return None, None

def calcular_combustible(distancia):
    rendimiento = 12  # km/litro (valor aproximado)
    combustible = distancia / rendimiento
    return combustible

def convertir_tiempo(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

def imprimir_narrativa(origen, destino, distancia, duracion, combustible):
    print(f"¡Viaje de {origen} a {destino}!")
    print(f"Distancia: {distancia:.1f} km")
    if duracion is not None:
        horas, minutos, segundos = convertir_tiempo(duracion)
        print(f"Duración: {horas} horas, {minutos} minutos, {segundos} segundos")
    else:
        print("Duración: No disponible")
    if combustible is not None:
        print(f"Combustible requerido: {combustible:.1f} litros")
    else:
        print("Combustible requerido: No disponible")

# Obtener las ciudades de origen y destino desde el usuario
origen = input("Ciudad de Origen: ")
destino = input("Ciudad de Destino: ")

# Obtener la distancia y duración del viaje
distancia, duracion = obtener_distancia(origen, destino)

if distancia is not None:
    # Calcular el combustible requerido
    combustible = calcular_combustible(distancia)

    # Imprimir resultados
    imprimir_narrativa(origen, destino, distancia, duracion, combustible)
else:
    # En caso de que no se pueda obtener la distancia y la duración del viaje
    print("No se puede calcular la distancia y la duración del viaje.")

# Agregar la letra "S" a la salida
print("S")