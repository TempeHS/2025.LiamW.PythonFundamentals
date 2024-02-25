fruit = input("Fruit: ")
fruit = fruit.strip().lower()
Fruits = {
    "lemon": "15",
    "lime": "20",
    "avocado": "50",
    "cantaloupe": "50",
    "honeydew melon": "50",
    "pineapple": "50",
    "strawberries": "50",
    "tangerine": "50",
    "grapefruit": "60",
    "nectarine": "60",
    "peach": "60",
    "plum": "70",
    "orange": "80",
    "watermelon": "80",
    "grapes": "90",
    "kiwifruit": "90",
    "pear": "100",
    "sweet cherries": "100",
    "banana": "110",
    "apple": "130",
}
if fruit in Fruits:
    print(f"Calories: {Fruits[fruit]}")
