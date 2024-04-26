result = {}

for i in range(100):
   N = int(input())
   result[i] = N
  
h_result_key = max(result, key = result.get)

print(result[h_result_key])
print(int(h_result_key) + 1)
