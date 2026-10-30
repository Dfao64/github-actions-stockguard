# StockGuard - GitHub Actions con Python
Autor: Daniel Abello

Practica de Big Data: clasificacion del inventario, pytest y CI.
Repositorio educativo independiente de RapidGo 360.

## Ejecutar
```bash
python -m pip install -r requirements.txt
python -m compileall src tests
pytest -v
```

Con minimo 20 y stock 7, el resultado es CRITICO: 7 <= 10 (50% de 20).
Los datos negativos y un minimo <= 0 generan ValueError.

## CI
Workflow CI StockGuard, job validar-python, Ubuntu y Python 3.12.
Disparadores: push a main, pull_request hacia main y workflow_dispatch.
Secuencia de aprendizaje: verde, fallo intencional, correccion, mejora por PR, ejecucion manual.

## Mejora propia
`detectar_sobrestock(actual, maximo)` alerta si actual > maximo. El limite exacto no alerta. Incluye seis casos de prueba (tres parametrizados).
