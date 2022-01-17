class Fruit:
    def __init__(self, weight):
        print('I am building a fruit')
        self.healthy = True
        self.weight = weight
        pass

    def __del__(self):
        print('I am dyiiiing')
        pass

    def __repr__(self):
        return "I am a fruit and I weigh " + str(self.weight)

    def __call__(self, *args, **kwargs):
        print('Who are you calling, young man')
        pass

    def example_method(self):
        print('I am a random method')


# example_fruit = Fruit(weight=65)
# example_fruit.example_method()
# example_fruit()
# print(example_fruit)
# del example_fruit


class Orange(Fruit):
    def __init__(self, weight):
        super(Orange, self).__init__(weight=weight)

    def round(self):
        print('Yes I am round')


orange = Orange(weight=4)
orange.round()
orange.example_method()

example_fruit = Fruit(weight=65)
example_fruit.round()
