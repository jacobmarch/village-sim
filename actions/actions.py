from typing import Any

class Action:
    def __init__(self, name: str) -> None:
        self.name = name

    def execute(self, entity: Any) -> str:
        pass

class Eat(Action):
    def __init__(self):
        super().__init__("Eat")

    def execute(self, entity: Any) -> str:
        entity.traits["hunger"].value -= 20
        return f"{entity.name} ate some food."

class Sleep(Action):
    def __init__(self):
        super().__init__("Sleep")

    def execute(self, entity: Any) -> str:
        entity.traits["energy"].value += 30
        return f"{entity.name} took a nap."

class Work(Action):
    def __init__(self):
        super().__init__("Work")

    def execute(self, entity: Any) -> str:
        entity.traits["energy"].value -= 10
        entity.traits["hunger"].value += 15
        return f"{entity.name} worked for a while."
