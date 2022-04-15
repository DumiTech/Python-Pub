class SuperClass(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print('Data:', self.data)

class SubClass(SuperClass): #Inhertiting from Data class
    def getTime(self):
        print('Time:', self.data)

if __name__ == '__main__':
    super = SuperClass(10)
    sub = SubClass(20)  #inherited Class -> Value passed to __init__of SuperClass (Base class)

    sub.getTime()
    super.getData()
    sub.getData()
