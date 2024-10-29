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
    "Amioun",
    "Akkar"
]


class Node:
    def __init__(self,info,n):
        self.info=info
        self.next=n

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 
        
    def addToHead(self,val):
        if self.size==0:
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,self.head)
            self.head=n
            self.size+=1
            
    def addToTail(self,val):
        if self.size==0:
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,None)
            self.tail.next=n
            self.tail=n
            self.size+=1
            
    def printLL(self):
        temp=self.head
        while temp!=None:
            print(" -> ",temp.info,end=" ")
            temp=temp.next
        print()

    def linkedListToList(self):
        temp=self.head
        list1 = []
        while temp!=None:
            list1.append(temp.info)
            temp=temp.next
        return list1

class Graph:
    def __init__(self,list1):
        self.list=[]
        self.cities = list1
        for i in range(len(self.cities)):
            self.list.append(LinkedList())
            
    def add_edge(self,n1,n2):#O(1)
        self.list[n1].addToHead(self.cities[n2])
        self.list[n2].addToHead(self.cities[n1])

        
    def print_graph(self): #O(v^2)
        for i in self.list: #O(v)
            i.printLL() #O(v)

    def print_neighbors(self, n1):
        print(f"{self.cities[n1]}:",end=" ")
        self.list[n1].printLL()
    
    def get_neighbors(self, n1):
        return self.list[n1].linkedListToList()

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
    def __init__(self, drivers, citiesList):
        self.drivers = drivers
        self.avCity = citiesList
        self.graph = Graph(self.avCity)

    def addCity(self, city):
        self.avCity.append(city)
        self.graph.list.append(LinkedList())
        r = input("Does the entered city has neighbor(YES):")
        r = r.upper()
        if r == "YES":
            while(1):
                c1 = input("Enter the neighbor city:")
                c1 = c1.capitalize()
                if c1 in self.avCity:
                    self.graph.add_edge(self.avCity.index(city), self.avCity.index(c1))
                else:
                    print("Invalid City")
                c = input("Enter Yes to add another neighbor: ")
                c = c.upper()
                if c != "YES":
                    break

    def addDriver(self):
        name = input("Enter Driver Name: ")
        sCity = input("Enter Driver Start City: ")
        sCity = sCity.capitalize()
        
        if len(drivers) > 0:
            idNB = int(drivers[-1].ID[2:]) + 1
            id = f"ID{idNB}"
        else:
            id = "ID1"
        
        if sCity not in self.avCity:
            result = input("If you wnat to add this city to dataBase type YES: ")
            result = result.upper()
            if result == "YES":
                self.addCity(sCity)
                drivers.append(Driver(id, name, sCity))
        else:
            drivers.append(Driver(id, name, sCity))            
        
def viewAllDrivers(deliveryCompany):
    # print(deliveryCompany.drivers[0].name)
    for driver in deliveryCompany.drivers:
        driver.displayDriver()

def addDriver(deliveryCompany):
    deliveryCompany.addDriver()

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
        return
    else:
        print("Invalid input")


def showCities(deliveryCompany):
    cities = sorted(deliveryCompany.avCity, reverse=True)
    print("Available Cities: ", end = "")
    for city in cities:
        print(city, end = ", ")


def searchCity(deliveryCompany):
    s = input("Search a city: ")
    print("Result:", end = " ")
    for city in deliveryCompany.avCity:
        if city.__contains__(s):
            print(city, end = ", ")

def printNeighboringCities(deliveryCompany):
    city = input("Enter City Name: ")
    if city in deliveryCompany.avCity:
        deliveryCompany.graph.print_neighbors(deliveryCompany.avCity.index(city))
    else:
        print("The entered city is not available")


def getAllCityNeighbor(deliveryCompany, city, s = []):
    l = deliveryCompany.graph.get_neighbors(deliveryCompany.avCity.index(city))
    l = list(set(l) - set(s))
    s.append(city)
    if len(l) > 0:
        for c in l:
            getAllCityNeighbor(deliveryCompany, c, s)
    return s

def printDriversDeliveringToCity(deliveryCompany):
    city = input("Enter the city you want get delivered in: ")
    city = city.capitalize()
    c = getAllCityNeighbor(deliveryCompany, city)
    if city in deliveryCompany.avCity:
        for driver in deliveryCompany.drivers:
            if driver.startCity in c:
                driver.displayDriver()

def cityMenu(deliveryCompany):
    print("Enter: ")
    print("\t 1. To show cities")
    print("\t 2. To search city") 
    print("\t 3. To print neighboring cities")
    print("\t 4. To print Drivers delivering to city")
    choise = int(input())
    if choise == 1:
        showCities(deliveryCompany)
    elif choise == 2:
        searchCity(deliveryCompany)
    elif choise == 3:
        printNeighboringCities(deliveryCompany)
    elif choise == 4:
        printDriversDeliveringToCity(deliveryCompany)
    else:
        print("Invalid input")

    
drivers = []
drivers.append(Driver("ID1", "Max Verstappen", "Tyre"))
drivers.append(Driver("ID2", "Charles Leclerc", "Batroun"))
drivers.append(Driver("ID3", "Lando Norris", "Batroun"))

deliveryCompany = DeliveryCompany(drivers, availableCities)
# g = Graph(DC.avCity)
# g.add_edge(availableCities.index("Akkar"),availableCities.index("Byblos"))
# g.add_edge(availableCities.index("Beirut"), availableCities.index("Byblos"))
# g.add_edge(availableCities.index("Sidon"), availableCities.index("Zahle"))

availableCities.sort(reverse=True)
print("Hello!", end = " ")
while(1):
    print("Please enter:")
    print("\t 1. To go to the drivers' menu") 
    print("\t 2. To go to the cities' menu") 
    print("\t 3. To exit the system")

    choise = int(input())
    if choise == 1:
        driverMenu(deliveryCompany)
    elif choise == 2:
        cityMenu(deliveryCompany)
    elif choise == 3:
        exit(0)
    else:
        print("Invalid input")