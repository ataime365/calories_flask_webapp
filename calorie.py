from temperature import Temperature

class Calorie:
    """ Represents the amount of calories calculated with
        BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        
    def calculate(self):
        result = 10*self.weight + 6.25*self.height - 5*self.age + 5 - self.temperature*10
        return result

if __name__ == "__main__":
    temperature = Temperature(country='italy', city='rome').get()
    temperature = int(temperature)
    calorie = Calorie(176, 68, 32, temperature)
    calorie_value = calorie.calculate()
    print(calorie_value)