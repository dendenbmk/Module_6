class Horse:

    def __init__(self, x_distance=0, sound='Frrr', y_distance=0):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx


class Eagle:

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self, x_distance, y_distance):
        super().__init__(x_distance, y_distance)

    #
    #
    # def move(self, ):
    #
    #
    #
    # def get_pos(self):
    #     return


p1 = Pegasus()



# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()
