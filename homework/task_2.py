def unique_list(input_list):
    final_list = []
    for item in input_list:
        if item not in final_list:
            final_list.append(item)
    return final_list
