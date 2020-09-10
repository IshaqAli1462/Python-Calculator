from operator import pow, truediv, mul, add, sub  

ops = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def calculate(s):
    if s.isdigit():
        return float(s)
    for c in ops.keys():
        left, op, right = s.partition(c)
        if op in ops:
            return ops[op](calculate(left), calculate(right))

calc = input("Type calculation:\n")
print("Answer: " + str(calculate(calc)))