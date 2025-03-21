class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipe_map = {recipe: set(ing) for recipe, ing in zip(recipes, ingredients)}
        result = []

        made_something = True
        while made_something:
            made_something = False
            for recipe in list(recipe_map.keys()):
                if recipe_map[recipe].issubset(supply_set):
                    supply_set.add(recipe)
                    result.append(recipe)
                    del recipe_map[recipe] 
                    made_something = True

        return result
