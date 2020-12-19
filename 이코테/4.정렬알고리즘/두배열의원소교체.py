def function(A,B,K):
    A.sort()
    B.sort(reverse=True)
    for i in range(K):
        if A[i]<B[i]:
            A[i],B[i]=B[i],A[i]
        else:
            break
    return sum(A)

if __name__ == "__main__":
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(function(A,B,K))