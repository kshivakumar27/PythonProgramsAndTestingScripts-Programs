from abc import ABC,abstractmethod

class LTTS_Employee(ABC):
    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def mask(self):
        pass

    def lunch(self):
        print("have lunch")

class Hardware_Employees(LTTS_Employee):

    def security(self):
        print("use id cards")

    def mask(self):
        print("use cloth mask")

class Software_Employees(LTTS_Employee):
    def security(self):
        print("use id finger printer scanner")

    def mask(self):
        print("use n92 mask")

    def lunch(self):
        print("will take lunch in office")


h_emp = Hardware_Employees()
s_emp = Software_Employees()

h_emp.security()