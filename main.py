import os
from UI.config_ui import ConfigUI
from core.check_in import check_in_thread
from utils import add_to_startup, is_added_to_startup, decrypt_data, getDataPath,get_old_exe_paths,get_current_app_version
from utils.os import delete_file


class CheckInApp:
    def __init__(self):

        # Variables to store user preferences
        self.username =  ""
        self.password =  ""
        self.start_time =  ""
        self.end_time =  ""
        self.weekdays =  set()
        self.appVersion = ""

        self.cancelled = False

        data_path = getDataPath() 

        if not os.path.exists(data_path):
            self.cancelled = ConfigUI.showConfigUI()


        self.preference_exists = os.path.exists(data_path)

        if not self.cancelled and self.preference_exists:
            self.load_preferences()

    
    def load_preferences(self):
        data_path = getDataPath()

        with open(data_path, 'rb') as file:
            encrypted_data = file.read()
            preferences = decrypt_data(encrypted_data)

        self.username = preferences.get('username', '')
        self.password = preferences.get('password', '')
        self.start_time = preferences.get('start_time', '')
        self.end_time = preferences.get('end_time', '')
        self.weekdays = set(preferences.get('weekdays', []))
    
    def check_in(self):
        check_in_thread(self)


if __name__ == '__main__':
    if not is_added_to_startup():
        add_to_startup()

    # Get old exe paths, if exists in current app executable directory
    old_exe_paths = get_old_exe_paths(get_current_app_version())

    if old_exe_paths and len(old_exe_paths) > 0:
        for path in old_exe_paths:
            # Delete the old executable files
            delete_file(path)

    app = CheckInApp()

    if not app.cancelled and app.preference_exists:
        app.check_in()
   