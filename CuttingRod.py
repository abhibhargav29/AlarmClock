def rodCutting(price, n): 
    val = [0 for x in range(n+1)] 
    val[0] = 0
    
    #For each i make a max_vala nd store it in val array
    for i in range(1, n+1): 
        #Find max val by using the already present values for smaller numbers in the val array
        max_val = -1
        for j in range(i): 
             max_val = max(max_val, price[j] + val[i-j-1]) 
        val[i] = max_val 
  
    return val[n] 

arr = list(map(int, input().split()))
n = int(input())
print(rodCutting(arr,n))
