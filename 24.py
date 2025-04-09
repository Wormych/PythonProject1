class Vehicle:
    speed = 60
    __vin = ""

    def __init__(self, speed_from_user, vin_from_user):
        self.speed = speed_from_user
        self.__vin = vin_from_user

    def show_speed(self):
        print(f'Speed of vehicle: {self.speed}')

    def show_vin(self):
        print(f'VIN of vehicle: {self.__vin[0:3]}******')

    def get_vin(self):
        return f'VIN of vehicle: {self.__vin[0:3]}******'


class Bus(Vehicle):
    def __init__(self, speed_from_user, vin_from_user, decks_number_from_user):
        super().__init__(speed_from_user, vin_from_user)
        self.__decks_number = decks_number_from_user

    def print_info(self):
        print(f'Speed: {self.speed}, Decks: {self.__decks_number}, VIN: {self.get_vin()}')


bus = Bus(100, "Dubciuse8723", 2)
bus.print_info()
