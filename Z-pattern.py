size = 7 
for i in range(size * size):
  row = i // size
  col = i % size
  if row==0 or row==size-1 or row+col == size-1:
    print("$", end="")
  else:
    print(" ", end="")

  if col == size-1:
    print()