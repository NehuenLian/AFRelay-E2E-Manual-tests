# Tests E2E manuales para AFRelay

Scripts de prueba end-to-end (E2E) para validar los endpoints de la API **AFRelay** (WSFE).

## Descripción

Este repositorio contiene un conjunto de scripts que permiten testear manualmente los endpoints de la API AFRelay, la API que traduce JSON a SOAP del Webservice Facturación Electrónica (WSFE) de AFIP a través

## Estructura

- **wsfe/**: Scripts para testear endpoints que consultan al WSFE
  - `execute_all.py`: Ejecuta todas las pruebas en secuencia, útil para comprobaciones rápidas.
  - `utils.py`: Funciones auxiliares compartidas
  - En cuanto al resto de los archivos, cada uno representa un script para consultar cada endpoint disponible

- **health_checks/**: Scripts para verificar la salud de la API
  - `consult_liveness.py`: Verifica que la API está activa
  - `consult_readiness.py`: Verifica que la API está lista para recibir requests

## Uso

**ATENCION**: Si vas a realizar los tests E2E asegurate de estar en el entorno de homologación de ARCA en tu instancia de AFRelay y de haber configurado un archivo `.env` siguiendo la estructura de `.env.example`.

### Ejecutar todas las pruebas WSFE
```bash
python wsfe/execute_all.py
```

### Verificar liveness
```bash
python health_checks/consult_liveness.py
```

### Verificar readiness
```bash
python health_checks/consult_readiness.py
```

Ver `requirements.txt` para las dependencias necesarias.