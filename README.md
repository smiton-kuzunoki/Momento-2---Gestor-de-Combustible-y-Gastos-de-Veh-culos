# 🚛 Control de Gastos - Flota Vehicular

## Configuración inicial (Estudiante 1 ejecuta esto una sola vez)

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv

# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 2. Inicializar el repositorio Git
git init
git add .
git commit -m "feat: estructura base y menú principal"
```

## Ejecutar el programa

```bash
python main.py
```

---

## Guía por estudiante

### Estudiante 1 — `main` (ya hecho)
- `main.py` → menú principal con `while` loop
- `gastos = []` → lista compartida entre módulos

### Estudiante 2 — rama `feature/registro`
```bash
git checkout -b feature/registro
# Editar registro.py → completar registrar_gasto()
git add registro.py
git commit -m "feat: módulo de registro de gastos"
git checkout main
git merge feature/registro
```

### Estudiante 3 — rama `feature/consulta`
```bash
git checkout -b feature/consulta
# Editar consulta.py → completar ver_gastos()
# En main.py: descomentar las líneas del import y la llamada a ver_gastos(gastos)
git add consulta.py main.py
git commit -m "feat: módulo de consulta y total de gastos"
git checkout main
git merge feature/consulta
```

### Estudiante 4 — rama `feature/busqueda`
```bash
git checkout -b feature/busqueda
# Editar busqueda.py → completar buscar_gasto()
# En main.py: descomentar las líneas del import y la llamada a buscar_gasto(gastos)
git add busqueda.py main.py
git commit -m "feat: módulo de búsqueda por placa"
git checkout main
git merge feature/busqueda
```

---

## Estructura del proyecto

```
control_gastos/
├── main.py         # Estudiante 1 - Menú principal
├── registro.py     # Estudiante 2 - Registrar gasto
├── consulta.py     # Estudiante 3 - Ver total
├── busqueda.py     # Estudiante 4 - Buscar por placa
├── .gitignore
└── README.md
```

## Estructura del diccionario de gasto

```python
gasto = {
    "placa":    "ABC-123",      # str  — placa del vehículo
    "concepto": "Gasolina",     # str  — tipo de gasto
    "valor":    85000.0         # float — monto en pesos
}
```
