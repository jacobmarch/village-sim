from entity_types import Creature, Structure, Organization
from typing import List
import random
from simulation.relationships import RelationshipTracker

class Simulation:
    def __init__(self):
        self.creatures: List[Creature] = []
        self.structures: List[Structure] = []
        self.organizations: List[Organization] = []
        self.relationship_tracker = RelationshipTracker()
        self.setup_entities()

    def setup_entities(self):
        # Create some initial entities
        self.creatures.extend([
            Creature("Alice", "Human"),
            Creature("Bob", "Human"),
            Creature("Charlie", "Human"),
            Creature("Diana", "Human")
        ])
        self.structures.extend([
            Structure("House"),
            Structure("Farm"),
            Structure("Market")
        ])
        
        # Create initial organization
        initial_org = self.creatures[0].create_organization("Village Council", [self.creatures[1]], self.structures[0])
        self.organizations.append(initial_org)

    def run(self):
        day = 1
        while True:
            input(f"Press Enter to advance to day {day}...")
            self.advance_simulation(day)
            day += 1

    def advance_simulation(self, day: int):
        print(f"\n--- Day {day} ---")
        
        # Update all entities
        for creature in self.creatures:
            action_result = creature.update()
            print(action_result)
        
        for structure in self.structures:
            structure.update()
        
        for organization in self.organizations:
            organization.update()
        
        # Creature interactions
        self.creature_interactions()
        
        # Update and manage organizations
        self.manage_organizations()
        
        # Print current state
        self.print_state()

    def creature_interactions(self):
        for _ in range(len(self.creatures) // 2):  # Each creature interacts once on average
            creature1, creature2 = random.sample(self.creatures, 2)
            interaction_type = random.choice(["positive", "neutral", "negative"])
            
            if interaction_type == "positive":
                change = random.randint(1, 10)
                print(f"{creature1.name} and {creature2.name} had a positive interaction!")
            elif interaction_type == "neutral":
                change = 0
                print(f"{creature1.name} and {creature2.name} had a neutral interaction.")
            else:  # negative
                change = random.randint(-10, -1)
                print(f"{creature1.name} and {creature2.name} had a negative interaction.")
            
            self.relationship_tracker.update_relationship(creature1, creature2, change)

    def manage_organizations(self):
        # Randomly create, join, leave organizations, or change leadership
        for creature in self.creatures:
            if random.random() < 0.1:  # 10% chance to perform an organization action
                action = random.choice(["create", "join", "leave", "change_leader"])
                if action == "create" and len(self.creatures) > 1 and len(self.structures) > 0 and not creature.leading_organization:
                    eligible_members = [c for c in self.creatures if c != creature and not c.leading_organization]
                    if eligible_members:
                        other_member = random.choice(eligible_members)
                        structure = random.choice(self.structures)
                        new_org = creature.create_organization(f"{creature.name}'s Group", other_member, structure)
                        if new_org:
                            self.organizations.append(new_org)
                            print(f"{creature.name} created a new organization: {new_org.name}")
                    else:
                        print(f"{creature.name} tried to create an organization, but there were no eligible members")
                elif action == "join" and self.organizations:
                    org_to_join = random.choice(self.organizations)
                    if org_to_join.add_member(creature):
                        print(f"{creature.name} joined {org_to_join.name}")
                    else:
                        print(f"{creature.name} tried to join {org_to_join.name}, but they're already a member")
                elif action == "leave" and creature.organizations:
                    org_to_leave = random.choice(creature.organizations)
                    org_to_leave.remove_member(creature)
                    print(f"{creature.name} left {org_to_leave.name}")
                elif action == "change_leader" and creature.leading_organization:
                    org = creature.leading_organization
                    if org.choose_new_leader(self.relationship_tracker):
                        print(f"{org.leader.name} became the new leader of {org.name}")
                    else:
                        print(f"No change in leadership for {org.name}")

        # Check for and remove invalid organizations
        self.organizations = [org for org in self.organizations if org.is_valid()]

    def print_state(self):
        print("\nCurrent Simulation State:")
        print("Creatures:")
        for creature in self.creatures:
            print(f"  - {creature}")
        print("Structures:")
        for structure in self.structures:
            print(f"  - {structure}")
        print("Organizations:")
        for organization in self.organizations:
            print(f"  - {organization}")
            # Display Leader Information
            print(f"    Leader: {organization.leader.name if organization.leader else 'None'} (Days in charge: {organization.leader_days_in_charge})")
            # Display Members
            members = ', '.join(creature.name for creature in organization.creatures if isinstance(creature, Creature))
            print(f"    Members: {members}")
            # Display Meeting Place
            print(f"    Meeting Place: {organization.meeting_place.name if organization.meeting_place else 'None'}")
        # Print relationships
        self.relationship_tracker.print_relationships()
        print()