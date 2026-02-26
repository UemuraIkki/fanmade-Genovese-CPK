import numpy as np

def basil_sauce(NoP):
    """
    This function calculates the amount of basil sauce needed for a given number of people (NoP).
    """
    ingredients = {
        "basil_leaves": 5,
        "pine_nuts": 1.25,
        "parmesan_cheese": 1.25,
        "garlic": 0.5,
        "olive_oil": 12.5,
        "salt": 0.1, 
        "black_pepper": 0.1
    }
    for key in ingredients:
        ingredients[key] *= NoP
    return ingredients

def main():
    NoP = int(input("Enter the number of people(calculating 100g of pasta for each): "))
    sauce = basil_sauce(NoP)
    for ingredient, amount in sauce.items():
        if ingredient in ["basil_leaves", "garlic"]:
            print(f"{ingredient}: {amount} 個")
        print(f"{ingredient}: {amount}g")

if __name__ == "__main__":
    main()