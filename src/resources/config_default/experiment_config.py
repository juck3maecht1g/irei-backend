from enum import Enum


class experiment_config(Enum):
    EXPERIMENT_INTERFACE = "experiment_interface"
    ACTIVE_ACTIONLIST = "active_actionlist"
    NUMBER_OF_SHORTCUTS = "number_of_shortcuts"
    SHORTCUTS = "shortcuts"
    MAPPING = "mapping"
    LAB = "laboratory"
    EXP_ROBS = "experiment_robot_ips"
    MODE = "mode"
    SAVE_POS_ROB = "save_position_robot_ip"
    OPEN_GRIPPER_ROB = "open_gripper_robot_ips"
    CLOSE_GRIPPER_ROB = "close_gripper_robot_ips"
    SWITCH_GRIPPER_ROB = "switch_gripper_robot_ips"
    USED_SPACE = "used_space"
    VARIABLES = "variables"


    DEFAULT_DATA = {
        EXPERIMENT_INTERFACE: "max",
            ACTIVE_ACTIONLIST: "",
            NUMBER_OF_SHORTCUTS: 1,
            SHORTCUTS: [{
               "name": {}
            }],
            MAPPING: {
                "alName": [[[]]],
                "alName2": [],
                },
            LAB: "labname dummy",
            EXP_ROBS: ["ex_ip1", "ex_ip2"],
            MODE: "test_mode",
            SAVE_POS_ROB: "ex_ip2",
            OPEN_GRIPPER_ROB: ["open_ip", "open_ip1"],
            CLOSE_GRIPPER_ROB: ["close_ip"],
            SWITCH_GRIPPER_ROB: ["switch_ip"],
            USED_SPACE: "joint",
            VARIABLES: {
                "example_name1": {
                    "cartesian": {
                        "coord": [10, 10, 10],
                        "quat": [10, 1, 1, 1]
                    },
                    "joint": {
                        "values": [10, 10, 10, 10, 10, 10, 10]
                    }
                }
            }
        }
    