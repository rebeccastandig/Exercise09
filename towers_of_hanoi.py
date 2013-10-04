# take n-1 in start to temp
# take bottom s[0] and put it in end
# take n-1 out of temp and put in end
# pop temp[0] and append that onto end
# if temp = []:
    # return

def towers_of_hanoi(start,end):
    temp = start[1:]
    if len(temp) < 1:
        return
    end.append(start.pop(0))
    start = temp
    print "Start is: ", start
    print "Temp is: ", temp
    print "End is: ", end
    towers_of_hanoi(start, end)
    return towers_of_hanoi(start, end)

towers_of_hanoi([4,3,2,1], [])