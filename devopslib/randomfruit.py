from random import choices


def fruit():
    fruits = ["apple", "mango", "banana"]
    return choices(fruits)[0]


def meal(beverage):
    my_fruit = fruit()
    print(f"Your fruit is {my_fruit} and your beverage is {beverage}")
    if my_fruit == "cherry":
        complete_meal = f"your meal is {my_fruit} and {beverage}"
        return complete_meal
    alternate_meal = f"your meal is steak and {beverage}"
    return alternate_meal
