
def open_or_senior(data):
    new_list = []
    for i in data:
        if (i[0] >= 55) and (i[1] <= 7):
            new_list.append("Senior")
        else:
            new_list.append("Open")

    return(print(new_list))

open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
