import pandas as pd
import numpy as np

# Leer los datos
ingresos_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Ingresos')
reservas_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Reservas')
adr_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='ADR')

print("=== ANÁLISIS DE DATOS POR TIPO DE HABITACIÓN ===\n")

# Procesar ingresos por tipo
tipos_habitacion = ingresos_df['Tipo'].unique()
print("Tipos de habitación encontrados:", tipos_habitacion)

# Calcular totales por tipo para 2024 y 2025
meses_2024 = [col for col in ingresos_df.columns if '2024' in str(col)]
meses_2025 = [col for col in ingresos_df.columns if '2025' in str(col)]

print(f"\nMeses 2024: {len(meses_2024)}")
print(f"Meses 2025: {len(meses_2025)}")

# Estadísticas por tipo de habitación
stats_por_tipo = {}

for tipo in tipos_habitacion:
    tipo_data = ingresos_df[ingresos_df['Tipo'] == tipo]
    
    # Ingresos totales
    ingresos_2024 = tipo_data[meses_2024].sum().sum()
    ingresos_2025 = tipo_data[meses_2025].sum().sum()
    
    # Promedio por cabaña
    num_cabanas = len(tipo_data)
    ingresos_promedio_2024 = ingresos_2024 / num_cabanas if num_cabanas > 0 else 0
    ingresos_promedio_2025 = ingresos_2025 / num_cabanas if num_cabanas > 0 else 0
    
    # ADR promedio
    adr_tipo = adr_df[adr_df['Tipo'] == tipo]
    adr_promedio = adr_tipo[meses_2024 + meses_2025].mean().mean()
    
    # Ocupación promedio
    reservas_tipo = reservas_df[reservas_df['Tipo'] == tipo]
    ocupacion_2024 = reservas_tipo[meses_2024].sum().sum() / (num_cabanas * 365) * 100
    ocupacion_2025 = reservas_tipo[meses_2025].sum().sum() / (num_cabanas * 365) * 100
    
    stats_por_tipo[tipo] = {
        'num_cabanas': num_cabanas,
        'ingresos_2024': ingresos_2024,
        'ingresos_2025': ingresos_2025,
        'ingresos_promedio_2024': ingresos_promedio_2024,
        'ingresos_promedio_2025': ingresos_promedio_2025,
        'adr_promedio': adr_promedio,
        'ocupacion_2024': ocupacion_2024,
        'ocupacion_2025': ocupacion_2025
    }
    
    print(f"\n{tipo}:")
    print(f"  Número de cabañas: {num_cabanas}")
    print(f"  Ingresos totales 2024: ${ingresos_2024:,.2f}")
    print(f"  Ingresos totales 2025: ${ingresos_2025:,.2f}")
    print(f"  Ingresos promedio por cabaña 2024: ${ingresos_promedio_2024:,.2f}")
    print(f"  Ingresos promedio por cabaña 2025: ${ingresos_promedio_2025:,.2f}")
    print(f"  ADR promedio: ${adr_promedio:,.2f}")
    print(f"  Ocupación promedio 2024: {ocupacion_2024:.1f}%")
    print(f"  Ocupación promedio 2025: {ocupacion_2025:.1f}%")

# Datos mensuales para gráficas
print("\n=== DATOS MENSUALES PARA GRÁFICAS ===")

# Preparar datos para gráficas de líneas
meses_labels = []
for col in meses_2024 + meses_2025:
    if '2024' in str(col):
        mes = str(col).split('-')[1] + '/24'
    else:
        mes = str(col).split('-')[1] + '/25'
    meses_labels.append(mes)

print("Etiquetas de meses:", meses_labels)

# Datos de ocupación mensual por tipo
ocupacion_mensual = {}
for tipo in tipos_habitacion:
    reservas_tipo = reservas_df[reservas_df['Tipo'] == tipo]
    num_cabanas = len(reservas_tipo)
    
    ocupacion_mensual[tipo] = []
    for col in meses_2024 + meses_2025:
        ocupacion_mes = reservas_tipo[col].sum().sum() / (num_cabanas * 30) * 100
        ocupacion_mensual[tipo].append(ocupacion_mes)

# Datos de ADR mensual por tipo
adr_mensual = {}
for tipo in tipos_habitacion:
    adr_tipo = adr_df[adr_df['Tipo'] == tipo]
    adr_mensual[tipo] = adr_tipo[meses_2024 + meses_2025].mean().tolist()

print("\nDatos de ocupación mensual por tipo:")
for tipo, datos in ocupacion_mensual.items():
    print(f"{tipo}: {[f'{x:.1f}%' for x in datos]}")

print("\nDatos de ADR mensual por tipo:")
for tipo, datos in adr_mensual.items():
    print(f"{tipo}: {[f'${x:.2f}' for x in datos]}")

# Guardar resultados en un archivo para usar en el HTML
with open('dashboard_data.json', 'w') as f:
    import json
    json.dump({
        'stats_por_tipo': stats_por_tipo,
        'meses_labels': meses_labels,
        'ocupacion_mensual': ocupacion_mensual,
        'adr_mensual': adr_mensual
    }, f, indent=2)

print("\nDatos guardados en dashboard_data.json")
