
import re
while True:
    
    expresion = r'([a-z]+||[0-9]+)(\@)([a-z]+||[0-9]+)(\.)([a-z]+)'
    resultado = re.compile(expresion)
    prueba = raw_input("entrada: ")
    busqueda = re.search(resultado,prueba)
    if prueba=="":
        break
    if busqueda:
        print "qA"
        print prueba
    else:
        print "qr"
