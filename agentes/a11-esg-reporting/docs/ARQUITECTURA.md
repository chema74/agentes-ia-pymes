# Arquitectura a11-esg-reporting

Componente local para generar datos ESG sintéticos, calcular métricas y producir informes Markdown.

## Flujo
1. `data_generator.py`: genera dataset sintético.
2. `esg_calculator.py`: calcula métricas y flags.
3. `report_generator.py`: produce informe por empresa y resumen ejecutivo.
4. `main.py`: orquesta ejecución por CLI.
