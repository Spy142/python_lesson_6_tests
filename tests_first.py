def prost_int(N):
    if N<=0:
        print('Введите целое число от 1 до 1000')
        return False
    if N==1:return False
    if N==3:return True
    i = 2
    while i*i <= N and N % i != 0:
        i+=1
    # Мой первый вариант
    # answer = 0
    # for i in range(2,int((N // N**0.5)+1),1):
    #     if N % i == 0:
    #         answer = 0
    #         break
    #     else:
    #         answer = 1
    return i*i > N

def test_prost_chisla_1():
    assert prost_int(6) == False

def test_prost_chisla_2():
    assert prost_int(3) == True

def test_prost_chisla_3():
    assert prost_int(11) == True

def test_prost_chisla_4():
    assert prost_int(20) == False

def test_prost_chisla_5():
    assert prost_int(1) == False
