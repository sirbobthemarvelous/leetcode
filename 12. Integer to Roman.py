class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        while(num>999):
            answer += "M"
            num -= 1000
        if(num>99):
            if(num>899):
                answer+= "CM"
                num-=900
            elif(num>=400 and num<=499):
                answer+= "CD"
                num-=400
            elif(num >499):
                answer+= "D"
                num-=500
            while(num>99):
                answer+= "C"
                num-=100
        if(num>9):
            if(num>89):
                answer+= "XC"
                num-=90
            elif(num>=40 and num<=49):
                answer+= "XL"
                num-=40
            elif(num >49):
                answer+= "L"
                num-=50
            while(num>9):
                answer+= "X"
                num-=10
        if(num==9):
            answer+="IX"
            num -= 9
        elif(num==4):
            answer+="IV"
            num-=4
        elif(num>4):
            answer+="V"
            num-=5
        while(num>0):
            answer+= "I"
            num-=1
        #make a program focusing on digits
        return answer