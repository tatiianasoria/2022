#################################################
# hw0.py
#
# Nombre:tatiana soria
# DNI: 36178477
#################################################

#################################################
# Funciones que tenés que programar
#################################################

def hello_world():
# Modificar este código para que devuelva el string "Hello World!"
    
    return "Hello World!"




#################################################
# Funciones de Test (no modificar)
#################################################

def test_hello():
    print('Testeando testHelloWorld()... ', end='')
    assert hello_world() == "Hello World!"
    print('Pasó!')

#################################################
# main
#################################################

def main():
    test_hello()   

if __name__ == '__main__':
    main()
