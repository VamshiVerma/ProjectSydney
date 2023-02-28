import streamlit as st
import openai

# Replace FINE_TUNED_MODEL with the name of your fine-tuned model
model_name = "davinci:ft-personal-2023-02-24-03-55-15"

openai.api_key ="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"

def on_submit(prompt):
    # Make the completion request
    completion = openai.Completion.create(model=model_name, prompt=prompt)

    # Get the completion text from the first choice in the choices list
    text = completion.choices[0]["text"]

    return text

def main():
    # Create the main page title
    st.title("Fine-tuned GPT-3")

    # Create the input field
    prompt = st.text_input("Enter prompt:")

    # Create the submit button and display the result
    if st.button("Submit"):
        result = on_submit(prompt)
        st.write(result)

if __name__ == "__main__":
    main()
