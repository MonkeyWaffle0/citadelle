class Card:
    def __init__(self, color):
        self.color = color

        # For tests with colorama lib
        if color == "Red":
            self.fg = "\033[91m"
        elif color == "Blue":
            self.fg = "\033[94m"
        elif color == "Yellow":
            self.fg = "\033[93m"
        elif color == "Green":
            self.fg = "\033[32m"
        elif color == "Purple":
            self.fg = "\033[35m"

        # Size of the card, etc...