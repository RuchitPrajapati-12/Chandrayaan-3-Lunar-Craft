class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    # Methods for movement and rotation
    def move_forward(self):
         if self.direction == 'N':
            self.y += 1
         elif self.direction == 'S':
            self.y -= 1
         elif self.direction == 'E':
            self.x += 1
         elif self.direction == 'W':
            self.x -= 1
         elif self.direction == 'Up':
            self.z += 1
         elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        pass

    def turn_up(self):
        pass

    def turn_down(self):
        pass

    def execute_commands(self, commands):
        pass
