import gspread
import os
from dotenv import load_dotenv
import json
from google.oauth2.service_account import Credentials

# Cargar configuración
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

google_creds_json_str = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON')

if google_creds_json_str:
    try:
        google_creds_dict = json.loads(google_creds_json_str)
    except json.JSONDecodeError:
        credentials_path = os.path.join(os.path.dirname(__file__), '..', google_creds_json_str)
        with open(credentials_path, 'r') as f:
            google_creds_dict = json.load(f)
else:
    raise ValueError("Variable GOOGLE_APPLICATION_CREDENTIALS_JSON no encontrada")

# Conectar
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_info(google_creds_dict, scopes=scopes)
gc = gspread.authorize(credentials)

# Abrir la hoja de cálculo
spreadsheet = gc.open('FrozenLake_QTable')

print("✓ Conectado exitosamente")

# Función optimizada para obtener o crear una hoja
def get_or_create_worksheet(spreadsheet, sheet_name, rows=100, cols=20):
    try:
        worksheet = spreadsheet.worksheet(sheet_name)
        print(f"✓ Hoja '{sheet_name}' encontrada")
        return worksheet
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=rows, cols=cols)
        print(f"✓ Hoja '{sheet_name}' creada")
        return worksheet

# Obtener hojas
sh1 = get_or_create_worksheet(spreadsheet, "Tablero", rows=50, cols=10)
sh2 = get_or_create_worksheet(spreadsheet, "Q-Table", rows=100, cols=20)

# ========== OPTIMIZACIÓN: USAR BATCH_UPDATE ==========
print("🚀 Actualizando datos en lote...")

# Preparar todos los datos para la hoja "Tablero"
tablero_data = [
    ['', 'Juego Frozen Lake', '', '', ''],      # Fila 2
    ['', 'Tablero 4x4', '', '', ''],            # Fila 3
    ['', '', '', '', ''],                        # Fila 4 (vacía)
    ['', 'S', 'F', 'F', 'F'],                  # Fila 5
    ['', 'F', 'H', 'F', 'H'],                  # Fila 6
    ['', 'F', 'F', 'F', 'H'],                  # Fila 7
    ['', 'H', 'F', 'F', 'G']                   # Fila 8
]

# Una sola llamada para toda la hoja "Tablero"
sh1.update(values=tablero_data, range_name='A2:E8')

# Preparar datos para la Q-Table
qtable_header = [['Q-Table para Frozen Lake']]
qtable_columns = [['Estado', 'Arriba', 'Abajo', 'Izquierda', 'Derecha']]

# Generar todos los estados de una vez
qtable_states = []
for i in range(16):
    qtable_states.append([f'Estado {i}', 0.0, 0.0, 0.0, 0.0])

# Actualizar Q-Table en tres llamadas mínimas
sh2.update(values=qtable_header, range_name='A1')
sh2.update(values=qtable_columns, range_name='A3:E3')
sh2.update(values=qtable_states, range_name='A4:E19')

print("✓ Operaciones completadas (optimizadas)")
print(f"🔗 URL: {spreadsheet.url}")

# Mostrar hojas disponibles
worksheets = spreadsheet.worksheets()
print(f"\n📊 Hojas disponibles: {len(worksheets)}")
for i, ws in enumerate(worksheets, 1):
    print(f"  {i}. {ws.title}")