class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Eagle', 'Ostrich', 'Cassowaries']


    def printMembers(self):
        print('Printing members of the dangerous.birds class')
        for member in self.members:
            print('\t%s ' % member)
