n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

first = array[0]
second = array[1]

re = m//(k+1)
result = first * re * k
result += second * re
result += first * (m % (k+1))

print(result)
