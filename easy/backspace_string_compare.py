#My solution
#O(n + m) time, O(n + m) space
class Solution:
    #Strategy: Utilise a stack, popping from stack if we come across a backspace
    #Else, ensure the current char isn't a backspace, and push
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.stackify(s) == self.stackify(t)
        
    def stackify(self, word):
        s = []
        for letter in word:
            if letter == '#' and len(s):
                s.pop()
            elif letter != '#':
                s.append(letter)
        return s
    
#The O(n) time and O(1) space solution (not mine, just the concept)
class Solution:
    #Essentially, we start iterating from the back of both strings
    #We keep track of the number of '#'s, we come across. For each iteration, we will delete any necessary chars based on the number of backspaces we come across
    #At the end of this, we check if any of the iterators are negative(meaning there is no more word left) and the other is positive(there is still word left)
    #If this is true, we can return False immediately
    #Else, both iterators are at valid chars, and we verify they are the same, returning false if they are not
    #We do this until both iterators are empty (have iterated through both strings), and if we haven't already return false, return True
    def backspaceCompare(self, S, T):

        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0
        
        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break
            
            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break
            
            
            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a" 
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False
            
            si -= 1
            ti -= 1
        return True
