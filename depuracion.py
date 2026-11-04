"""
depuracion.py
Consolida los registros exportados de Publish or Perish (Google Académico) para PI1 y PI2,
elimina duplicados por título normalizado y deja un registro de los conteos.

Entradas (misma carpeta):  PI1_crudo.csv, PI2_crudo.csv
Salidas:                   registros_sin_duplicados.csv, conteos_depuracion.txt

Uso:  python depuracion.py
"""
import re
import pandas as pd

# 1. Carga de los CSV crudos
pi1 = pd.read_csv("PI1_crudo.csv")
pi2 = pd.read_csv("PI2_crudo.csv")
pi1["PI"] = "PI1"
pi2["PI"] = "PI2"

# 2. Unión y conteo de registros identificados
total = pd.concat([pi1, pi2], ignore_index=True)

# 3. Normalización del título (minúsculas, solo letras y números) para detectar duplicados
total["titulo_norm"] = (
    total["Title"].fillna("").str.lower().apply(lambda s: re.sub(r"[^a-z0-9 ]", "", s)).str.strip()
)

# 4. Registrar en qué pregunta(s) aparece cada estudio (PI1, PI2 o PI1;PI2)
total["PIs"] = total.groupby("titulo_norm")["PI"].transform(lambda s: ";".join(sorted(set(s))))

# 5. Eliminación de duplicados (se conserva la primera aparición)
sin_dup = total.drop_duplicates(subset="titulo_norm", keep="first")
sin_dup = sin_dup.drop(columns=["titulo_norm", "PI"])
sin_dup.to_csv("registros_sin_duplicados.csv", index=False)

# 6. Registro de conteos (insumo del diagrama PRISMA 2020)
conteos = (
    f"Registros PI1: {len(pi1)}\n"
    f"Registros PI2: {len(pi2)}\n"
    f"Total identificado: {len(total)}\n"
    f"Duplicados eliminados: {len(total) - len(sin_dup)}\n"
    f"Registros tras depurar: {len(sin_dup)}\n"
)
with open("conteos_depuracion.txt", "w", encoding="utf-8") as f:
    f.write(conteos)
print(conteos)
