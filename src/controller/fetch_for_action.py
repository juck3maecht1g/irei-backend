from src.controller.__init__ import app
from flask import request
from src.controller.choose_lr_controller import ChooseLRController
from src.model.action.action import Action
from src.model.action.action_list import ActionList
from src.model.action.listable_action import ListableAction
from src.model.action.listable_factory import ListableFactory

from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.alr_interface import AlrInterface
from src.model.action.action_list import ActionList
from src.controller.fetch_for_action_util import *

#TODO open/close/switch gripper
class FetchForAction:

    action_list_handler: ActionListHandler
    experiment_config_handler: ExperimentConfigHandler
    alr_interface: AlrInterface
    listable_factory: ListableFactory
    current_button_index= 0
    current_mapping_pos= []
    current_list_name = 0

    @staticmethod
    def set_experiment_config_handler(experiment_config_handler) -> None:
        FetchForAction.experiment_config_handler = experiment_config_handler

    @staticmethod
    def set_action_list_handler(given_action_list_handler):
        FetchForAction.action_list_handler = given_action_list_handler

    @staticmethod
    def set_alr_interface(alr_interface) -> None:
        FetchForAction.alr_interface = alr_interface


    # @staticmethod
    # def listable_action_mapping(action: ListableAction) -> dict:
    #     robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
    #     action_dict = action.map_dictify(robot_list)
    #     return action_dict
    

    # """
    # this method returns the names of all action lists as string list
    # and displays it to the frontens
    # """
    @app.route("/api/get-action_lists")
    @staticmethod
    def get_action_lists():
        action_lists = FetchForAction.action_list_handler.get_lists()
       
        return action_lists
    


    #this method takes a sting from the route and sets it as name of the currently aktive action list
    @app.route("/api/set_action_list", methods=['POST'])
    @staticmethod
    def set_current_list():
        try:
            data = request.get_json() 
            for action_list in FetchForAction.action_list_handler.get_lists():
                if action_list == data["name"]:
                   
                    FetchForAction.current_list_name = data["name"]
                    if FetchForAction.experiment_config_handler.has_mapping(FetchForAction.current_list_name):
                        temp_table = FetchForAction.experiment_config_handler.get_map(FetchForAction.current_list_name)
                    else:
                        temp_list = FetchForAction.action_list_handler.get_list(FetchForAction.current_list_name)
              
                        temp_table = temp_list.do_mapping()
                     
                        FetchForAction.experiment_config_handler.set_map(FetchForAction.current_list_name, temp_table)
                    FetchForAction.experiment_config_handler.set_shortcut(FetchForAction.current_button_index, FetchForAction.current_list_name, temp_table)
                    return 'Done', 201
            return 'no action list', 201
        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)






    @app.route("/api/get_action_list_content")
    @staticmethod
    def get_action_list_content():
        action_list = FetchForAction.action_list_handler.get_list(FetchForAction.current_list_name)
        print("LIST", action_list)
        content = action_list.nr_dictify()["content"]
        return content




    ##wo mapping
    @app.route("/api/append_action", methods=['POST'])
    @staticmethod
    def append_action():
        print("APPEND ACTION")
        try:
            data = request.get_json()#{"marker": "append_action", "key": "wait", "robot": ["ex_ip1"], "time": 71283956238}#request.get_json() 
            action: Action
            print("MARKER", data["marker"])
            if data["marker"] == "append_action":
                print("KEY", data["key"])
                if data["key"] == "move":
                    positions = FetchForAction.experiment_config_handler.get_vars()
                    for position in positions:
                        type = FetchForAction.experiment_config_handler.get_used_space()
                        if data["position"]== position.get_name(): 
                            data["name"]= position.get_name()
                            data["coord"] = position.get_coordinate(type)
                            data["type"] = type
                           
                if not "list" in data["key"]:
                    map = FetchForAction.experiment_config_handler.get_shortcut_map(FetchForAction.current_button_index)
                    new_mapping = extend_mapping(map, data["robot"])
                    data["robot_nrs"] = convert_ip_to_nrs(map, data["robot"]) #missing mapping dict
                    action = ListableFactory.create_single_action(data)
                   
                else:
                    action = FetchForAction.action_list_handler.get_list(data["name"])
                    print("ACTION", action)
                print("ACTION AFTER ELSE", action)
                FetchForAction.action_list_handler.add_action(FetchForAction.current_list_name, action)
                print("ADDED", )
                mapping = FetchForAction.experiment_config_handler.get_shortcut_map(FetchForAction.current_button_index)
                if not "list" in data["key"]:
                    new_mapping = extend_mapping(mapping, ips=data["robot"])
                else:
                    new_mapping = extend_mapping(mapping=mapping, list_name=data["name"], list_map=FetchForAction.experiment_config_handler.get_map(data["name"]))
                
                print("MAPPING",new_mapping)
                FetchForAction.experiment_config_handler.set_map(FetchForAction.current_list_name, new_mapping)   
                FetchForAction.experiment_config_handler.set_shortcut_map(FetchForAction.current_button_index, new_mapping)
                return 'Done', 201
        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)       



    # wo mapping
    @app.route("/api/delete_action", methods=['POST'])
    @staticmethod
    def delete_action():
        try:
            data = request.get_json()
            print("DATA", data)
            if data["marker"] == "delete_action":
                action_list = FetchForAction.action_list_handler.get_list(FetchForAction.current_list_name)
                FetchForAction.action_list_handler.del_action(FetchForAction.current_list_name, data["position"])
                mapping = FetchForAction.experiment_config_handler.get_shortcut_map(FetchForAction.current_button_index)
                new_mapping = mapping_delete(action_list, mapping, data["position"])
                FetchForAction.experiment_config_handler.set_map(FetchForAction.current_list_name, new_mapping)   
                FetchForAction.experiment_config_handler.set_shortcut(FetchForAction.current_button_index, FetchForAction.current_list_name,new_mapping)
            return 'Done', 201
        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)
    



    @app.route("/api/swap_action", methods=['POST'])
    @staticmethod
    def swap_action():
        try:
            robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
            data = request.get_json()
            if data["marker"] == "swap":
                first = data["first"]
                second = data["second"]
           
                FetchForAction.action_list_handler.swap_action(FetchForAction.current_list_name, first, second)
                return 'Done', 201
        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)
    
    @app.route("/api/create_action_list", methods=['POST'])
    @staticmethod
    def create_action_list():
        try:
            data = request.get_json() 
            if data["marker"] == "create_action_list":
                
                FetchForAction.action_list_handler.create(data["name"], data["key"])
                FetchForAction.current_list_name = data["name"]
                return 'Done', 201
        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)
    




    def get_active_lists(): # useless because info in buttons
        pass

    @app.route("/api/executeList", methods=['POST'])
    @staticmethod
    def post_execute_list():
        try:
            data = request.get_json()
           
            if data["marker"] == "execute_action_list":
                name = FetchForAction.experiment_config_handler.get_shortcuts()[FetchForAction.current_button_index]
                name = name[0]
               
                action_list = FetchForAction.action_list_handler.get_list(name)
                
                map = FetchForAction.experiment_config_handler.get_shortcut_map(FetchForAction.current_button_index)
               
                to_execute = action_list.map_dictify(map)
               
                FetchForAction.alr_interface.execute_list(to_execute)
                return 'Done', 201
            else:
                return 'marker missmatched', 201

        except Exception as e: 
            print("ERROR",e.__str__())
            return str(e)
        






    @app.route("/api/set_coordinate_type", methods=['POST'])
    @staticmethod
    def post_coordinate_type():
        try:
            data = request.get_json()
            if data["marker"] == "execute_action_list":
                FetchForAction.experiment_config_handler.set_use_space(data["type"])
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e: 
                print("ERROR",e.__str__())
                return str(e)
        



    # need to test
    @app.route("/api/get_coordinates")
    @staticmethod
    def get_coordinates():
     
        type = FetchForAction.experiment_config_handler.get_used_space()
        to_return: list[dict] = []
        positions = FetchForAction.experiment_config_handler.get_vars()
        for position in positions:
            coordinate = dict()
            coordinate["name"] = position.get_name()
            coordinate["coordinate"] = position.get_coordinate(type)
            to_return.append(coordinate)
        return to_return
       
    
    # need to test
    @app.route("/api/get_mapping_table")
    @staticmethod
    def get_mapping_table():
        if FetchForAction.experiment_config_handler.has_mapping(FetchForAction.current_list_name):
            total_table = FetchForAction.experiment_config_handler.get_map(FetchForAction.current_list_name)
            
            if FetchForAction.current_mapping_pos[0] == -1:
                return get_mapping_list_part(total_table)
            else:
                action_list = FetchForAction.action_list_handler.get_list(FetchForAction.current_list_name)
                action_list = action_list.nr_dictify()
                look_up_list = navigate_by_content_pos(action_list, FetchForAction.current_mapping_pos)
                temp = total_table
                #temp
                look_up_list.pop()
                for x in look_up_list:
                    print("temp", temp)
                    temp = temp["sublist"][x]
                return get_mapping_list_part(temp)
        else:
            temp_list = FetchForAction.action_list_handler.get_list(FetchForAction.current_list_name)
            temp_table = temp_list.do_mapping()
            FetchForAction.experiment_config_handler.set_map(FetchForAction.current_list_name, temp_table)
            return {0: "ip0", 1: "ip0",} #temp_table



    @app.route("/api/set_mapping_in_table", methods=['POST'])
    @staticmethod
    def set_mapping_in_table():
        try:
            total= FetchForAction.experiment_config_handler.get_map(FetchForAction.current_list_name)
            list =  total
            data = request.get_json()
            if not FetchForAction.current_mapping_pos[0] == -1:
                for x in FetchForAction.current_mapping_pos:       
                    list = list["sublist"] [x]
            

            for elem in data:
                for key in elem:
                    list[int(key)] = elem[key] 

            #if not FetchForAction.current_mapping_pos[0] == -1:
                #total = FetchForAction.replace_sub_list_buttom_up(total, list, FetchForAction.current_mapping_pos)
            #else:
            # total = list
        
            FetchForAction.experiment_config_handler.set_map(FetchForAction.current_list_name, total)  
            if not FetchForAction.current_mapping_pos[0] == -1:
                FetchForAction.experiment_config_handler.set_shortcut_map(FetchForAction.current_button_index, total)
            return "Done", 201
        except Exception as e: 
                print("ERROR",e.__str__())
                return str(e)
        
   
    @app.route("/api/set_mapping_pos", methods=['POST'])
    @staticmethod
    def set_mapping_pos():
        try:
            data = request.get_json()
            FetchForAction.current_mapping_pos = data

            return "Done", 201
        except Exception as e: 
                    print("ERROR",e.__str__())
                    return str(e)
        

    @app.route("/api/set_button_index", methods=['POST'])
    @staticmethod
    def set_button_index():
        try :
            data = request.get_json() 
            FetchForAction.current_button_index = data 
            return "Done", 201
        except Exception as e: 
                print("ERROR",e.__str__())
                return str(e)
        



    @app.route("/api/get_action_list_button_content")
    @staticmethod
    def get_action_list_button_content():
        shortcuts = FetchForAction.experiment_config_handler.get_shortcuts()
       
        return shortcuts

