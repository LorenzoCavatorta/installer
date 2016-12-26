from candidate_program import CandidateProgram
from prompt import Prompt
import sys

def exit_installer(prompt=None):
    if prompt:
        prompt.greet_off()        
    sys.exit(0)

if __name__ == "__main__":

    prompt = Prompt()
    prompt.greet()
    candidate = CandidateProgram()
#    candidate.update_sys_list()
    candidate.aka_name = prompt.ask_name()
    if candidate.lookup_name_in_current_repos(candidate.aka_name):
        success_text = 'found a program in your current repos called exactly {0}'.format(candidate.aka_name)
        ask_text = '\nDo you want me to install that one?'
        if prompt.ask_confirmation(success_text + ask_text):
            candidate.name_in_repo = candidate.aka_name
            candidate.install()
            candidate.dump_success()
        exit_installer(prompt)
    if prompt.ask_confirmation('Do you want to install one from this list? '):
        candidate.name_in_repo = prompt.ask_text('Which one? ')
        candidate.install()
        candidate.dump_success()
        exit_installer(prompt)
    if prompt.ask_confirmation('Do you need to add a repo?'):
        candidate.ppa_repo = prompt.ask_text('Insert PPA repo details [or press enter to skip to sources.list repo].\nppa:')
        if candidate.ppa_repo:
            candidate.add_repo_ppa()
            candidate.lookup_name_in_current_repos(candidate.aka_name)
            candidate.name_in_repo = prompt.ask_text('Which one would you like to install? ')
            candidate.install()
            candidate.dump_success()
            exit_installer(prompt)
        else:
            candidate.deb_repo = prompt.ask_text('Insert string to add to apt sources. \ndeb ')
            candidate.add_repo_deb()
            candidate.lookup_name_in_current_repos(candidate.aka_name)
            candidate.name_in_repo = prompt.ask_text('Which one would you like to install? ')
            candidate.install()
            candidate.dump_success()
            exit_installer(prompt)

