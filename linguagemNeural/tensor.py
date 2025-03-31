import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text  # Para lidar com tokenização

# Carregar um modelo BERT pré-treinado
model_url = "https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1"
model = hub.load(model_url)

def predict_message(message):
    # Tokenize a mensagem e realize a predição
    message_input = [message]
    embeddings = model(message_input)
    # Aqui você pode usar embeddings para classificações ou outras tarefas
    return embeddings

# Testar com uma mensagem de exemplo
message = "Oi, como você está?"
result = predict_message(message)
print(result)

# Para testar sem usar Docker, você pode criar um ambiente virtual localmente:
# 1. Crie um ambiente virtual: `python -m venv venv`
# 2. Ative o ambiente virtual:
#    - No Windows: `venv\Scripts\activate`
#    - No macOS/Linux: `source venv/bin/activate`
# 3. Instale as dependências necessárias: `pip install tensorflow tensorflow_hub tensorflow_text numpy`
# 4. Execute o script diretamente no terminal: `python tensor.py`