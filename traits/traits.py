class Trait:
    def __init__(self, name: str, value: float, min_value: float = 0, max_value: float = 100) -> None:
        self.name = name
        self.value = max(min(value, max_value), min_value)
        self.min_value = min_value
        self.max_value = max_value

    def update(self, value: float) -> None:
        self.value = max(min(value, self.max_value), self.min_value)

    def __str__(self) -> str:
        return f"{self.name}: {self.value:.1f}"

class BooleanTrait(Trait):
    def __init__(self, name: str, value: bool) -> None:
        super().__init__(name, float(value), 0, 1)

    def update(self, value: bool) -> None:
        super().update(float(value))

    def __str__(self) -> str:
        return f"{self.name}: {bool(self.value)}"

# Add more specific trait classes as needed
