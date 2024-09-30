from typing import List, Optional, TYPE_CHECKING
import random

if TYPE_CHECKING:
    from .creature import Creature
    from .structure import Structure

class Organization:
    def __init__(self, name: str, leader: 'Creature', members: List['Creature'] = None, structures: List['Structure'] = None) -> None:
        self.name = name
        self.leader: 'Creature' = leader
        self.creatures: List['Creature'] = [leader] + [m for m in members if m != leader]
        self.structures: List['Structure'] = structures
        self.meeting_place: Optional['Structure'] = structures[0] if structures else None
        self.days_existed: int = 0
        self.leader_days_in_charge: int = 0

    def add_member(self, creature: 'Creature') -> bool:
        if creature not in self.creatures:
            self.creatures.append(creature)
            creature.join_organization(self)
            return True
        return False

    def remove_member(self, creature: 'Creature') -> None:
        if creature in self.creatures:
            self.creatures.remove(creature)
            creature.leave_organization(self)
            if creature == self.leader:
                self.choose_new_leader()

    def change_leader(self, new_leader: 'Creature') -> bool:
        if new_leader in self.creatures and new_leader != self.leader and not new_leader.leading_organization:
            old_leader = self.leader
            self.leader = new_leader
            self.leader_days_in_charge = 0
            if old_leader:
                old_leader.stop_leading_organization(self)
            new_leader.start_leading_organization(self)
            return True
        return False

    def choose_new_leader(self) -> bool:
        potential_leaders = [c for c in self.creatures if c != self.leader and not c.leading_organization]
        if potential_leaders:
            new_leader = random.choice(potential_leaders)
            return self.change_leader(new_leader)
        elif self.creatures and self.leader not in self.creatures:
            # If the current leader is not in the organization, choose a new leader from existing members
            new_leader = random.choice(self.creatures)
            return self.change_leader(new_leader)
        return False

    def add_structure(self, structure: 'Structure') -> None:
        if structure not in self.structures:
            self.structures.append(structure)
            if not self.meeting_place:
                self.meeting_place = structure

    def remove_structure(self, structure: 'Structure') -> None:
        if structure in self.structures:
            self.structures.remove(structure)
            if self.meeting_place == structure:
                self.meeting_place = self.structures[0] if self.structures else None

    def is_valid(self) -> bool:
        return len(self.creatures) >= 2 and len(self.structures) >= 1 and (self.leader is None or self.leader in self.creatures)

    def update(self) -> None:
        self.days_existed += 1
        self.leader_days_in_charge += 1

    def __str__(self) -> str:
        leader_name = self.leader.name if self.leader else "None"
        return f"Organization: {self.name} (Leader: {leader_name}, Members: {len(self.creatures)}, Structures: {len(self.structures)}, Days Existed: {self.days_existed}, Leader Days in Charge: {self.leader_days_in_charge})"
