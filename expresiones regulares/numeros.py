import re
expresion = r'([0-9]+)'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda = re.search(resultado,prueba)
if busqueda:
    print "qA\nes un numero"
    print busqueda.group()
    
else:
    print "qr\n NO es un numero"
