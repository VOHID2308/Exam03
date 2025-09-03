class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        return (self.hours, self.minutes) < (other.hours, other.minutes)



t1 = Time(10, 30)
t2 = Time(12, 15)
print(t1 < t2)   
