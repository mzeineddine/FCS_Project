# We Deliver: A system for a delivery company 
# In your system, you should keep track of two things:  
availableCities = [
    "Beirut",
    "Tripoli",
    "Sidon",
    "Tyre",
    "Byblos",
    "Baalbek",
    "Zahle",
    "Jounieh",
    "Batroun",
    "Nabatieh",
    "Aley",
    "Halba",
    "Amioun"
]

# 1. The drivers that the company has, their worker ID, their name, and their start city. 
class Driver:
    def __init__(self, id, name, sCity):
        self.name = name
        self.ID = id
        self.startCity = sCity
    def displayDriver(self):
        print(self.ID, "\t",self.name, "\t", self.startCity)
# 2. The cities that the company delivers to and where the driver can go from that city.
class DeliveryCompany:
    def __init__(self, drivers):
        self.drivers = drivers
    def addDriver(self):
        name = input("Enter Driver Name: ")
        sCity = input("Enter Driver Start City: ")
        sCity = sCity.capitalize()
        
        if len(drivers) > 0:
            idNB = int(drivers[-1].ID[2:]) + 1
            id = f"ID{idNB}"
        else:
            id = "ID1"
        
        if sCity not in availableCities:
            result = input("If you wnat to add this city to dataBase type YES: ")
            result = result.upper()
            if result == "YES":
                availableCities.append(sCity)
                drivers.append(Driver(id, name, sCity))
                # print(availableCities)
        else:
            drivers.append(Driver(id, name, sCity))
        start(self)
            
        
def viewAllDrivers(deliveryCompany):
    # print(deliveryCompany.drivers[0].name)
    for driver in deliveryCompany.drivers:
        driver.displayDriver()
    start(deliveryCompany)

def addDriver(deliveryCompany):
    deliveryCompany.addDriver()
    start(deliveryCompany)

def getDriverName(driver):
    return driver.startCity

def checkSimilarDriver(deliveryCompany):
    deliveryCompany.drivers.sort(key = getDriverName)
    city = deliveryCompany.drivers[0].startCity
    print(city, end = ": ")
    for driver in deliveryCompany.drivers:
        if driver.startCity == city:
            print(driver.name, end = ", ")
        else:
            city = driver.startCity
            print("\n"+city, end = ": ")
            print(driver.name, end = ", ")
    print()

    # for city in availableCities:
    #     print(city, end = ": ")
    #     for driver in deliveryCompany.drivers:
    #         if driver.startCity == city:
    #             print(driver.name, end = ", ")    
    #     print("")
    start(deliveryCompany)

def driverMenu(deliveryCompany):
    print("Enter: ")
    print("\t 1. To view all the drivers ")
    print("\t 2. To add a driver") 
    print("\t 3. Check similar drivers")
    print("\t 4. To go back to the main menu")
    choise = int(input())
    if choise == 1:
        viewAllDrivers(deliveryCompany)
    elif choise == 2:
        addDriver(deliveryCompany)
    elif choise == 3:
        checkSimilarDriver(deliveryCompany)
    elif choise == 4:
        start(deliveryCompany)
    else:
        print("Invalid input")

def start(deliveryCompany):
    print("Hello! Please enter:")
    print("\t 1. To go to the drivers' menu") 
    print("\t 2. To go to the cities' menu") 
    print("\t 3. To exit the system")

    choise = int(input())
    if choise == 1:
        driverMenu(deliveryCompany)
    elif choise == 2:
        print("You will go to cities' menu")
    elif choise == 3:
        exit(0)
    else:
        print("Invalid input")
drivers = []
drivers.append(Driver("ID1", "Max Verstappen", "Tyre"))
drivers.append(Driver("ID2", "Charles Leclerc", "Batroun"))
drivers.append(Driver("ID3", "Lando Norris", "Batroun"))

DC = DeliveryCompany(drivers)

start(DC)