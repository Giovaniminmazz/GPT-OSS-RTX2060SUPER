# GPT-OSS para RTX 2060 Super (8GB VRAM)

Este proyecto te permite ejecutar el modelo GPT-OSS 20B en una GPU con 8 GB de VRAM aplicando cuantización y offloading para optimizar memoria.

---

## Requisitos

- Python 3.10+
- NVIDIA RTX 2060 Super (8GB VRAM)
- Espacio libre > 20 GB para pesos del modelo

---

## Instalación

1. Clona este repositorio:

"```bash"
git clone https://github.com/tu_usuario/gpt-oss-2060super.git
cd gpt-oss-2060super

2. Instala las dependencias:

pip install -r requirements.txt

3. Descarga los pesos del modelo:

./download_model.sh

4. Ejecuta el modelo cuantizado:

python run_quantized_gpt_oss.py

### Notas:

    Se usa bitsandbytes para cuantización a 4-bit y accelerate para offload de memoria.

    Se recomienda cerrar otros procesos que consuman GPU para liberar memoria.


---

### 2. requirements.txt

- torch
- transformers
- accelerate
- safetensors
- bitsandbytes


---

### 3. download_model.sh

"```bash"
#!/bin/bash
echo "Descargando pesos del modelo GPT-OSS 20B..."
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b ./model_weights
echo "Modelo descargado en ./model_weights"