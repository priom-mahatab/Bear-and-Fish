import random
from fish import Fish
from bear import Bear

class Ecosystem:
    def __init__(self, size):
        self.river = [None] * size

    def populate(self, num_bears, num_fish):
        #populating with bears
        for _ in range(num_bears):
            while True:
                index = random.randint(0, len(self.river)-1)
                if self.river[index] is None:
                    self.river[index] = Bear()
                    break

        #populating with fish
        for _ in range(num_fish):
            while True:
                index = random.randint(0, len(self.river)-1)
                if self.river[index] is None:
                    self.river[index] = Fish()
                    break

    def move_creatures(self):
        """Move creatures to empty slots"""
        for i in range(len(self.river)):
            creature = self.river[i]
            if creature is not None:
                new_index = creature.move(i, len(self.river))
                if new_index != i:
                    if self.river[new_index] is None:
                        self.river[new_index], self.river[i] = self.river[i], None
                    else:
                        self.handle_collision(i, new_index)

    def handle_collision(self, index1, index2):
        creature1 = self.river[index1]
        creature2 = self.river[index2]

        if type(creature1) == type(creature2):
            # Reproduction
            empty_indices = [i for i, val in enumerate(self.river) if val is None]
            if empty_indices:
                new_creature = creature1.reproduce()
                self.river[random.choice(empty_indices)] = new_creature
        else:
            # Fish dies
            if isinstance(creature1, Bear) and isinstance(creature2, Fish):
                self.river[index2] = None
            elif isinstance(creature1, Fish) and isinstance(creature2, Bear):
                self.river[index1] = None

    def display_river(self):
        river_representation = ""
        for slot in self.river:
            if slot is None:
                river_representation += "[ ]"
            elif isinstance(slot, Bear):
                river_representation += "[B]"
            elif isinstance(slot, Fish):
                river_representation += "[F]"
        print(river_representation)

    def run_simulation(self, steps):
        for step in range(steps):
            print(f"--- Stage {step+1} ---")
            self.move_creatures()
            self.display_river()