import re
cadena = "Hola a todos los itc de este grupo"

m = re.search(r'itc', cadena)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
    
m = re.search(r'irs', cadena)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
else:
    print(m)
    
m = re.match(r'hola', cadena, re.IGNORECASE | re.ASCII)
if m:
    print(m.span())
    print(m.string)
    print(m.group())