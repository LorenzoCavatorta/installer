class Prompt():

    def ask_name(self):
        return input('name: ')

    def write_to_prompt(self, text=''):
        print(text)
    
    def greet(self, greet_text=None):
        default_greet_text = 'Hi there! So you want to install a new program? give me a couple of infos.'
        self.write_to_prompt(greet_text or default_greet_text)

    def ask_confirmation(self, request_text=''):
        yes_no_prompt = ' (yes/NO): '
        affermative_answers = ('yes', 'y', 'affermative', 'yep', 'yup')
        reply = input(request_text + yes_no_prompt)
        return reply.lower() in affermative_answers
