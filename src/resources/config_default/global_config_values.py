from enum import Enum


class GlobalConfigValues(Enum):
    CONFIG_NAME = "global_config"
    LABS = "laboratories"
    ROBOTS = "robots"
    NAME = "name"
    IP = "ip"
    EXPERIMENT_MODES = "experiment_modes"
    ACTIVE_USER = "active_user"
    USERS = "users"
    LANGUAGE = "language"

    DEFAULT_DATA = {
            LABS: {
                "Lab Name 1": {
                    ROBOTS: {
                        "11.11.11.11":{
                            NAME: "Robname 1",
                        },
                       "22.22.22.22": {
                            NAME: "Robname 2",
                        },
                        "33.33.33.33": {
                            NAME: "Robname 3",
                        }
                    },
                },
            },
            EXPERIMENT_MODES: ["Experiment Modus 1", "Experiment Modus 2", "Experiment Modus 3"],

            ACTIVE_USER: "Max",
            USERS: {
                "Max": {
                    LANGUAGE: "english",
                },

                "Moritz": {
                    LANGUAGE: "german",
                }
            }
        }