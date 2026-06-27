class Student:
    "Common base class for all student"
    
    def __init__(self, name=None, major=None, IP=None):
        self.name = name
        self.major = major
        self.IP = IP
        
    def getName(self):
        return self.name
        
    def getMajor(self):
        return self.major
        
    def getIP(self):
        return self.IP
        
    def setName(self,name):
        self.name = name
        
    def setMajor(self,major):
        self.major = major
        
    def setIP(self,IP):
        self.IP = IP
        
    def deleteData(self):
        self.name = None
        self.major = None
        self.IP = None

student = Student()

print("\n===== OOP Program =====")
print("1. Declare Object")
print("2. Display Object")
print("3. Change Object Value")
print("4. Delete Object")
print("5. Exit Program")

while True:
    menu = input("Enter Menu (1|2|3|4|5): ")
    
    if menu == "1":
        name = input("Enter Name: ")
        major = input("Enter Major: ")
        IP = float(input("Enter IP: "))
        student = Student(name, major, IP)
        print("Data Successfully Added")

    elif menu == "2":
        studentName = student.getName()
        print("Name:", studentName)
        studentMajor = student.getMajor()
        print("Major:", studentMajor)
        studentIP = student.getIP()
        print("IP:", studentIP)

    elif menu == "3":
        change = input("What would you like to change (Name/Major/IP): ")
       
        if change == "Name": 
            new_name = input("Enter New Name: ")
            student.setName(new_name)
            print("Name Data Successfully Changed")
        
        elif change == "Major": 
            new_major = input("Enter New Major: ")
            student.setMajor(new_major)
            print("Major Data Successfully Changed")
      
        elif change == "IP": 
            new_IP = input("Enter New IP: ")
            student.setIP(new_IP)
            print("IP Data Successfully Changed")
        
        else:
            print("invalid change")
            
    elif menu == "4":
        student.deleteData()
        print("Data Successfully Deleted")
        
    elif choice == "5":
        print("Thank you for using my program.")
        break

    else:
        print("Invalid Menu")