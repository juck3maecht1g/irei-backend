from enum import Enum


class ExpConfigValues(Enum):
    CONFIG_NAME = "experiment_config"

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
    SHORTCUT_NAME = "name"


    DEFAULT_DATA = {
        EXPERIMENT_INTERFACE: "",
            ACTIVE_ACTIONLIST: "",
            SHORTCUTS: [{"name" :{}}],
            MAPPING: {},
            LAB: "",
            EXP_ROBS: [],
            MODE: "Experiment Modus 1",
            SAVE_POS_ROB: [],
            OPEN_GRIPPER_ROB: [],
            CLOSE_GRIPPER_ROB: [],
            SWITCH_GRIPPER_ROB: [],
            USED_SPACE: "joint",
            VARIABLES: {}
        }
    