import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_response(prompt, model, tokenizer, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def chat():
    model_name = "gpt2"

    # Load tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Load model
    model = GPT2LMHeadModel.from_pretrained(model_name)

    print("Welcome to the GPT-2 Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = generate_response(user_input, model, tokenizer)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()

