def get_num_words(i):
    num_words = len(i.split())
    return num_words

def num_of_times(i):
    count = i.lower()
    dict_count = {}
    for k in count:
        if k in dict_count:
            dict_count[k] += 1
        else:
            dict_count[k] = 1
    return dict_count

def sort_on(dict):
    return dict["num"]

def dict_words(dict):
    list_dict = []
    for key, value in dict.items():
        char_info = {"char": key, "num": value}
        list_dict.append(char_info)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
    
