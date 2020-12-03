# complexity n^2
import sys
report = []
for line in sys.stdin.readlines():
    report.append(int(line.rstrip()))
report = sorted(report)

# 3SUM two pointers solution
for p in range(len(report) - 1):
    a = p + 1
    b = len(report) - 1
    while a != b:
        if report[p] + report[a] + report[b] == 2020:
            print(report[p] * report[a] * report[b])
            break
        elif report[p] + report[a] + report[b] > 2020:
            b -= 1
        else:
            a += 1
