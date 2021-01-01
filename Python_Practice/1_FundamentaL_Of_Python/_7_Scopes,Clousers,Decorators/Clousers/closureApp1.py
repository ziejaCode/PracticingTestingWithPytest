
# class that will take a paramether and to others and get average value from all numbers added
class Avarager:
    def __init__(self):
        self.numbers = []

    def add(self, num):
        self.numbers.append(num)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


# class is called
a = Avarager()
print(a.add(23))
print(a.add(10)) 
print(a.add(13))

# same functionality in closure
def aver():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = aver()
print(a(23))
print(a(10))
print(a(13))
print(a.__closure__)