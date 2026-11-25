class Plant:
    def __init__(self, name: str, height: float, day_age: int) -> None:
        # height 是参数名，而 _height 是对象内部的属性名。它们是两个不同的东西。
        self.name = name
        self._height = 0.0
        self._day_age = 0
        self.set_height(height)
        self.set_age(day_age)
        self.get_height()
        self.get_age()

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        else:
            self._height = height
            return True

    def set_age(self, day_age: int) -> bool:
        if day_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        else:
            self._day_age = day_age
            return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._day_age

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print("Plant Created: ", end="")
    rose.show()
    print("")
    if rose.set_height(25):
        print(f"Height updated: {rose.get_height()}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    print("")
    if not rose.set_height(-5):
        print("Height update rejected")
    if not rose.set_age(-5):
        print("Age update rejected")
    print("")
    print(f"Current state:", end="")
    rose.show()
