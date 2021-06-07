class Solution(object):
    def suggestedProducts(self, products, searchWord):
        
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        check = sorted(products)
        result = []
        for update in range(1,len(searchWord)+1):
            #limit it to 3 elements each time
            early = False
            insertNum=0
            temp = []
            for word in check:
                if word.startswith(searchWord[:update]):
                    temp.insert(insertNum,word)
                    insertNum+=1
                    
                if insertNum==3:
                    result.insert(update,temp)
                    early = True
                    break
            if early == False:
                result.insert(update,temp)
                    
        return result
                    
        