# function for add two number.
class operation :
    def add(self,a,b):
        self.c = self.a + self.b
        return self.c
    
    def sub(self,p,q):
        self.r=self.p-self.q
        return self.r

obj = operation()

result = obj.add(a=10 , b= 100)
result2 = obj.sub(p=20, q=10)

print(result)
print(result2)


