class Direction:
    def __init__(self, step_size_on_x_axis, step_size_on_y_axis):
        self.step_size_on_x_axis = step_size_on_x_axis
        self.step_size_on_y_axis = step_size_on_y_axis

    def right(self):
        pass

    def left(self):
        pass

class N(Direction):
    def __init__(self):
        super().__init__(0, 1)

    def left(self):
        return W()

    def right(self):
        return E()

class S(Direction):
    def __init__(self):
        super().__init__(0, -1)

    def right(self):
        return W()

    def left(self):
        return E()

class E(Direction):
    def __init__(self):
        super().__init__(1, 0)

    def right(self):
        return S()

    def left(self):
        return N()

class W(Direction):
    def __init__(self):
        super().__init__(-1, 0)

    def right(self):
        return N()

    def left(self):
        return S()