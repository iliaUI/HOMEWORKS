def cakes(recipe, available):
    # Initialize the maximum number of cakes to a large number
    max_cakes = float('inf')

    # Iterate through each ingredient in the recipe
    for ingredient, amount_needed in recipe.items():
        if ingredient not in available:
            # If an ingredient is not available, we can't make any cakes
            return 0
        else:
            # Calculate the number of cakes we can make with the available amount of this ingredient
            amount_available = available[ingredient]
            cakes_with_ingredient = amount_available // amount_needed
            # Update the maximum number of cakes to the minimum across all ingredients
            max_cakes = min(max_cakes, cakes_with_ingredient)

    return max_cakes
