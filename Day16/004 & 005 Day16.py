#Object has attributes and methods

"""Attributes are the properties or data of an object while the methods are the
   operations that an object can perform"""

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric", "Water","Fire"])
table.align ="l"
print(table)
