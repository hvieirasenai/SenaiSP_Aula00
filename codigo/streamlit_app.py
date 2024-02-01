import openai
import streamlit as st

# Substitua "SUA_CHAVE_DE_API" pela sua chave de API OpenAI
openai.api_key = "SUA_CHAVE_DE_API"

def gera_resposta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Escolha o engine adequado para a sua aplicação
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chatbot Interativo com OpenAI e Streamlit")

    user_message = st.text_input("Você:")
    
    if st.button("Enviar"):
        chat_prompt = f"\nUsuário: {user_message}\nChatbot:"
        chatbot_response = gera_resposta(chat_prompt)
        st.text(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()
