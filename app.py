import pickle
import streamlit as st

# Carregando o modelo treinado
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache_data()

# Definindo a função que fará a previsão usando os dados que o usuário insere
def prediction(age, education, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose):
    prediction = classifier.predict([[age, education, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    if prediction == 1:
        pred = 'Terá problema cardíaco'
    else:
        pred = 'Não terá problema cardíaco'

    return pred

# Esta é a função principal na qual definimos nossa página da web
def main():
    # Elementos de front-end da página da web
    html_temp = """
    <div style = background-color: yellow; padding: 13px>
    <h1 style = color: black; text-align: center>Predição de Problema Cardíaco</h1>
    </div>"""

    # Exibir o front-end
    st.markdown(html_temp, unsafe_allow_html=True)

    # As linhas a seguir criam caixas nas quais o usuário pode inserir os dados necessários para fazer previsões
    age = st.number_input('Idade',
                         min_value=0,
                         max_value=100,
                         value=32,
                         help="Informe sua idade")
    education = st.number_input('Nível de educação',
                              min_value=1,
                              max_value=4,
                              value=4,
                              help="""
                              1 - Sem ensino fundamental
                              2 - Ensino fundamental completo
                              3 - Ensino médio completo
                              4 - Ensino superior completo
                              """)
    cigsPerDay = st.number_input('Cigarros por dia',
                              min_value=0,
                              max_value=100,
                              value=0,
                              help="Digite um valor de 0 a 100")
    totChol = st.number_input('Nível de colesterol total (mg/dL)',
                         min_value=0,
                         max_value=1000,
                         value=234,
                         help="Digite um valor de 0 a 1000")
    sysBP = st.number_input('Pressão Arterial Sistólica (mmHg)',
                           min_value=0,
                           max_value=500,
                           value=128,
                           help="Digite um valor de 0 a 500")
    diaBP = st.number_input('Pressão Sanguínea Diastólica (mmHg)',
                           min_value=0,
                           max_value=300,
                           value=82,
                           help="Digite um valor de 0 a 300")
    BMI = st.number_input('IMC',
                           min_value=0,
                           max_value=100,
                           value=25,
                           help="Digite um valor de 0 a 100")
    heartRate = st.number_input('Frequência Cardíaca (bpm)',
                           min_value=0,
                           max_value=300,
                           value=75,
                           help="Digite um valor de 0 a 300")
    glucose = st.number_input('Nível de Glicose (mg/dl)',
                           min_value=0,
                           max_value=600,
                           value=78,
                           help="Digite um valor de 0 a 600")
    
    # Quando 'Prever' for clicado, faça a previsão e armazene-a
    if st.button('Prever'):
        result = prediction(age, education, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose)
        st.success(result)
    
if __name__ == '__main__':
    main()
