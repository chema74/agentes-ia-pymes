# Arquitectura a12-finanzas-anomalias

Componente local para detección de anomalías financieras en datos sintéticos con explicabilidad.

## Flujo
1. `data_generator.py`: genera transacciones sintéticas con fraude inyectado.
2. `fraud_detector.py`: entrena y aplica Isolation Forest.
3. `explainer.py`: construye explicaciones interpretables.
4. `main.py`: orquesta modo demo o entrada CSV.
