class Rabbit:
    def __init__(self, color="blue"):
        self.color = color
    
    def voice(self):
        print("clunking")

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color