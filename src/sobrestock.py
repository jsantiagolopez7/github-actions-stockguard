def detectar_sobrestock(stock_actual: int, stock_maximo: int) -> bool:
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_maximo <= 0:
        raise ValueError("El stock maximo debe ser mayor que cero")

    return stock_actual > stock_maximo


def porcentaje_inventario(stock_actual: int, stock_maximo: int) -> float:
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_maximo <= 0:
        raise ValueError("El stock maximo debe ser mayor que cero")

    return round(stock_actual / stock_maximo * 100, 1)
