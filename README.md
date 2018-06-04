# Ruolin's Leetcode Practice NoteBook
A repo for Ruolin's LC practice

## Array

### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)
```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        max_product_ending_i = min_product_ending_i = max_product = nums[0]
        for i in range(1, len(nums)):
            prev = [max_product_ending_i*nums[i], min_product_ending_i*nums[i] , nums[i]]
            max_product_ending_i = max(prev)
            min_product_ending_i = min(prev)
            max_product = max(max_product_ending_i, max_product)
        
        return max_product
                                        
```
Template for subarray DP problem. 

Use the though of `max_ending_here` DP. It is a similar problem to "Max sub array". 

### [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)
```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        
        for _ in range(rowIndex):
            res = [x+y for x,y in zip([0]+res, res+[0])]
        
        return res
```
VERY GOOD PROBLEM.
Use 0 as a padding number for each row.

Use `zip()` to compose each numbers from previous row. Very smart.

### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        p = nums[0]
        for i in range(1, len(nums)):
            res[i] = p
            p *= nums[i]
        
        p = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i]  *= p
            p *= nums[i]
                
        return res
```
Calculate products from start to end and then from end to start without considering `n[i]` at `i` position
### [667. Beautiful Arrangement II](https://leetcode.com/problems/beautiful-arrangement-ii/description/)
```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        nums = [1] * n
        
        diff = k
        for i in range(1, k+1):
            if i % 2 == 1:
                nums[i] = nums[i-1] + diff
            else:
                nums[i] = nums[i-1] - diff
            diff -= 1
        for i in range(k+1, n):
            nums[i] = (i+1)
                
        return nums
```
We firstly satisfy the condition of k different differences. Then we append rest of numbers.

## Two Pointer

### [18. 4Sum](https://leetcode.com/problems/4sum/description/)

```python 
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.NSum(nums, target, 4, [], results)
        
        return results
        
    def NSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        
        if N == 2:
            l,r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] 
                if s == target:
                    
                    results.append(result + [nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]: # Remove the replicate results
                        l += 1 
                    while l < r and nums[r] == nums[r+1]:  # Remove the replicate results
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            
        else:
            for i in range(len(nums)-N+1):
                if target < N*nums[i] or target > N*nums[-1]: # Avoid unnecessary search. 
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.NSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
                    
        return 
                    
                
            
```
Template. Very good solution 
Sort the list, then reduce the problem to 2Sum by backtracking. 

### [27. Remove Element](https://leetcode.com/problems/remove-element/description/)
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
            else:
                i += 1
        return i
```
Remember to use '<=' in the loop of two pointer algorithms. 

## Hashtable

### [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

```python 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = collections.Counter(nums).most_common(k)
        
        return [x[0] for x in res]
```
Use `most_common` after `Counter`

### [454. 4Sum II](https://leetcode.com/problems/4sum-ii/description/)
```python 
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a+b for a in A for b in B)
        
        return sum(AB[-c-d] for c in C for d in D)
        
```
Remember of usage of `collections.Counter`

The idea is to use hashtable and count all possible sum (a+b)values of AB elements, and then find all negative sums (-c-d) of CD that equal to the hashed sum of AB. For each time we find a match `AB[-c-d]`, we add the value of `AB[-c-d]` to our returned count. 

### [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_sum = 0
        count = 0
        _hash = {0:1} # hash 0 elements' sum
        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - k
            if diff in _hash:
                count += _hash[diff]
                
            if cur_sum in _hash:
                _hash[cur_sum] += 1
            else:
                _hash[cur_sum] = 1
                
        return count
                                     
```
We want to find subarrays that are added to `k`. 

Use hash table to store all cumulative sums, and then use `cur_sum[j] - cur_sum[i]` to find sums ending at `j`. Then for any `j`, if there are `y` `cur_sum[i]` such that `cur_sum[j] = cur_sum[i] - k`, then there will be `y` sums ending at `j` equals to k. 


### [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/)
```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = {},{}
        for i,x in enumerate(nums):
            start.setdefault(x,i)
            end[x] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        
        return min(end[x] - start[x] + 1 for x in c if c[x] == degree)

```
`dict.setdefault(x,i)` adds an element only if they key does not exist.

`collections.Counter(nums)` returns a dict that counts elements' frequency. Each entry is `{'element':count}`

### Contains Duplicate II
```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i,x in enumerate(nums):
            if x in d and i-d[x] <= k:
                    return True
            d[x] = i
        
        return False
```
## Dynamic Programming 

### [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/)

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-j-1]
        
        return res[n]
             
```
The idea is based on [this](https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)). 



