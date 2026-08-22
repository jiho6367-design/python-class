class FourCal :
    def __init__(self,x,y) :
        self.x = x
        self.y = y 
    def __repr__(self):
          return f"FourCal({self.x}, {self.y})"
    def add(self):
        return self.x + self.y
    def mul(self):
            return self.x * self.y
    def sub(self):
            return self.x - self.y
    def div(self):
            return self.x / self.y   

class MoreFourCal(FourCal) :
      def pow(self):
            return self.x ** self.y
      
class SafeFourCal(FourCal) :
    def div(self):
        if self.y == 0 : 
                return 0
        else :
                self.x / self.y

if __name__ == "__main__" :  
    a = MoreFourCal(4,2)

    print(a.add())
    print(a.mul())
    print(a.sub())
    print(a.div())
    print(a.pow())

    b = SafeFourCal(4,0)

    print(b.add())
    print(b.mul())
    print(b.sub())
    print(b.div())


            