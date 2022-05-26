from behave import given, when, then
from main import get_roots

@given("coef {a:g}, {b:g}, {c:g}")
def given_c(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when("Something")
def calculation(context):
    context.result = get_roots(context.a, context.b, context.c)

@then("Result {result}")
def get_result(context, result):
    context.result = result
