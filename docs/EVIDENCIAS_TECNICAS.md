# Evidencias Técnicas del Portfolio

## Estado verificable actual

Este repositorio contiene 10 agentes técnicos demostrables para PYMES. Cada agente mantiene una base documental V1, datos ficticios en JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*), un script local de consola y pruebas `unittest`.

La evidencia técnica actual se basa en validación local, datos ficticios controlados y revisión humana. No se presenta como IA (*Artificial Intelligence – Inteligencia Artificial*) funcional, API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) real, dashboard ni sistema productivo.

## Qué se puede demostrar hoy

- Ejecución de scripts locales por agente.
- Pruebas `unittest` por agente.
- Validación de JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de ejemplo.
- Validación global del repositorio.
- Ejecución mediante GitHub Actions con CI (*Continuous Integration – Integración Continua*).
- Ausencia de dependencias externas para la validación técnica actual.

## Evidencias por agente

### 01-agente-onboarding-inteligente

- Script local existente: `agentes/01-agente-onboarding-inteligente/src/validar_expediente.py`.
- Carpeta de tests: `agentes/01-agente-onboarding-inteligente/tests/`.
- JSON ficticio asociado: `agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json`.
- Qué demuestra realmente: validación local de un expediente ficticio de onboarding, detección de campos o estados relevantes y generación de una salida orientada a revisión humana.

### 02-agente-documental-inteligente

- Script local existente: `agentes/02-agente-documental-inteligente/src/validar_inventario_documental.py`.
- Carpeta de tests: `agentes/02-agente-documental-inteligente/tests/`.
- JSON ficticio asociado: `agentes/02-agente-documental-inteligente/datos_ejemplo/inventario_documental_ficticio.json`.
- Qué demuestra realmente: validación local de un inventario documental ficticio, identificación de incidencias de estructura y apoyo a una revisión humana sin OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*) real.

### 03-agente-seguimiento-clientes

- Script local existente: `agentes/03-agente-seguimiento-clientes/src/validar_cartera_clientes.py`.
- Carpeta de tests: `agentes/03-agente-seguimiento-clientes/tests/`.
- JSON ficticio asociado: `agentes/03-agente-seguimiento-clientes/datos_ejemplo/cartera_clientes_ficticia.json`.
- Qué demuestra realmente: validación local de una cartera ficticia de seguimiento de clientes, con reglas básicas aplicables a un contexto CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*) simulado.

### 04-agente-generador-propuestas

- Script local existente: `agentes/04-agente-generador-propuestas/src/validar_propuesta.py`.
- Carpeta de tests: `agentes/04-agente-generador-propuestas/tests/`.
- JSON ficticio asociado: `agentes/04-agente-generador-propuestas/datos_ejemplo/propuesta_ficticia.json`.
- Qué demuestra realmente: validación local de una propuesta ficticia, comprobación de estructura mínima y generación de observaciones para revisión humana.

### 05-agente-operaciones-pymes

- Script local existente: `agentes/05-agente-operaciones-pymes/src/validar_operaciones.py`.
- Carpeta de tests: `agentes/05-agente-operaciones-pymes/tests/`.
- JSON ficticio asociado: `agentes/05-agente-operaciones-pymes/datos_ejemplo/operaciones_pymes_ficticias.json`.
- Qué demuestra realmente: validación local de tareas y bloqueos operativos ficticios, con reglas simples para ordenar incidencias sin automatización productiva.

### 06-agente-control-cobros-flujo-caja

- Script local existente: `agentes/06-agente-control-cobros-flujo-caja/src/validar_cobros_flujo_caja.py`.
- Carpeta de tests: `agentes/06-agente-control-cobros-flujo-caja/tests/`.
- JSON ficticio asociado: `agentes/06-agente-control-cobros-flujo-caja/datos_ejemplo/cobros_flujo_caja_ficticios.json`.
- Qué demuestra realmente: validación local de cobros y previsión operativa ficticia, con salida de consola para revisión humana y sin prometer resultados financieros.

