from behave import Given, When, Then  # type: ignore # pylint: disable=no-name-in-module
import requests


@Given('we connect to the server on port "{port}"')
def step_impl(context, port):
    context.port = port


@When('sending a GET request to "{}"')
def step_impl(context, endpoint):
    response = requests.get(f"http://localhost:{context.port}{endpoint}")
    context.response = response

@Then('we get a "{}" status code')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@Then('we get a "{}" status code with the content type of "{}"')
def step_impl(context, status_code, expected_content_type):
    assert context.response.status_code == int(status_code)
    assert context.response.headers['Content-Type'] == expected_content_type

@Then('the body contains "{expected_body}"')
def step_impl(context, expected_body):
    print (context.response.content)
    assert context.response.content == expected_body.encode()