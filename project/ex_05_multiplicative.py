from delta import Compiler, Phase

source = '1 + 2 * 3 + 4 * 5'

c = Compiler('program')
c.realize(source, Phase.CODE_GENERATION)
# print(c.parse_tree_str)
print(c.wat_code)
# print(c.result)