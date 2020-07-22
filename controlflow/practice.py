#code
import sys

test_cases = input()
if not test_cases.isdigit():
    sys.exit(1)
else:
    t = int(test_cases)

if not(t > 0 and t <= 200):
    sys.exit(1)
cases = []
for i in range(t):
    n = input()
    if not n.isdigit():
        sys.exit(1)
    else:
        n = int(n)
    cases.append(n)

for case in cases:
    print(case**3+case)
