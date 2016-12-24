from behave import given, when, then

@given('that I\'m prompted with a question about what I want to install')
def run_prompt(context):
    context.program = context.prompt.ask_name()
    print(type(context.program))

@when('I enter the name of a program that is in the std library')
def enter_test_program(context):
    assert(context.program.aka_name == context.prompt.test_aka_name)

@then('installer installs that program')
def run_install(context):
    pass
