class Plant:
    def __init__(self, name: str, height: float, day_age: int) -> None:
        self.name = name
        self.height = height
        self.day_age = day_age
        # self：正在初始化的那个植物对象 Python 会自动传入，你不用自己填写。

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.day_age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    for plant in [rose, oak, cactus, sunflower, fern]:
        # plant 就是在上行第一次被赋值的，不需要提前声明。
        print("Created: ", end="")
        plant.show()
