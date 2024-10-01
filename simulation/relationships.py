class RelationshipTracker:
    def __init__(self):
        self.relationships = {}
        self.relationship_classifications = [
            (-100, -90, "sworn enemies"),
            (-90, -75, "hate"),
            (-75, -50, "dislike"),
            (-50, -25, "unfriendly"),
            (-25, 0, "slightly negative"),
            (0, 25, "neutral"),
            (25, 50, "slightly positive"),
            (50, 75, "friendly"),
            (75, 90, "close"),
            (90, 100, "best friends")
        ]

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
            classification = self.classify_relationship(score)
            print(f"  {name1} - {name2}: {score} ({classification})")

    def get_vote_probability(self, voter, candidate):
        relationship = self.get_relationship(voter, candidate)
        # Convert relationship score (-100 to 100) to probability (0 to 1)
        return (relationship + 100) / 200

    def classify_relationship(self, score):
        for low, high, classification in self.relationship_classifications:
            if low <= score < high:
                return classification
        return "best friends"  # For score == 100