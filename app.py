import pickle
import streamlit as st

# Carregando o modelo treinado
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache_data()

# Definindo a função que fará a previsão usando os dados que o usuário insere
def prediction(cp, thalach, oldpeak, ca, thal):
    prediction = classifier.predict([[cp, thalach, oldpeak, ca, thal]])

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
    cp = st.number_input('Tipo de dor no peito',
                         min_value=0,
                         max_value=3,
                         value=0,
                         help="""
                         0 - angina típica\n
                         1 - angina atípica\n
                         2 - não anginoso\n
                         3 - assintomático""")
    thalach = st.number_input('Frequência cardíaca máxima alcançada',
                              min_value=50,
                              max_value=250,
                              value=50)
    oldpeak = st.number_input('Depressão de ST induzida por exercício em relação ao repouso',
                              min_value=0.0,
                              max_value=10.0,
                              value=0.0)
    ca = st.number_input('Número de vasos principais coloridos por fluoroscopia',
                         min_value=0,
                         max_value=4,
                         value=0)
    thal = st.number_input('Talassemia',
                           min_value=0,
                           max_value=3,
                           value=0,
                           help="""
                           0-1 = normal\n
                           2 = defeito corrigido\n
                           3 = defeito reversível""")
    
    # Quando 'Prever' for clicado, faça a previsão e armazene-a
    if st.button('Prever'):
        result = prediction(cp, thalach, oldpeak, ca, thal)
        st.success(result)
    
if __name__ == '__main__':
    main()
