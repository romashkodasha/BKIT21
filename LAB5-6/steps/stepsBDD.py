from behave import given, when, then
from main import find_path

@given('choises "{a}", "{b}", "{c}"')
def given_c(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when("Something")
def calculation(context):
    context.result = find_path(context.a, context.b, context.c)

@then('Result "{result}"')
def get_result(context, result):
    assert context.result == result