
def example_sum_function(a, b=2, c=3):
    return a + b + c


# sum1 = example_sum_function(1, 2, 3)
# sum2 = example_sum_function(a=1, b=2, c=3)
# sum3 = example_sum_function(1)
# print(sum1, sum2, sum3)


class Fruit:
    def __init__(self, weight=35):
        print('I am building a fruit')
        self.inner_weight = weight
        # self.healthy = True
        # pass

    def __del__(self):
        print('I am dying :(')
        pass

    def __repr__(self):
        return "I am a fruit and I weigh " + str(self.inner_weight)

    # def __call__(self, *args, **kwargs):
    #     print('Who are you calling, young man')
    #     pass
    #
    def example_method(self):
        print('I am a random method')
        return 'great class'


# example_fruit = Fruit(weight=40)
# print(example_fruit.inner_weight)
# print(example_fruit)
# example_fruit.example_method()
# del example_fruit

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

    # def __del__(self):
    #     print("I'm an orange and I don't care about dying")


orange = Orange(weight=4)
print(orange)
del orange
# orange.round()
# orange.example_method()
#
# example_fruit = Fruit(weight=65)
# example_fruit.round()
