'''
Problem Statement: 
Given a String, find the length of longest substring without any repeating character.
'''

'''
OPTIMAL APPROACH USING HASHING:
TC = O(N) = SC
'''
def uniqueSubstrings(st) :
    # Write your code here.
    if st == "":
        return 0
    maxL = 0
    subs = {}
    p1 = 0
    i = 0
    while i < len(st):
        if st[i] in subs:
            p1 = max(subs[st[i]] + 1, p1)
            
        subs[st[i]] = i
        maxL = max(maxL, i - p1 + 1)
        i += 1
 
    return maxL

if __name__ == "__main__":
    s = 'abacdede'
    print("Length of longest substring without repeating characters is", uniqueSubstrings(s))