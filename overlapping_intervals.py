def merge_intervals(intervals):
    intervals.sort()
    new_list = []
    min_num = intervals[0][
        0
    ]  # assume that the min number is the min of the first interval
    max_num = intervals[0][1]  # and the max number is the max of the first interval
    for i in intervals:
        if (
            max_num >= i[0]
        ):  # if the max number of the previous interval is greater or equal the min of the current interval so there is overlapping
            max_num = max(max_num, i[1])  # we edit teh max_num

        else:
            new_list.append(
                [min_num, max_num]
            )  # if not so there is not overlapping and we append the interval to the new list

            min_num = i[0]  # and append the min max
            max_num = i[1]

    new_list.append([min_num, max_num])

    return new_list


print(merge_intervals([[1, 3], [2, 4], [6, 8], [3, 6]]))
