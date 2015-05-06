import os


class RecipeController:
    """Controller to manage loading the recipes"""

    _RECIPE_DIR = "recipe_source/OpenYourMouth/"

    def __init__(self):
        new_recipe_list = self.__refresh_recipe_listing(self._RECIPE_DIR)
        self.recipe_file_list = dict(zip(range(len(new_recipe_list) + 1), new_recipe_list))

    def list_all(self):
        """Gets a list of all the markdown files"""
        return self.recipe_file_list

    def by_id(self, recipe_id):
        """Gets the contents of one recipe by it's id or none if not found"""
        recipe = self.recipe_file_list.get(int(recipe_id))
        return self.__load_recipe(recipe) if recipe else None

    def __load_recipe(self, filename):
        """Reads the entire filename"""
        with open(self._RECIPE_DIR + filename) as f:
            return f.read()

    @staticmethod
    def __refresh_recipe_listing(path):
        """Gets a fresh listing of the recipes recursively from the directory passed in"""
        recipes = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                   for name in files
                   if name.endswith(".md")]
        return list(filter(lambda x: x != "README.md", map(lambda x: x[len(path):], recipes)))