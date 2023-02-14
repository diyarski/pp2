def histogram(s):
    for n in s:
        output = ''
        times = n
        while(times > 0):
            output += '*'
            times = times - 1
        print(output)

histogram([4, 9, 7])
