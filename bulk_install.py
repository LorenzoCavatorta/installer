from prompt import Prompt
from candidate_program import CandidateProgram, JsonLogger
import sys

if __name__ == "__main__":
    instructions_json = JsonLogger()
    instructions = instructions_json.open_and_read()

    prompt = Prompt()
    json_location_string = 'installing all prorgams from {0}'.format(instructions_json.location)
    prompt.greet(add=json_location_string)
    prompt.write_to_prompt('here\'s the list of what I found:')
    prompt.write_separator()
    prompt.column_print(list(instructions.keys()))
    prompt.write_separator()
    if not prompt.ask_confirmation('would you like to procede?'):
        prompt.write_to_prompt('Ok, bye!')
        sys.exit(0)
    for program, install_instruction in instructions.items():
        candidate = CandidateProgram(**install_instruction)
        candidate.add_repo_ppa()
        candidate.add_repo_deb()
        candidate.install(v=1)
        
