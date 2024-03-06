# %% Imports
import numpy as np
import streamlit as st
from itertools import cycle
import pandas as pd
from io import BytesIO
import json

# %% Params
import data.tradepacks.params as tp
tiles, cities, tradepacks, tradepackBaseValue, numColsPriceTab, numColsDemandTab = tp.loadParams()

# %% Inputs (setting default)
import data.tradepacks.inputs as ti
materialsPrices, demandsPerCent, bonusPerCent, route, demands, bonusesPerCentChoices = ti.loadInputs()

# %% Classes (error treatment)
class missingMaterialPrice(Exception):
    def __init__(self, e):
        self.value = f"Material '{e.args[0]}' nao encontrado. Faça upload do arquivo de preços com este material e seu valor."

    def __str__(self):
        return repr(self.value)

class incorrectMaterialPriceType(Exception):
    def __init__(self, mats):
        self.value = f"O preço de {mats} precisa ser um número. Faça upload do arquivo de preços com seu valor corrigido."

    def __str__(self):
        return repr(self.value)
    
class missingTradepackDemand(Exception):
    def __init__(self, trpck):
        self.value = f"Tradepack '{trpck}' não está na lista de demandas. Faça uploado do arquivo de demandas adicionando este tradepack e sua demanda (%)."

    def __str__(self):
        return repr(self.value)
    
# %% Functions
def loadExamples(keyError = False, nanPrice = False, nonePrice = False):
    mp = {'Coal': 205,
          'Cotton': 320,
          'Small Log': 160,
          'Wool': 600}
    
    tp = {'Glaceforde Explorers Kit': {'Wool':10,'Small Log':30,'Coal':40},
          'Kindling Kit':{'Small Log':38,'Coal':40,'Cotton':10}}

    if keyError:
        tp = {**tp, 'Ravencrest Finest Wears':{'Cotton':8,'Wool':8,'Hide':8},}

    if nanPrice:
        mp['Cotton'] = np.nan
    
    if nonePrice:
        mp['Wool'] = None
    
    return mp, tp

def computeTradepackCosts(tradepacks=tradepacks, materialsPrices=materialsPrices):
    tradepacksCosts = {}
    for t in list(tradepacks.keys()):
        try:
            tradepacksCosts = {**tradepacksCosts, t:sum([materialsPrices[k]*v for k,v in tradepacks[t].items()])}
            assert sum(np.isnan(list(tradepacksCosts.values())))==0, f"there is a material in {[k for k in tradepacks[t].keys()]} with {np.nan} as price"
        except KeyError as e:
            raise missingMaterialPrice(e)
        except TypeError as e:
            raise incorrectMaterialPriceType([k for k in tradepacks[t].keys()])
    return tradepacksCosts

def computeTradepackSellPrices(route, bonus, tradepacks=tradepacks, __formula_alternativa__ = False):
    '''
    tradepack formula: (tradepackBaseValue + 6*tiles)*demand*(1+bonus)
    '''
    tradepackSellPrices = {}
    if __formula_alternativa__:
        for t in list(tradepacks.keys()):
            try:
                tradepackSellPrices = {**tradepackSellPrices, t:int(round((12000 + tiles[route]*8)*demands[t]*(1+bonus)*0.8,2))}
            except KeyError as e:
                raise missingTradepackDemand(t)
    else:
        for t in list(tradepacks.keys()):
            try:
                tradepackSellPrices = {**tradepackSellPrices, t:int(round((tradepackBaseValue + tiles[route]*6)*demands[t]*(1+bonus),2))}
            except KeyError as e:
                raise missingTradepackDemand(t)
    return tradepackSellPrices

def createDataFrame(route, bonus, tradepacks=tradepacks,materialsPrices=materialsPrices,__formula_alternativa__ = False):
    tradepackCosts = computeTradepackCosts(tradepacks=tradepacks, materialsPrices=materialsPrices)
    tradepackSellPrices = computeTradepackSellPrices(route=route, bonus=bonus, tradepacks=tradepacks,__formula_alternativa__=__formula_alternativa__)
    tradepackProfits = {}
    for t in list(tradepackCosts.keys()):
        tradepackProfits = {**tradepackProfits, t:(tradepackSellPrices[t]-tradepackCosts[t])}
    df = pd.DataFrame({'Custo':tradepackCosts,
                       'Valor de Venda':tradepackSellPrices,
                       'Lucro':tradepackProfits})
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
st.markdown('# Calculadora de Tradepacks')
st.write('Atualize os preços e as demandas em suas respectivas abas. Manual para salvar os dados [aqui](https://github.com/gcastro-vish/tradepack-calculator/tree/main?tab=readme-ov-file#como-salvar-os-dados) e manual para inclusão de dados [aqui](https://github.com/gcastro-vish/tradepack-calculator/tree/main?tab=readme-ov-file#como-incluir-novos-dados)')
st.write('A fórmula utilizada nos calculos é')
st.write('$ValorDeVenda = (ValorBase + 6*Distância)*Demanda*(1+Bônus)$')
st.write(f'Atualmente o valor base é :red[{tradepackBaseValue}]')

