# frozenlake_sheet
Implementación del algoritmo Q-Learning para el juego FrozenLake con visualización en tiempo real usando Google Sheets.

## 🎯 DESCRIPCIÓN
Este proyecto entrena un agente de Q-Learning para navegar en el entorno FrozenLake de Gymnasium, mostrando la evolución de la Q-table y estadísticas de entrenamiento directamente en Google Sheets.

## 📋 CARACTERÍSTICAS
- ✅ Algoritmo Q-Learning para FrozenLake
- 📊 Visualización en tiempo real de la Q-table en Google Sheets
- 📈 Dashboard con métricas de entrenamiento
- 🔄 Actualización automática durante el entrenamiento
- 📱 Acceso desde cualquier dispositivo con Google Sheets

## 🚀 INSTALACIÓN

### Clonar el repositorio
```bash
git clone https://github.com/financieras    /frozenlake_sheet.git
```

### Ir a la carpeta del proyecto
```bash
cd frozenlake_sheet
```

### Crear un entorno virtual llamado '.venv'
```bash
python3 -m venv .venv
```

### Activar el entorno virtual
```bash
# En macOS/Linux:
source .venv/bin/activate

# En Windows:
.venv\Scripts\activate
```

### Actualizar pip (recomendado)
```bash
pip install --upgrade pip
```

### Instalar las dependencias
```bash
pip install -r requirements.txt
```

## ⚙️ CONFIGURACIÓN

### 1. Configurar Google Cloud Console
- Crear proyecto en [Google Cloud Console](https://console.cloud.google.com/)
- Habilitar Google Sheets API y Google Drive API
- Crear cuenta de servicio y descargar credenciales JSON

### 2. Crear hoja de Google Sheets
- Crear nueva hoja llamada `FrozenLake_QTable`
- Compartir con el email de la cuenta de servicio (permisos de Editor)

### 3. Configurar variables de entorno
Crear archivo `.env` en la raíz del proyecto:
```env
GOOGLE_APPLICATION_CREDENTIALS_JSON={"type":"service_account",...}
SPREADSHEET_NAME=FrozenLake_QTable
```

## 🧪 PROBAR LA CONEXIÓN
```bash
python test_connection.py
```

## 🎮 EJECUTAR EL ENTRENAMIENTO
```bash
python src/main.py
```

## 📊 VISUALIZACIÓN
Una vez iniciado el entrenamiento, podrás ver en tiempo real:
- **Q-Table**: Valores de la función Q para cada estado-acción
- **Statistics**: Historial de episodios, recompensas y pasos
- **Dashboard**: Métricas de rendimiento y gráficos

## 📁 ESTRUCTURA DEL PROYECTO
```
frozenlake_sheet/
├── src/
│   ├── main.py              # Script principal
│   ├── q_learning.py        # Algoritmo Q-Learning
│   └── sheets_handler.py    # Conexión con Google Sheets
├── test_connection.py       # Prueba de conexión
├── requirements.txt         # Dependencias
├── .env                     # Variables de entorno (no subir a git)
├── .gitignore              # Archivos a ignorar
└── README.md               # Este archivo
```

## 🔧 DESACTIVAR EL ENTORNO VIRTUAL
Al terminar de trabajar:
```bash
deactivate
```

## 📄 LICENCIA
Este proyecto está bajo la Licencia MIT.

---
⚡ **Creado para aprender Q-Learning de forma visual e interactiva**
