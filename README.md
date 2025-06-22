# 🤖 Emoji Predictor AI Model 🎉

Welcome to the **Emoji Predictor** — an AI-powered web app that predicts the most relevant emoji for any sentence or message using state-of-the-art Natural Language Processing!

This model is fine-tuned on real-world tweets using the `tweet_eval` dataset, and deployed using **Gradio** for easy interaction.

---

## 📌 Project Overview

- 💬 **Input**: A sentence or short message (e.g., "I'm so happy today!")
- 🎯 **Output**: The most suitable emoji (e.g., 😊)
- 🧠 **Model**: Fine-tuned `roberta-base`
- 🗂️ **Dataset**: `cardiffnlp/tweet_eval` (emoji subset with 20 emoji labels)
- 🌐 **UI**: Built using Gradio for quick testing

---

---

## 💻 Demo

![Screenshot 2025-06-22 174950](https://github.com/user-attachments/assets/c8259a5a-8250-4605-adbf-2b9c44944f41)

---

---

## ⚙️Tech Stack

- 🤗  **Hugging Face Transformers**
- 🐍  **Python**
- 📊  **TweetEval Dataset**
- 🔠  **RoBERTa Model**
- 🌐  **Gradio Web Interface**

---

## 🚀 Try It Yourself (Locally)

```bash
pip install -r requirements.txt
python app.py
