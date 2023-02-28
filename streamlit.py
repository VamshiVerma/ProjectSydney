import streamlit as st
import openai

# Replace FINE_TUNED_MODEL with the name of your fine-tuned model
model_name = "davinci:ft-personal-2023-02-24-03-55-15"

openai.api_key = st.secrets["openkey"]
import streamlit as st
import openai
import json

st.title("Footrack")

# Suggested prompts
suggested_prompts =  ["Which team has the highest number of points this season?",
 "What team has the lowest goal difference this season?",
 "Which team has the most wins this season?",
 "What team has the most draws this season?",
 "Which team has the most losses this season?",
 "What team has the most goals scored this season?",
 "Which team has the fewest goals scored this season?",
 "What team has the most goals conceded this season?",
 "Which team has the fewest goals conceded this season?",
 "What team has the best goal difference this season?",
 "Which team has the worst goal difference this season?",
 "What team has the longest unbeaten streak this season?",
 "Which team has the most consecutive wins this season?",
 "What team has the most consecutive losses this season?",
 "Which team has the most consecutive draws this season?",
 "What team has the most goals scored in a single game this season?",
 "Which team has the most goals conceded in a single game this season?",
 "What team has the highest win percentage this season?",
 "Which team has the lowest win percentage this season?",
 "What team has the highest draw percentage this season?",
 "What team has the fewest draws away from home this season?",
 "What team has the most losses at home this season?",
 "Which team has the most losses away from home this season?",
 "What team has the fewest losses at home this season?",
 "Which team has the fewest losses away from home this season?",
 "What team has the most goals scored at home this season?",
 "Which team has the most goals scored away from home this season?",
 "What team has the fewest goals scored at home this season?",
 "Which team has the fewest goals scored away from home this season?",
 "What team has the most goals conceded at home this season?",
 "Which team has the most goals conceded away from home this season?",
 "What team has the fewest goals conceded at home this season?",
 "Which team has the fewest goals conceded away from home this season?",
 "What team has the most points in their group this season?"]

# Create the input field and submit button
input_prompt = st.selectbox("Select a suggested prompt or enter your own:", suggested_prompts, index=0)
user_prompt = st.text_input("Enter your own prompt:", "")

# Use the user's prompt if entered, otherwise use the selected suggested prompt
prompt = user_prompt if user_prompt else input_prompt

if st.button("Generate"):
    # Make the completion request
    completion = openai.Completion.create(model=model_name, prompt=prompt)

    # Get the completion text from the first choice in the choices list
    text = completion.choices[0]["text"]

    # Display the completion in the result text area
    st.text_area("Completion:", value=text, height=400, max_chars=None, key=None)

