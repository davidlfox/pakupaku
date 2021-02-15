class Teller:
    def __init__(self, colors, fortunes, position):
        self.colors = colors
        self.fortunes = fortunes
        self.position = position
    
    def toggle(self):
        self.position = not self.position

    def visible_numbers(self):
        if self.position:
            return [1,3,5,7]
        else:
            return [2,4,6,8]
    
    def __str__(self):
        return f'{self.colors[0]}'