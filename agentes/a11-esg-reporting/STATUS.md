# 🚦 Estado: Agente ESG Reporting

## V1.0 ✅ Operativa

| Componente | Estado |
|------------|--------|
| Datos sintéticos PYMES | ✅ |
| Cálculo métricas ESG | ✅ |
| Generación informes MD | ✅ |
| Trazabilidad (Audit ID) | ✅ |
| Demo automática | ✅ |

## Roadmap

### V1.1 (Q2 2026)
- [ ] Exportación a PDF (WeasyPrint)
- [ ] Dashboard Streamlit interactivo
- [ ] Integración con APIs de datos reales (OpenData)
- [ ] Tests con pytest

### V2.0 (Q3 2026)
- [ ] Docker-compose
- [ ] API REST con FastAPI
- [ ] Base de datos PostgreSQL para histórico

## Ejecutar

```powershell
git clone https://github.com/chema74/agente-esg-reporting
cd agente-esg-reporting
powershell -ExecutionPolicy Bypass -File scripts/demo/run_demo.ps1