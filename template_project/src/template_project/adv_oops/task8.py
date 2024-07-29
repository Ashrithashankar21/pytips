class Duck:
    def quack(self):
        return "Quack!"


class Goose:
    def honk(self):
        return "Honk!"


class Robot:
    def quack(self):
        return "Robot quack!"


def make_it_quack(duck):
    try:
        print(duck.quack())
    except AttributeError:
        print("This object can't quack.")


duck = Duck()
goose = Goose()
robot = Robot()

make_it_quack(duck)
make_it_quack(goose)
make_it_quack(robot)
