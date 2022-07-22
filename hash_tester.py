"""Una función criptográfica hash es un algoritmo matemático que transforma cualquier
bloque arbitrario de datos en una nueva serie de caracteres con una longitud fija.
Independientemente de la longitud de los datos de entrada, el valor hash de salida
tendrá siempre la misma longitud."""

def header():
    a = """
.__                  .__          __                   __                
|  |__ _____    _____|  |__     _/  |_  ____   _______/  |_  ___________
|  |   \\__  \  /  ___/  |  \    \   __\/ __ \ /  ___/\   __\/ __ \_  __ \\\

|   Y  \/ __ \_\___ \|   Y  \    |  | \  ___/ \___ \  |  | \  ___/|  | \/
|___|  (____  /____  >___|  /____|__|  \___  >____  > |__|  \___  >__|
     \/     \/     \/     \/_____/         \/     \/            \/     

                                                         <Rodrigo Sánchez>
    """
    print(a)

#Imprimimos el header creado para la app
header()
#Solicitamos el mensaje que vamos a hashear al usuario
mensaje = input("Introduce el mensaje: ")
#Calcular el hash del mensaje
hash_nb = hash(mensaje)
#Imprimimos el hash del mensaje
print("\nEl hash del mensaje es:", hash_nb)