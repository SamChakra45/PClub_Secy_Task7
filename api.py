from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import re
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("clickbait_generator.h5")


def clean_text(text):
  text = re.sub(r',', '', text)
  text = re.sub(r'\'', '',  text)
  text = re.sub(r'\"', '', text)
  text = re.sub(r'\(', '', text)
  text = re.sub(r'\)', '', text)
  text = re.sub(r'\n', '', text)
  text = re.sub(r'“', '', text)
  text = re.sub(r'”', '', text)
  text = re.sub(r'’', '', text)
  text = re.sub(r'\.', '', text)
  text = re.sub(r';', '', text)
  text = re.sub(r':', '', text)
  text = re.sub(r'\-', '', text)

  return text

train1_data = pd.read_csv("train1.csv")
Headlines = train1_data["headline"]
Classification = train1_data["clickbait"]

clickbait_sentences = []

for i,headline in enumerate(Headlines):
    if Classification[i] == 1:
        clickbait_sentences.append(clean_text(headline))
        
clickbait_sentences = [text.lower() for text in clickbait_sentences]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(clickbait_sentences)

@app.route("/generate_clickbait", methods=["POST"])
def generate_clickbait():
    data = request.json
    seed_text = data["seed_text"]
    num_words = data["num_words"]

    # Generate text using the model
    generated_text = generate_text(seed_text, num_words)

    response = {
        "generated_text": generated_text
    }
    return jsonify(response)

def generate_text(seed_text, num_words):
    for _ in range(num_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=25, padding='pre')
        predicted = model.predict(token_list)
        predicted_word_index = np.argmax(predicted)
        predicted_word = tokenizer.index_word[predicted_word_index]
        seed_text += " " + predicted_word
    return seed_text

if __name__ == "__main__":
    app.run()
