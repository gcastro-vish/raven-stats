# %% Imports
import numpy as np
import streamlit as st
from itertools import cycle
import pandas as pd
from io import BytesIO
import json

# %% Params
tiles = {'Seabeeze - Orca Bay': 713,
         'Seabreeze - Margrove': 943,
         'Seabreeze - Tarmire': 1011,
         'Seabreeze - Ravencrest': 1115,
         'Seabreeze - Riverend': 1528,
         'Seabreeze - Darzuac': 1687,
         'Seabreeze - Defiance': 1888,
         'Ravencrest - Margrove': 233,
         'Ravencrest - Tarmire': 392,
         'Ravencrest - Orca Bay': 402,
         'Ravencrest - Riverend': 412,
         'Ravencrest - Darzuac': 577,
         'Ravencrest - Defiance': 773,
         'Margrove - Orca Bay': 437,
         'Margrove - Riverend': 584,
         'Margrove - Tarmire': 626,
         'Margrove - Darzuac': 811,
         'Margrove - Defiance': 945,
         'Gilead - Riverend': 1133,
         'Gilead - Margrove': 978,
         'Gilead - Orca Bay': 542,
         'Gilead - Seabreeze': 699,
         'Gilead - Tarmire': 617,
         'Gilead - Darzuac': 1207,
         'Gilead - Ravencrest': 745,
         'Gilead - Defiance': 1494,
         'Orca Bay - Riverend': 814,
         'Orca Bay - Tarmire': 298,
         'Orca Bay - Darzuac': 888,
         'Orca Bay - Defiance': 1175}

tradepacks = {'Glaceforde Explorers Kit': {'Wool':10,'Small Log':30,'Coal':40},
              'Campfire Roast': {'Small Log':22,'Stone':130,'Chicken':8},
              'Bakers Basics': {'Milk':15,'Egg':30,'Ground Flour':35},
              'Building Materials':{'Stone':100,'Small Log':22,'Hide':10},
              'Basic Rations':{'Wheat':15,'Corn':10,'Apple':10},
              'Crafting Basics':{'Copper Ore':40,'Hide':10,'Small Log':25},
              'Settler\'s Rations':{'Wheat':30,'Carrot':35,'Corn':10},
              'Slums Provisions':{'Cotton':10,'Shank':8,'Potato':80},
              'Ravencrest Finest Wears':{'Cotton':8,'Wool':8,'Hide':8},
              'Kindling Kit':{'Small Log':38,'Coal':40,'Cotton':10},
              'Barbecue Specialty':{'Beef':10,'Chicken':5,'Coal':30,'Honey':6},
              'Pickled Vegetables':{'Cabbage':15,'Carrot':50,'Salt':8},
              'Dairy Delivery':{'Milk':15,'Cheese':1,'Egg':30},
              'Butcher\'s Box':{'Beef':5,'Chicken':8,'Shank':5,'Cheese':1},
              'Strawberry Cakes':{'Honey':10,'Ground Flour':50,'Strawberry':40,'Milk':10},
              'Sajecho\'s Spices':{'Onion':15,'Orange':4,'Salt':5},
              'Kabbar\'s Omelets':{'Egg':30,'Cheese':1,'Pepper':15},
              'Brined Shank':{'Shank':10,'Salt':8,'Pepper':10},
              'Sailor\'s Remedy':{'Carrot':20,'Orange':5,'Bean':20},
              'Seabreeze Rum':{'Corn':10,'Cabbage':8,'Banana':5,'Blueberry':30},
              'Sombreshade\'s Pie':{'Pumpkin':5,'Milk':10,'Ground Flour':20,'Honey':13},
              'Sajecho Fruit Basket':{'Banana':2,'Watermelon':1,'Orange':4,'Grape':10}
             }

tradepackBaseValue = 9600

numColsPriceTab = 5
numColsDemandTab = 4

# %% Inputs (setting default)
materialsPrices = {'Apple': 510,
                   'Banana': 1000,
                   'Bean': 215,
                   'Beef': 20,
                   'Blueberry': 125,
                   'Cabbage': 320,
                   'Carrot': 150,
                   'Cheese': 2200,
                   'Chicken': 320,
                   'Coal': 205,
                   'Copper Ore': 65,
                   'Corn': 220,
                   'Cotton': 320,
                   'Egg': 315,
                   'Grape': 280,
                   'Ground Flour': 95,
                   'Hide': 500,
                   'Honey': 200,
                   'Milk': 350,
                   'Onion': 300,
                   'Orange': 1400,
                   'Pepper': 310,
                   'Potato': 150,
                   'Pumpkin': 1738,
                   'Salt': 180,
                   'Shank': 20,
                   'Small Log': 160,
                   'Stone': 50,
                   'Strawberry': 130,
                   'Watermelon': 3800,
                   'Wheat': 190,
                   'Wool': 600}

demandsPerCent = {'Aged Meat':126,
'Bakers Basics':126,
'Barbecue Specialty':85,
'Basic Rations':76,
'Brined Shank':50,
'Building Materials':127,
'Butcher\'s Box':51,
'Campfire Roast':114,
'Crafting Basics':112,
'Dairy Delivery':125,
'Fried Chicken':100,
'Glaceforde Explorers Kit':126,
'Kabbar\'s Omelets':124,
'Kindling Kit':134,
'Margrove Ale Ingredients':100,
'Pickled Vegetables':120,
'Ravencrest Finest Wears':128,
'Rohna Smoked Ham':100,
'Sailor\'s Remedy':121,
'Sajecho Fruit Basket':121,
'Sajecho\'s Spices':81,
'Seabreeze Rum':125,
'Settler\'s Rations':96,
'Slums Provisions':91,
'Sombreshade\'s Pie':133,
'Strawberry Cakes':126,
'Winemakers Kit':100}

bonusPerCent = 0
route = 'Seabreeze - Ravencrest'
demands = {k:v/100 for k,v in demandsPerCent.items()}
bonusesPerCentChoices = [0,5,20,25,40,45]

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
    tradepack formula: (tradepackBaseValue + 8*tiles)*demand*(1+bonus)
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
                tradepackSellPrices = {**tradepackSellPrices, t:int(round((tradepackBaseValue + tiles[route]*8)*demands[t]*(1+bonus),2))}
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

# %% app
st.set_page_config(layout='wide')
st.title('Calculadora de Tradepacks')
st.write('Atualize os preços e as demandas em suas respectivas abas')
st.write('A fórmula utilizada nos calculos é')
st.write('$ValorDeVenda = (ValorBase + 8*Distância)*Demanda*(1+Bônus)$')
st.write(f'Atualmente o valor base é :red[{tradepackBaseValue}]')

bufferTradepacks = BytesIO()
with pd.ExcelWriter(bufferTradepacks, engine='xlsxwriter') as writer:
    pd.DataFrame({'materiais':tradepacks}).to_excel(writer, sheet_name='Demandas')
    

with st.sidebar:
    route = st.selectbox(label='Rota para fazer a entrega',
                            options=sorted(list(tiles.keys())))
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
# %%
