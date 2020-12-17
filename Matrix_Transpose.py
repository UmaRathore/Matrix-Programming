# Transpose Matrix with user defined Rows and Columns along with values


rows = int(input("Enter number of rows for matrix : " ))
cols = int(input("Enter number of columns for matrix : "))

arr = [[0 for i in range(cols)] for j in range(rows)]
trr = [[0 for i in range(rows)] for j in range(cols)]

for r in range(rows):
  for c in range(cols):
      arr[r][c] = int(input("Enter matrix for element"+str(r)+str(c)+" :"))
      trr[c][r] = arr[r][c]

for y in arr:
  print(y)

print("Transpose")

for x in trr:
  print(x)

# End
