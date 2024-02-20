class Fishes:
    def __init__(self):
        self.members = ['Shark', 'Tuna', 'Trout']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)
