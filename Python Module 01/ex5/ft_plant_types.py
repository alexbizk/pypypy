class Plant:
    def __init__(self, name: str, height: float, day_age: int) -> None:
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


class Flower(Plant):
    def __init__(
        self, name: str, height: float, day_age: int, color: str
    ) -> None:
        super().__init__(name, height, day_age)  # 基本信息交给 Plant 设置，颜色由 Flower 自己设置。
        self.color = color
    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")


if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
