"""
Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""

class Computer(object):
    provider = "ATX8 MP"
    def get_info(self):
        print("\nBest computer in the field.")
        print("Processor Count: 16")
        print("Processor Speed: 4.9 GHz")
        print("Processor Socket: Sockel AM4\n")

class CPU(Computer):
    provider = "AMD"
    def get_info(self):
        print("Wattage: 105 watts")

if __name__ == '__main__':
    pc = Computer()
    processor = CPU()

    pc.get_info()
    processor.get_info()
    processor.get_info()
    print(processor.provider)