# function for add two number.
class operation :
    def add(self,a,b):
        self.c = self.a + self.b
        return self.c
    
obj = operation()

result = obj.add(a=10 , b= 100)

print(result)