from faker import Faker


class Static_Device:

    def __init__(self):
        # Location
        self.__idDev = None
        self.__lat = None
        self.__lon = None
        self.__building = None
        fake = Faker()
        self.__name = fake.mac_address()


    # Getters
    def getIdDev(self):
        return self.__idDev

    def getLatitude(self):
        return float(self.__lat)

    def getLongitude(self):
        return float(self.__lon)

    def getBuilding(self):
        return self.__building

    def getName(self):
        return self.__name

    # Setters
    def setIdDev(self, idDev):
        self.__idDev = idDev

    def setLatitude(self, lat):
        self.__lat = lat

    def setLongitude(self, lon):
        self.__lon = lon

    def setBuilding(self, b):
        self.__building = b


class Smoke_detector(Static_Device):

    def __init__(self):
        super(Smoke_detector, self).__init__()
        self.__status = 0
        self.__type = 4

    # Getters
    def getType(self):
        return self.__type

    def getStatus(self):
        if self.__status == 0:
            return "OK"
        else:
            return "FIRE DETECTED"

    def getInfo(self):
        print("STATIC DEVICE INFO:")
        print("type = smoke_detector")
        print()
        print("STATUS:")
        print(self.getStatus())

    # Setters
    def setStatus(self, status):
        self.__status = status

    def jsonRegSmoke(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonSmoke(self):
        return {'id': self.getIdDev(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'status': self.getStatus()}


class WeatherStation(Static_Device):

    def __init__(self):
        super(WeatherStation, self).__init__()
        self.__id = None
        self.__temp = None
        self.__temp_unit = "C"
        self.__hum = None
        self.__hum_unit = "%"
        self.__air = None
        self.__air_unit = "hPa"
        self.__type = 5

    def set_temperature(self, t):
        self.__temp = t

    def set_humidity(self, h):
        self.__hum = float(h) * 100

    def set_air_pressure(self, a):
        self.__air = a

    def getType(self):
        return self.__type

    def get_info(self):
        print("Weather station:")
        print()
        print("Temperatura: %d C" % self.__temp)
        print("Humitat: %d %%" % self.__hum)
        print("Pressio aire: %d hPa" % self.__air)

    def jsonRegWheather(self):
        return {'name': self.getName(),
                'type': self.getType()}

    def jsonWeather(self):
        return {'id': self.getIdDev(),
                'latitude': self.getLatitude(),
                'longitude': self.getLongitude(),
                'temperature': self.__temp,
                'humidity': self.__hum,
                'air': self.__air}