from handlers.admin import message_about_deletion
from handlers.client import message_about_buying
from handlers.other import just_answerer
from behave import given, when, then

@given(u'There is a painting named "{painting_name}"')
def step_impl(context, painting_name:str):
    context.painting_name=painting_name

@when(u'The painting is bought')
def step_impl(context):
    context.result=message_about_buying(context.painting_name)

@when(u'The painting is deleted')
def step_impl(context):
    context.result=message_about_deletion(context.painting_name)

@then(u'Send the message: {result}')
def step_impl(context, result):
    assert context.result==result

@when(u'The message is got: {message}')
def step_impl(context, message):
    context.result=just_answerer(message)



