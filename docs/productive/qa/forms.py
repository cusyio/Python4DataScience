import gc


class Form:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Form):
    def __init__(self, length=1, x=0, y=0):
        super().__init__(x, y)
        self.length = length

    def circumference(self):
        return 4 * self.length


class Circle(Form):
    pi = 3.14159

    def __init__(self, diameter=1, x=0, y=0):
        super().__init__(x, y)
        self.diameter = diameter

    def circumference(self):
        return self.diameter * Circle.pi


class SquaresAndCircles:
    pi = 3.14159

    @classmethod
    def circumferences(cls):
        csum = 0
        for obj in gc.get_objects():
            if isinstance(obj, Square):
                csum = csum + 4 * obj.length
            if isinstance(obj, Circle):
                csum = csum + obj.diameter * cls.pi
        return csum


class CircumferenceFormInstances:
    def circumferences():
        csum = 0
        for obj in gc.get_objects():
            if isinstance(obj, Form) and hasattr(obj, "circumference"):
                csum = csum + obj.circumference()
        return csum
