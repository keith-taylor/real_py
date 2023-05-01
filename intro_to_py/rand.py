import random

heads = 0
tails = 0
tosses = 10_000

def coinflip(iterations):
    head_count = 0
    tail_count = 0
    for i in range (iterations):
        if random.randint(0,1) == 0:
            head_count += 1
        else:
            tail_count += 1
    return (head_count, tail_count)


heads, tails = coinflip(tosses)

print(f"heads: {heads}")
print(f"tails: {tails}")