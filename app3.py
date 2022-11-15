import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import requests
import json
from PIL import Image

image = Image.open('Streamlit/logo.png')

st.image(image, width=480)
st.title('CURRENCY CONVERTER APP')
st.markdown("""
this app converts one currency into other
""")

st.sidebar.header("Input Options:-")

currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
demo = st.sidebar.slider("slide this", 1.0, 5.0, 2.2)
base_price = st.sidebar.selectbox('select currency', currency_list)
symbol_price = st.sidebar.selectbox("select target currency", currency_list)

@st.cache
def load_data():
    url = ''.join(['https://api.rateapi.io/api/latest?base=',base_price, '&symbols=',symbol_price])
    response = requests.get(url)
    data = response.json()
    base_currency = pd.Series(data['base'], name='base_currency')
    rates_df = pd.DataFrame.from_dict(data['rates'].items())
    rates_df.columns = ['converted_currency', 'price']
    conversion_data = pd.Series(data['data'], name='data')
    df = pd.concat([base_currency, rates_df, conversion_data], axis=1)
    return df

df = load_data()
st.header('Currency converter')
st.write(df)



