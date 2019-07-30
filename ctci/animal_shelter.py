# problem 3.6

class Animal:
    def __init__(self, animal, id):
        self.animal = animal
        self.id = id
        self.next = None
    def __str__(self):
        return 'Animal({}, {})'.format(self.animal, self.id)
    def __repr__(self):
        return self.__str__()

class EmptyShelterException(Exception):
    pass

class AnimalNotAvailableException(Exception):
    pass

class Shelter:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, animal, id):
        val = Animal(animal, id)
        if not self.head and not self.tail:
            self.head = val
            self.tail = val
        else:
            self.tail.next = val
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            raise EmptyShelterException
        else:
            val = self.head
            self.head = self.head.next
            return val

    def dequeueAnimal(self, animal):
        if not self.head:
            raise EmptyShelterException
        else:
            trailer = None
            cur = self.head
            while cur and cur.animal != animal:
                trailer = cur
                cur = cur.next
            if not cur:
                raise AnimalNotAvailableException
            if trailer:
                trailer.next = cur.next
            else:
                self.head = self.head.next
            return cur
