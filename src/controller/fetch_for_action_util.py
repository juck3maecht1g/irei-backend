

from src.model.action.action_list import ActionList


def extend_mapping(mapping: dict, ips: list[str] = None, list_name: str = None, list_map: dict = None) -> dict:
        if ips is None:
            mapping["sublist"].append(list_map)
            return mapping
        for ip in ips:
            if ip in list(mapping.values()):
                continue
            free_key = 0
            
            while free_key in mapping.keys():
                free_key +=1
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
        new_position = position
        new_position.pop(0)
        toplist.insert(position[0],replace_sub_list_buttom_up(next_list, list, new_position))
    main_list["sublist"] = toplist
    return main_list



def get_mapping_list_part(table: dict()):
    to_return = table
    print("TO RETURN",to_return)
    del to_return["sublist"]
    return to_return


def navigate_by_content_pos(action_list: dict, content_pos: list[int], list_counter = []):
    list_counter = list_counter
    counter = 0
    print("content", content_pos)
    for x in range(0, content_pos[0]):
        if action_list["content"][x]["key" ] == "sequential_list" or action_list["content"][x]["key" ] == "parallel_list":
            counter += 1
    list_counter.append(counter)
    next = content_pos[0]
    content_pos.pop(0)
   
  
    if not len(content_pos) == 0:
        list_counter = (navigate_by_content_pos(action_list["content"][next], content_pos, list_counter))
        print("\n\n next", list_counter)
    return list_counter


def mapping_delete(action_list: ActionList, mapping, pos):
    if action_list.content[pos].key == "sequential_list" or action_list.content[pos].key == "parallel_list":
        print("actionCONTENT",action_list.content[pos])
        list_count = 0
        for x in range(0, pos):
           if action_list.content[x].key == "sequential_list" or action_list.content[x].key == "parallel_list":
               list_count +=1
        del mapping["sublist"][list_count]
        return mapping
    print("actionCONTENT",action_list.content[pos])
    robot_nrs = action_list.content[pos].robot_nrs
    for nr in robot_nrs:
        counter = 0
        for elem in action_list.content:
           if elem.key == "sequential_list" or elem.key == "parallel_list":
               continue
           else:
               if nr in elem.robot_nrs:
                   counter += 1
        if counter == 1:
            del mapping[nr]
    return mapping
