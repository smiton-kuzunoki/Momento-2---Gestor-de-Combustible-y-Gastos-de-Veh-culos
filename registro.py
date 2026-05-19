# ============================================================
#  Módulo de Registro de Gastos
#  Angelica Ruiz - Rama: feature/registro
# ============================================================

def registrar_gasto(gastos):
    """
    Pide los datos de un gasto por consola y lo agrega
    a la lista compartida 'gastos' como un diccionario.
    """
    print("\n--- REGISTRAR NUEVO GASTO ---")

    # Solicitar y validar la placa del vehículo
    while True:
        placa = input("  Placa del vehículo: ").strip().upper()
        if placa:
            break
        print("  ⚠️  La placa no puede estar vacía.")

    # Solicitar y validar el concepto
    while True:
        concepto = input("  Concepto (Ej: Gasolina, Peaje, Mantenimiento): ").strip()
        if concepto:
            break
        print("  ⚠️  El concepto no puede estar vacío.")

    # Solicitar y validar el valor
    while True:
        valor_texto = input("  Valor ($): ").strip()
        try:
            valor = float(valor_texto)
            if valor <= 0:
                print("  ⚠️  El valor debe ser mayor a cero.")
            else:
                break
        except ValueError:
            print("  ⚠️  Ingrese un número válido (Ej: 50000).")

    # Crear el diccionario con los datos del gasto
    gasto = {
        "placa":    placa,
        "concepto": concepto,
        "valor":    valor
    }

    # Agregar el diccionario a la lista compartida
    gastos.append(gasto)

    print(f"\n  ✅ Gasto registrado exitosamente:")
    print(f"     🚗 Placa   : {gasto['placa']}")
    print(f"     📋 Concepto: {gasto['concepto']}")
    print(f"     💰 Valor   : ${gasto['valor']:,.2f}")
