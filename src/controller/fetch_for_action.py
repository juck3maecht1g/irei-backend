from typing import Tuple
from flask import request

from src.controller.__init__ import app
from src.model.action.action_list import ActionList
from src.model.action.listable_action import ListableAction
from src.model.fileStorrage.ActionListHandler import ActionListHandler
from src.model.fileStorrage.ExperimentConfigHandler import ExperimentConfigHandler
from src.model.alr_interface import AlrInterface


class FetchForAction:
    action_list_handler: ActionListHandler
    exp_config_handler: ExperimentConfigHandler
    current_action_list: ActionList
    alr_interface: AlrInterface

    @staticmethod
    def set_exp_config_handler(action_list_handler: ActionListHandler) -> None:
        FetchForAction.action_list_handler = action_list_handler

    @staticmethod
    def set_exp_config_handler(exp_config_handler: ExperimentConfigHandler) -> None:
        FetchForAction.exp_config_handler = exp_config_handler

    @staticmethod
    def set_alr_interface(alr_interface: AlrInterface) -> None:
        FetchForAction.alr_interface = alr_interface

    @staticmethod
    def listable_action_mapping(action: ListableAction) -> dict:
        robot_list = FetchForAction.exp_config_handler.get_exp_robots()
        action_dict = action.dictify(robot_list)
        return action_dict

    @app.route("/api/get-action_lists")  # gets name of all action lists
    @staticmethod
    def get_action_lists() -> list[str]:
        robot_list = FetchForAction.exp_config_handler.get_exp_robots()
        action_lists: list[ActionList] = FetchForAction.action_list_handler.get_all_lists(
        )
        to_return = []
        for action_list in action_lists:
            action_dict = action_list.dictify_to_display(robot_list)
            to_return.append(action_dict["name"])
        return to_return

    @app.route("/api/set_action_list", methods=['POST'])
    @staticmethod
    def set_current_list() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] != "set_action_list":
            return "F", 300
        for action_list in FetchForAction.action_list_handler.get_all_lists():
            if action_list.get_name() == data:
                FetchForAction.current_action_list = action_list
            return 'Done', 201

        return 'failed', 201

    @app.route("/api/get_action_list_content")
    @staticmethod
    def get_action_list_content() -> list[dict]:
        robot_list = FetchForAction.exp_config_handler.get_exp_robots()
        to_return = []
        for action in FetchForAction.current_action_list.get_content():
            action_dict = action.dictify_to_display(robot_list)
            to_return.append(action_dict)
        return to_return

    ##
    @app.route("/api/append_action", methods=['POST'])
    @staticmethod
    def append_action() -> Tuple[str, int]:
        robot_list = FetchForAction.exp_config_handler.get_exp_robots()
        data = request.get_json()
        if data["marker"] == "append_action":
            if data["key"] == "move":
                positions = FetchForAction.exp_config_handler.get_positions()
                for position in positions:
                    if data["position"] == position.get_name():
                        data["position"] = position
                        data["type"] = FetchForAction.exp_config_handler.get_coordinate_type(
                        )
            action = FetchForAction.action_list_handler.build(data)
            temp_list = FetchForAction.current_action_list
            temp_list.add_action(action)
            if FetchForAction.alr_interface.validate_action(temp_list.dictify(robot_list)):
                FetchForAction.action_list_handler.add(
                    FetchForAction.current_action_list, action)
                FetchForAction.current_action_list.add_action(action)
                return 'Done', 201
            else:
                return 'failed', 300

    @app.route("/api/delete_action", methods=['POST'])
    @staticmethod
    def delete_action() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "delete_action":
            FetchForAction.action_list_handler.delete_action(
                FetchForAction.current_action_list, data["position"])
            FetchForAction.current_action_list.delete_action(data["position"])
            return 'Done', 201

    @app.route("/api/swap_action", methods=['POST'])
    @staticmethod
    def swap_action() -> Tuple[str, int]:
        robot_list = FetchForAction.exp_config_handler.get_exp_robots()
        data = request.get_json()
        if data["marker"] == "swap":
            first = data["first"]
            second = data["second"]
            temp_list = FetchForAction.current_action_list
            temp_list.swap(first, second)
            if FetchForAction.alr_interface.validate_action(temp_list.dictify(robot_list)):
                FetchForAction.action_list_handler.swap(
                    FetchForAction.current_action_list, first, second)
                FetchForAction.current_action_list.swap(first, second)
                return 'Done', 201

    @app.route("/api/create_action_list", methods=['POST'])
    @staticmethod
    def create_action_list() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "create_action_list":
            FetchForAction.action_list_handler.create(
                data["name"], data["key"])
            return 'Done', 201

    def get_active_lists() -> None:  # useless because info in buttons
        pass

    @app.route("/api/executeList", methods=['POST'])
    @staticmethod
    def post_execute_list() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "execute_action_list":
            for action_list in FetchForAction.action_list_handler.get_all_lists():
                if action_list.get_name() == data["name"]:
                    robots = FetchForAction.exp_config_handler.get_exp_robots()
                    to_execute = action_list.dictify(robots)
                    FetchForAction.alr_interface.execute_sequenzial_list(
                        to_execute)

                return 'Done', 201
        else:
            return 'failed', 201

    @app.route("/api/set_coordinate_type", methods=['POST'])
    @staticmethod
    def post_coordinate_type() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "execute_action_list":
            FetchForAction.exp_config_handler.set_coordinate_type(
                data["type"])
            return 'Done', 201
        else:
            return 'failed', 201

    @app.route("/api/get_coordinates")
    @staticmethod
    def get_coordinates() -> list[dict]:
        type = FetchForAction.exp_config_handler.get_coordinate_type()
        to_return = []
        positions = FetchForAction.exp_config_handler.get_positions()
        for position in positions:
            coordinate = dict()
            coordinate["name"] = position.get_name()
            coordinate["coordinate"] = position.get_coordinate(type)
            to_return.append(coordinate)
        return to_return
