import random
from collections import defaultdict

import matplotlib.pyplot as plt


class Attribute:
    def __init__(self, name, min_roll, max_roll):
        self.name = name
        self.min_roll = min_roll
        self.max_roll = max_roll

    def roll(self):
        return random.randint(self.min_roll, self.max_roll)


class Ingredient:
    def __init__(self, multiplier):
        self.multiplier = multiplier
        self.attributes = []

    def add_attribute(self, name, min_roll, max_roll):
        self.attributes.append(Attribute(name, min_roll, max_roll))

    def roll_attributes(self):
        rolled_values = {}
        for attribute in self.attributes:
            rolled_value = round(attribute.roll() * self.multiplier)
            if attribute.name in rolled_values:
                rolled_values[attribute.name] += rolled_value
            else:
                rolled_values[attribute.name] = rolled_value
        return rolled_values


class Item:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if len(self.ingredients) < 6:
            self.ingredients.append(ingredient)
        else:
            print("Maximum of 6 ingredients reached")

    def roll_item(self):
        final_attributes = defaultdict(int)
        for ingredient in self.ingredients:
            rolled_values = ingredient.roll_attributes()
            for name, value in rolled_values.items():
                final_attributes[name] += value
        return final_attributes


def get_user_input():
    item = Item()
    num_ingredients = int(input("Enter the number of ingredients (up to 6): "))

    for i in range(num_ingredients):
        multiplier = float(input(f"Enter multiplier for ingredient {i+1}: "))
        ingredient = Ingredient(multiplier)

        num_attributes = int(
            input(f"Enter the number of attributes for ingredient {i+1}: ")
        )
        for j in range(num_attributes):
            name = input(f"Enter name of attribute {j+1} for ingredient {i+1}: ")
            min_roll = int(input(f"Enter min roll for {name}: "))
            max_roll = int(input(f"Enter max roll for {name}: "))
            ingredient.add_attribute(name, min_roll, max_roll)

        item.add_ingredient(ingredient)

    return item


def simulate_rolling(item, num_simulations):
    simulation_results = defaultdict(list)

    for _ in range(num_simulations):
        rolled_item = item.roll_item()
        for name, value in rolled_item.items():
            simulation_results[name].append(value)

    return simulation_results


def plot_simulation_results(results):
    for name, values in results.items():
        min_value = min(values)
        max_value = max(values)
        bins = range(min_value, max_value + 2)  # Ensure bin includes max value
        plt.figure(figsize=(10, 6))
        plt.hist(values, bins=bins, alpha=0.75, edgecolor="black", align="left")
        plt.title(f"Distribution of {name}")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.xticks(bins)  # Ensure ticks are at every integer
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    item = get_user_input()
    num_simulations = int(input("Enter the number of simulations: "))
    simulation_results = simulate_rolling(item, num_simulations)

    print("Simulation results:")
    for name, values in simulation_results.items():
        print(f"{name}: {values[:5]} ...")  # Print first 5 values as a sample

    plot_simulation_results(simulation_results)
