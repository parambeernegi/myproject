# Dynamic programming and greedy algorithm
# cut rod problem


# given length of rode is n inches and a table of prices pi fro i from 1 to n
# comupute the maximum revenue rn obtainable by cutting up th e rod and  selling the pieces,


    if n==0:
         return 0
    q=-1    
    for i in range(1,n):
        q=max(q,p[i]+cut_rod(p,n-i))
    return q
     
print(cut_rod([10],3))
