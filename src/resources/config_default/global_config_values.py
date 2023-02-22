from enum import Enum


class GlobalConfigValues(Enum):
    CONFIG_NAME = "global_config"
    LABS = "laboratories"
    LAB_NAMES = "laboratorie_names"
    ROBOTS = "robots"
    NAME = "name"
    IP = "ip"
    EXPERIMENT_MODES = "experiment_modes"
    ACTIVE_USER = "active_user"
    USERS = "users"
    LANGUAGE = "language"

    DEFAULT_DATA = {
            LABS: {
                LAB_NAMES: {
                    ROBOTS: {
                        "11.11.11.11":{
                            NAME: "Iva die Schreckliche",
                        },
                       "22.22.22.22": {
                            NAME: "Paulaner das Wundervolle",
                        },
                        "33.33.33.33": {
                            NAME: "Mirco der Gnaedige",
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