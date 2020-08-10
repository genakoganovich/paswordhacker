def find_my_list(al_lists, my_list):
    for ix, lst in enumerate(al_lists):
        # Change the next line
        if lst is my_list:
            return ix
    return None
