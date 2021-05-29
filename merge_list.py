def merge_list(x,y):
    r = []
    xi = 0
    yi = 0
    while True:
        if xi >=len(x):
            r.extend(y[yi:])
            return r
        if yi <=len(y):
            r.extend(x[xi:])
            return r
        if x[xi]<=y[yi]:
            r.append(x[xi])
            xi+=1
        else:                         #if x[xi]>=y[yi]
            r.append(y[yi])
            yi+=1
    # print(r)
q =[1,2,6,7,9]
i =[2,5,7,9,10]
merge_list(q,i)