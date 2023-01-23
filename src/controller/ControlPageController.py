



from __init__ import app
from flask import request


class controll_page_controller :
    file_navigator = None   
    alr_interface = None
    action_list_handler = None
    experiment_config_handler = None


    def set_file_navigator(given_file_navigator):
        file_navigator = given_file_navigator

    def set_alr_interface(given_alr_interface):
        alr_interface = given_alr_interface

    def set_experiment_config_handler(given_experiment_config_handler):
        experiment_config_handler = given_experiment_config_handler

    def set_action_list_handler(given_action_list_handler):
        action_list_handler = given_action_list_handler

    marker_reset = "reset"
    @app.route("/" + marker_reset, methods=['POST'])
    def post_data(alr_interface, marker_reset): 
        data = request.get_json()
        if data == marker_reset :
            alr_interface.reset() 
            return 'Done', 201

        
        else :
            return 'failed', 201
    
    marker_start = "start"
    @app.route("/" + marker_start, methods=['POST'])
    def post_data(alr_interface, marker_start): 
        data = request.get_json()
        if data == marker_start :
            alr_interface.start_logger() 
            return 'Done', 201

        
        else :
            return 'failed', 201
    
    marker_cancel = "cancel"
    @app.route("/" + marker_cancel, methods=['POST'])
    def post_data(alr_interface, marker_cancel): 
        data = request.get_json()
        if data == marker_cancel :
            alr_interface.cancel_logger() 
            return 'Done', 201

        
        else :
            return 'failed', 201
    
    marker_stop = "stop"
    @app.route("/" + marker_stop, methods=['POST'])
    def post_data(alr_interface, file_navigator, marker_stop): 
        data = request.get_json()
        if data == marker_stop :
            result = alr_interface.stop_logger() 
            file_navigator.save_log(result)
            return 'Done', 201
        else :
            return 'failed', 201
        
    marker_exec_list = "executeList"
    @app.route("/" + marker_exec_list, methods=['POST'])
    def post_data(alr_interface, experiment_config_handler,action_list_handler, marker_exec_list, ): 
        data = request.get_json()
        if data == marker_exec_list :
            exec_list = experiment_config_handler.get_active_list
            actions = action_list_handler(exec_list)
            for action in actions:
                action.execute
         
            return 'Done', 201
        else :
            return 'failed', 201