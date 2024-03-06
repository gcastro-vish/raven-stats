# %% Imports
import numpy as np
import streamlit as st
from itertools import cycle
import pandas as pd
from io import BytesIO
import json

# %% Page Header
st.set_page_config(layout='wide')
st.markdown("""
<style>
.small-font {
    font-size:15px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('# RavenStats <p class="small-font">(Feito por Vish. Ravendawn nick (Angerhorn): Vish Tankao)</p>', unsafe_allow_html=True)

cols = st.columns(4)

with cols[0]:
    if st.button("Home :house:"):
        st.switch_page("app.py")
with cols[1]:
    if st.button("Tradepacks :package:"):
        st.switch_page("pages/tradepack.py")
with cols[2]:
    if st.button("Fazenda :female-farmer:"):
        st.switch_page("pages/farm.py")
with cols[3]:
    if st.button("Crafting :hammer_and_wrench:"):
        st.switch_page("pages/crafting.py")

# %% Page Body
st.markdown('''
            * **Home**: Página inicial
            * **Tradepacks**: Calculadora de tradepacks: custos, lucros e valor de venda
            * **Fazenda**: Calculadora de farm: custos, lucros e maior xp
            * **Crafting**: Calculadora de crafting: custos, lucros e maior xp
            ''')