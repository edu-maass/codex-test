import pandas as pd
import numpy as np

# Leer el archivo Excel
try:
    # Leer la hoja de Reservas (ocupación)
    reservas_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Reservas')
    ingresos_df = pd.read_excel('Reporte_Ingresos_Ocupacion.xlsx', sheet_name='Ingresos')
    
    print("=== DATOS DE RESERVAS (OCUPACIÓN) ===")
    print(reservas_df.head())
    print("\nColumnas disponibles:", reservas_df.columns.tolist())
    
    print("\n=== DATOS DE INGRESOS ===")
    print(ingresos_df.head())
    print("\nColumnas disponibles:", ingresos_df.columns.tolist())
    
    # Calcular ocupación para cada cabaña
    print("\n=== CÁLCULO DE OCUPACIÓN REAL ===")
    
    # Obtener columnas de meses para 2024 y 2025
    meses_2024 = [col for col in reservas_df.columns if '2024' in str(col)]
    meses_2025 = [col for col in reservas_df.columns if '2025' in str(col)]
    
    print(f"Meses 2024: {meses_2024}")
    print(f"Meses 2025: {meses_2025}")
    
    # Calcular ocupación total por cabaña
    for index, row in reservas_df.iterrows():
        cabana = row['Cabaña'] if 'Cabaña' in reservas_df.columns else row.iloc[0]
        
        # Sumar ocupación de todos los meses de 2024
        ocupacion_2024 = sum([row[mes] for mes in meses_2024 if pd.notna(row[mes])])
        
        # Sumar ocupación de todos los meses de 2025
        ocupacion_2025 = sum([row[mes] for mes in meses_2025 if pd.notna(row[mes])])
        
        print(f"Cabaña {cabana}:")
        print(f"  Ocupación 2024: {ocupacion_2024:.1f} días")
        print(f"  Ocupación 2025: {ocupacion_2025:.1f} días")
        
        # Calcular porcentaje de ocupación (asumiendo 365 días por año)
        porcentaje_2024 = (ocupacion_2024 / 365) * 100
        porcentaje_2025 = (ocupacion_2025 / 365) * 100
        
        print(f"  Porcentaje 2024: {porcentaje_2024:.1f}%")
        print(f"  Porcentaje 2025: {porcentaje_2025:.1f}%")
        print()
        
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    print("Verificando archivos disponibles...")
    
    import os
    files = os.listdir('.')
    excel_files = [f for f in files if f.endswith('.xlsx')]
    print(f"Archivos Excel encontrados: {excel_files}")
