<div align="center">
    <img src="https://img.shields.io/badge/GPT--OSS-20B-blueviolet?style=for-the-badge&logo=nvidia" alt="GPT-OSS 20B" height="40" />
    <h1>🤖 GPT-OSS para RTX 2060 Super (8GB VRAM)</h1>
    <p>Ejecuta el modelo <b>GPT-OSS 20B</b> en tu GPU de 8GB VRAM con cuantización y offloading optimizados.</p>
</div>

---

## 🚀 Características

- Cuantización a 4-bit con <b>bitsandbytes</b>
- Offloading de memoria con <b>accelerate</b>
- Optimizado para RTX 2060 Super (8GB VRAM)
- Fácil instalación y uso

---

## 🖥️ Requisitos

| Requisito      | Detalle                 |
| -------------- | ----------------------- |
| Python         | 3.10+                   |
| GPU            | NVIDIA RTX 2060 Super   |
| VRAM           | 8 GB                    |
| Disco          | > 20 GB libres          |

---

## ⚡ Instalación rápida

```bash
# 1. Clona este repositorio
git clone https://github.com/tu_usuario/gpt-oss-2060super.git
cd gpt-oss-2060super

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Descarga los pesos del modelo
./download_model.sh

# 4. Ejecuta el modelo cuantizado
python run_quantized_gpt_oss.py
```

<details>
<summary>📋 <b>Notas importantes</b></summary>

- Se usa <b>bitsandbytes</b> para cuantización a 4-bit y <b>accelerate</b> para offload de memoria.
- Cierra otros procesos que consuman GPU para liberar memoria.

</details>

---

## 📦 Dependencias principales

| Paquete        | Uso principal         |
| -------------  | -------------------- |
| torch          | Deep Learning        |
| transformers   | Modelos de lenguaje  |
| accelerate     | Offloading           |
| safetensors    | Pesos eficientes     |
| bitsandbytes   | Cuantización         |

---

## 📥 Script de descarga (`download_model.sh`)

```bash
#!/bin/bash
echo "Descargando pesos del modelo GPT-OSS 20B..."
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b ./model_weights
echo "Modelo descargado en ./model_weights"
```

---

## 🤝 Créditos

- Basado en [GPT-OSS 20B](https://huggingface.co/openai/gpt-oss-20b)
- Adaptado para RTX 2060 Super por Giovaniminmazz

---

<div align="center">
    <b>¡Listo para usar IA de última generación en tu GPU de 8GB! 🚀</b>
</div>