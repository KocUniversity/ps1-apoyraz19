n, B = list(map(int, input().strip().split()))
T = 0

# your code here
out = 0
power = n-1 

for i in range(1,n+1):
  if (i%2 == 0):
    val = (2**i)+1
  else:
    val = (3**i)+1

  val = val**power
  out += val
  power -= 1

val2 = B/out

if val2 > 10000:
  T = -1
else:
  for i in range(1,10000+1):
    if i > (val2):
      T += i
      break








# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)