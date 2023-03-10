

from src.controller.irei import initialize, register_experiment
import enum
import threading
import multiprocessing
import time
from typing import Dict
from alr_sim.sims import SimFactory


class SimpleExp(threading.Thread):
    class Mode(enum.Enum):
        MODE_A = "mode_a"
        MODE_B = "mode_b"
        MODE_PLAY_VARS = "play_variables"

    def __init__(self, robots: list[dict]):
        print("robots", robots)
        # Start Threading stuff
        super().__init__()

        factory = SimFactory.SimRepository.get_factory("pybullet")
        self.scene = factory.create_scene()
        self.robots: Dict[SimFactory.RobotBase] = {}
        for i, r in enumerate(robots):
            self.robots[r["ip"]] = factory.create_robot(
                self.scene, base_position=[i, 0, 0]
            )

        self.scene.start()

        self.selected_mode = None
        self.stop_all = False
        self.flipper = 1
        self.start()

    def run(self) -> None:

        while not self.stop_all:
            if self.selected_mode == self.Mode.MODE_PLAY_VARS:
                time.sleep(0.1)
                continue

            all_robots = list(self.robots.values())

            r: SimFactory.RobotBase

            target = [0.3, 0.0, 0.3]
            if self.selected_mode == self.Mode.MODE_A:
                target = [self.flipper * 0.1 + 0.3, 0.0, 0.3]
            elif self.selected_mode == self.Mode.MODE_B:
                target = [0.3, 0.0, self.flipper * 0.1 + 0.3]

            for r in all_robots[:-1]:
                r.gotoCartPositionAndQuat(
                    target, [0, 1, 0, 0], global_coord=False, block=False
                )
            all_robots[-1].gotoCartPositionAndQuat(
                target, [0, 1, 0, 0], global_coord=False, block=True
            )
            self.flipper *= -1
            time.sleep(1)

    @staticmethod
    def get_name():
        return "Simple Kitbash Experiment"

    # handles the process of an emergency stop
    def emergency_stop(self) -> bool:
        self.stop_all = True
        return True

    # changes the mode the experiment is running in to the mode specified by given string
    def set_mode(self, mode: str) -> bool:
        for m in self.Mode:
            if mode in (m.name, m.value):
                self.selected_mode = m
                return True
        return False

    # resets the scene of the experiment
    def reset(self) -> bool:
        self.scene.reset()
        return True

    # logger
    # start the logger for the experiment
    def start_log(self) -> bool:
        self.scene.start_logging()
        return True

    def cancel_log(self) -> bool:
        self.scene.stop_logging()
        return True

    # stops the logger for the experiment and return the logged data
    def stop_log(self) -> dict:
        self.scene.stop_logging()

        log_dict = {}

        for robot_name, robot in self.robots.items():
            robot_log = robot.robot_logger.log_dict_full
            for signal_name, signal_val in robot_log.items():
                log_dict[f"{robot_name}_{signal_name}"] = signal_val

        return log_dict

    # positional
    # returns the current cartesian position data of the robot with the ip given as str
    def get_cartesian_of(self, robot: str) -> dict:
        return self.robots[robot].current_c_pos

    # returns the current quaternion data of the robot with the ip given as str
    def get_quat_of(self, robot: str) -> dict:
        return self.robots[robot].current_c_quat

    # returns the current joint position data of thr robot with the ip given as str
    def get_joint_of(self, robot: str) -> dict:
        return self.robots[robot].current_j_pos

    # gripper
    # changes state of all robots list[str] which ips are in the given list
    def change_grippper_state(self, robot, robots: list[str]) -> bool:
        pass

    # opens the gripper of the robot dict{"name":str,"ip":str}specified by ip
    def open_gripper(self, robot: str) -> bool:
        self.robots[robot].open_fingers()
        return True

    # closes the gripper of the robot dict{"name":str,"ip":str}specified by ip
    def close_gripper(self, robot: str) -> bool:
        self.robots[robot].close_fingers()
        return True

    # action
    # validates is the given dictionarry is a valid action or action list
    def validate_action(self, action: dict, parallel=False) -> bool:
        print("\n\n\n", action)
        if action["key"] == "parallel_list":
            if parallel:
                return False
            valid = True
            for sub_action in action["content"]:
                valid = valid & self.validate_action(sub_action, True)
                if not valid:
                    return False

        if action["key"] == "sequential_list":
            valid = True
            for sub_action in action["content"]:
                valid = valid & self.validate_action(sub_action, parallel)
                if not valid:
                    return False

        return True

    # executes the actions specified by the given dictionary in the way specified by the dictionary
    #
    # if key == "sequential_list" the "content" (list[dict]) is meant to be proccessed sequential
    # if key == "parallel_list" the "content" (list[dict]) is meant to be proccessed parallel
    # if key == "close_gripper" the gripper of "robots" specified by their ip (list[str]) is to be closed
    # if key == "open_gripper" the gripper of "robots" specified by their ip (list[str]) is to be opend
    # if key == "custom" the "robots" specified by their ip (list[str]) execute the "action" (string) containing a String specifying the custom action
    # if key == "move" the "robots" specified by their ip (list[str]) to the "coord"["values"] (dict) wich are of "type"(string)
    # f??r jeden type
    # if key == "wait" the "robots" specified by their ip (list[str]) wait for "time" (int)
    #
    #
    #
    def execute_list(self, action: dict, nested=False) -> bool:
        if not nested:
            self.selected_mode = self.Mode.MODE_PLAY_VARS

        key = action["key"]

        if key == "parallel_list":
            raise NotImplementedError(
                "Parallel Actions are not supported right now")

        elif key == "sequential_list":
            for sub_action in action["content"]:
                self.execute_list(sub_action, True)

        elif key == "close_gripper":
            for r in action["robots"]:
                self.close_gripper(r)

        elif key == "open_gripper":
            for r in action["robots"]:
                self.open_gripper(r)

        elif key == "move":
            print("Only Support JOINT for now")
            # For Cartesian use gotoCartPositionAndQuat() instead of gotoJointPosition()

            for r in action["robots"]:
                self.robots[r].gotoJointPosition(
                    action["coord"]["values"], block=False
                )

        elif key == "wait":

            for r in action["robots"]:
                self.robots[r].wait(action["time"], block=False)
            self.robots[action["robots"]].wait(action["time"], block=True)

        else:
            raise NotImplementedError(f"Action {key} is not implemented")

        if not nested:
            self.selected_mode = self.Mode.MODE_A
        return True


if __name__ == "__main__":
    register_experiment(SimpleExp)
    initialize()
    exp = SimpleExp([{"name": "test"}, {"name": "test2"}])

    exp.set_mode("mode_a")
    time.sleep(10)
    exp.set_mode("mode_b")

    time.sleep(10)
    # exp.emergency_stop()
