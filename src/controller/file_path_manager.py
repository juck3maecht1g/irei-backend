from src.controller.__init__ import app
from flask import request




class FilePathManager:


    pc_data_handler= None


    @staticmethod
    def  pc_data_handler(given_file_navigator):
        FilePathManager. pc_data_handler = given_file_navigator


    #@app.route("/api/get_content")
    #@staticmethod 
    #def get_content():

    @app.route("/api/navigate_up", method=['Post'])
    @staticmethod
    def navigate_down():
         data = request.get_json()
         FilePathManager.pc_data_handler.navigate_to_parent()

    @app.route("/api/navigate_down", method=['Post'])
    @staticmethod
    def navigate_down():
         data = request.get_json()
         FilePathManager.pc_data_handler.navigate_to_child(data)
         

    @app.route("/api/create_dirctory", method=['Post'])
    @staticmethod
    def navigate_down():
         data = request.get_json()
         FilePathManager.pc_data_handler.create_directory(data)

    @app.route("/api/delete_dirctory", method=['Post'])
    @staticmethod
    def navigate_down():
         data = request.get_json()
         FilePathManager.pc_data_handler.delete_directory(data)

#potential use but not jet
    @app.route("/api/delete_file", method=['Post'])
    @staticmethod
    def navigate_down():
         data = request.get_json()
         FilePathManager.pc_data_handler.delete_file(data)