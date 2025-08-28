# Datos reales de ocupación del Excel
ocupacion_real = {
    1: (13.7, 38.4),
    2: (20.5, 36.4),
    3: (22.5, 46.6),
    4: (24.4, 45.2),
    5: (20.3, 35.1),
    6: (24.4, 51.8),
    7: (18.4, 33.7),
    8: (15.6, 26.0),
    9: (29.9, 56.2),
    10: (42.5, 44.7),
    11: (20.3, 42.2),
    12: (25.8, 48.8),
    13: (16.4, 37.8),
    14: (19.2, 44.9),
    15: (17.5, 37.8),
    16: (18.9, 34.8),
    17: (8.8, 15.9),
    19: (0.0, 0.0)
}

print("=== KPIs DE OCUPACIÓN REALES ===")
for cabana, (ocup_2024, ocup_2025) in ocupacion_real.items():
    print(f"Cabaña {cabana}: 2024: {ocup_2024}%, 2025: {ocup_2025}%")

print("\n=== INSTRUCCIONES PARA ACTUALIZAR ===")
print("Necesitas agregar estos KPIs a cada cabaña en el HTML:")
print("1. Buscar la sección de metrics-grid de cada cabaña")
print("2. Agregar después de los ingresos y antes del ADR:")
print("   - Ocupación 2024: [porcentaje]%")
print("   - Ocupación 2025: [porcentaje]%")
print("3. Ajustar el grid para 6 tarjetas en lugar de 4")
