from src.controller.__init__ import app
from flask import request


class FilePathManager:


    pc_data_handler = None


    @staticmethod
    def  pc_data_handler(given_file_navigator):
        FilePathManager. pc_data_handler = given_file_navigator


    #@app.route("/api/get_content")
    #@staticmethod 
    #def get_content():
