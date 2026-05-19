# ==========================================
#  Módulo de Búsqueda de Gastos
#  Santiago Rey- Rama: feature/busqueda
# ==========================================
def buscar_gasto(gastos):
    """
    Busca todos los gastos de un vehículo por su placa.
    """
    print("\n--- BUSCAR GASTO POR PLACA ---")

    # 1. Verificar si hay datos antes de buscar
    if not gastos:
        print("  ❌ No hay gastos registrados en el sistema para buscar.")
        return

    # 2. Pedir la placa al usuario
    placa_buscada = input("  Ingrese la placa a buscar: ").strip().upper()
    
    # Variable bandera para saber si encontramos al menos un registro
    encontrado = False
    total_vehiculo = 0

    print(f"\nGastos encontrados para el vehículo [{placa_buscada}]:")
    print("-" * 40)

    # 3. Recorrer la lista 'gastos' con un ciclo for
    for gasto in gastos:
        # 4. Comparar la placa ingresada con la de cada diccionario
        if gasto['placa'] == placa_buscada:
            print(f"  • {gasto['concepto']}: ${gasto['valor']:,.2f}")
            total_vehiculo += gasto['valor']
            encontrado = True

    # 5. Imprimir un mensaje si no se encontraron resultados
    if not encontrado:
        print("  ❌ No se encontraron gastos registrados para esa placa.")
    else:
        print("-" * 40)
        print(f"  💰 Total acumulado del vehículo: ${total_vehiculo:,.2f}")
