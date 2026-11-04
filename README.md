# Revisión sistemática: Zero Trust Architecture en sistemas y arquitectura de software

Datos crudos, scripts y artefactos de la **Fase 3 (Ejecución, Recolección de Datos y Construcción de Artefactos)** del trabajo de titulación. Investigación de tipo bibliográfico y documental, siguiendo la guía **PRISMA 2020**.

## Preguntas de investigación

- **PI1:** Principios de diseño, componentes y arquitecturas de software en Zero Trust.
- **PI2:** Desafíos, barreras de adopción y patrones de migración hacia Zero Trust.

## Ejecución de la búsqueda

- **Fuente:** Google Académico, mediante Publish or Perish 8.19.5300.9483.
- **Fecha de ejecución:** 3 de noviembre de 2026.
- **Filtro temporal:** 2019–2026.
- **Máximo de resultados por consulta:** 1000 (límite de la plataforma). Se desmarcaron las opciones *Citations* y *Patents*.

**Cadena PI1**

```
("Zero Trust Architecture" OR "Zero Trust Security Model") AND ("Software Systems" OR "Software Architecture") AND ("Design Principles" OR "Architectural Principles" OR "Components")
```

**Cadena PI2**

```
("Zero Trust Architecture" OR "Zero Trust Security Model") AND ("Software Systems" OR "Software Architecture") AND ("Migration" OR "Migration Patterns" OR "Legacy Systems" OR "Adoption") AND ("Challenges" OR "Limitations" OR "Barriers")
```

## Conteos (flujo PRISMA 2020)

| Etapa | Registros |
|---|---|
| Estimación de Google Académico (PI1 / PI2) | ~1.360 / ~1.210 |
| Registros exportados (PI1 / PI2) | 964 / 965 |
| **Total identificado** | **1.929** |
| Duplicados eliminados | 698 |
| **Registros cribados** | **1.231** |
| Excluidos en la etapa automatizada (no mencionan Zero Trust en título ni resumen; motivo E1) | 544 |
| Candidatos para lectura de título y resumen | 687 |

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `PI1_crudo.csv` | Exportación cruda de la búsqueda de PI1 |
| `PI2_crudo.csv` | Exportación cruda de la búsqueda de PI2 |
| `depuracion.py` | Script que une los CSV, elimina duplicados y registra los conteos |
| `registros_sin_duplicados.csv` | Resultado de la depuración (1.231 registros) |
| `cribado_listo.xlsx` | Hoja de cribado (columnas ZeroTrust, Etapa, Decisión, Motivo) y hoja de resumen con los conteos |
| `matriz_extraccion.xlsx` | Matriz de extracción: ID de estudio, autores, título, año, fuente, aportes a PI1 y aportes a PI2 |

## Reproducibilidad

1. Ejecutar las dos cadenas en Publish or Perish (fuente Google Scholar, años 2019–2026, máximo 1000) y guardar los resultados como `PI1_crudo.csv` y `PI2_crudo.csv`.
2. Colocar ambos archivos junto a `depuracion.py` y ejecutar `python depuracion.py` (requiere `pandas`).
3. Los conteos se escriben en `conteos_depuracion.txt`.

## Códigos de motivo de exclusión

E1: fuera de tema o mención de pasada de Zero Trust · E2: sin aporte a PI1 ni a PI2 · E3: fuera del rango 2019–2026 · E4: idioma distinto de inglés o español · E5: sin acceso al resumen o al texto.

## Limitaciones

- Google Académico limita la visualización a unos 1.000 resultados por consulta y sus estimaciones varían entre ejecuciones; las cifras corresponden a la ejecución del 3 de noviembre de 2026.
- El cribado de título y resumen de los registros restantes y la extracción de datos sobre ellos continúan en curso.
- Las cadenas están formuladas en inglés, por lo que el corpus es mayoritariamente en ese idioma.
