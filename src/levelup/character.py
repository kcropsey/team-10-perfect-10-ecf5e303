class Character:
    name = ""
    default_name = "Perfect 10"

    def __init__(self, character_name = None):
        if character_name is None:
            character_name = self.default_name
        self.name = character_name
        self.move_count = 0

    def enter_map(self, map):
        self.map = map
        self.position = map.starting_position
    
    def move(self, direction):
        self.move_count = self.move_count + 1
        self.position = self.map.calculatePosition(self.position, direction) 