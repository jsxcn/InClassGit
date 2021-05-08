class Person:
    def __init__(first, last):
        self.first = first
        self.last = last

@property
def fullname(self):
    return '{} {}'.format(self.first, self.last)