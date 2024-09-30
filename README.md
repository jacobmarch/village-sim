# village-sim

This is a basic simulation of a village where the user can watch how various villagers interact with each other and the environment. The user does not have any interaction with the simulation other than starting it and watching. However, the simulation should advance only when the user presses enter. 

## Running the simulation

To run the simulation, simply run the `main.py` file:

```bash
python main.py
```

## Basic Structure

The simulation is built using a series of classes and functions that model the behavior of the villagers, buildings, and other entities in the village.

Every entity in the simulation should be an instance of one of the classes in the `entity_types` folder. However, they should be composed of various traits and actions which are instances of the classes in the `traits` and `actions` folders. The code will use a combination of inheritance and composition to achieve this.

### Creatures

Creatures are the basic entities in the simulation. They are any thing that lives and can interact with the environment. These could be humans, animals, plants, monsters, robots, etc. They do not need to be alive to be considered a creature.

### Structures

Structures are the buildings and other structures in the village. They are any thing that is not a creature and can interact with the environment. These could be houses, barns, fences, trees, etc.

### Organizations

Organizations are groups of creatures and structures that work together. These could be families, guilds, governments, etc. Organizations must have at least two members (creatures), one structure, and a leader to be considered valid. Creatures can join, leave, and create organizations. A creature can be a member of multiple organizations but can only lead one organization at a time. Creatures cannot join an organization they are already a part of. 

Organizations track how long they have existed and how long the current leader has been in charge. Leadership can change if the current leader leaves the organization or steps down. If an organization falls below two members, loses all its structures, or loses its leader without a replacement, it is disbanded. Each organization has a designated meeting place, which is one of its structures.

### Actions

Actions are the things that creatures and structures can do. These could be eating, sleeping, working, fighting, etc. Every action should have a specific effect on the creature or structure performing it.

### Traits

Traits are the things that creatures and structures have. These could be hunger, thirst, happiness, sadness, etc.

