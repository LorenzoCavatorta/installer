import subprocess
import re
import os
import json
from prompt import Prompt

class CandidateProgram():

    default_update_command = 'sudo apt-get update'
    default_install_command = 'sudo apt-get install -y {0}'
    default_add_ppa_command = 'sudo add-apt-repository -y ppa:{0}'
    
    def __init__(self, **kwargs):
        self.aka_name = ''
        self.name_in_repo = '' 
        self.install_command_text = ''
        self.install_type = 'std from std repo'
        self.ppa_repo = ''
        self.deb_repo = ''
        for key, value in kwargs.items():
            setattr(self, key, value)


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
        print('candidates found in your local repos: ')
        Prompt.column_print(program_list)
        return program_name in program_list
        
    def update_sys_list(self):
        update_command = BashCommand(self.default_update_command, v=0)
        update_command.run()
        
    def install(self, v=3):
        self.install_command_text = self.default_install_command.format(self.name_in_repo)
        install_command = BashCommand(self.install_command_text, v)
        print('installing: {0}'.format(self.name_in_repo))
        install_command.run()

    def dump_success(self):
        success_logger = JsonLogger()
        install_infos = dict( aka_name = self.aka_name,
                              name_in_repo = self.name_in_repo,
                              install_command_text = self.install_command_text,
                              install_type = self.install_type,
                              ppa_repo = self.ppa_repo,
        )
        success_logger.write_to_file({self.aka_name: install_infos})

    def add_repo_ppa(self, v=3, add_command_text=default_add_ppa_command):
        if not self.ppa_repo:
            return
        add_repo_command = BashCommand(add_command_text.format(self.ppa_repo), v=v)
        add_repo_command.run()
        self.update_sys_list()

    def add_repo_deb(self, v=3):
        if not self.deb_repo:
            return
        full_repo_string = 'deb {0}'.format(self.deb_repo)
        
        self.update_sys_list()

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
        try:
            assert self.execution_results.returncode == 0
        except AssertionError:
            Prompt.write_to_prompt('!!!Something went wrong there!!!')
            raise
        
class JsonLogger():

    default_json_dir = os.path.dirname(os.path.realpath(__file__))
    default_json_filename = 'programs.json'
    default_json_location = os.path.join(default_json_dir, default_json_filename)
    
    def __init__(self, location = default_json_location):
        self.location = location

    def write_to_file(self, single_dict):
        current_json = self.open_and_read(create_folder=True)
        if current_json:
            current_json.update(single_dict)
        else:
            current_json = single_dict
        with open(self.location, 'w+') as f:
            json.dump(current_json, f)
            
    def open_and_read(self, create_folder=False):
        if os.path.exists(self.location):
            with open(self.location, 'r') as f:
                return json.load(f)
        else:
            if create_folder:
                FileHandler.exist_create_folder(os.path.dirname(self.location))
            return False

class FileHandler():
    
    @staticmethod
    def exist_create_folder(folderpath):
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
