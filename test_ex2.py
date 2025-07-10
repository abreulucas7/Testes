def primeiro_elemento(lista):
    if lista:
        return lista[0]
    return None 

def test_primeiro_elemento(): 
    assert primeiro_elemento(lista=['um','dois','tres']) == 'dois'

def test_primeiro_elemento2():
    assert primeiro_elemento(lista=None) == True