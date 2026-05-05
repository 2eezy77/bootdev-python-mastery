# Exits loop after the conditional is met, otherwise it would've gone until the range() ended.
for n in range(50):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break
