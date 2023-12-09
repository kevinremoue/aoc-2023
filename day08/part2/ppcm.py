def ppcm(*args):
    L = list( args )
    while len( L ) > 1:
        a = L[-1]
        L.pop()
        b = L[-1]
        L.pop()
        L.append( ppcm(a,b) )


print(ppcm(20093,22357,14999,13301,17263,12169))

# 10371555451871