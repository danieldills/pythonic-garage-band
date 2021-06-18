class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def to_list():
      pass

class Musician:
    def __init__(self, name, type, instrument, solo):
      self.name = name
      self.type = type
      self.instrument = instrument
      self.solo = solo

    def __str__(self):
      return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
      return f"{self.type} instance. Name = {self.name}"

    def get_instrument(self):
      return f"{self.instrument}"

    def play_solo(self):
      return f"{self.solo}"
        
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "Guitarist", "guitar", "face melting guitar solo")

class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name, "Bassist", "bass", "bom bom buh bom")

class Drummer(Musician):
    def __init__(self, name):
      super().__init__(name, "Drummer", "drums", "rattle boom crash")
