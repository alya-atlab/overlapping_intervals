def merge_intervals(intervals):
    intervals.sort()
    new_list =[]
    min_num = intervals[0][0]
    max_num = intervals[0][1]
    print("min", min_num)
    print("max", max_num)
    print("-----------")
    for i in intervals:              
        if max_num >= i[0] :
            if(max_num < i[1]):
                max_num = i[1]
            print("min", min_num)
            print("max", max_num) 
                       
        else:
            new_list.append([min_num , max_num]) 
            print("min", min_num)
            print("max", max_num)
            min_num = i[0]
            max_num = i[1]
                 
    new_list.append([min_num , max_num]) 
        
    return new_list
    
print(merge_intervals([[1,3], [2,4], [6,8], [3,6]]))      
            
        