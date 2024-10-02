'''LC Que. 345 Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['A','E','I','O','U','a','e','i','o','u']
        fl=list(s)
        left,right=0,len(fl)-1
        while left<=right:
            if fl[left] in l and fl[right] in l:
                fl[left],fl[right]=fl[right],fl[left]
                left+=1
                right-=1
            elif fl[left] in l and fl[right] not in l:
                right-=1
            else:
                left+=1
        return ''.join(fl)

