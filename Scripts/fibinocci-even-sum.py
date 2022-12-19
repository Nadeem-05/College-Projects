while True:
    try:
        testcase = int(input("enter no of test cases"))
        break
    except:
        print("enter valid values")
        continue
if testcase<=0:
    print("invalid")
else:
    l = [1,2]
    j=1
    p =1
    while p<=testcase:
        try:
            n = int(input("Enter till range"))
        except:
            print("write valid values")
            continue
        j=1
        l=[1,2]
        if n>2:
            while l[j]<=n:
                sum = l[j-1] + l[j]
                l.append(sum)
                j+=1
            l.remove(l[len(l)-1])
            add = 0
            for i in l:
                if i%2==0:
                    add+=i
                else:
                    continue
            print(add)
            p+=1
        else:
            print("please enter valid values")
