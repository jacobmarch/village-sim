from typing import Dict, List, Optional, TYPE_CHECKING
from traits import Trait, BooleanTrait
from actions import Action, Eat, Sleep, Work
import random

if TYPE_CHECKING:
    from .organization import Organization
    from .structure import Structure

class Creature:
    def __init__(self, name: str, race: str) -> None:
        self.name = name
        self.race = race
        self.traits: Dict[str, Trait] = {
            "hunger": Trait("Hunger", 0),
            "energy": Trait("Energy", 100),
            "sentient": BooleanTrait("Sentient", True),
            "intelligence": Trait("Intelligence", 50, 0, 100),
            "strength": Trait("Strength", 50, 0, 100),
            "agility": Trait("Agility", 50, 0, 100),
            "charisma": Trait("Charisma", 50, 0, 100),
        }
        self.actions: List[Action] = [Eat(), Sleep(), Work()]
        self.organizations: List['Organization'] = []
        self.leading_organization: Optional['Organization'] = None

    def join_organization(self, organization: 'Organization') -> bool:
        if organization not in self.organizations:
            self.organizations.append(organization)
            return True
        return False

    def leave_organization(self, organization: 'Organization') -> None:
        if organization in self.organizations:
            self.organizations.remove(organization)
            if organization == self.leading_organization:
                self.stop_leading_organization(organization)

    def start_leading_organization(self, organization: 'Organization') -> None:
        if not self.leading_organization:
            self.leading_organization = organization

    def stop_leading_organization(self, organization: 'Organization') -> None:
        if self.leading_organization == organization:
            self.leading_organization = None
            organization.leader = None

    def create_organization(self, name: str, other_member: 'Creature', structure: 'Structure') -> 'Organization':
        from .organization import Organization
        if not self.leading_organization:
            new_org = Organization(name, self, [other_member], [structure])
            self.join_organization(new_org)
            self.start_leading_organization(new_org)
            other_member.join_organization(new_org)
            return new_org
        return None

    def update(self) -> str:
        # Simulate natural changes
        self.traits["hunger"].update(self.traits["hunger"].value + 5)
        self.traits["energy"].update(self.traits["energy"].value - 3)

        # Choose and execute a random action
        action = random.choice(self.actions)
        return action.execute(self)

    def __str__(self) -> str:
        traits_str = ", ".join(str(trait) for trait in self.traits.values())
        orgs_str = ", ".join(org.name for org in self.organizations)
        leader_str = f"Leading: {self.leading_organization.name}" if self.leading_organization else "Not leading any organization"
        return f"Creature: {self.name} ({self.race}) [{traits_str}] [Organizations: {orgs_str}] [{leader_str}]"