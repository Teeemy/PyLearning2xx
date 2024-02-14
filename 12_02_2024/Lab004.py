# cntinue is an alternate of break

for num in range(1,10):
    if num % 2 == 0:  # all the numbers that will divide 2 without remainder from(1,10)
        print(f"Found Even number {num}")
        continue # if the condition is false, continue till it execute all the numbers
    print(f"Odd number {num}")
