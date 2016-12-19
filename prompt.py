from cmd import Cmd

class Prompt(Cmd):

    def do_ask_name(self,line):
        print('give me the name')

    def do_EOF(self,line):
        return True


if __name__ == '__main__':
    Prompt().cmdloop()
