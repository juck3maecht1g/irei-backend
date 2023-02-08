

class TestClass:
    
# robots as list[dict{"name":str,"ip"str}]
    def __init__(self, robots:list[dict]):
        pass

# gets the name the experiment is ment to be displayed as
    @staticmethod
    def get_name() -> str:
        pass

# handles the process of an emergency stop
    def emergency_stop(self) -> bool:
        pass

# changes the mode the experiment is running in to the mode specified by given string
    def set_mode(self,mode:str) -> bool:
        pass
# resets the scene of the experiment
    def reset() -> bool:
        pass


#logger

    # start the logger for the experiment
    def start_log(self) -> bool:
        pass
    # stops the logger for the experiment
    def cancel_log(self) -> bool:
            pass

    # stops the logger for the experiment and return the logged data
    def stop_log(self) -> dict: 
        pass

# positional 
    #returns the current cartesian position data of thr robot dict{"name":str,"ip":str}with the given ip
    def get_cartesian_position_of(self, robot:dict) -> dict:
        pass

    #returns the current joint position data of thr robot dict{"name":str,"ip":str}with the given ip
    def get_joint_position_of(self,robot: dict) -> dict:
        pass

# gripper
    # changes state of all robots list[dict{"name":str,"ip"str}] which ips are in the given list
    def change_grippper_state(self,robots: list[dict]) -> bool:
        pass

    # opens the gripper of the robot dict{"name":str,"ip":str}specified by ip
    def open_gripper(self, robot: dict) -> bool:
        pass

    # closes the gripper of the robot dict{"name":str,"ip":str}specified by ip
    def close_gripper(self,robot: dict) -> bool:
        pass

    # todo gripper state

# action
    # validates is the given dictionarry is a valid action or action list
    def validate_action(self,action:dict) -> bool:
        pass

    # executes the actions specified by the given dictionary in the way specified by the dictionary
    #
    # if key == "sequential_list" the "content"(list[dict]) is ment to be proccessed sequential
    # if key == "parallel_list" the "content"(list[dict]) is ment to be proccessed parallel
    # if key == "close_gripper" the gripper of "robots" (list[dict{"name":str,"ip"str}])is to be closed
    # if key == "open_gripper" the gripper of "robots" (list[dict{"name":str,"ip"str}])is to be opend
    # if key == "custom" the "robots" (list[dict{"name":str,"ip"str}])execute the "action"(string) containing a String specifying the custom action  
    # if key == "move" the "robots" (list[dict{"name":str,"ip"str}])to the "coordiante"(dict)wich are of "type"(string)
                # für jeden type
    # if key == "wait" the "robots" (list[dict{"name":str,"ip"str}])wait for "time" (int)
    # 
    # 
    #    
    def execute_list(self,action_list_dict: dict) -> bool:
        pass