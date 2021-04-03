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


high = 10000
low = 0 
save = 0
guess = (high+low)//2
epsilon = 0.001
val2 = B/out


if val2 > 10000:
  guess = -1
else:
  while abs(guess - val2) > epsilon:
    if guess < val2:
      low = guess
    else:
      save = guess
      high = guess

    guess = (high+low)//2
  
    if guess == low:
      guess = save
      break 

T = guess






# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)