## Backtracking

### [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

```python
class Solution(object):
    def letterCombinations2(self, digits): # Iteration
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':'abc', 
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        if len(digits) == 0:
            return []
        
        res = ['']
        for x in digits:
            letters = mapping[x]
            new_res = []
            for r in res:
                for l in letters:
                    new_res += [r + l]
            res = new_res
            
        return res
    def letterCombinations(self, digits): # Recursion
        mapping = {'2':'abc', 
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        def recurr(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return list(mapping[digits[0]])
            letters = mapping[digits[0]]
            res = []
            for l in letters:
                tail = recurr(digits[1:])
                for x in tail:
                    res.append(l+x)
            return res
        return recurr(digits)
    
```



### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)
```python
class Solution:
    def generateParenthesis(self, n):
        def recur(n):
            if n==1: return set(["()"])
            
            res = set()
            for x in recur(n-1):
                for i in range(len(x)):
                    res.add(x[:i] + "()" + x[i:])
            
            return res
        return list(recur(n))
        
            
```
Recursion solution


[47. Permutations II](https://leetcode.com/problems/permutations-ii/description/)
```python
class Solution(object):
    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recur(nums):
            if len(nums) == 1: return [nums]
            dup = set()
            res = []
            for i in range(len(nums)):
                if nums[i] in dup:
                    continue
                dup.add(nums[i])
                for x in recur(nums[:i] + nums[i+1:]):
                    res.append([nums[i]] + x)
            
            return res
            
        return recur(nums)
    
    def permuteUnique(self, nums): # Top-Down Recursion
        
        res = []
        def recur(nums, temp, result):
            if len(nums) == 0:
                result.append(temp)
                return
            dup = set()
            for i in range(len(nums)):
                if nums[i] in dup:
                    continue
                dup.add(nums[i])
                recur(nums[:i] + nums[i+1:],  temp + [nums[i]], result)
           
        recur(nums, [], res)
        return res
```

Recursion solution. Also use TOP-DOWN recursion. 

### [46. Permutations](https://leetcode.com/problems/permutations/description/)

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def per(nums):
            if len(nums) == 1: return [[nums[0]]]
            res = []
            for i,x in enumerate(nums):
                for s in per(nums[:i]+nums[i+1:]):
                    res += [[x] + s]
            return res
        return per(nums)
        
```

### [77. Combinations](https://leetcode.com/problems/combinations/description/)
```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        x = 1
        temp = []
        res = []
        while True:
            if len(temp) == k:
                res.append(temp[:])
            if len(temp) == k or x > n - k + len(temp) + 1: # cut search space by stop searching if there are not enough numbers
                if not temp:
                    return res
                x = temp.pop() + 1 # General rule: if the return temp condition is not met, just break the condition without inserting node to the temp. Don't insert new node to the temp here. Insert in next iteration
            else:
                temp.append(x) 
                x += 1 
        
        
```
Backtracking model template. 

See comment for cutting search space technique


### [401. Binary Watch](https://leetcode.com/problems/binary-watch/description/)
```python
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(0,12):
            for m in range(0, 60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append('%d:%02d' % (h,m))
        return res
```
Try all different times and return the one with `num` number of `1`.

It is a reverse thinking of solving problem. We work from time to binary, not from binary to time. 

### [78. Subsets](https://leetcode.com/problems/subsets/description/)

```python 
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for x in nums:
            res += [[x] + i for i in res]
        return res
```     
GOOD PROBLEM. Remember this formula for generating all possible combinations.           

### [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/description/)
```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i,X):
            if i == 1:
                return 1
            
            return sum(count(i-1,X-{x}) for x in X if x % i == 0 or i % x == 0)
        return count(N, set(range(1,N+1)))
                
```

Trick: lower ith is likely to contain "beautiful" value, so we run backwards so we can eliminate "unbeautiful" chains faster. This makes our search space smaller. 


## Math
### [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = lambda x,y: x*y
        return max(reduce(f, heapq.nlargest(3, nums)), reduce(f, heapq.nsmallest(2, nums) + heapq.nlargest(1, nums)))

```
`heapq.nlargest(n, nums)` is `O(n*nums)`. It means that it can be `O(n)` if n is a constant and nums is `n`.

## Linked List

### General Rules
In most cases, use 'while cur' in the loop condition, but if `cur = cur.next.next...` is possible in the loop, use 'while cur and cur.next'

### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
```python 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dum = ListNode(0)
        dum.next = head
        slow = dum
        fast = dum.next
        while fast and fast.next:
            if fast is slow: return True
            slow = slow.next
            fast = fast.next.next
        
        return False
```
Use slow-fast pointers approach for linked list cycle problems to avoid additional memory cost

### [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dum = ListNode(0)
        dum.next = head
        slow = dum
        fast = slow.next
        
        found_cycle = False
        while fast and fast.next:
            if fast is slow:
                found_cycle = True
                break
            fast = fast.next.next
            slow = slow.next
        
        if not found_cycle:
            return None
        
        slow = slow.next 
        while not (slow is dum):
            dum = dum.next
            slow = slow.next
            
        return dum
            
```
See (https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation).

This is a Math problem. Drawing the graph makes the solution easier to understand. 

If Slow has moved `k` steps, then Fast has moved `2k+1` steps (it starts at the second node). If they meet at this position, we know `k+nc = 2k + 1` where `c` is the length of the cycle and `n` is an integer and `n>=0`. Then `k = nc-1`. Let `k=a+b` where `a` is the distance between the start of the list to the start of the cycle. Then `a = nc - b - 1` where `nc - b` is the distance between meeting point and the start of the cycle (the distance of the "other side" curve of the cycle). 

### [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dum = ListNode(0)
        dum.next = head
        prev = dum
        while head and head.next: # head and head.next
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dum.next
            

```
use both `head` and `head.next` in the while loop condition if `head` could be assigned by `head.next.next` in the loop.

### [817. Linked List Components](https://leetcode.com/problems/linked-list-components/description/)
```python 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents2(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        comp = []
        cur = head
        prev_val = -1
        count = 0
        while cur:
            if cur.val in g and (len(comp) == 0 or comp[-1] == prev_val):
                comp.append(cur.val)
            else:
                if len(comp) > 0: 
                    count += 1
                comp = []
            prev_val = cur.val
            cur = cur.next
        if len(comp) > 0:
            count += 1
            
        
        return count
    
    def numComponents(self, head, G): # better solution
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res

```
See the better solution. 
Its idea is to count when the condition we cannot build larger component and we don't need to store each component in this problem. 


### [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        previous_node = None
        while current_node:
            next_temp = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_temp
        return previous_node
            
            
```
Template for reversing linked lists. 

## Binary Search

### [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a,b = 0, len(nums) - 1
        while a<=b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                b = m-1
            else:
                a = m+1
        
        return a 
```
Template for binary search insertion. Pay attention to `<=`.

The return value is `a` not `m`. 

## Divide and Conquer

### [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)
```python
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        res = []
        for i, x in enumerate(input):
            if x in'+-*':
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute(input[i+1:])
                for x1 in a:
                    for x2 in b:
                        if x == '+':
                            res.append(x1+x2)
                        elif x == '-':
                            res.append(x1-x2)
                        else:
                            res.append(x1*x2)
        return res
    
            
```
Divide and Conquer example.



### [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)

```python 
    def searchMatrix(self, matrix, target):
        
        top,right = 0, len(matrix[0]) - 1
        top_bound = len(matrix) - 1
        
        while top <= top_bound and right >= 0:
            if matrix[top][right] == target:
                return True
            elif matrix[top][right] > target:
                right -= 1
            else:
                top += 1
        return False 
```
Rule out ineligible rows and columns

## String

### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return len(s)

        slow,fast = 0,0
        _hash = {}
        max_len = 1
        while fast < len(s):
            if s[fast] in _hash and slow <= _hash[s[fast]]:
                slow = _hash[s[fast]] + 1
            else:
                max_len = max(max_len, fast - slow + 1)
            _hash[s[fast]] = fast
            fast += 1
  
        return max_len
```
`_hash` maps from character to its index. `slow` then uses index of previous repeated character to jump.  

Template: This jumping with index is a template


### [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)

```python 
class Solution(object):
    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split(' ')
        res = []
        for word in sl:
            res += list(word)[::-1] + [' ']
        
        return "".join(res[:-1])
    
    def reverseWords(self, s): # One line version, faster. 
        return ' '.join(x[::-1] for x in s.split())
```
`join` joins strings with given delimiter. 

### [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/description/)

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        res = ['' for i in range(numRows)]
        movingDown = True
        i = 0
        step = -1
        for x in s:
            res[i] += x
            if i == len(res) - 1 or i == 0:
                step *= -1
                
            if movingDown:
                i += step
            else:
                i -= step
                
        return "".join(res)
```
Use `+=` to append character to a string. It is also fast. 

Use `step` and `step *= -1` to reverse the moving direction. 

### [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index = []
        for l in letters:
            if s.count(l) == 1:
                index += [s.index(l)]
        return min(index) if len(index) > 0 else -1
```
Use `count`


## String

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)
```python
class Solution(object):
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram(self, s, t):
            return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
```
Example usage of `all`. 

It is also normal to see that we use alphabet to search and check chars in strings. 

## Tree

### [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/description/)
```python 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findDuplicateSubtrees(self, root): 
        
        def hash_tree(root):
            if not root:
                return None
            tree_id = (hash_tree(root.left), root.val, hash_tree(root.right))
            count[tree_id].append(root)
            return tree_id
        
        count = collections.defaultdict(list)
        hash_tree(root)
        return [nodes.pop() for nodes in count.values() if len(nodes) >= 2]
        
        
            
```
This is how do we hash a tree.
### [449. Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)
```python 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        stack = [root]
        res = []
        while stack:
            x = stack.pop()
            res.append(str(x.val))
            
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        
        return ' '.join(res)
                
            
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(int(s) for s in data.split())
        def build(min_val, max_val):
            if queue and min_val < queue[0] < max_val:
                root = TreeNode(queue.popleft())
                root.left = build(min_val, root.val)
                root.right = build(root.val, max_val)
                return root
            return None
        return build(float('-inf'), float('inf'))
                
```
See function `build`. It is an O(n) way to build a binary search tree given a string from pre-ordered tree traversal. 




### [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

```python 
    def preorderTraversal(self, root):
        
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            x = stack.pop()
            
            res.append(x.val)

            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        return res
```
Use stack to do the preorder traversal. 

### [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

```python 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym(a,b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            
            return a.val == b.val and sym(a.right, b.left) and sym(a.left, b.right)
        
        if not root:
            return True
        else:
            return sym(root.left, root.right)
        
```

### [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/description/)

```python 
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(values):
            if len(values) == 1:
                return [TreeNode(values[0])]
            if len(values) == 0:
                return []
            
            res = []
            for i, x in enumerate(values):
                left_set = generate(values[:i])
                right_set = generate(values[i+1:])
                
                if len(left_set) == 0: # 
                    for r in right_set:
                        node = TreeNode(x)
                        node.right = r
                        res.append(node)
                        
                elif len(right_set) == 0:
                    for l in left_set:
                        node = TreeNode(x)
                        node.left = l
                        res.append(node)                
                else:
                    for l in left_set: 
                        for r in right_set:
                            node = TreeNode(x)
                            node.left = l
                            node.right = r
                            res.append(node)
            
            return res
        
        return generate(range(1,n+1))
```
Example of how to take cartesian product of two lists (`left_set` and `right_set`)

## Heap

### [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

```python
class Solution(object):

    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]
```
Use `heapq`
