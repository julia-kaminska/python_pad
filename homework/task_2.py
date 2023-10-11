def unique_list(my_list):
    final_list = []
    for item in my_list:
        if item not in final_list:
            final_list.append(item)
    return final_list
