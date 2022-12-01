def ExpoMod2(x, expo, n):
    binary = format(expo, 'b')
    e = binary[1:]
    y = x
    for i in range(len(e)):
        y = (y * y) % n
        #print(y)
        if e[i] == '1':
            y = (y * x) % n
            #print(y)
    return y
print('TADA! This the answer', ExpoMod2(23, 43, 36))
