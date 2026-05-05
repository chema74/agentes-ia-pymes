# Arquitectura de [NOMBRE DEL AGENTE]

## Propósito del documento
Este documento describe la arquitectura conceptual y técnica prevista del agente. Debe detallar cómo se plantea su funcionamiento sin declarar como implementado ningún elemento que todavía no exista.

## Estado de la arquitectura
- Estado documental: [NO INICIADO | EN CURSO | COMPLETADO].
- Estado técnico: [NO INICIADO | EN CURSO | COMPLETADO].
- Código funcional: [SÍ | NO | PARCIAL, ESPECIFICAR].
- Integraciones activas: [NINGUNA | LISTAR INTEGRACIONES REALES].
- Dependencias reales: [NINGUNA | LISTAR DEPENDENCIAS EXISTENTES].

[Estos campos deben completarse siempre con estado real, no con estado aspiracional.]

## Visión conceptual
[Describir el agente como sistema de trabajo:]
- Qué información recibe: [DESCRIBIR ENTRADAS].
- Qué procesamiento realiza: [DESCRIBIR LÓGICA GENERAL].
- Qué salida genera: [DESCRIBIR RESULTADOS].
- Qué revisión humana necesita: [DESCRIBIR PUNTOS DE CONTROL].
- Qué límites debe respetar: [DESCRIBIR LÍMITES OPERATIVOS Y TÉCNICOS].

## Componentes previstos
[Usar esta lista como guía. No todos los agentes tienen que usar todos los componentes.]
- Entrada de datos.
- Validación básica.
- Procesamiento de reglas.
- Clasificación inicial.
- Generación de salida.
- Registro de trazabilidad.
- Dashboard futuro.
- Integración futura con IA (*Artificial Intelligence – Inteligencia Artificial*).
- Integración futura con Google Workspace.

## Flujo general previsto
[Describir el flujo en lenguaje funcional, sin código:]
1. Entrada de información.
2. Validación inicial.
3. Procesamiento.
4. Generación de resultado.
5. Revisión humana.
6. Registro o almacenamiento.
7. Seguimiento posterior.

## Arquitectura V1 implementable
[Definir la V1 (*Version 1 – Versión 1*) con criterio mínimo y verificable:]
- Estructura simple.
- Resultado verificable.
- Sin sobreingeniería.
- Sin integraciones reales complejas si no son necesarias.
- Con datos de ejemplo si procede.
- Con salidas demostrables.

[La V1 debe poder explicarse y validarse en contexto real de PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).]

## Arquitectura V2 futura
[Documentar la V2 (*Version 2 – Versión 2*) como evolución posible, no como estado actual. Puede incluir:]
- Google Workspace.
- Dashboard.
- Automatización documental.
- Clasificación asistida.
- Integración con modelos de lenguaje.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*).
- Base de datos.
- Alertas.
- Conectores externos.
- Compatibilidad con flujos de CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*), cuando aplique.

[Esta sección no debe describirse como ya implementada.]

## Datos previstos
[Documentar con precisión:]
- Datos de entrada: [DESCRIBIR].
- Datos intermedios: [DESCRIBIR].
- Datos de salida: [DESCRIBIR].
- Datos que no deben tratarse en la fase inicial: [DESCRIBIR].
- Consideraciones básicas de privacidad: [DESCRIBIR MEDIDAS MÍNIMAS].

## Integraciones previstas
[Separar claramente:]
- Integraciones no existentes: [LISTAR].
- Integraciones previstas: [LISTAR].
- Integraciones descartadas en fase inicial: [LISTAR].

## Control humano
Cada agente debe definir en qué puntos interviene una persona para revisar, validar o corregir resultados. [Especificar responsables, momento de revisión y criterio de aceptación o corrección.]

## Riesgos técnicos
[Evaluar riesgos reales antes de implementar. Ejemplos:]
- Automatizar un proceso mal definido.
- Mezclar datos incompletos con decisiones automáticas.
- Prometer IA donde solo hay reglas.
- Crear dependencias externas innecesarias.
- Sobredimensionar la V1.

## Fuera de alcance inicial
[Declarar límites explícitos. Lista guía:]
- Agente autónomo completo.
- Producción real.
- Multiempresa.
- Integraciones críticas.
- Decisiones sensibles sin supervisión.
- Sustitución de criterio profesional.
- Seguridad avanzada si no está implementada.

## Criterios de validación técnica
[Responder estas preguntas de control:]
- ¿La arquitectura se entiende sin código?
- ¿La V1 puede implementarse de forma mínima?
- ¿Está claro qué componentes no existen aún?
- ¿La V2 está planteada como evolución?
- ¿Hay revisión humana?
- ¿Se evitan promesas no verificables?

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
