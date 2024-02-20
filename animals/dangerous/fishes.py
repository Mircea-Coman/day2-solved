class Fishes:
    def __init__(self):
        self.members = ['Shark', 'Piranha', 'Pufferfish']

    def printMembers(self):
        print('Printing members of the dangerous.fish class')
        for member in self.members:
            print('\t%s ' % member)
