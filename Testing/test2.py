from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(prompt, model_dir, max_length=10):
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=max_length, num_return_sequences=1)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    model_dir = "C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.9 (Matching JSON Pairs)/gpt2-finetuned"
    prompt = "what can we do today"
    print("Generated Text:", generate_text(prompt, model_dir))
