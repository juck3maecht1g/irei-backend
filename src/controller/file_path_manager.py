from typing import Tuple
from flask import request

from src.controller.__init__ import app
from src.model.fileStorrage.PcDataHandler import PcDataHandler


class FilePathManager:
    pc_data_handler: PcDataHandler

    @staticmethod
    def set_pc_data_handler(data_handler: PcDataHandler) -> None:
        FilePathManager.pc_data_handler = data_handler

    @app.route("/api/get_content")
    @staticmethod
    def get_content() -> dict:
        child_experiments = FilePathManager.pc_data_handler.get_dir_child_experiments()
        content = FilePathManager.pc_data_handler.get_dir_content()
        # list1 - list2 for difference
        not_childer = content.difference(child_experiments)
        to_return = dict()
        to_return["to_navigate"] = child_experiments
        to_return["cant_navigate"] = not_childer
        return to_return

    @app.route("/api/navigate_up", method=['Post'])
    @staticmethod
    def navigate_down() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "navigate_up":
            FilePathManager.pc_data_handler.navigate_to_parent()
            return "Done", 201
        return "F", 300

    @app.route("/api/navigate_down", method=['Post'])
    @staticmethod
    def navigate_down() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "navigate_down":
            FilePathManager.pc_data_handler.navigate_to_child(data.dir)
            return "Done", 201
        return "F", 300

    @app.route("/api/create_dirctory", method=['Post'])
    @staticmethod
    def navigate_down() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "crerate":
            FilePathManager.pc_data_handler.create_directory(data["name"])
            return "Done", 201
        return "F", 300

    @app.route("/api/delete_dirctory", method=['Post'])
    @staticmethod
    def navigate_down() -> Tuple[str, int]:
        data = request.get_json()
        if data["marker"] == "delete_directory":
            FilePathManager.pc_data_handler.delete_directory(data["name"])
            return "Done", 201
        return "F", 300

    # potential use but not jet

    @app.route("/api/delete_file", method=['Post'])
    @staticmethod
    def navigate_down() -> None:
        data = request.get_json()
        FilePathManager.pc_data_handler.delete_file(data)
