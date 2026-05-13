#!/bin/bash
# Demo ejecutable en <2 minutos

echo "💰 Agente de Detección de Fraude - Demo"
echo "========================================"
echo "⏱️  Tiempo estimado: 90 segundos"
echo "💾 Hardware: Optimizado para 8GB RAM"
echo ""

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo " Creando entorno virtual..."
    python -m venv .venv
fi

# Activar entorno (detecta OS automáticamente)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# Instalar dependencias
echo " Instalando dependencias..."
pip install -q -r ../../requirements.txt

# Generar datos demo
echo ""
echo "📊 Generando datos sintéticos..."
python ../../src/data_generator.py

# Entrenar modelo
echo ""
echo "🔧 Entrenando detector..."
python ../../src/main.py --demo --train --model ../../models/demo_model.pkl

# Ejecutar detección
echo ""
echo "🔍 Ejecutando detección..."
python ../../src/main.py --demo --model ../../models/demo_model.pkl --output ../../demo/results.json

echo ""
echo "✅ Demo completada!"
echo "📄 Ver resultados: demo/results.json"
echo "📊 Ver informe: demo/informe.md"