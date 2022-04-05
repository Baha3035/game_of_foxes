class Fox:
    def __init__(self, color="orange"):
        self.color = color

    def voice(self):
        print("fox bark")

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
