# Criterios del Portfolio

## Criterios de diseño
- Cada agente debe responder a un problema empresarial reconocible.
- Cada agente debe mantener alcance explícito y verificable.
- Cada agente debe evitar prometer automatización o inteligencia no implementadas.
- La documentación debe separar V1 implementada, V2 futura y fuera de alcance.

## Criterios mínimos por agente
Cada agente del portfolio debe incluir, como mínimo:
- documentación Markdown suficiente para entender el caso de uso,
- un JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) ficticio válido,
- un script local de consola en Python,
- pruebas `unittest`,
- mensajes y errores en castellano,
- revisión humana como parte explícita del flujo.

## Criterios de implementación
- La V1 actual debe funcionar con biblioteca estándar de Python.
- No se incorporan dependencias externas salvo justificación futura clara.
- No se debe presentar como implementado ningún conector, API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*), dashboard, integración real o capa de IA (*Artificial Intelligence – Inteligencia Artificial*) que no exista.

## Criterios de validación
- El script local debe poder ejecutarse por consola.
- Debe existir al menos una prueba de ejecución correcta y pruebas mínimas de error.
- El agente debe trabajar con datos ficticios y trazables.
- La documentación debe coincidir con los nombres reales de scripts, tests y JSON.

## Criterios de veracidad
- No inventar capacidades.
- No presentar una validación local como producto operativo real.
- No presentar datos ficticios como evidencia de uso real.
- No ocultar límites funcionales.

## Criterios de evolución
- V1 implementada: documentación, JSON ficticio, script local y pruebas.
- V2 futura: integraciones, automatizaciones, interfaces y posibles componentes avanzados.
- Fuera de alcance actual: producto completo, automatización real de negocio y promesas no verificables.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