### 07-agente-pipeline-comercial

- Script local existente: `agentes/07-agente-pipeline-comercial/src/validar_pipeline_comercial.py`.
- Carpeta de tests: `agentes/07-agente-pipeline-comercial/tests/`.
- JSON ficticio asociado: `agentes/07-agente-pipeline-comercial/datos_ejemplo/pipeline_comercial_ficticio.json`.
- Qué demuestra realmente: validación local de oportunidades comerciales ficticias, estados de pipeline y datos de ejemplo sin integración real con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*).

### 08-agente-formacion-interna

- Script local existente: `agentes/08-agente-formacion-interna/src/validar_formacion_interna.py`.
- Carpeta de tests: `agentes/08-agente-formacion-interna/tests/`.
- JSON ficticio asociado: `agentes/08-agente-formacion-interna/datos_ejemplo/formacion_interna_ficticia.json`.
- Qué demuestra realmente: validación local de rutas y módulos formativos ficticios, aplicables a una simulación de LMS (*Learning Management System – Sistema de Gestión del Aprendizaje*) sin plataforma integrada.

### 09-agente-analisis-mercado

- Script local existente: `agentes/09-agente-analisis-mercado/src/validar_analisis_mercado.py`.
- Carpeta de tests: `agentes/09-agente-analisis-mercado/tests/`.
- JSON ficticio asociado: `agentes/09-agente-analisis-mercado/datos_ejemplo/analisis_mercado_ficticio.json`.
- Qué demuestra realmente: validación local de señales de mercado ficticias y criterios de revisión, sin RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*) real ni fuentes externas vivas.

### 10-agente-revision-cumplimiento

- Script local existente: `agentes/10-agente-revision-cumplimiento/src/validar_revision_cumplimiento.py`.
- Carpeta de tests: `agentes/10-agente-revision-cumplimiento/tests/`.
- JSON ficticio asociado: `agentes/10-agente-revision-cumplimiento/datos_ejemplo/revision_cumplimiento_ficticia.json`.
- Qué demuestra realmente: validación local de una revisión interna ficticia, seguimiento de evidencias y criterios de revisión humana en un contexto RGPD (*General Data Protection Regulation – Reglamento General de Protección de Datos*) simulado.

## Validación global

El repositorio incluye un script de validación global:

```bash
python scripts/validar_repositorio.py
```

Esta validación global comprueba:

- Los tests de los 10 agentes.
- Los 10 JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de ejemplo.

El workflow `.github/workflows/validacion.yml` permite ejecutar esta validación técnica automatizada mediante GitHub Actions como CI (*Continuous Integration – Integración Continua*) del repositorio.

## Límites actuales

- No hay IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) real.
- No hay dashboard.
- No hay Google Workspace.
- No hay integraciones reales.
- No hay RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*) real.
- No hay OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*) real.
- No hay automatización productiva.
- No se trabaja con datos reales de clientes.

## Valor técnico para portfolio

Esta base es valiosa como portfolio técnico porque muestra estructura modular, criterios de veracidad y pruebas reproducibles. Cada agente separa documentación, datos ficticios controlados, script de consola y pruebas `unittest`.

La validación transversal permite revisar el estado del conjunto sin depender de servicios externos. También mantiene una separación clara entre la V1 implementada, la V2 futura y lo que queda fuera de alcance.

## Evolución futura

Como fases futuras, no implementadas en el estado actual, podrían explorarse:

- Integración de IA (*Artificial Intelligence – Inteligencia Artificial*) real.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) local.
- Dashboard.
- Google Workspace.
- Conectores externos.
- Despliegue o demo web.

Estas líneas pertenecen a evolución futura y requieren nueva implementación, nuevas pruebas y revisión humana antes de presentarse como funcionalidad disponible.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
