#1151 - Easy Fibonacci

N = int(input())

Result = [0,1]

for i in range(2, N):
    Result.append(Result[i - 1] + Result[i -2])
  
print(*Result)
