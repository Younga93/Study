class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big <= 0:
                return False
            else:
                self.big -= 1
                return True
        elif carType == 2:
            if self.medium <= 0:
                return False
            else:
                self.medium -= 1
                return True
        elif carType == 3:
            if self.small <= 0:
                return False
            else:
                self.small -= 1
                return True
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

input1 = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
input2 = [[1, 1, 0], [1], [2], [3], [1]]
obj = ParkingSystem(1,1,0)
print(obj.big)
print(obj.medium)
print(obj.small)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))


