import copy
import random
# Consider using the modules imported above.

class Hat:
    contents: list = []

    def __init__(self, **balls_input):
        self.contents.clear()

        for i in range(len(list(balls_input.values()))):
            for j in range(list(balls_input.values())[i]):
                self.contents.append(list(balls_input.keys())[i])
        
    def draw(self, number_of_balls: int):
        drawn_balls: list = []
        contents_copy = copy.copy(self.contents)

        while number_of_balls > 0:
            drawn_ball = random.randint(0, len(contents_copy) - 1)
            drawn_balls.append(contents_copy[drawn_ball])
            contents_copy.remove(contents_copy[drawn_ball])
            number_of_balls -= 1

            if len(contents_copy) == 0:
                contents_copy = self.contents.copy()

        self.contents = contents_copy
        return drawn_balls

def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    balls_color_list: list = []
    number_balls_list: list = []
    number_balls_counted: list = []
    m: int = 0
    
    balls_color_list.clear()
    number_balls_list.clear()

    balls_color_list = list(expected_balls.keys())
    number_balls_list = list(expected_balls.values())
    number_balls_counted: list = []

    for i in range(num_experiments):
        copied_hat = copy.copy(hat)
        contents = copied_hat.draw(number_of_balls=num_balls_drawn)
        number_balls_counted.clear()
        
        for j in range(len(balls_color_list)):
            number_balls_counted.append(0)

            for k in range(len(contents)):
                if contents[k] == balls_color_list[j]:
                    number_balls_counted[j] += 1
        
        all_balls_found = True
        for j in range(len(number_balls_counted)):
            if number_balls_counted[j] < number_balls_list[j]:
                all_balls_found = False
                break

        if all_balls_found:
            m += 1

    return (m / num_experiments)
