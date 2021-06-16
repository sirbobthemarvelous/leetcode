class Evenly:
    def fibonacci2(term1:int, term2:int) -> int:
        return term1+term2
    first = 0
    second = 1
    total = 0
    while fibonacci2(first,second)<4000000 :
        third = fibonacci2(first,second)
        if third%2==0:
            total += third
        first = second
        second = third
    print (total)

