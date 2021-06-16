import math

class Prime:
    def findLargeFactor(source:int)->int:
        def isPrime(source:int)->bool:
            for factor in range(2,int(math.sqrt(source)+1)):
                if source%factor==0:
                    return False
            return True

        for candidate in range(int(math.sqrt(source)),1,-1):
            if source%candidate==0 and isPrime(candidate):
                return candidate
        return 1
    print (findLargeFactor(600851475143))