from typing import List, Optional, TYPE_CHECKING
import random

if TYPE_CHECKING:
    from .creature import Creature
    from .structure import Structure

class Organization:
    def __init__(self, name: str, leader: 'Creature', members: List['Creature'], structures: List['Structure']) -> None:
        self.name = name
        self.days_existed: int = 0
        self.leader = leader
        self.creatures: List['Creature'] = members  # Ensure this is a flat list
        self.structures = structures  # Initialize structures
        self.meeting_place = structures[0] if structures else None  # Initialize meeting_place
        self.leader_days_in_charge = 0  # Initialize leader_days_in_charge

    def update(self):
        self.leader_days_in_charge += 1

    def add_member(self, creature: 'Creature') -> bool:
        if creature not in self.creatures:
            self.creatures.append(creature)  # Append individual Creature instances
            return True
        return False

    def remove_member(self, creature: 'Creature') -> bool:
        if creature in self.creatures:
            self.creatures.remove(creature)
            if creature == self.leader:
                self.leader = None
                self.leader_days_in_charge = 0
            return True
        return False

    def is_valid(self) -> bool:
        return len(self.creatures) >= 2 and self.meeting_place is not None

    def choose_new_leader(self, relationship_tracker) -> bool:
        if len(self.creatures) < 2:
            return False

        candidates = [c for c in self.creatures if c != self.leader]
        votes = {candidate: 0 for candidate in candidates}

        for voter in self.creatures:
            vote_probabilities = [
                (candidate, relationship_tracker.get_vote_probability(voter, candidate))
                for candidate in candidates
            ]
            total_probability = sum(prob for _, prob in vote_probabilities)
            
            if total_probability > 0:
                random_value = random.random() * total_probability
                cumulative_probability = 0
                for candidate, probability in vote_probabilities:
                    cumulative_probability += probability
                    if random_value <= cumulative_probability:
                        votes[candidate] += 1
                        break

        new_leader = max(votes, key=votes.get)
        if new_leader != self.leader:
            self.leader = new_leader
            self.leader_days_in_charge = 0
            return True
        return False

    def __str__(self) -> str:
        leader_name = self.leader.name if self.leader else "None"
        return f"Organization: {self.name} (Leader: {leader_name}, Members: {len(self.creatures)}, Structures: {len(self.structures)}, Days Existed: {self.days_existed}, Leader Days in Charge: {self.leader_days_in_charge})"
