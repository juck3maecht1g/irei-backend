from src.controller.__init__ import app
from flask import request
from src.controller.choose_lr_controller import ChooseLRController
from src.model.action.action_list import ActionList
from src.model.action.listable_action import ListableAction

from src.model.file_storage.experiment_config_handler import ExperimentConfigHandler
from src.model.file_storage.global_config_handler import GlobalConfigHandler
from src.model.file_storage.action_list_handler import ActionListHandler
from src.model.alr_interface import AlrInterface
from src.model.action.action_list import ActionList

#TODO open/close/switch gripper
class FetchForAction:

    action_list_handler: ActionListHandler
    experiment_config_handler: ExperimentConfigHandler
    alr_interface: AlrInterface
    current_mapping_pos= []
    current_action_list: ActionList

    @staticmethod
    def set_experiment_config_handler(action_list_handler) -> None:
        FetchForAction.action_list_handler = action_list_handler

    @staticmethod
    def set_action_list_handler(given_action_list_handler):
        FetchForAction.action_list_handler = given_action_list_handler

    @staticmethod
    def set_alr_interface(alr_interface) -> None:
        FetchForAction.alr_interface = alr_interface


    @staticmethod
    def listable_action_mapping(action: ListableAction) -> dict:
        robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
        action_dict = action.map_dictify(robot_list)
        return action_dict

    @app.route("/api/get-action_lists") # gets name of all action lists
    @staticmethod
    def get_action_lists():
        robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
        action_lists: list[ActionList] = FetchForAction.action_list_handler.get_lists()
        to_return = []
        for action_list in action_lists:
            action_dict = action_list.dictify_to_display(robot_list)
            to_return.append(action_dict["name"])
            to_return.append(action_dict["name"])
        return to_return
    

    @app.route("/api/set_action_list", methods=['POST'])
    @staticmethod
    def set_current_list():
        try:
            data = request.get_json()
            
            for action_list in FetchForAction.action_list_handler.get_lists():
                if action_list.get_name() == data:
                    FetchForAction.current_action_list = action_list
                return 'Done', 201

            return 'no action list', 201
        except Exception as e:
            return str(e)

    @app.route("/api/get_action_list_content")
    @staticmethod
    def get_action_list_content():
        robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
        to_return: list[dict] = []
        for action in FetchForAction.current_action_list.get_content():
            action_dict = action.dictify_to_display(robot_list) # possiblility for dictify exists
            to_return.append(action_dict)
        return to_return

    ##
    @app.route("/api/append_action", methods=['POST'])
    @staticmethod
    def append_action():
        try:
            robot_list = FetchForAction.experiment_config_handler.get_exp_robots()
            data = request.get_json()
            if data["marker"] == "append_action":
                if data["key"] == "move":
                    positions = FetchForAction.experiment_config_handler.get_positions()
                    for position in positions:
                        if data["position"]== position.get_name():
                            data["position"]= position
                            data["type"] = FetchForAction.experiment_config_handler.get_coordinate_type()
                action = FetchForAction.action_list_handler.build(data)
                temp_list = FetchForAction.current_action_list
                temp_list.add_action(action)
                if FetchForAction.alr_interface.validate_action(temp_list.map_dictify(robot_list)):
                    FetchForAction.action_list_handler.add(FetchForAction.current_action_list, action)
                    FetchForAction.current_action_list.add(action)
                    return 'Done', 201
                else: return 'no valid action', 300
        except Exception as e:
            return str(e)       

    @app.route("/api/delete_action", methods=['POST'])
    @staticmethod
    def delete_action():
        try:
            data = request.get_json()
            if data["marker"] == "delete_action":
                FetchForAction.action_list_handler.delete_action(FetchForAction.current_action_list, data["position"])
                FetchForAction.current_action_list.delete_action(data["position"])
            return 'Done', 201
        except Exception as e:
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
                temp_list = FetchForAction.current_action_list
                temp_list.swap(first, second)
                if FetchForAction.alr_interface.validate_action(temp_list.map_dictify(robot_list)):
                    FetchForAction.action_list_handler.swap(FetchForAction.current_action_list, first, second)
                    FetchForAction.current_action_list.swap(first, second)
                    return 'Done', 201
        except Exception as e:
            return str(e)
    
    @app.route("/api/create_action_list", methods=['POST'])
    @staticmethod
    def create_action_list():
        try:
            data = request.get_json()
            if data["marker"] == "create_action_list":
                FetchForAction.action_list_handler.create(data["name"], data["key"])
                return 'Done', 201
        except Exception as e:
            return str(e)
    




    def get_active_lists(): # useless because info in buttons
        pass

    @app.route("/api/executeList", methods=['POST'])
    @staticmethod
    def post_execute_list():
        try:
            data = request.get_json()
            if data["marker"] == "execute_action_list":
                for action_list in FetchForAction.action_list_handler.get_lists():
                    if action_list.get_name() == data["name"]:
                        robots = FetchForAction.experiment_config_handler.get_exp_robots()
                        to_execute = action_list.dictify(robots)
                        FetchForAction.alr_interface.execute_sequenzial_list(to_execute)


                    return 'Done', 201
            else:
                return 'marker missmatched', 201

        except Exception as e:
            return str(e)
    @app.route("/api/set_coordinate_type", methods=['POST'])
    @staticmethod
    def post_coordinate_type():
        try:
            data = request.get_json()
            if data["marker"] == "execute_action_list":
                FetchForAction.experiment_config_handler.set_coordinate_type(data["type"])
                return 'Done', 201
            else:
                return 'marker missmatched', 201
        except Exception as e:
                return str(e)
        



    # need to test
    @app.route("/api/get_coordinates")
    @staticmethod
    def get_coordinates():
     
        type = FetchForAction.experiment_config_handler.get_coordinate_type()
        to_return = list[dict]
        positions = FetchForAction.experiment_config_handler.get_vars()
        for position in positions:
            coordinate = dict()
            coordinate["name"] = position.get_name()
            coordinate["coordinate"] = position.get_coordinate()
            to_return.append(coordinate)
        return to_return
       

    #todo
    def get_mapping_list_part(table: dict()):
        to_return = []
        for elem in table["mapping"]:
            if elem["type"] == "action":
                to_return.append(elem)
        return to_return


    # need to test
    @app.route("/api/get_mapping_table")
    @staticmethod
    def get_mapping_table():
        total_table = FetchForAction.experiment_config_handler.get_mapping_table(FetchForAction.current_action_list.name)
        if FetchForAction.current_mapping_pos[0] == -1:
            return FetchForAction.get_mapping_list_part(total_table)
        else:
            temp = total_table
            for x in FetchForAction.current_mapping_pos:
                temp = temp [x]
            return  FetchForAction.get_mapping_list_part(temp)
       



    @app.route("/api/set_mapping_in_table", methods=['POST'])
    @staticmethod
    def get_mapping_table():
        total= FetchForAction.experiment_config_handler.get_mapping_table(FetchForAction.current_action_list.name)
        list = total
        data = request.get_json()
        for x in FetchForAction.current_mapping_pos:
                list = list [x]
        robots = ChooseLRController.get_robots_from_ip(data["ip"])
        robots_index = 0
        for pos in range(0, len(list["mapping"])):
            if not list["mapping"][pos]["type"] == "list":
                list["mapping"][pos]["robot"] = robots[robots_index]
                robots_index =+ 1




        FetchForAction.experiment_config_handler.set_mapping_table(FetchForAction.current_action_list, total)   



        return "Done", 201
       
    @app.route("/api/set_mapping_pos", methods=['POST'])
    @staticmethod
    def set_mapping_pos():
        data = request.get_json()
        FetchForAction.current_mapping_pos = data["position"]
        return "Done", 201
       