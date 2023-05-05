#Solves longest subsequence problem using memoization
#references: GeeksForGeeks, class slides
#version: 5/4/23

def solveLCS(sub1, sub2, memo):

    #check to see if problem has been solved already 
    if (sub1, sub2) in memo:
        return memo[(sub1, sub2)]

    # check to make sure strings are not null
    if not sub1 or not sub2:
        memo[(sub1, sub2)] = ''
        return ''

    # use recursion to sort through each character 
    if sub1[-1] == sub2[-1]:
        memo[(sub1, sub2)] = solveLCS(sub1[:-1], sub2[:-1], memo) + sub1[-1]
        return memo[(sub1, sub2)]
    else:
        lcsub1 = solveLCS(sub1[:-1], sub2, memo)
        lcsub2 = solveLCS(sub1, sub2[:-1], memo)
        memo[(sub1, sub2)] = lcsub1 if len(lcsub1) > len(lcsub2) else lcsub2
        return memo[(sub1, sub2)]

# memo dict to hold already computed values
memo={}

#sequences
sub1 = "AGGTAB"
sub2 = "GXTXAYB"

#test
print(solveLCS(sub1, sub2))
