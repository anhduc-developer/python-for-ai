class Person:
    def __init__(self, id, name, birth, gpa):
        self.id = id
        self.name = name
        self.birth = birth
        self.gpa = gpa
    def __str__(self):
        return f'{self.id} {self.name} {self.birth} {self.gpa:.2f}'
    
if __name__ == "__main__":
    a = Person(input(), input(), input(), float(input()))
    print(a)