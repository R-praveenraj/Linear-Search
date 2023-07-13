#Given an array A and an integer B, find the number of occurrences of B in A.

def linearsearch(A,B):
    count=0
    for i in A:
        if i==B:
            count+=1

    return count

A = [1, 2, 2]
B = 2 

print(linearsearch(A,B))