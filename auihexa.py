
import requests
import time
import os

IP = "http://10.110.12.41/"

SENSORES = {
    "O5D150": {
        "nome": "Sensor fotoeletrico de distancia a laser",
        "tipo": "Distancia",
        "fabricante": "ifm"
    },
    "KI5309": {
        "nome": "Sensor de proximidade capacitivo",
        "tipo": "Capacitancia",
        "fabricante": "ifm"
    },
    "IF6123": {
        "nome": "Sensor de proximidade indutivo",
        "tipo": "Indutivo",
        "fabricante": "ifm"
    }
}


def consultar(porta, dado):
    requisicao = {
        "code": "request",
        "cid": 4711,
        "adr": f"/iolinkmaster/port[{porta}]/iolinkdevice/{dado}/getdata"
    }

    try:
        resposta = requests.post(IP, json=requisicao, timeout=5)
        resultado = resposta.json()

        if resultado.get("code") == 200:
            return resultado["data"]["value"]

        return None

    except Exception:
        return None


while True:
    os.system("cls")

    print("=" * 60)
    print("          MONITORAMENTO IO-LINK - AL1300")
    print("=" * 60)

    for porta in range(1, 4):

        modelo = consultar(porta, "productname")
        hexadecimal = consultar(porta, "pdin")

        print(f"\nPORTA {porta}")
        print("-" * 60)

        if modelo is not None:
            modelo = str(modelo).strip()
            info = SENSORES.get(modelo)

            if info:
                print(f"Modelo:       {modelo}")
                print(f"Nome:         {info['nome']}")
                print(f"Tipo:         {info['tipo']}")
                print(f"Fabricante:   {info['fabricante']}")
            else:
                print(f"Modelo:       {modelo}")
                print("Nome:         Modelo ainda nao cadastrado")

        else:
            print("Sensor nao identificado")

        if hexadecimal is not None:
            hexadecimal = str(hexadecimal)
            decimal = int(hexadecimal, 16)

            print(f"Hexadecimal:  {hexadecimal}")
            print(f"Decimal:      {decimal}")
            print(f"Binario:      {format(decimal, 'b')}")

        else:
            print("Dados:        Sem resposta")

    print("\n" + "=" * 60)
    print("Atualizando a cada 2 segundos...")
    print("Pressione CTRL + C para encerrar.")

    time.sleep(2)
