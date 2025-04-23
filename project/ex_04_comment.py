from delta import Compiler

source = '''
    // A line comment.

    1+2+3
    
    /* 
    A block
    comment.
    */
    -
    3
'''

c = Compiler('program')
c.realize(source)
print(c.result)
