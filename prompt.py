class Prompt():

    default_greet_text = 'Hi there! Let\'s install some stuff!'
    
    def ask_name(self):
        return input('name: ')

    @staticmethod
    def write_to_prompt(text=''):
        print(text)

    @staticmethod
    def write_separator(length=20, space_before=False, space_after=False):
        separator = '-' * length
        print_string = '\n' + separator if space_before else separator
        if space_after:
            print_string += '\n'
        print(print_string)

    def greet(self, greet_text=default_greet_text, add=''):
        Prompt.write_to_prompt(greet_text + '\n' + add)

    def ask_confirmation(self, request_text=''):
        yes_no_prompt = ' (yes/NO): '
        affermative_answers = ('yes', 'y', 'affermative', 'yep', 'yup')
        negative_answers = ('', 'no', 'n', 'nope', 'no way', 'negative')
        reply = input(request_text + yes_no_prompt)
        while reply not in affermative_answers + negative_answers:
            Prompt.write_to_prompt('That\'s not an accepted reply')
            reply = input(request_text + yes_no_prompt)
        return reply.lower() in affermative_answers

    def ask_text(self, request_text=''):
        return input(request_text)

    @staticmethod
    def column_print(str_list, col_number = 3):
        try:
            assert isinstance(str_list, list)
        except AssertionError:
            Prompt.write_to_prompt('something went wrong when printing your stuff')
            return        
        max_length = max([len(s) for s in str_list] or [0]) + 1
        remains = len(str_list)%col_number
        column_string = ' '.join(['{' + str(i) + ':' + str(max_length)  + '}'  for i in range(col_number)])
        Prompt.write_separator(max_length * col_number)
        for i in range(len(str_list)//col_number):
            print(column_string.format(*str_list[i:i+col_number]))
        column_string = ' '.join(['{' + str(i) + ':' + str(max_length)  + '}'  for i in range(remains)])
        print(column_string.format(*str_list[-remains:]))
        Prompt.write_separator(max_length * col_number)
    
    @staticmethod
    def greet_off():
        greet_off_default = 'See Ya!'
        Prompt.write_to_prompt(greet_off_default)
