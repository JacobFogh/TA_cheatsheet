def special_occurrence(my_list):
    for i in range(len(my_list) - 1):
        if my_list[i] == 5:
            if (my_list[i + 1] == 7 and my_list[i + 2]) != 7:
                return i
            elif (my_list[i + 1] != 7 and my_list[i + 2]) == 7:
                return i



print(special_occurrence([2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]))