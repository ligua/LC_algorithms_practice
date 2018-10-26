class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n > 1:
                    return False
                else:
                    return True
            else:
                return n == 0
        if n == 0:
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
                
                
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            
        return n == 0