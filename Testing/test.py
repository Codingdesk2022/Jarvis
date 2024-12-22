import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch.utils.data import Dataset

# Define a custom dataset class for loading and preparing the training data
class TextDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=512):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.texts = file.readlines()
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx].strip()
        # Tokenize and create a dictionary for the input
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        # Squeeze to remove batch dimension
        input_ids = encoding['input_ids'].squeeze(0)
        attention_mask = encoding['attention_mask'].squeeze(0)
        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': input_ids  # Add labels to calculate the loss
        }

# Fine-tune the GPT-2 model using the custom dataset and create tokenizer files
def fine_tune_gpt2(file_path, output_dir='./gpt2-finetuned', epochs=3, batch_size=2):
    # Load the tokenizer and model from the pretrained 'gpt2' model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token  # Set padding token for GPT-2
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Create a dataset for training
    dataset = TextDataset(file_path, tokenizer)

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir='./logs',
        logging_steps=500,
        overwrite_output_dir=True,
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    # Train the model
    trainer.train()

    # Save the model and tokenizer after training
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    print(f"Model and tokenizer saved in: {output_dir}")

# Replace 'path/to/your/textfile.txt' with the path to your plain text file
file_path = 'C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.9 (Matching JSON Pairs)/Testing/TrainingData.txt'

# Run the fine-tuning function
fine_tune_gpt2(file_path)
