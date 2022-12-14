# from dataclasses import dataclass, field

@dataclass()
class Smartphone:
    # memory: int
    # apps: list = field(default_factory=list)
    # is_on: bool = False

    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False
        # self.used_memory = 0

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        # self.used_memory += app_memory
        if app_memory <= self.memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif app_memory <= self.memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
