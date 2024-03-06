farmMaterials = ['Acorn',
                 'Apple',
                 'Banana',
                 'Bean',
                 'Blueberry',
                 'Brocolli',
                 'Cabbage',
                 'Carrot',
                 'Cherry',
                 'Corn',
                 'Cotton',
                 'Garlic',
                 'Grape',
                 'Moonberry',
                 'Onion',
                 'Orange',
                 'Pea',
                 'Pepper',
                 'Potato',
                 'Pumpkin',
                 'Strawberry',
                 'Sunberry',
                 'Watermelon',
                 'Wheat']

farmStats = {'Acorn': {'Collet':3, 'Worst':6, 'Best':12},
             'Apple': {'Collet':3, 'Worst':3, 'Best':6},
             'Banana': {'Collet':3, 'Worst':6, 'Best':12},
             'Bean': {'Collet':1, 'Worst':9, 'Best':15},
             'Blueberry': {'Collet':1, 'Worst':9, 'Best':15},
             'Brocolli': {'Collet':1, 'Worst':3, 'Best':6},
             'Cabbage': {'Collet':1, 'Worst':2, 'Best':4},
             'Carrot': {'Collet':1, 'Worst':2, 'Best':4},
             'Cherry': {'Collet':3, 'Worst':6, 'Best':12},
             'Corn': {'Collet':3, 'Worst':6, 'Best':9},
             'Cotton': {'Collet':3, 'Worst':4, 'Best':8},
             'Garlic': {'Collet':1, 'Worst':6, 'Best':12},
             'Grape': {'Collet':1, 'Worst':2, 'Best':4},
             'Moonberry': {'Collet':1, 'Worst':3, 'Best':9},
             'Onion': {'Collet':1, 'Worst':3, 'Best':6},
             'Orange': {'Collet':3, 'Worst':3, 'Best':6},
             'Pea': {'Collet':1, 'Worst':9, 'Best':15},
             'Pepper': {'Collet':1, 'Worst':9, 'Best':15},
             'Potato': {'Collet':1, 'Worst':2, 'Best':4},
             'Pumpkin': {'Collet':1, 'Worst':2, 'Best':4},
             'Strawberry': {'Collet':1, 'Worst':6, 'Best':12},
             'Sunberry': {'Collet':1, 'Worst':3, 'Best':9},
             'Watermelon': {'Collet':1, 'Worst':2, 'Best':4},
             'Wheat': {'Collet':1, 'Worst':3, 'Best':9}}

numColsPriceTab = 5

def loadParams():
    return farmMaterials, farmStats, numColsPriceTab