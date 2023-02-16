

from src.model.action.action_list import ActionList


def extend_mapping(mapping: dict, ips: list[str]) -> dict:
        for ip in ips:
            if ip in list(mapping.values()):
                continue
            free_key = 0
            while free_key in mapping.keys():
                free_key +=1
            print("freekey", free_key)
            mapping[free_key] = ip
        return mapping
    

def convert_ip_to_nrs(mapping:dict, ips:list[str]) -> list[str]:
    numbers = []
    for ip in ips:
        if ip in mapping.values():
            for k in mapping.keys():
                if mapping[k] == ip:
                    numbers.append(k)
        else:
            free_key = 0
            while free_key in mapping.keys():
                free_key +=1
            numbers.append(free_key)
    return numbers

def replace_sub_list_buttom_up(main_list, list, position: list[int]):
    toplist = main_list["sublist"]
    if len(position)== 0:
        list["sublist"] = toplist
        return list
    else:  
        next_list = toplist[position[0]]
        print(position), print("position")
        new_position = position
        new_position.pop(0)
        print(position)
        toplist.insert(position[0],replace_sub_list_buttom_up(next_list, list, new_position))
    main_list["sublist"] = toplist
    return main_list



def get_mapping_list_part(table: dict()):
    to_return = table
    del to_return["sublist"]
    return to_return


def navigate_by_content_pos(action_list: dict, content_pos: list[int]):
    list_counter = []
    counter = 0
    for x in range(0, content_pos[0]):
        if action_list["content"][x]["key" ] == "sequential_list" or action_list["content"][x]["key" ] == "parallel_list":
            counter += 1
    list_counter.append(counter)
    next = content_pos[0]
    content_pos = content_pos.pop(0)
    if not len(content_pos) == 0:
        list_counter.append(navigate_by_content_pos(action_list["content"][next], content_pos))
    return list_counter


def mapping_delete(action_list: ActionList, mapping, pos):
    if action_list.content[pos]["key"] == "sequential_list" or action_list.content[pos]["key"] == "parallel_list":
        list_count = 0
        for x in range(0, pos):
           if action_list.content[pos]["key"] == "sequential_list" or action_list.content[pos]["key"] == "parallel_list":
               list_count +=1
        del mapping["sublist"][0]
        return mapping
    robot_nrs = action_list.content[pos]["robot_nrs"]
    for nr in robot_nrs:
        counter = 0
        for elem in action_list.content:
           if elem["key"] == "sequential_list" or elem["key"] == "parallel_list":
               continue
           else:
               if nr in elem["robot_nrs"]:
                   counter += 1
        if counter == 1:
            del mapping[nr]
    return mapping
