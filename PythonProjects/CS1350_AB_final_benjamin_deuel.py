class Student:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.grades = []
    
    def addGrade(self, grade):
        if not isinstance(grade, int) and not isinstance(grade, float): return False
        if grade < 0 or grade > 100: return False
        self.grades.append(grade)
        return True
    
    def getAverage(self):
        if self.grades == []: return 0
        total = sum(self.grades)
        return total / len(self.grades)
    
    def getStatus(self):
        if self.grades == []: return "No grades"
        avg = self.getAverage()
        if avg >= 70: return "Passing"
        return "Failing"

'''
student = Student("Alice", "12345")
print(student.addGrade(85))
print(student.addGrade(92))
print(student.addGrade(150))
print(student.getAverage())
print(student.getStatus())
'''

def safeGetElement(lst, ind, default=None):
    if not isinstance(lst, list): return default
    if not isinstance(ind, int): return default
    if ind < 0 or ind >= len(lst): return default
    
    try: val = lst[ind]
    except IndexError: print("Error: index out of range"); return default
    except TypeError: print("Error: incorrect type provided"); return default
    except Exception: print("Error: other error occured"); return default
    return val

'''
print(safeGetElement([1, 2, 3], 1))
print(safeGetElement([1, 2, 3], 10, -1))
print(safeGetElement("N/A", 0, -1))
'''

def powerRecursive(x, n):
    if n == 0: return 1
    if n <= 1: return x * n
    return x * powerRecursive(x, n-1)

'''
print(powerRecursive(2, 3))
print(powerRecursive(5, 2))
print(powerRecursive(10, 0))
print(powerRecursive(3, 4))
'''

import os, shutil

def getFileStats(path):
    stats = {"lines": 0, "words": 0, "characters": 0}
    lines = []

    try:
        with open(path, "r") as file:
            lines = file.readlines()
    except Exception:
        return None
    
    stats["lines"] = len(lines)
    stats["characters"] = sum([len(l) for l in lines])
    stats["words"] = sum([len(" ".join(l.split(" ")).split(" ")) for l in lines])
    return stats

'''
print(getFileStats("C:\\Users\\BDDeuel01\\Downloads\\PythonProjects\\PythonProjects\\contacts.py"))
'''

def analyzeSales(sales):
    data = {"total_revenue": 0, "high_value": 0, "low_stock": 0, "average_price": 0}

    if not isinstance(sales, list): return None
    if sales == []: return None

    data["total_revenue"] = sum(list(map(lambda x: x["quantity"] * x["price"], sales)))
    data["high_value"] = list(map(lambda y: y["product"], list(filter(lambda x: (x["quantity"] * x["price"]) > 100, sales))))
    data["low_stock"] = list(map(lambda y: y["product"], list(filter(lambda x: x["quantity"] < 10, sales))))
    data["average_price"] = sum(list(map(lambda x: x["price"], sales))) / len(sales)
    return data

'''
sdata = [
    {"product": "Widget", "quantity": 5, "price": 25.00},
    {"product": "Gadget", "quantity": 15, "price": 10.00},
    {"product": "Tool", "quantity": 1, "price": 50.00}
]

print(analyzeSales(sdata))
'''