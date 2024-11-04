def merge_intervals(intervals):
    new_list =[]
    for i in intervals:
        min_num = i[0]
        max_num = i[1]
        for j in intervals:
            if max_num > j[0] and max_num < j[1]:
                max_num = j[1]
                intervals.remove(j)
        
        new_list.append([min_num , max_num]) 
        
    return new_list
    
print(merge_intervals( [ [1,2], [2,4], [6,8]]))      
            
        