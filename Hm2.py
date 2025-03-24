import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 500

    def to_study(self):
        print("Time to study")
        self.progress += 0.2
        self.gladness -= 7
        self.money -= 25

    def work(self):
        if self.money > 100:
            pass
        elif self.money < 100:
            print("Time to work")
            self.gladness -= 2.5
            self.money += (random.randint(500,1000))

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += (random.randint(1,10))
        self.progress -= 0.1
        self.money -= 10

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= -3:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 0:
            print("Died of hunger")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:*^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")
bohdan = Student(name="Bohdan")
for day in range(3650):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
    if bohdan.alive == False:
        break
    bohdan.live(day)