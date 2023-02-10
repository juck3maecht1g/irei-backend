import json
from src.controller.__init__ import app
from flask import request

from src.controller.control_page_controller import ControlPageController




class FilePathManager:
     pc_data_handler= None

     @staticmethod
     def  set_pc_data_handler(given_file_navigator):
          FilePathManager.pc_data_handler = given_file_navigator


     @app.route("/api/get_content")
     @staticmethod 
     def get_content():
          child_experiments = FilePathManager.pc_data_handler.get_dir_child_experiments()
          content = FilePathManager.pc_data_handler.get_dir_content()
          not_childer = content.difference(child_experiments)
          to_return = dict()
          to_return["to_navigate"] = child_experiments
          to_return["cant_navigate"] = not_childer
          return to_return

     @app.route("/api/navigate_up", methods=['Post'])
     @staticmethod
     def navigate_up():
          data = request.get_json()
          if data["marker"] == "navigate_up":
               FilePathManager.pc_data_handler.navigate_to_parent()
               return "Done", 201
          return "F", 300

     @app.route("/api/navigate_down", methods=['Post'])
     @staticmethod
     def navigate_down():
          data = request.get_json()
          if data["marker"] == "navigate_down":
               FilePathManager.pc_data_handler.navigate_to_child(data["dir"])
               return "Done", 201
          return "F", 300

     @app.route("/api/create_dirctory", methods=['Post'])
     @staticmethod
     def create_dir():
          data = request.get_json()
          if data["marker"] == "crerate":
               FilePathManager.pc_data_handler.create_directory(data["name"])
               return "Done", 201
          return "F", 300


     @app.route("/api/delete_dirctory", methods=['Post'])
     @staticmethod
     def delete_dir():
          data = request.get_json()
          if data["marker"] == "delete_directory":
               FilePathManager.pc_data_handler.delete_directory(data["name"])
               return "Done", 201
          return "F", 300


     #potential use but not jet
     @app.route("/api/delete_file", methods=['Post'])
     @staticmethod
     def delete_file():
          data = request.get_json()
          FilePathManager.pc_data_handler.delete_file(data)




     marker_get_base_name_dir = "get_base_name_dir"

     @app.route("/api/" + marker_get_base_name_dir)
     @staticmethod
     def get_base_name_dir() -> str:
          to_return = f"dir_from_{ControlPageController.get_identifier()}"
          return json.dumps(to_return)