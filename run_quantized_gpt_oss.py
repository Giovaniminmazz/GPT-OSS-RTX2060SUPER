from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "./model_weights"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    load_in_4bit=True,               # Cuantización 4-bit
    torch_dtype=torch.float16,
    offload_folder="offload",        # Carpeta para offload a disco/RAM
    offload_state_dict=True
)

prompt = "Hola, ¿cómo estás?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))