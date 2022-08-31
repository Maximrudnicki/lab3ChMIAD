from Film import Film

class Cartoon(Film):
    def __init__(self, name, year, duration, producer):
        super().__init__(name, year, duration)
        self.producer = producer

    def get_producer(self):
        return self.producer

    def set_producer(self):
        print("Enter producer:")
        self.producer = str(input())

    def show(self):
        super().show()
        print(f"Producer - {self.producer}.")

