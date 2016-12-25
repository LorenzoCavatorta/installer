from candidate_program import CandidateProgram
from prompt import Prompt

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
    else:
        pass
        
    
    
