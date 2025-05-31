from delta import Compiler, Phase

source = """
    var x, y;
    x = 5;
    if x - 5 {
        y = 1;
    } else if x * 0 {
        y = 2;
    } else {
        y = 4;
    }
    y
"""

c = Compiler('program')
c.realize(source, Phase.CODE_GENERATION)
# print(c.parse_tree_str)
# print(c.wat_code)
# print(c.result)