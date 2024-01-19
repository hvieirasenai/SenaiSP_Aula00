import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Um SIMPLES Exibidor de arquivos!!!

## Suba um arquivo e vejamos o que acontece :smile::heart:
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'wav', 'mp3', 'csv', 'json','mp4', 'mpeg']
)

if arquivo is not None:
    tipo_arquivo = arquivo.type.split('/')
    if tipo_arquivo == ['application', 'json']:
        st.json(loads(arquivo.read()))
    elif tipo_arquivo[0] == 'image':
        st.image(arquivo)
    elif tipo_arquivo == ['text', 'csv']:
        df = read_csv(arquivo).transpose()
        st.dataframe(df)
        st.bar_chart(df)
    elif tipo_arquivo == ['text', 'x-python']:
        st.code(arquivo.read().decode())
    elif tipo_arquivo[0] == 'audio':
        st.audio(arquivo)
    elif tipo_arquivo[0] == 'video':
        st.video(arquivo)
else:
    st.error('Ainda não tenho arquivo!')
