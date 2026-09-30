def dar_formato_precios(datos_json):
    """
    Toma el diccionario devuelto por la API de CoinGecko y
    lo transforma en un reporte limpio y ordenado para la pantalla.
    """
    if not datos_json:
        return "⚠️️ No hay datos para mostrar o la consulta falló."

    lineas = []
    lineas.append("=" * 50)
    lineas.append("        MONITOR DE CRIPTOMONEDAS EN TIEMPO REAL")
    lineas.append("=" * 50)

    for moneda, informacion in datos_json.items():
        nombre = moneda.capitalize()
        precio_usd = informacion.get("usd", 0)
        precio_pen = informacion.get("pen", 0)
        cambio_24h = informacion.get("usd_24h_change", 0)

        # Selecciona un icono según si el precio subió o bajó
        icono = "📈" if cambio_24h >= 0 else "📉"

        lineas.append(f"• {nombre.ljust(10)}: ${precio_usd:,.2f} USD | S/ {precio_pen:,.2f} PEN")
        lineas.append(f"  Variación 24h: {icono} {cambio_24h:+.2f}%")
        lineas.append("-" * 50)

    return "\n".join(lineas)