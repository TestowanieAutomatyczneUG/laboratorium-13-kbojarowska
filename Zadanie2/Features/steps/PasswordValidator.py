from behave import *

@when('password is empty string')
def step_impl(context):
    context.password = ""

@when('password contains too little numbers')
def step_impl(context):
    context.password = "12Slowo_"

@when('password contains too little big letters')
def step_impl(context):
    context.password = "123slowo_"

@when('password dont contain special character')
def step_impl(context):
    context.password = "123Slowo"

@when('password has minimum number of characters')
def step_impl(context):
    context.password = "421S+"

@when('password has many needed characters')
def step_impl(context):
    context.password = "++++++++13171461UUCFSKBJS"

@when('password has many mixed needed characters')
def step_impl(context):
    context.password = "+_1S2l3O4W5o_+"

@when('password is good password')
def step_impl(context):
    context.password = "123Slowo_"

@then("password is invalid")
def step_imp(context):
	assert context.checkPassword.ValidPassword(context.password) == False

@then("password is valid")
def test_imp(context):
	assert context.checkPassword.ValidPassword(context.password) == True