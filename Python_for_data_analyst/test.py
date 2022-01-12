class human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def speak(self):
        print(f"Hey I'm {self.name}. What's your name?")
