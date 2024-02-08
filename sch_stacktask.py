n = int(input())
naprav = list(map(int, input().split()))

stack = []

for i in naprav:
    if i == 1:
        if (stack and stack[-1] == 2) or (stack and stack[-1] == 1):
            stack.pop()
        else:
            stack.append(1)
    else:
        stack.append(2)

print(len(stack))
