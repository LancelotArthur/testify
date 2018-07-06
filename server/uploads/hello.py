f = open('1test.txt')
w = open('test_boundary', 'w')

a = f.readline()
b = a.strip('\n').split(' ')
c = []

while a:
    c.append(b)
    a = f.readline()
    b = a.strip('\n').split(' ')

for k, line in enumerate(c):
    if int(line[0]) == 0 or int(line[1]) == 0 or int(line[2]) == 0:
        c[k].append('IncompleteError')
        continue
    sales = 0
    commission = 0
    sales += 25 * int(line[0]) + 30 * int(line[1]) + 45 * int(line[2])
    if sales <= 1000:
        commission = sales * 0.1
    elif sales <= 1800:
        commission = sales * 0.15
    else:
        commission = sales * 0.2
    c[k] = [line[0], line[1], line[2], sales, commission]

for line in c:
    w.write(" ".join(map(str, line)) + '\n')

# if count[0] < 1 or count[0] > 70:
#     print("master wrong")
# elif count[1] < 1 or count[1] > 80:
#     print("display wrong")
# elif count[2] < 1 or count[2] > 80:
#     print("peripheral wrong")
# else:
#     if sales <= 1000:
#         commission = sales * 0.1
#     elif sales <= 1800:
#         commission = sales * 0.15
#     else:
#         commission = sales * 0.2


    # print("sales: ", sales, " commission: ", commission)

f.close()
w.close()
