import random
import re

def es_ip_valida(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False
    return True


def es_dominio_valido(dominio):
    # Acepta dominios como cuc.edu.co, google.com, etc.
    patron = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(patron, dominio) is not None


while True:
    print("\nINSTRUCCIONES:")
    print("- Ingrese un dominio válido (ej: google.com, cuc.edu.co)")
    print("- O una IP válida en formato IPv4 (ej: 142.251.132.174)")
    print("- No incluya http:// ni https://\n")

    host = input("Ingrese el host: ")

    host_valido = False

    if es_ip_valida(host):
        ip = host
        host_valido = True
    elif es_dominio_valido(host):
        ip = f"142.{random.randint(100,251)}.{random.randint(0,255)}.{random.randint(1,254)}"
        host_valido = True

    if host_valido:
        print(f"\nHaciendo ping a {host} [{ip}] con 32 bytes de datos:")

        contador = 1
        tiempos = []
        ttl = 117

        while contador <= 4:
            tiempo = random.randint(25, 90)
            tiempos.append(tiempo)
            print(f"Respuesta desde {ip}: bytes=32 tiempo={tiempo}ms TTL={ttl}")
            contador += 1

        print(f"\nEstadísticas de ping para {ip}:")
        print("    Paquetes: enviados = 4, recibidos = 4, perdidos = 0")
        print("    (0% perdidos)")

        print("Tiempos aproximados de ida y vuelta en milisegundos:")
        print(f"    Mínimo = {min(tiempos)}ms, Máximo = {max(tiempos)}ms, Media = {sum(tiempos)//4}ms")
    else:
        print(f"\nLa solicitud de ping no pudo encontrar el host {host}.")
        print("Compruebe el nombre y vuelva a intentarlo. SERVIDOR CAÍDO")

    otra = input("\n¿Desea ingresar otro host? (si/no): ").lower()
    if otra != "si":
        print("\nPrograma finalizado.")
        break