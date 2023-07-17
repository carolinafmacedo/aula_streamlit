import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import numpy as np
import pkg_resources
pkg_resources.require("statsmodels==0.12.2")
import statsmodels.api as sm

# Titulo do app
st.title('StockApp')

st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# baixando dados do yahoo
data = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))
fig.update_layout(title=f"{ticker_symbol}", xaxis_title='Data', yaxis_title='Preço')
st.plotly_chart(fig)

st.sidebar.title('Selecione o stock - Grafico 2')
ticker_symbol2 = st.sidebar.text_input('stock', 'MSFT', max_chars=10)

# baixando dados do yahoo
data2 = yf.download(ticker_symbol2, start='2020-01-01', end='2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data2)

# Exibir o gráfico
fig_close2 = go.Figure()
fig_close2.add_trace(go.Scatter(x=data2.index, y=data2['Close'], name='Fechamento'))
fig_close2.update_layout(title=f"{ticker_symbol2}", xaxis_title='Data', yaxis_title='Preço')
st.plotly_chart(fig_close2)

# CALCULAR IRF

returns2 = np.log(data2['Close']).diff().dropna()
model2 = sm.tsa.VAR(returns2)
results2 = model2.fit(maxlags=10, ic='aic')
irf2 = results2.irf(10)

# Exibir Grafico
fig_irf2 = go.Figure()
for i in range(len(returns2.columns)):
    fig_irf2.add_trace(go.Scatter(x=irf2.irfperiods, y=irf2.irfs[:, i, i], name=returns2.columns[i]))
    fig_irf2.update_layout(title='Impulse Response Function - Grafico 2', xaxis_title='Periodo', yaxis_title='IRF')
    st.plotly_chart(fig_irf2)
