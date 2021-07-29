'*******************************************************'
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
x = int(input('Enter an integer: '))
'*******************************************************'
while counter2**2 < x:
    counter2 += 1
    
if counter2**2 == x:
    print ('Root ' + str(counter2) + ' with a power of 2')

'*******************************************************'
while counter3**3 < abs(x):
    counter3 +=1

if counter3**3 == abs(x):
    if x < 0:
        counter3 = -counter3
    print ('Root ' + str(counter3) + ' with a power of 3')
'*******************************************************'
while counter4**4 < x:
    counter4 +=1
    
if counter4**4 == x:
    print ('Root ' + str(counter4) + ' with a power of 4')
'*******************************************************'
while counter5**5 < abs(x):
    counter5 +=1

if counter5**5 == abs(x):
    if x < 0:
        counter5 = -counter5
    print ('Root ' + str(counter5) + ' with a power of 5')
    
if counter2**2 != x and counter3**3 != x and counter4**4 != x and counter5**5 != x:
    print ('Number has no roots between and including powers 2 to 5')
