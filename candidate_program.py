import subprocess
import re
import os
import json

class CandidateProgram():

    default_update_command = 'sudo apt-get update'
    default_install_command = 'sudo apt-get install -y {0}'
    
    def __init__(self, aka_name='', name_in_repo=''):
        self.aka_name = aka_name
        self.name_in_repo = aka_name

    def lookup_name_in_current_repos(self, program_name):
        #self.update_sys_list()
        lookup_command_text = 'sudo apt-cache search {0}'.format(program_name)
        lookup_command = BashCommand(lookup_command_text, r='output')
        full_list = lookup_command.run()
        select_start_to_hyphen = re.compile(r'^(\S*)\s-')
        program_list = []
        for l in full_list.split('\n'):
            m = select_start_to_hyphen.search(l)
            if m:
                program_list.append(m.groups()[0])
        candidates_output = 'candidates found in your local repos:\n' + '\n'.join(program_list)
        print(candidates_output)
        return program_name in program_list
        
    def update_sys_list(self):
        update_command = BashCommand(self.default_update_command, v=0)
        update_command.run()
        
    def install(self):
        self.install_command_text = self.default_install_command.format(self.name_in_repo)
        install_command = BashCommand(self.install_command_text, v=3)
        print('installing: {0}'.format(self.name_in_repo))
        install_command.run()

    def dump_success(self):
        success_logger = JsonLogger()
        install_infos = dict( aka_name = self.aka_name,
                              name_in_repo = self.name_in_repo,
                              install_command_text = self.install_command_text,
                              install_type = 'std install in current repos',
        )
        success_logger.write_to_file({self.aka_name: install_infos})

class BashCommand():

    def __init__(self, command_body='', v=0, r=None):
        self.command = command_body
        self.verbose = v
        self.return_parameter = r

    def run(self):
        self.execution_results = subprocess.run(self.command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        self.handle_results()
        if self.return_parameter == 'output':
            return self.execution_results.stdout

    def handle_results(self):
        if self.verbose >= 2:
            print(self.execution_results.stdout)
        if self.verbose >= 1:
            print(self.execution_results.stderr)
        assert self.execution_results.returncode == 0
        
class JsonLogger():

    default_json_dir = os.path.dirname(os.path.realpath(__file__))
    default_json_filename = 'programs.json'
    default_json_location = os.path.join(default_json_dir, default_json_filename)
    
    def __init__(self, location = default_json_location):
        self.location = location

    def write_to_file(self, single_dict):
        current_json = self.open_and_read()
        if current_json:
            current_json.update(single_dict)
        else:
            current_json = single_dict
        with open(self.location, 'w+') as f:
            json.dump(current_json, f)
            
    def open_and_read(self):
        if os.path.exists(self.location):
            with open(self.location, 'r') as f:
                return json.load(f)
        else:
            self.exist_create_folder(os.path.dirname(self.location))
            return False

    @staticmethod
    def exist_create_folder(folderpath):
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
