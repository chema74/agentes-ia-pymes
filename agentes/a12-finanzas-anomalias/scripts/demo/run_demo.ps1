# Demo ejecutable en <2 minutos

# Resolver ruta raíz del proyecto automáticamente
$ProjectRoot = Resolve-Path "$PSScriptRoot/../.."
Set-Location $ProjectRoot

Write-Host " Agente de Detección de Fraude - Demo"
Write-Host "========================================"
Write-Host "⏱️  Tiempo estimado: 90 segundos"
Write-Host "💾 Hardware: Optimizado para 8GB RAM"
Write-Host ""

# Crear entorno virtual si no existe
if (-not (Test-Path ".venv")) {
    Write-Host "📦 Creando entorno virtual..."
    python -m venv .venv
}

# Activar entorno
Write-Host "🔌 Activando entorno..."
& ".venv\Scripts\Activate.ps1"

# Instalar dependencias
Write-Host "📥 Instalando dependencias..."
pip install -q -r requirements.txt

# Generar datos demo
Write-Host ""
Write-Host "📊 Generando datos sintéticos..."
python src/data_generator.py

# Entrenar modelo
Write-Host ""
Write-Host "🔧 Entrenando detector..."
python src/main.py --demo --train --model models/demo_model.pkl

# Ejecutar detección
Write-Host ""
Write-Host "🔍 Ejecutando detección..."
python src/main.py --demo --model models/demo_model.pkl --output demo/results.json

Write-Host ""
Write-Host "✅ Demo completada!"
Write-Host "📄 Ver resultados: demo/results.json"
Write-Host "📊 Ver informe: demo/informe.md"
