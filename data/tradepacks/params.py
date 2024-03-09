import numpy as np

tradepackMaterials = ['Acorn',
                   'Apple',
                   'Banana',
                   'Bean',
                   'Beef',
                   'Blueberry',
                #    'Brocolli',
                   'Cabbage',
                   'Carrot',
                   'Cheese',
                #    'Cherry',
                   'Chicken',
                   'Coal',
                   'Copper Ore',
                   'Corn',
                   'Cotton',
                   'Egg',
                   'Garlic',
                   'Grape',
                   'Ground Flour',
                   'Hide',
                   'Honey',
                   'Milk',
                   'Moonberry',
                   'Onion',
                   'Orange',
                   'Pea',
                   'Pepper',
                   'Potato',
                   'Pumpkin',
                   'Salt',
                   'Shank',
                   'Small Log',
                   'Stone',
                   'Strawberry',
                #    'Sunberry',
                   'Watermelon',
                   'Wheat',
                   'Wool']

tiles = {'Riverend - Margrove': 586,
         'Riverend - Orca Bay': 814,
         'Riverend - Seabreeze': 1528,
         'Riverend - Tarmire': 517,
         'Riverend - Darzuac': 535,
         'Riverend - Gilead': 1135,
         'Riverend - Glaceford': 881,
         'Riverend - Ravencrest': 414,
         'Riverend - Defiance': 361,
         'Margrove - Orca Bay': 437,
         'Margrove - Seabreeze': 943,
         'Margrove - Tarmire': 626,
         'Margrove - Darzuac': 810,
         'Margrove - Gilead': 979,
         'Margrove - Glaceford': 508,
         'Margrove - Ravencrest': 233,
         'Margrove - Defiance': 946,
         'Orca Bay - Seabreeze': 713,
         'Orca Bay - Tarmire': 298,
         'Orca Bay - Darzuac': 888,
         'Orca Bay - Gilead': 541,
         'Orca Bay - Glaceford': 945,
         'Orca Bay - Ravencrest': 402,
         'Orca Bay - Defiance': 1175,
         'Seabreeze - Tarmire': 1011,
         'Seabreeze - Darzuac': 1600,
         'Seabreeze - Gilead': 699,
         'Seabreeze - Glaceford': 787,
         'Seabreeze - Ravencrest': 1115,
         'Seabreeze - Defiance': 1888,
         'Tarmire - Darzuac': 589,
         'Tarmire - Gilead': 617,
         'Tarmire - Glaceford': 1133,
         'Tarmire - Ravencrest': 392,
         'Tarmire - Defiance': 877,
         'Darzuac - Gilead': 1207,
         'Darzuac - Glaceford': 1318,
         'Darzuac - Ravencrest': 577,
         'Darzuac - Defiance': 485,
         'Gilead - Glaceford': 1486,
         'Gilead - Ravencrest': 745,
         'Gilead - Defiance': 1495,
         'Glaceford - Ravencrest': 741,
         'Glaceford - Defiance': 1242,
         'Ravencrest - Defiance': 774,
         'Darzuac - Darzuac': 0,
         'Defiance - Defiance': 0,
         'Gilead - Gilead': 0,
         'Margrove - Margrove': 0,
         'Orca Bay - Orca Bay': 0,
         'Ravencrest - Ravencrest': 0,
         'Riverend - Riverend': 0,
         'Seabeeze - Seabeeze': 0,
         'Tarmire - Tarmire': 0}

cities = np.array(sorted(['Darzuac', 'Defiance', 'Gilead', 'Margrove', 'Orca Bay',
                          'Ravencrest', 'Riverend', 'Seabeeze', 'Tarmire']))

tradepacks = {'Aged Meat':{'Beef':12,'Salt':5,'Garlic':15},
              'Bakers Basics':{'Milk':15,'Egg':30,'Ground Flour':35},
              'Barbecue Specialty':{'Beef':10,'Chicken':5,'Coal':30,'Honey':6},
              'Basic Rations':{'Wheat':15,'Corn':10,'Apple':10},
            #   'Berry Basket':{'Strawberry':30,'Blueberry':50,'Moonberry':4,'Sunberry':8},
              'Brined Shank':{'Shank':10,'Salt':8,'Pepper':10},
              'Building Materials':{'Stone':100,'Small Log':22,'Hide':10},
              "Butcher's Box":{'Beef':5,'Chicken':8,'Shank':5,'Cheese':1},
              'Campfire Roast':{'Small Log':22,'Stone':130,'Chicken':8},
              'Crafting Basics':{'Copper Ore':40,'Hide':10,'Small Log':25},
            #   'Crips Produce':{'Apple':10,'Brocolli':5,'Pea':10,'Bean':5},
              'Dairy Delivery':{'Milk':15,'Cheese':1,'Egg':30},
            #   'Exotic Fruits':{'Watermelon':4,'Sunberry':8,'Moonberry':5},
              'Fried Chicken':{'Chicken':12,'Onion':10,'Garlic':10,'Ground Flour':20},
              'Fruit Basket':{'Grape':20,'Watermelon':2,'Cherry':5},
              'General Spices':{'Garlic':15,'Onion':15,'Pepper':10,'Salt':5},
              'Glaceforde Explorers Kit':{'Wool':10,'Small Log':30,'Coal':40},
              'Juicers Box':{'Apple':5,'Strawberry':15,'Cherry':5,'Banana':3},
              "Kabbar's Omelets":{'Egg':30,'Cheese':1,'Pepper':15},
              'Kindling Kit':{'Small Log':38,'Coal':40,'Cotton':10},
              'Margrove Ale Ingredients':{'Wheat':30,'Acorn':3,'Pumpkin':2},
              'Noble Delicacies':{'Moonberry':10,'Acorn':2,'Pepper':12},
              'Pickled Vegetables':{'Cabbage':15,'Carrot':50,'Salt':8},
            #   'Pie Making Kit':{'Apple':5,'Sunberry':5,'Cherry':4,'Ground Flour':30},
              'Ravencrest Finest Wears':{'Cotton':8,'Wool':8,'Hide':8},
            #   'Ravencrest Greens':{'Brocolli':10,'Pea':25,'Cabbage':15},
              'Rohna Smoked Ham':{'Shank':5,'Acorn':2,'Pea':10,'Salt':5},
              "Sailor's Remedy":{'Carrot':20,'Orange':5,'Bean':20},
              'Sajecho Fruit Basket':{'Banana':2,'Watermelon':1,'Orange':4,'Grape':10},
              "Sajecho's Spices":{'Onion':15,'Orange':4,'Salt':5},
              'Seabreeze Rum':{'Corn':10,'Cabbage':8,'Banana':5,'Blueberry':30},
              "Settler's Rations":{'Wheat':30,'Carrot':35,'Corn':10},
              'Slums Provisions':{'Cotton':10,'Shank':8,'Potato':80},
              "Sombreshade's Pie":{'Pumpkin':5,'Milk':10,'Ground Flour':20,'Honey':13},
              'Strawberry Cakes':{'Honey':10,'Ground Flour':50,'Strawberry':40,'Milk':10},
            #   'Vegetable Stew':{'Brocolli':5,'Pumpkin':5,'Bean':25,'Potato':40},
              'Winemakers Kit':{'Grape':40,'Blueberry':15,'Moonberry':5}}
tradepacks = dict(sorted(tradepacks.items()))
tradepackBaseValue = 10000

numColsPriceTab = 5
numColsDemandTab = 4

def loadParams():
    return tradepackMaterials, tiles, cities, tradepacks, tradepackBaseValue, numColsPriceTab, numColsDemandTab