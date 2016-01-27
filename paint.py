!#python3

sqft = int(input('Input paint coverage in sq ft per gallon: ' ))
wall = int(input('Input number of walls: '))
window = int(input('Input number of windows: '))
door = int(input('Input number of doors: '))
wall1=[] # Wall list lengths
wall2=[] # Wall list widths
win1=[] # Window list lengths
win2=[] # Window list widths
d1=[] # Door list lengths
d2=[] # Door list widths


for x in range(1, (wall) +1):
    print('Input length of wall ', x, ':')
    a = [int(x) for x in input().split(',')]
    wall1.append(a)
    print('Input width of wall ', x, ':')
    b = [int(x) for x in input().split(',')]
    wall2.append(b)   
print(wall2, ':', wall1)


for x in range(1, (window) +1):
    print('Input length of window ', x, ':')
    c = [int(x) for x in input().split()]
    win1.append(c)
    print('Input width of window ', x, ':')
    d = [int(x) for x in input().split()]
    win2.append(d)
print(win2, ':', win1)


for x in range(1, (door) +1):
    print('Input length of door', x, ':')
    e = [int(x) for x in input().split()]
    d1.append(e)
    print('Input width of door ', x, ':')
    f = [int(x) for x in input().split()]
    d2.append(f)
print(d1, ':', d2)

def listsum(wall1):
   if len(wall1) == 1:
        return wall1[0]
   else:
        return wall1[0] + listsum(wall1[1:])

print(listsum(wall1))
