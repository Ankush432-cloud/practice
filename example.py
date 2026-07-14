# function for add two number.
class operation :
    def add(self,a,b):
        self.c = a + b
        return self.c
    
    def sub(self,p,q):
        self.r= p-q
        return self.r
    
    def mul(self,f,d):
        self.e = f * d 
        return self.e

obj = operation()

result = obj.add(a=10 , b= 100)
result2 = obj.sub(p=20, q=10)
result3 = obj.mul(f=12 , d=10)

print(result)
print(result2)
print(result3)


