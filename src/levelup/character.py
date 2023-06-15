class Character:
    name = ""
    default_name = "Perfect 10"

    def __init__(self, character_name = None):
        if character_name is None:
            character_name = self.default_name
        self.name = character_name
