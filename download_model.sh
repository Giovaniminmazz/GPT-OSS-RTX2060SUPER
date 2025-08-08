```bash
#!/bin/bash
echo "Descargando pesos del modelo GPT-OSS 20B..."
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b ./model_weights
echo "Modelo descargado en ./model_weights"