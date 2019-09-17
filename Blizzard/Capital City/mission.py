class Capital:
    class __Capital:
        def __init__(self, city_name):
            self.city = city_name

        def name(self):
            return self.city

    __instance = None

    def __new__(cls, city_name):
        if not Capital.__instance:
            Capital.__instance = Capital.__Capital(city_name)
        return Capital.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)


if __name__ == '__main__':
    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
