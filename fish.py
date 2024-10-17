import random

class Fish:
    def __init__(self):
        self.type = "Fish"

    @staticmethod
    def move(current_index, river_length):
        """Random movement to adjacent position"""
        direction = random.choice([-1, 0, 1])
        new_index = current_index + direction

        return max(0, min(new_index, river_length - 1))

    def reproduce(self):
        """Creating a new instance of Fish"""
        return Fish()

    def __repr__(self):
        return f"Fish"