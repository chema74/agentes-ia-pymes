$ProjectRoot = Resolve-Path "$PSScriptRoot/../.."
Set-Location $ProjectRoot

Write-Host "🌱 Agente ESG Reporting - Demo"
Write-Host "========================================"
if (-not (Test-Path ".venv")) { python -m venv .venv }
& ".venv\Scripts\Activate.ps1"
pip install -q -r requirements.txt

Write-Host "📊 Generando datos y calculando métricas..."
python src/main.py --demo

Write-Host "✅ Demo completada. Revisa la carpeta reports/"
