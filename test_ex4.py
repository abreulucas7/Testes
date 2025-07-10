def ordena_lista(lista):
    return sorted(lista) 

def test_ordena_lista():
    assert ordena_lista(lista=[4,2,3,1]) == [1,2,3,4]