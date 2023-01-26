import sys

number = int(input())
for i in range (number):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)
