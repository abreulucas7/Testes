def inverte_string(s):
    return s[::-1] 

#def test_inverte_string():
    assert inverte_string("abcde") == "edcba" #Sem Erro 
    assert inverte_string("12345") == "54321" #Sem Erro 
    assert inverte_string("ABC") == "CBA" #Sem Erro 
    assert inverte_string("ABC") == "cba" #Erro 
    assert inverte_string("abc") == "CBA" #Erro
    assert inverte_string("abc123") == "123abc" #Erro
    assert inverte_string("abc123") == "321cba" #Sem Erro