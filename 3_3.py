n, m = map(int, input().split())
my_min = []

for i in range(n):
    my_min.append(min(list(map(int, input().split()))))

print(max(my_min))
