n = input('')
m = input('')
arr = []
evens = 0
odds = 0
split_m = m.split(' ')

for i in split_m:
    arr.append(int(i))

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        evens += arr[i]
    else:
        odds += arr[i]

print(abs(evens - odds))