bufferTradepacks = BytesIO()
with pd.ExcelWriter(bufferTradepacks, engine='xlsxwriter') as writer:
    pd.DataFrame({'materiais':tradepacks}).to_excel(writer, sheet_name='Demandas')    

with st.sidebar:
    cityCraft = st.selectbox(label='Cidade de craft do tradepack',
                             options=cities)
    citySell = st.selectbox(label = 'Cidade de venda do tradepack',
                            options = cities[~np.where(cities==cityCraft, True, False)])
    bonusPerCent = st.selectbox(label='Bonus Tradepack (%)',options=bonusesPerCentChoices)
    uploadedTradepacks = st.file_uploader(':arrow_up_small: Upload Tradepacks',
                                            type='xlsx')
    uploadedMaterialPrices = st.file_uploader(':arrow_up_small: Upload Preços',
                                            type='xlsx')
    uploadedDemandsPerCent = st.file_uploader(':arrow_up_small: Upload Demandas',
                                            type='xlsx')
    st.download_button(':small_red_triangle_down: Download Tradepacks',
                    bufferTradepacks,
                    file_name='tradepacks.xlsx',
                    mime='application/vnd.ms-excel')

tabs = st.tabs(['Lucros', 'Preços', 'Demandas'])

with tabs[1]:
    if uploadedMaterialPrices is not None:
        dfaux = pd.read_excel(uploadedMaterialPrices,index_col=0)
        materialsPrices = dfaux.to_dict()['valor']
    cols = st.columns(numColsPriceTab)
    for mat, col in zip(list(materialsPrices.keys()),cycle(np.arange(0,numColsPriceTab))):
        materialsPrices = {**materialsPrices, mat:cols[col].number_input(label=mat,min_value=20,value=materialsPrices[mat])}
    bufferMaterialPrices = BytesIO()
    with pd.ExcelWriter(bufferMaterialPrices, engine='xlsxwriter') as writer:
        pd.DataFrame({'valor':materialsPrices}).to_excel(writer, sheet_name='Preços')
        
    with st.sidebar:
        st.download_button(':small_red_triangle_down: Download Preços',
                        bufferMaterialPrices,
                        file_name='precos.xlsx',
                        mime='application/vnd.ms-excel')

with tabs[2]:
    if uploadedDemandsPerCent is not None:
        dfaux = pd.read_excel(uploadedDemandsPerCent,index_col=0)
        demandsPerCent = dfaux.to_dict()['demanda']
    cols = st.columns(numColsDemandTab)
    for dem, col in zip(list(demandsPerCent.keys()),cycle(np.arange(0,numColsDemandTab))):
        demandsPerCent = {**demandsPerCent, dem:cols[col].number_input(label=dem,min_value=0,value=demandsPerCent[dem])}
    demands = {k:v/100 for k,v in demandsPerCent.items()}
    bufferDemandsPerCent = BytesIO()
    with pd.ExcelWriter(bufferDemandsPerCent, engine='xlsxwriter') as writer:
        pd.DataFrame({'demanda':demandsPerCent}).to_excel(writer, sheet_name='Demandas')
        
    with st.sidebar:
        st.download_button(':small_red_triangle_down: Download Demandas',
                        bufferDemandsPerCent,
                        file_name='demandas.xlsx',
                        mime='application/vnd.ms-excel')

with tabs[0]:
    if uploadedTradepacks is not None:
        dfaux = pd.read_excel(uploadedTradepacks,index_col=0)
        dfaux_ = dfaux.to_dict()['materiais']
        tradepacks = {k:json.loads(v.replace("'",'"')) for k,v in dfaux_.items()}
    bonus = bonusPerCent/100
    route = [x for x in list(tiles.keys()) if cityCraft in x and citySell in x][0]
    df = createDataFrame(route=route, bonus=bonus, tradepacks=tradepacks, materialsPrices=materialsPrices)
    st.data_editor(df,
                    column_config={
                        'Custo':st.column_config.ProgressColumn(
                            'Custo',
                            help = 'Silver total para montar o tradepack',
                            format = '$%d',
                            min_value = int(df['Custo'].min()),
                            max_value = int(df['Custo'].max()),
                       ),
                        'Valor de Venda':st.column_config.ProgressColumn(
                            'Valor de Venda',
                            help = 'Calculado utilizando fórmula acima',
                            format = '$%d',
                            min_value = int(df['Valor de Venda'].min()),
                            max_value = int(df['Valor de Venda'].max()),
                       ),
                        'Lucro':st.column_config.ProgressColumn(
                            'Lucro',
                            help = 'Valor de Venda - Custo',
                            format = '$%d',
                            min_value = int(df['Lucro'].min()),
                            max_value = int(df['Lucro'].max()),
                       ),
                    },
                    use_container_width=True
                   )