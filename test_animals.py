# import animals
#
# m = animals.Mammals()
# m.printMembers()
#
# b = animals.Birds()
# b.printMembers()
#
# f = animals.Fishes()
# f.printMembers()

import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fishes()
dangerous_fish.printMembers()
