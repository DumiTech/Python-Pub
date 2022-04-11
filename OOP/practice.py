class MaxSizeList(object):
    def __init__(self, value):
        self.myList = []
        self.value = value

    def push(self, text_input):
        try:
            text_input = str(text_input)
            self.myList.append(text_input)
        except ValueError:
            print("You can only push strings!")

    def getList(self):
        print(self.myList[-self.value:])

if __name__ == '__main__':
    a = MaxSizeList(2)
    b = MaxSizeList(5)

    a.push('Ola ')
    a.push('Python ')

    b.push('are ')
    b.push('you ')
    b.push('the ')
    b.push('best ')
    b.push('language? ')

    a.getList()
    b.getList()