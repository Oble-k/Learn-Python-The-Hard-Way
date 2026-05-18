# Composition
class Other(object):

    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(Parent):

    def __init__(self):
        self.other = Other()
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("_"*20)
dad.override()
son.override()
print("_"*20)
dad.altered()
son.altered()