# ============================================================
#  Control de Gastos de Vehículos - Empresa de Transporte
#  Estudiante 1: Estructura y Menú Principal
# ============================================================

from registro import registrar_gasto       # Estudiante 2
# from consulta import ver_gastos           # Estudiante 3 (descomentar cuando esté listo)
# from busqueda import buscar_gasto         # Estudiante 4 (descomentar cuando esté listo)

# Lista compartida donde se guardan todos los gastos
gastos = []

def mostrar_menu():
    print("\n" + "=" * 45)
    print("   🚛  CONTROL DE GASTOS - FLOTA VEHICULAR")
    print("=" * 45)
    print("  1. Registrar nuevo gasto")
    print("  2. Ver total de gastos")
    print("  3. Buscar gasto por placa")
    print("  4. Salir")
    print("=" * 45)

def main():
    print("\n¡Bienvenido al sistema de control de gastos!")

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            registrar_gasto(gastos)

        elif opcion == "2":
            print("\n  [Módulo pendiente - Estudiante 3]")
            # ver_gastos(gastos)

        elif opcion == "3":
            print("\n  [Módulo pendiente - Estudiante 4]")
            # buscar_gasto(gastos)

        elif opcion == "4":
            print("\n  👋 Hasta luego. ¡Buena jornada!\n")
            break

        else:
            print("\n  ⚠️  Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
