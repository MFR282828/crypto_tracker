import requests

def obtener_precios_cripto(criptos=["bitcoin", "ethereum", "solana"]):
    """
    Se conecta a la API pública de CoinGecko para obtener
    el precio actual en USD y PEN (Soles).
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    parametros = {
        "ids": ",".join(criptos),       # Convierte ['bitcoin', 'ethereum'] en 'bitcoin,ethereum'
        "vs_currencies": "usd,pen",     # Monedas a consultar (Dólares y Soles)
        "include_24hr_change": "true"   # Incluye el porcentaje de cambio en 24 horas
    }
    
    try:
        # Petición HTTP a la API con un tiempo límite de espera de 10 segundos
        respuesta = requests.get(url, params=parametros, timeout=10)
        
        # Verifica si la API devolvió un código de éxito (200 OK)
        respuesta.raise_for_status()
        
        # Convierte los datos recibidos (JSON) a un diccionario de Python
        return respuesta.json()
        
    except requests.exceptions.RequestException as error:
        # Captura errores de red o servidores caídos para evitar que el programa colapse
        print(f"[ERROR DE RED] No se pudo obtener la información: {error}")
        return None