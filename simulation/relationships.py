class RelationshipTracker:
    def __init__(self):
        self.relationships = {}

    def get_relationship(self, creature1, creature2):
        key = self._get_key(creature1, creature2)
        return self.relationships.get(key, 0)  # Default relationship score is 0

    def update_relationship(self, creature1, creature2, change):
        key = self._get_key(creature1, creature2)
        current_score = self.relationships.get(key, 0)
        new_score = max(-100, min(100, current_score + change))  # Clamp between -100 and 100
        self.relationships[key] = new_score

    def _get_key(self, creature1, creature2):
        # Ensure consistent key regardless of creature order
        return tuple(sorted([creature1.name, creature2.name]))

    def print_relationships(self):
        print("\nCreature Relationships:")
        for (name1, name2), score in self.relationships.items():
            print(f"  {name1} - {name2}: {score}")