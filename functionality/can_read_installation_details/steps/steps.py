from behave import given, when, then

@given('that I\'m prompted with a question about what I want to install')
def run_prompt(context):
    context.prompt.ask_name()

@when('I enter the name of a program that is in the std library')
def enter_test_program(context):
    pass

@then('installer installs that program')
def run_install(context):
    pass
