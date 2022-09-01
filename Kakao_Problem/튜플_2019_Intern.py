def solution(s):
    s_list = parse_str(s)
    
    return get_tuple(s_list)


def get_tuple(s_list):
    answer = []
    
    for num_list in s_list:
        answer.append((set(num_list) - set(answer)).pop())
    
    return [int(el) for el in answer]
    
    
def parse_str(s):
    s_by_split = s.lstrip("{").rstrip("}").split("},{")
    s_list = [el.split(",") for el in s_by_split]
    
    return sorted(s_list, key=len)
