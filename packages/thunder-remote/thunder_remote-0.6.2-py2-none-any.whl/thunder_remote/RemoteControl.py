from __future__ import print_function

import os
import csv

from multiprocessing import Process, Queue
from inputs import devices, get_gamepad, NoDataError
from RemoteControlEvents import RemoteControlEvents
from thunder_remote.ControllerMapping import ControllerMapping
from thunder_remote.DebugLevel import DebugLevel


class RemoteControl:
    event_queue = Queue()
    control_queue = Queue()
    events = RemoteControlEvents()
    is_sleeping = False

    # TODO: write documentation
    def __init__(self, in_proc=False, profile="default", debug_level=DebugLevel.NONE, profiles_path='profiles',
                 start_sleeping=False):
        """
        Create a new RemoteControl instance and init it.

        :param profile: the controller profile to load
        :param debug_level: the debug level
        :param profiles_path: alternate path to the profile
        :param start_sleeping: start controller sleeping
        """

        self.debug_level = debug_level
        self.is_sleeping = start_sleeping

        self.remote_online = False
        self.tries_loading_profile = 1
        self.profile = profile
        self.controller_name = "Unknown"
        self.thread = None
        self.remote_found = True
        self.profile_loaded = False
        self.profiles_path = profiles_path
        self.start_sleeping = start_sleeping
        self.alarm = None
        self.in_proc = in_proc
        self.clock = None

        RemoteControl.is_sleeping = self.is_sleeping

        print("> INIT THUNDER-REMOTE")
        if not devices.gamepads:
            self.remote_found = False
            print("> No gamepad detected!")
        else:
            print("> Gamepad detected!")

        print(">")
        print("> Loading profile '" + self.profile + "'")

        self.controller_mapping = self.load_profile()
        if not self.profile_loaded:
            print("> Unable to load a profile!")
        else:
            print("> Profile for '" + self.controller_name + "' loaded!")

        print(">")

        if self.remote_found and self.profile_loaded:
            print("> Remote control is now ready for activation!")
            self.proc = Process(group=None, target=RemoteControl.control, name="thunder_remote",
                                args=(RemoteControl.event_queue, RemoteControl.control_queue, start_sleeping,
                                      debug_level, self.controller_mapping, False))

            if not in_proc:
                self.clock = Process(group=None, target=RemoteControl.alarm_clock, name="thunder-remote-clock",
                                     args=(RemoteControl.event_queue, self.controller_mapping))

    def activate(self):
        """
        Starts either the remote control process and the watcher process or only the watcher process,
        depending on the in_proc attribute.
        """

        if self.remote_online:
            print("> Remote control already activated!")
        else:
            self.remote_online = True
            if self.start_sleeping:
                self.sleep()

            print("> Remote control activated!")
            if self.in_proc:
                self.proc.start()

            self.clock.start()

    def deactivate(self):
        """
        Deactivates
        """

        self.remote_online = False
        RemoteControl.control_queue.put(["deactivate"])
        print("> Remote control deactivated!")

    def wake(self):
        """

        """

        if self.is_sleeping:
            self.is_sleeping = False
            RemoteControl.is_sleeping = False

            if self.debug_level == DebugLevel.BASIC:
                print("> [DEBUG] WAKE_UP")

    def sleep(self):
        """

        """

        if not self.is_sleeping:
            self.is_sleeping = True
            RemoteControl.is_sleeping = True

            RemoteControl.control_queue.put(["sleep"])

            if self.debug_level == DebugLevel.BASIC:
                print("> [DEBUG] SLEEP")

    def listen(self):
        """

        """

        if not RemoteControl.event_queue.empty():
            action = RemoteControl.event_queue.get()

            code, state = None, None
            method = action[0]

            if method == "alarm":
                RemoteControl.events.wake_up()

            if len(action) == 3:
                code = action[1]
                state = action[2]

            for event in RemoteControl.events.__iter__():
                if event.__name__ == method:
                    if code is not None and state is not None:
                        if self.debug_level == DebugLevel.QUEUE:
                            print("> [DEBUG] QUEUE-OUT: {0} {1}".format(code, state))

                        event.__call__(code, state)
                    else:
                        event.__call__()

    def active_control(self):
        """

        """

        RemoteControl.plain_control(self.is_sleeping, self.debug_level, self.controller_mapping)

    def load_profile(self):
        """

        :return: the current controller mapping
        """

        controller_mapping = ControllerMapping()

        try:
            path = self.profiles_path + '/' + self.profile + '.csv'
            if self.debug_level == DebugLevel.BASIC:
                print(">", path)

            if self.profiles_path is 'profiles':
                path = os.path.dirname(os.path.realpath(__file__)) + '/' + path

            if not os.path.isfile(path):
                print("> Profile '" + self.profile + "' not found!")
                return None

            self.tries_loading_profile += 1
            with open(path, 'r') as csvFile:
                reader = csv.DictReader(csvFile)

                for profile in reader:
                    # CONTROLLER NAME
                    self.controller_name = profile['CONTROLLER']

                    # LEFT BUTTONS
                    controller_mapping.BTN_NORTH = profile['BTN_NORTH']
                    controller_mapping.BTN_EAST = profile['BTN_EAST']
                    controller_mapping.BTN_SOUTH = profile['BTN_SOUTH']
                    controller_mapping.BTN_WEST = profile['BTN_WEST']

                    # START AND SELECT
                    controller_mapping.START = profile['START']
                    controller_mapping.SELECT = profile['SELECT']

                    # CROSS
                    controller_mapping.CROSS_Y = profile['CROSS_Y']
                    controller_mapping.CROSS_X = profile['CROSS_X']

                    # STICK R & STICK L
                    controller_mapping.STICK_RIGHT_Y = profile['STICK_R_Y']
                    controller_mapping.STICK_RIGHT_X = profile['STICK_R_X']
                    controller_mapping.STICK_LEFT_Y = profile['STICK_L_Y']
                    controller_mapping.STICK_LEFT_X = profile['STICK_L_X']

                    # TRIGGER AND SHOULDER
                    controller_mapping.TRIGGER_R = profile['TRIGGER_R']
                    controller_mapping.SHOULDR_R = profile['SHOULDER_R']
                    controller_mapping.TRIGGER_L = profile['TRIGGER_L']
                    controller_mapping.SHOULDR_L = profile['SHOULDER_L']

                    # THUMBS
                    controller_mapping.THUMB_R = profile['THUMB_R']
                    controller_mapping.THUMB_L = profile['THUMB_L']

                    # WAKE UP
                    controller_mapping.WAKE_UP = profile['WAKE_UP']

                    # VALUES FOR STICK MOVEMENT
                    fward_vals = profile['FORWARD_VALUES'].split(';')
                    bward_vals = profile['BACKWARD_VALUES'].split(';')

                    controller_mapping.FORWARD_VALUES = range(int(fward_vals[0]), int(fward_vals[1]) + 1)
                    if fward_vals[2] == "True":
                        controller_mapping.FORWARD_VALUES.reverse()

                    controller_mapping.BACKWARD_VALUES = range(int(bward_vals[0]), int(bward_vals[1]) + 1)
                    if bward_vals[2] == "True":
                        controller_mapping.BACKWARD_VALUES.reverse()

                self.profile_loaded = True

        except (KeyError, IOError):
            print("> Invalid profile! Switching back to default!")
            self.profile = "default"
            if self.tries_loading_profile == 1:
                self.load_profile()
            else:
                self.profile_loaded = False

        return controller_mapping

    @property
    def is_available(self):
        """

        :return: is a remote control available
        """

        return self.remote_found

    @classmethod
    def percent_value(cls, (state, common, alternate)):
        """

        :return: the normalized state
        """

        mod = 1
        values = common

        if state not in values:
            values = alternate
            mod = -1

            if state not in values:
                return 0

        return (state - float(values[0])) / (values[values.__len__() - 1] - values[0]) * mod

    @classmethod
    def alarm_clock(cls, queue, controller_mapping):
        """

        :param queue:
        :param controller_mapping:
        """
        while True:
            try:
                events = get_gamepad()

                for event in events:
                    code = event.code
                    state = event.state

                    if code in controller_mapping.WAKE_UP and state == 1 and RemoteControl.is_sleeping:
                        queue.put(['alarm'])
                        break
            except NoDataError:
                pass

    @classmethod
    def plain_control(cls, sleeping, debug_mode, controller_mapping):
        """

        :param sleeping:
        :param debug_mode:
        :param controller_mapping:
        """

        RemoteControl.control(None, RemoteControl.control_queue, sleeping, debug_mode, controller_mapping)

    @classmethod
    def control(cls, queue, c_queue, sleeping, debug, controller_mapping, plain=True):
        """

        :param plain: running in main process or in a process of its own
        :param queue: the queue for piping events to the main process
        :param c_queue: the queue for receiving commands
        :param sleeping: start controller sleeping
        :param debug: the debug level
        :param controller_mapping: the current controller mapping
        """

        is_running = True
        is_sleeping = sleeping
        debug_level = debug

        prev_cross_state = None

        while is_running:
            if not c_queue.empty():
                cmd = c_queue.get()
                if cmd[0] == "sleep":
                    is_sleeping = True
                    is_running = False if plain else is_running

                if cmd[0] == "deactivate":
                    is_running = False

            if not is_running or is_sleeping:
                return

            try:
                events = get_gamepad(blocking=False)
            except NoDataError:
                break

            for event in events:
                code = event.code
                state = event.state
                calc_props = (state, controller_mapping.FORWARD_VALUES, controller_mapping.BACKWARD_VALUES)

                if not is_sleeping:
                    if debug_level == DebugLevel.EVENT:
                        RemoteControl.events.on_any(code, state) if plain else queue.put(["on_any", code, state])

                    # BUTTON RELEASED
                    if state == 0:

                        # RIGHT BUTTONS
                        if code in controller_mapping.BTN_NORTH:
                            RemoteControl.events.on_north(code, state) if plain else queue.put(
                                ["on_north", code, state])

                        if code in controller_mapping.BTN_EAST:
                            RemoteControl.events.on_east(code, state) if plain else queue.put(["on_east", code, state])

                        if code in controller_mapping.BTN_SOUTH:
                            RemoteControl.events.on_south(code, state) if plain else queue.put(
                                ["on_south", code, state])

                        if code in controller_mapping.BTN_WEST:
                            RemoteControl.events.on_west(code, state) if plain else queue.put(["on_west", code, state])

                        # START AND SELECT
                        if code in controller_mapping.START:
                            RemoteControl.events.on_start(code, state) if plain else queue.put(
                                ["on_start", code, state])

                        if code in controller_mapping.SELECT:
                            RemoteControl.events.on_select(code, state) if plain else queue.put(
                                ["on_select", code, state])

                    # CONTROLLER CROSS
                    if code in controller_mapping.CROSS_Y or code in controller_mapping.CROSS_X:

                        # CROSS NORTH AND SOUTH
                        if code in controller_mapping.CROSS_Y:
                            if state == -1:
                                RemoteControl.events.on_cross_north_p(code, state) if plain else queue.put(
                                    ["on_cross_north_p", code, state])
                                prev_cross_state = -1

                            if state == 1:
                                RemoteControl.events.on_cross_south_p(code, state) if plain else queue.put(
                                    ["on_cross_south_p", code, state])
                                prev_cross_state = 1

                            if state == 0:
                                if prev_cross_state == 1:
                                    RemoteControl.events.on_cross_south_r(code, state) if plain else queue.put(
                                        ["on_cross_south_r", code, state])
                                else:
                                    RemoteControl.events.on_cross_north_r(code, state) if plain else queue.put(
                                        ["on_cross_north_r", code, state])

                        # CROSS WEST AND EAST
                        if code in controller_mapping.CROSS_X:
                            if state == -1:
                                RemoteControl.events.on_cross_west_p(code, state) if plain else queue.put(
                                    ["on_cross_west_p", code, state])
                                prev_cross_state = -1

                            if state == 1:
                                RemoteControl.events.on_cross_east_p(code, state) if plain else queue.put(
                                    ["on_cross_east_p", code, state])
                                prev_cross_state = 1

                            if state == 0:
                                if prev_cross_state == 1:
                                    RemoteControl.events.on_cross_east_r(code, state) if plain else queue.put(
                                        ["on_cross_east_r", code, state])
                                else:
                                    RemoteControl.events.on_cross_west_r(code, state) if plain else queue.put(
                                        ["on_cross_west_r", code, state])

                    # TRIGGERS
                    if code in controller_mapping.TRIGGER_L or code in controller_mapping.TRIGGER_R:

                        # LEFT TRIGGER
                        if code in controller_mapping.TRIGGER_L:
                            RemoteControl.events.on_trigger_left(code, state) if plain else queue.put(
                                ["on_trigger_left", code, state])

                        # RIGHT TRIGGER
                        if code in controller_mapping.TRIGGER_R:
                            RemoteControl.events.on_trigger_right(code, state) if plain else queue.put(
                                ["on_trigger_right", code, state])

                    # SHOULDERS
                    if code in controller_mapping.SHOULDR_L or code in controller_mapping.SHOULDR_R:

                        # LEFT SHOULDER
                        if code in controller_mapping.SHOULDR_L:

                            # ON RELEASE
                            if state == 0:
                                RemoteControl.events.on_shoulder_left_r(code, state) if plain else queue.put(
                                    ["on_shoulder_left_r", code, state])

                            # WHEN PRESSED
                            if state == 1:
                                RemoteControl.events.on_shoulder_left_p(code, state) if plain else queue.put(
                                    ["on_shoulder_left_p", code, state])

                        # RIGHT SHOULDER
                        if code in controller_mapping.SHOULDR_R:

                            # ON RELEASE
                            if state == 0:
                                RemoteControl.events.on_shoulder_right_r(code, state) if plain else queue.put(
                                    ["on_shoulder_right_r", code, state])

                            # WHEN PRESSED
                            if state == 1:
                                RemoteControl.events.on_shoulder_right_p(code, state) if plain else queue.put(
                                    ["on_shoulder_right_p", code, state])

                    # LEFT STICK
                    if code in controller_mapping.STICK_LEFT_X or code in controller_mapping.STICK_LEFT_Y:

                        # ANY MOVEMENT
                        RemoteControl.events.on_stick_left(code, RemoteControl.percent_value(
                            calc_props)) if plain else queue.put(
                            ["on_stick_left", code, RemoteControl.percent_value(calc_props)])

                        # X-AXIS
                        if code in controller_mapping.STICK_LEFT_X:

                            # ANY X-AXIS MOVEMENT
                            RemoteControl.events.on_stick_left_x(code, RemoteControl.percent_value(
                                calc_props)) if plain else queue.put(
                                ["on_stick_left_x", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT EAST
                            if state in calc_props[1]:
                                RemoteControl.events.on_stick_left_east(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_left_east", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT WEST
                            if state in calc_props[2]:
                                RemoteControl.events.on_stick_left_west(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_left_west", code, RemoteControl.percent_value(calc_props)])

                        # Y-AXIS
                        if code in controller_mapping.STICK_LEFT_Y:

                            # ANY Y-AXIS MOVEMENT
                            RemoteControl.events.on_stick_left_y(code, RemoteControl.percent_value(
                                calc_props)) if plain else queue.put(
                                ["on_stick_left_y", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT NORTH
                            if state in calc_props[1]:
                                RemoteControl.events.on_stick_left_north(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_left_north", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT SOUTH
                            if state in calc_props[2]:
                                RemoteControl.events.on_stick_left_south(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_left_south", code, RemoteControl.percent_value(calc_props)])

                    # RIGHT STICK
                    if code in controller_mapping.STICK_RIGHT_X or code in controller_mapping.STICK_RIGHT_Y:

                        # ANY MOVEMENT
                        RemoteControl.events.on_stick_right(code, RemoteControl.percent_value(
                            calc_props)) if plain else queue.put(
                            ["on_stick_right", code, RemoteControl.percent_value(calc_props)])

                        # X-AXIS
                        if code in controller_mapping.STICK_RIGHT_X:

                            # ANY X-AXIS MOVEMENT
                            RemoteControl.events.on_stick_right_x(code, RemoteControl.percent_value(
                                calc_props)) if plain else queue.put(
                                ["on_stick_right_x", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT EAST
                            if state in calc_props[1]:
                                RemoteControl.events.on_stick_right_east(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_right_east", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT WEST
                            if state in calc_props[2]:
                                RemoteControl.events.on_stick_right_west(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_right_west", code, RemoteControl.percent_value(calc_props)])

                        # Y-AXIS
                        if code in controller_mapping.STICK_RIGHT_Y:

                            # ANY Y-AXIS MOVEMENT
                            RemoteControl.events.on_stick_right_y(code, RemoteControl.percent_value(
                                calc_props)) if plain else queue.put(
                                ["on_stick_right_y", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT NORTH
                            if state in calc_props[1]:
                                RemoteControl.events.on_stick_right_north(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_right_north", code, RemoteControl.percent_value(calc_props)])

                            # MOVEMENT SOUTH
                            if state in calc_props[2]:
                                RemoteControl.events.on_stick_right_south(code, RemoteControl.percent_value(
                                    calc_props)) if plain else queue.put(
                                    ["on_stick_right_south", code, RemoteControl.percent_value(calc_props)])
                else:
                    if (code in controller_mapping.WAKE_UP) and not plain:
                        is_sleeping = False
                        RemoteControl.events.wake_up() if plain else queue.put(['wake_up'])
