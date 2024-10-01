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

Creatures are the basic entities in the simulation. They are any thing that lives and can interact with the environment. These could be humans, animals, plants, monsters, robots, etc. They do not need to be alive to be considered a creature. Each creature has a race (e.g., orc, elf, dwarf) and a set of traits that define its characteristics and abilities.

### Traits

Traits are the characteristics and abilities that creatures and structures have. These include both physical and mental attributes. Some examples of traits are:

- Sentient (boolean): Determines if the creature is capable of complex thought and decision-making.
- Intelligence (int): Represents the creature's cognitive abilities and problem-solving skills.
- Strength (int): Represents the creature's physical power and ability to perform tasks requiring force.
- Agility (int): Represents the creature's speed, reflexes, and coordination.
- Charisma (int): Represents the creature's ability to influence and interact with others.
- Hunger (float): Represents the creature's need for food.
- Energy (float): Represents the creature's current energy level.

Traits can be either boolean (true/false) or numeric (with a value range, typically 0-100). The specific traits a creature has can vary based on its race and individual characteristics.

### Structures

Structures are the buildings and other structures in the village. They are any thing that is not a creature and can interact with the environment. These could be houses, barns, fences, trees, etc.

### Organizations

Organizations are groups of creatures and structures that work together. These could be families, guilds, governments, etc. Organizations must have at least two members (creatures), one structure, and a leader to be considered valid. Creatures can join, leave, and create organizations. A creature can be a member of multiple organizations but can only lead one organization at a time. Creatures cannot join an organization they are already a part of. 

Organizations track how long they have existed and how long the current leader has been in charge. Leadership can change if the current leader leaves the organization or steps down. If an organization falls below two members, loses all its structures, or loses its leader without a replacement, it is disbanded. Each organization has a designated meeting place, which is one of its structures.

### Actions

Actions are the things that creatures and structures can do. These could be eating, sleeping, working, fighting, etc. Every action should have a specific effect on the creature or structure performing it.

## Simulation Logic

The simulation operates in discrete steps, advancing only when the user presses the Enter key. Each step involves the following processes:

1. **Input Handling**: Waits for the user to press Enter to proceed to the next simulation step.
2. **Entity Updates**: Iterates through all entities (creatures, structures, organizations) and updates their states based on their traits and actions.
3. **Interaction Processing**: Handles interactions between entities, such as creatures interacting with structures or other creatures.
4. **Environment Changes**: Applies any changes to the environment that result from entity actions.
5. **Logging and Output**: Outputs the current state of the simulation to the user for observation.

### Event Loop

The main loop of the simulation is controlled by user input. Each iteration of the loop represents a single time step in the simulation where all entities perform their actions and the environment updates accordingly.

## Simulation Structure

The codebase is organized into several modules to promote modularity and ease of maintenance:

- **main.py**: Entry point of the simulation. Initializes the simulation and starts the event loop.
- **simulation/simulation.py**: Contains the core simulation engine that manages entities and the simulation loop.
- **entity_types/**: 
  - **creature.py**: Defines the `Creature` class and its behaviors.
  - **organization.py**: Defines the `Organization` class and related functionalities.
  - **__init__.py**: Initializes the entity_types module.
- **actions/actions.py**: Defines various `Action` classes that entities can perform.
- **traits/**:
  - **__init__.py**: Initializes the traits module.
  - Other trait-related classes and definitions.

### Classes and Their Interactions

- **Creature Class**: Represents living entities with traits and the ability to perform actions. Creatures can belong to organizations and interact with structures.
- **Organization Class**: Manages groups of creatures and structures, handling leadership and membership dynamics.
- **Action Classes**: Encapsulate behaviors that entities can perform, affecting their traits or other entities.
- **Trait Classes**: Represent various states or characteristics of entities that influence their behavior and interactions.

## Variables

Key variables in the simulation include:

- **Entities List**: Maintains all active creatures, structures, and organizations in the simulation.
- **Simulation Clock**: Tracks the number of steps elapsed since the simulation started.
- **User Input**: Captures the Enter key press to advance the simulation.
- **Entity Attributes**: Variables within entities that represent their current state, such as hunger level, happiness, etc.
- **Organization Metrics**: Variables tracking the duration of organizations, leadership tenure, and membership counts.

## Future Steps and Ideas

To enhance the simulation and provide a more immersive experience, the following future steps and ideas are proposed:

1. **Expanded Entity Types**:
   - Introduce more diverse creature types with unique traits and behaviors.
   - Add additional structure types with specific functionalities.

2. **Advanced AI Behaviors**:
   - Develop more sophisticated AI for creatures, enabling complex interactions and decision-making processes.
   - Implement goals and motivations for creatures to drive their actions.

3. **Environmental Factors**:
   - Introduce weather systems, seasons, and other environmental variables that affect entity behavior and village dynamics.
   - Simulate resource management, such as food, water, and materials.

4. **Event System**:
   - Create random events or scenarios that can impact the simulation, such as natural disasters, festivals, or conflicts.
   
5. **Persistence and Saving**:
   - Implement saving and loading functionality to preserve the state of the simulation between sessions.

6. **Performance Optimization**:
   - Optimize the simulation loop and entity management to handle larger villages with more entities efficiently.

7. **Career and Progression**:
   - Implement a career and progression system for creatures, allowing them to advance in their roles and responsibilities within organizations.

8. **Family Systems**:
   - Implement family systems for creatures, allowing them to have children and manage their family life.

9. **Trade and Commerce**:
   - Implement a trade and commerce system, allowing creatures to trade resources and goods with each other.

10. **Research and Development**:
    - Implement a research and development system, allowing creatures to research and develop new technologies and ideas.

11. **Education and Learning**:
    - Implement an education and learning system, allowing creatures to learn new skills and knowledge.

12. **Health and Disease**:
    - Implement a health and disease system, allowing creatures to suffer from illnesses and injuries.

13. **Social and Cultural Systems**:
    - Implement social and cultural systems, allowing creatures to have relationships and cultural practices.

14. **Diverse Creature Types**:
    - Implement a wider variety of creature races with unique trait distributions and abilities.
    - Create special traits or abilities for specific races (e.g., elves might have enhanced agility, dwarves might have increased strength).

15. **Trait-based Interactions**:
    - Develop more complex interaction systems based on creature traits (e.g., high-charisma creatures might be more successful in leadership roles).
    - Implement trait-based decision making for AI-controlled creatures.

Implementing these enhancements will make the village simulation more engaging and robust, providing a solid foundation for future development and expansion.

