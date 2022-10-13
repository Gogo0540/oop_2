class Human:
    def __new__(cls, name, age, growth):
        instance = super().__new__(cls)
        instance.name = name
        instance.age = age
        instance.growth = growth

        return instance



human = Human("Ruslan", 17, 178)
print(human.age)