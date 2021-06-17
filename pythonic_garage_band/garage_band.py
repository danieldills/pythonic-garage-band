class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

class Musician:
    def __init__(self, name, type, instrument):
      self.name = name
      self.type = type
      self.instrument = instrument

    def __str__(self):
      return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
      return f"{self.type} instance. Name = {self.name}"

    def get_instrument(self):
      pass

    def play_solo(self):
      pass
        
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "Guitarist", "guitar")

    def get_instrument(self):
      return f"guitar"

class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name, "Bassist", "bass")

    def get_instrument(self):
      return f"bass"

class Drummer(Musician):
    def __init__(self, name):
      super().__init__(name, "Drummer", "drums")
      
    def get_instrument(self):
      return f"drums"
