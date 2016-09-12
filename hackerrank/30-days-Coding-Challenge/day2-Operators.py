'''by blondiebytes
Objective 
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
'''

import math
mealCost = float(input())
tipPercent=int(input())
taxPercent=int(input())
print("The total meal cost is",int(round(mealCost+(mealCost*(tipPercent/100))+(mealCost*(taxPercent/100)))),"dollars.")
