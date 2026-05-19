# ============================================================
#  Módulo de Consulta de Gastos
#  Angelica Ruiz - Rama: feature/calculos (o feature/consulta)
# ============================================================

def ver_gastos(gastos):
    """
    Muestra todos los gastos registrados y calcula el total.
    """
    print("\n--- RESUMEN TOTAL DE GASTOS ---")

    # 1. Verificar si la lista 'gastos' está vacía
    if not gastos:
        print("  ❌ No hay gastos registrados en el sistema.")
        return

    # Inicializamos el acumulador en cero
    total_acumulado = 0

    print(f"{'PLACA':<10} | {'CONCEPTO':<20} | {'VALOR':<12}")
    print("-" * 48)

    # 2. Recorrer la lista con un ciclo for e imprimir cada gasto
    for gasto in gastos:
        print(f"{gasto['placa']:<10} | {gasto['concepto']:<20} | ${gasto['valor']:,.2f}")
        # 3. Calcular el total acumulado
        total_acumulado += gasto['valor']

    print("-" * 48)
    print(f"💰 GASTO TOTAL ACUMULADO: ${total_acumulado:,.2f}")