from delta import Compiler, Phase

source = '+ - ! ! 2'

c = Compiler('program')
c.realize(source)
# print(c.parse_tree_str)
# print(c.wat_code)
print(c.result)
