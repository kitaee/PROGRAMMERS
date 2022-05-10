def solution(price, money, count):
    for k in range(1,count+1):
        money -= (price*k)
    if(money>=0):
        return 0
    else:
        return -money
