# StockGuard

Práctica de GitHub Actions (Big Data, Línea de Profundización I). Clasifica el riesgo de inventario de un producto según su stock actual y su stock mínimo.

| Condición | Resultado |
|---|---|
| stock actual = 0 | AGOTADO |
| stock actual ≤ 50 % del mínimo | CRITICO |
| stock actual ≤ mínimo | BAJO |
| otro caso | NORMAL |

Valores negativos o un stock mínimo ≤ 0 son inválidos (`ValueError`).

Cada push o Pull Request hacia `main` ejecuta el workflow `CI StockGuard` (`.github/workflows/ci.yml`), que valida la sintaxis con `compileall` y corre las pruebas con `pytest`.
