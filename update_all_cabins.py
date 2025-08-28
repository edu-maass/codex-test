import pandas as pd
import json

# Leer los datos del Excel
ingresos_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Ingresos')
reservas_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Reservas')

# Calcular totales por cabaña para 2024 y 2025
meses_2024 = [col for col in ingresos_df.columns if '2024' in str(col)]
meses_2025 = [col for col in ingresos_df.columns if '2025' in str(col)]

# Crear diccionario con datos de cada cabaña
cabins_data = {}

for index, row in ingresos_df.iterrows():
    # Verificar que la habitación sea válida
    if pd.notna(row['habitacion']) and row['habitacion'] != 'Total' and str(row['habitacion']).replace('.0', '').isdigit():
        cabana_num = int(float(row['habitacion']))
        
        # Calcular ingresos totales
        ingresos_2024 = row[meses_2024].sum()
        ingresos_2025 = row[meses_2025].sum()
        
        # Calcular ocupación
        reservas_row = reservas_df[reservas_df['habitacion'] == row['habitacion']]
        if not reservas_row.empty:
            ocupacion_2024 = reservas_row[meses_2024].sum().sum() / 365 * 100
            ocupacion_2025 = reservas_row[meses_2025].sum().sum() / 365 * 100
        else:
            ocupacion_2024 = 0
            ocupacion_2025 = 0
        
        # Calcular ADR promedio
        adr_2024 = ingresos_2024 / 365 if ocupacion_2024 > 0 else 0
        adr_2025 = ingresos_2025 / 365 if ocupacion_2025 > 0 else 0
        
        cabins_data[cabana_num] = {
            'ingresos_2024': ingresos_2024,
            'ingresos_2025': ingresos_2025,
            'ocupacion_2024': ocupacion_2024,
            'ocupacion_2025': ocupacion_2025,
            'adr_2024': adr_2024,
            'adr_2025': adr_2025,
            'tipo': row['Tipo']
        }

# Guardar datos en JSON
with open('cabins_data.json', 'w') as f:
    json.dump(cabins_data, f, indent=2)

print("Datos de cabañas guardados en cabins_data.json")

# Mostrar resumen
print("\n=== RESUMEN DE DATOS POR CABAÑA ===")
for cabana_num in sorted(cabins_data.keys()):
    data = cabins_data[cabana_num]
    print(f"Cabaña {cabana_num} ({data['tipo']}):")
    print(f"  Ingresos 2024: ${data['ingresos_2024']:,.2f}")
    print(f"  Ingresos 2025: ${data['ingresos_2025']:,.2f}")
    print(f"  Ocupación 2024: {data['ocupacion_2024']:.1f}%")
    print(f"  Ocupación 2025: {data['ocupacion_2025']:.1f}%")
    print(f"  ADR 2024: ${data['adr_2024']:.2f}")
    print(f"  ADR 2025: ${data['adr_2025']:.2f}")
    print()
