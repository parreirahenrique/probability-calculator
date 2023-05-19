import copy
import random
# Consider using the modules imported above.

class Hat:
    contents: list = []
    

    def __init__(self, **balls_input):
        for i in range(len(list(balls_input.values()))):
            for j in range(list(balls_input.values())[i]):
                self.contents.append(list(balls_input.keys())[i])

    def draw(self, number_of_balls: int):
        drawn_balls: list = []
        contents_copy = self.contents.copy()

        while number_of_balls > 0:
            drawn_ball = random.randint(0, len(contents_copy) - 1)
            drawn_balls.append(contents_copy[drawn_ball])
            contents_copy.remove(contents_copy[drawn_ball])
            number_of_balls -= 1

            if len(contents_copy) == 0:
                contents_copy = self.contents.copy()


        return drawn_balls

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
