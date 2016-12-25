class Prompt():

    default_greet_text = 'Hi there! Let\'s install some stuff!'
    
    def ask_name(self):
        return input('name: ')

    def write_to_prompt(self, text=''):
        print(text)

    @staticmethod
    def write_separator():
        separator = '------------------------------'
        print('\n' + separator + '\n')

    def greet(self, greet_text=default_greet_text, add=''):
        self.write_to_prompt(greet_text + '\n' + add)

    def ask_confirmation(self, request_text=''):
        yes_no_prompt = ' (yes/NO): '
        affermative_answers = ('yes', 'y', 'affermative', 'yep', 'yup')
        reply = input(request_text + yes_no_prompt)
        return reply.lower() in affermative_answers

    @staticmethod
    def column_print(str_list, col_number = 4):
        max_length = max([len(s) for s in str_list]) + 1
        remains = len(str_list)%col_number
        column_string = ' '.join(['{' + str(i) + ':' + str(max_length)  + '}'  for i in range(col_number)])
        for i in range(len(str_list)//col_number):
            print(column_string.format(*str_list[i:i+col_number]))
        column_string = ' '.join(['{' + str(i) + ':' + str(max_length)  + '}'  for i in range(remains)])
        print(column_string.format(*str_list[-remains:]))
