from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Load model and tokenizer from saved folder
model = AutoModelForSequenceClassification.from_pretrained(r"D:/complete-emoji-model")
tokenizer = AutoTokenizer.from_pretrained(r"D:/complete-emoji-model")

# Emoji ID to Emoji character
id2emoji = {
    0: '❤',   1: '😍',  2: '😂',  3: '💕',  4: '🔥',
    5: '😊',  6: '😎',  7: '✨',  8: '💙',  9: '😘',
    10: '📷', 11: '🇺🇸', 12: '☀', 13: '💜', 14: '😉',
    15: '💯', 16: '😁', 17: '🎄', 18: '📸', 19: '😜'
}

emoji_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def predict_emoji(text):
    result = emoji_classifier(text)
    label = int(result[0]["label"].replace("LABEL_", ""))
    return f"{id2emoji[label]}"

# Create User Interface
import gradio as gr

iface = gr.Interface(
    fn=predict_emoji,
    inputs=gr.Textbox(lines=2, placeholder="Type a message here..."),
    outputs="text",
    title="Emoji Predictor 🤖✨",
    description="Enter a sentence and get a predicted emoji!"
)

iface.launch()