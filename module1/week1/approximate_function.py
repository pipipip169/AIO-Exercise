#Calculate fractoria

def fractoria(n):
  """
  Calculates the factorial of a non-negative integer n.

  Args:
    n: The non-negative integer to calculate the factorial of.

  Returns:
    The factorial of n.
  """
  if n==0:
    return 1
  else:
    return n*fractoria(n-1)

#Calculate Maclaurin expansion

def maclaurin_expansion(fn=input("Input function name:"), x=input("Input x="), n=input("Input n=")):
  """
  Calculates the Maclaurin expansion of a given function up to the nth order.

  Args:
    fn: The name of the function to expand.
    x: The value at which to evaluate the expansion.
    n: The order of the expansion.

  Returns:
    The Maclaurin expansion of the function up to the nth order.
  """
  if not x.isnumeric() or not n.isnumeric():
    print("x and n must be a number")
    return
  n=int(n)
  x=float(x)
  sum=0 # Initialize sum to 0
  if fn=="sin": #sin
    for i in range(n):
      sum+=((-1)**i*x**(2*i+1))/fractoria(2*i+1)

  elif fn=="cos": #cos
    for i in range(n):
      sum+=((-1)**i*x**(2*i))/fractoria(2*i)
  
  elif fn=="sinh": #sinh
    for i in range(n):
      sum+=x**(2*i+1)/fractoria(2*i+1)

  elif fn=="cosh": #cosh
    for i in range(n):
      sum+=x**(2*i)/fractoria(2*i)
  else:
    print(f"{fn} is not supported")
  if fn in ("sin", "cos", "sinh", "cosh"):
    print(f"f{fn}({x})={sum}")


#testing
maclaurin_expansion()