# 🚦 Estado del Proyecto: Agente Finanzas PYME

## Versión Actual: V1.0 (✅ Operativa)

| Componente | Estado | Descripción |
|------------|--------|-------------|
| **Generación de datos** | ✅ Completo | Datos sintéticos realistas con Faker |
| **Detector (Isolation Forest)** | ✅ Completo | scikit-learn, sin GPU requerida |
| **Explicabilidad (XAI)** | ✅ Completo | Reglas de negocio + scores interpretables |
| **Demo ejecutable** | ✅ Listo | `powershell -File scripts/demo/run_demo.ps1` |
| **Informe automático** | ✅ Listo | Genera `demo/informe.md` con alertas |

## Roadmap

### V1.1 (Q2 2026)
- [ ] Integración SHAP/LIME para feature importance visual
- [ ] Métricas de evaluación: Precision, Recall, F1-Score
- [ ] API REST con FastAPI para integración externa

### V2.0 (Q3 2026)
- [ ] Docker-compose con límites de RAM
- [ ] Tests automatizados con pytest
- [ ] Dashboard Streamlit para visualización interactiva

## Cómo Ejecutar
```powershell
git clone https://github.com/chema74/agente-finanzas-pyme
cd agente-finanzas-pyme
powershell -ExecutionPolicy Bypass -File scripts/demo/run_demo.ps1