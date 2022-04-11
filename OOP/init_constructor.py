class Computer():
    #__init__ is used to set values as soon as new object are created
    #__init__ is a keyword hence it has to be named like it is
    def __init__(self):
        self.start = 0
        self.boot_time = 4
    
    def increment_time(self):
        self.boot_time += 1

pc = Computer()
print(f"\nFirst object boot time: {pc.boot_time} s")

pc.increment_time()
pc.increment_time()

print(f"First object boot time after installing many programs on it: {pc.boot_time} s")


pc2 = Computer()
print(f"\nSecond object boot time: {pc2.boot_time} s")
