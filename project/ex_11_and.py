from delta import Compiler, Phase

source = '10 && 20 && 30'

c = Compiler('program')
c.realize(source, phase=Phase.CODE_GENERATION)
# print(c.parse_tree_str)
