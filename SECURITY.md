# Security Policy

## Alcance

Este repositorio es un laboratorio local de agentes para PYMES. No esta diseniado como servicio productivo en red.

## Reporte de vulnerabilidades

Si detectas una vulnerabilidad, abre una incidencia con etiqueta `security` y aporta:

- descripcion del riesgo;
- pasos de reproduccion;
- impacto esperado;
- propuesta de mitigacion.

No publiques secretos ni credenciales en la incidencia.

## Reglas de seguridad operativa

- No subir datos reales de clientes.
- No subir tokens, claves API ni contrasenias.
- Mantener `salidas/` y `espacio_trabajo/` fuera de Git.
- Ejecutar `pip-audit` antes de releases importantes.

## Modelo de amenazas minimo

Riesgos cubiertos por controles actuales:

- fuga accidental de secretos en commits;
- ejecuciones locales con archivos no UTF-8 que rompen validaciones;
- introduccion de dependencias vulnerables;
- rutas arbitrarias en lectura de historicos del editor local.

Controles activos:

- CI con `pip-audit`;
- validacion UTF-8 automatica;
- tests de rutas arbitrarias en API local de historico/comparador;
- checklist de release V2.
