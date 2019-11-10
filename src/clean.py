
# Data cleaning related functions:

def resub_list(array, sub_before, sub_after):
    # re.sub for e in array
    import re
    return [re.sub(sub_before,sub_after,e) for e in array]
