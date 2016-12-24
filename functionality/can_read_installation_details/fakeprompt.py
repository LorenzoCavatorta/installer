from cantidate_program import CandidateProgram


class FakePrompt():
    test_aka_name = 'test_aka'
        
    def ask_name(self):
        aka_name = self.test_aka_name
        candidate = CandidateProgram(aka_name)
        return candidate
    
