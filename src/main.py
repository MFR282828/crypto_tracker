import sys
from src.api_client import obtener_precios_cripto
from src.formatter import dar_formato_precios

def ejecutar_aplicacion():
    """
    Función principal que coordina el flujo del programa:
    1. Solicita datos a la API.
    2. Valida la respuesta.
    3. Aplica formato visual.
    4. Muestra el reporte en pantalla.
    """
    print("Conectando con CoinGecko para consultar el mercado...\n")
    
    # 1. Obtenemos los datos desde el módulo api_client
    datos = obtener_precios_cripto()
    
    # 2. Verificamos si hubo un fallo de red
    if datos is None:
        print("❌ Error crítico: La aplicación no pudo obtener los precios. Revisa tu conexión.")
        sys.exit(1)
        
    # 3. Transformamos los datos a un reporte estético con el módulo formatter
    reporte = dar_formato_precios(datos)
    
    # 4. Imprimimos el resultado final
    print(reporte)

if __name__ == "__main__":
    ejecutar_aplicacion()