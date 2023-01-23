



from __init__ import app
from flask import request


class controll_page_controller :
    file_navigator = None   
    alr_interface = None
    experiment_config_handler = None


    def set_file_navigator(given_file_navigator):
        file_navigator = given_file_navigator

    def set_alr_interface(given_alr_interface):
        alr_interface = given_alr_interface

    def set_experiment_config_handler(given_experiment_config_handler):
        experiment_config_handler = given_experiment_config_handler


    @app.route("/reset", methods=['POST'])
    def post_data(): 
        data = request.get_json()
        if data == 'reset' :
            alr_interface.reset() 
            return 'Done', 201

        
        with open('testing.txt', 'w') as f:
            f.write(data)
            
            
        return 'failed', 201
    

    @app.route("/start", methods=['POST'])
    def post_data(): 
        data = request.get_json()
        if data == 'start' :
            alr_interface.start_logger() 
            return 'Done', 201

        
        with open('testing.txt', 'w') as f:
            f.write(data)
            
            
        return 'failed', 201
    
    marker = "cancel"
    @app.route("/" + marker, methods=['POST'])
    def post_data(): 
        data = request.get_json()
        if data == marker :
            alr_interface.cancel_logger() 
            return 'Done', 201

        
        with open('testing.txt', 'w') as f:
            f.write(data)
            
            
        return 'failed', 201
    
    marker = "stop"
    @app.route("/" + marker, methods=['POST'])
    def post_data(): 
        data = request.get_json()
        if data == marker :
            result = alr_interface.stop_logger() 
            file_navigator.save_log(result)
            return 'Done', 201

        
        with open('testing.txt', 'w') as f:
            f.write(data)
            
            
        return 'failed', 201