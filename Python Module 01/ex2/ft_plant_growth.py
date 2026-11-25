class Plant:
    name: str
    height: float
    day_age: int

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.day_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day_age} days old")


if __name__ == "__main__":  # 不在"中间"，而是**"运行部分"的开头**。
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.day_age = 30

    initial_height = rose.height
    # initial_height = rose.height 可以直接使用，不必声明类型；
    # 也可以明确写成：initial_height: float = rose.height
    print("=== Garden Plant Registry ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")
