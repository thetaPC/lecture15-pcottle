import random
# Alright lets make a pizza!


from __future__ import print_function

import random
def getCheese():
    return 'A bit of Mozzarella cheese'

def getSauce():
    return 'some basic Marinara sauce'
    
def getMushroom():
    return 'A lot of mushrooms'
    
def getPepperoni():
    return '%d pepperoni slices' % random.randrange(1, 3)

def getPepperoni():
    return '%d pepperoni slices' % random.randrange(3, 400)

def getIngredients():
    return [
        getMushroom(),
        getPepperoni(),
        getCheese(),
        getSauce(),
        getPepperoni()
    ]

def printPizza():
    ingredients = getIngredients()
    print("Here is our pizza! It has %d ingredient(s)" % (len(ingredients)))
    print("\n".join(
        [str(num + 1) + ': ' + i for (num, i) in enumerate(ingredients)]
    ))

print('''
 ____  __  ____  ____   __     ____  __  _  _  ____
(  _ \(  )(__  )(__  ) / _\   (_  _)(  )( \/ )(  __)
 ) __/ )(  / _/  / _/ /    \    )(   )( / \/ \ ) _)
(__)  (__)(____)(____)\_/\_/   (__) (__)\_)(_/(____)
''')

printPizza()

print('''
 __  __           __
 \ \/ /_ ____ _  / /
  \  / // /  ' \/_/
  /_/\_,_/_/_/_(_)
''')
