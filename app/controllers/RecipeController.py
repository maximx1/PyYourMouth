import os


class RecipeController:
    """Controller to manage loading the recipes"""

    _RECIPE_DIR = "recipe_source/OpenYourMouth/"

    def __init__(self):
        new_recipe_list = self.refresh_recipe_listing(self._RECIPE_DIR)
        self.recipe_file_list = dict(zip(range(len(new_recipe_list) + 1), new_recipe_list))

    def list_all(self):
        """Gets a list of all the markdown files"""
        return self.recipe_file_list

    @staticmethod
    def __refresh_recipe_listing(path):
        """Gets a fresh listing of the recipes recursively from the directory passed in"""
        recipes = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                   for name in files
                   if name.endswith(".md")]
        return list(filter(lambda x: x != "README.md", map(lambda x: x[len(path):], recipes)))