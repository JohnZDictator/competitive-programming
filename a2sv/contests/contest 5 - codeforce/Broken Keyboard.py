n = int(input())

for x in range(n):
    val = str(input())
    output = []
    strOutput = []
    for c in range(len(val)):
        if not output:
            output.append(c)
            strOutput.append(val[c])
        elif val[output[-1]] == val[c]:
            if c == output[-1] + 1:
                output.pop()
                strOutput.pop()
            else:
                continue 
        else:
            if val[c] not in strOutput:
                output.append(c)
                strOutput.append(val[c])
    strOutput.sort()
    print(''.join(strOutput))