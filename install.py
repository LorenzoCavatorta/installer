from candidate_program import CandidateProgram
from prompt import Prompt
from sys import exit

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
        candidate.install_flag = prompt.ask_confirmation(success_text + ask_text)
        if candidate.install_flag:
            candidate.name_in_repo = candidate.aka_name
            candidate.install()
            candidate.dump_success()
        exit_installer(prompt)
    if prompt.ask_confirmation('Do you want to install one from this list? '):
        candidate.name_in_repo = prompt.ask_text('Which one? ')
        candidate.install()
        candidate.dump_success()
    if prompt.ask_confirmation('Do you need to add a repo?'):
        repo_name = prompt.ask_text('Insert repo details: ')
        candidate.add_repo_ppa(repo_name)

