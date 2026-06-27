class student:
    "Common base class for all student"
    
    def __init__(self, name="Student", major="Computer Science", IP="3.5"):
        self.name = name
        self.major = major
        self.IP = IP
        
    def displayStudent(self):
        print("\n----- Student Biodata -----")
        print("Name:", self.name)
        print("Major:", self.major)
        print("IP:", self.IP)

name = input("Enter Name: ")
major = input("Enter Major: ")
IP = input("Enter IP: ")


student1 = student(name,major,IP)

student1.displayStudent()
