import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Titulo do app
st.title('StockApp')

st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# baixando dados do yahoo
data = yf.download(ticker_symbol, start = '2020-01-01', end = '2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data['Close'], name = 'Fechamento'))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig)

st.sidebar.title('Selecione o stock - Grafico 2')
ticker_symbol2 = st.sidebar.text_input('stock', 'MSFT', max_chars=10)

# baixando dados do yahoo
data2 = yf.download(ticker_symbol2, start = '2020-01-01', end = '2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico
fig_close2 = go.Figure()
fig_close2.add_trace(go.Scatter(x = data2.index, y = data2['Close'], name = 'Fechamento'))
fig_close2.update_layout(title = f"{ticker_symbol2}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig_close2)
