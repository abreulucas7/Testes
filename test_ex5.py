def eh_par(n):
    return n % 2 == 0 

def test_eh_par():
    assert eh_par(2) == True 

def test_eh_par2():
    assert eh_par(3) == False