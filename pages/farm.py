# %% Imports
import numpy as np
import streamlit as st
from itertools import cycle
import pandas as pd
from io import BytesIO
import json
#%%
# # %% Params
import data.farm.params as fp
farmMaterials, farmStats, numColsPriceTab = fp.loadParams()

# # %% Inputs (setting default)
import data.farm.inputs as fi
farmQuantities = fi.loadInputs()

if 'materialPrices' not in st.session_state:
    import data.inputs as di
    materialsPrices = di.loadInputs()
    st.session_state['materialPrices'] = materialsPrices
else:
    materialsPrices = st.session_state['materialPrices']

# %% Functions
def computeTotalCost(farmStats, farmQuantities):
    for mat in farmStats:
        farmStats = {**farmStats, mat:{**farmStats[mat], 'totalCost':farmStats[mat]['cost']*farmQuantities[mat]}}
    return farmStats

def computeProfit(farmStats, materialsPrices, farmQuantities):
    productsProfits = {}
    for mat in farmStats:
        productsProfits = {**productsProfits, mat:{'profitWorst':(farmStats[mat]['worst']*materialsPrices[mat]*farmQuantities[mat]- farmStats[mat]['totalCost']),
                                                  'profitBest':(farmStats[mat]['best']*materialsPrices[mat]*farmQuantities[mat] - farmStats[mat]['totalCost'])}}
    return productsProfits

def splitOutput(farmStats, productsProfits):
    materialCollect = {mat:farmStats[mat]['collect'] for mat in farmStats}
    materialWorst = {mat:farmStats[mat]['worst'] for mat in farmStats}
    materialBest = {mat:farmStats[mat]['best'] for mat in farmStats}
    materialCost = {mat:farmStats[mat]['cost'] for mat in farmStats}
    materialTotalCost = {mat:farmStats[mat]['totalCost'] for mat in farmStats}
    materialProfitWorst = {mat:productsProfits[mat]['profitWorst'] for mat in farmStats}
    materialProfitBest = {mat:productsProfits[mat]['profitBest'] for mat in farmStats}
    return materialCollect, materialWorst, materialBest, materialCost, materialTotalCost, materialProfitWorst, materialProfitBest

def createDataFrame(farmStats, materialsPrices, farmQuantities):
    farmStats = computeTotalCost(farmStats=farmStats, farmQuantities=farmQuantities)
    productsProfits = computeProfit(farmStats, materialsPrices, farmQuantities)
    materialCollect, materialWorst, materialBest, materialCost, materialTotalCost, materialProfitWorst, materialProfitBest = splitOutput(farmStats, productsProfits)
    df = pd.DataFrame({#'Coletas (x vezes)': materialCollect,
                    #   'Pior cenário': materialWorst,
                    #   'Melhor cenário': materialBest,
                    #   'Custo de plantação': materialCost,
                      'Quantidade': farmQuantities,
                      'Custo Total': materialTotalCost,
                      'Lucro Pior Cenário':materialProfitWorst,
                      'Lucro Melhor Cenário':materialProfitBest})
    return df
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
st.write('em breve...')
df = createDataFrame(farmStats, materialsPrices, farmQuantities)
st.data_editor(df)