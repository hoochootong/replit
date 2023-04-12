n, m = map(int, input().split())
arr = []
max_val = 0
# for i in range(n):
#   l = list(map(int, input().split()))
#   max_val = max(max_val, min(l))
# print(max_val)  

max_val = 0
for i in range(n):
  l = list(map(int, input().split()))
  min_value = 10001
  for element in l:
    min_value = min(min_value, element)
  max_val = max(max_val, min_value)

print(max_val)

max_val = 0
for i in range(n):
  l = list(map(int, input().split()))