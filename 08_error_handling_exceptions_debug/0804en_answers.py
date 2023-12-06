# Intentionally Buggy Countdown Timer

countdown = 10

while countdown > 0:  # Bug 1: The condition should be countdown > 0
    print(countdown)
    countdown -= 1    # Bug 2: It should decrement countdown by 1

print("Blast Off!")  # Bug 3: It should print "Blast Off!"
