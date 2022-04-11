class Program:
    # Class attribute
    varX = 3
    varY = 9

    # Class method
    def calculus_local_scope(self, varX, varY):
        return self.varX * self.varY

    def calculus_global_scope(self, varX, varY):
        return varX * varY


varX = 1
varY = 2

firstObject = Program()
print(firstObject)  # object's memory hex
print(firstObject.varX, firstObject.varY)
print(firstObject.calculus_local_scope(varX, varY))
print(firstObject.calculus_global_scope(varX, varY))

print()

varX = 3
varY = 4

secondObject = Program()
print(secondObject)  # object's memory hex
print(secondObject.varX, firstObject.varY)
print(secondObject.calculus_local_scope(varX, varY))
print(secondObject.calculus_global_scope(varX, varY))
