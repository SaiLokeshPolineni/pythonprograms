
def max_number(x):
    num_st = str(abs(x))
    new_st=""
    count = 0
    if x >=0:
        for i in num_st:
            if int(i) < 5 and count == 0:
                new_st+="5"
                new_st += i
                count +=1
            else:
                new_st+=i
        out = int(new_st)
        print(out)
    else:
        for i in num_st:
            if int(i) > 5 and count == 0:
                new_st += "5"
                new_st += i
                count += 1
            else:
                new_st += i
        out = abs(int(new_st))
        print(out)



max_number(10)
max_number(268)
max_number(670)
max_number(0)
max_number(-999)