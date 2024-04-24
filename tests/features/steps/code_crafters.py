"""
Tests
"""
import os
import requests
from behave import Given  # type: ignore # pylint: disable=no-name-in-module
from behave import Then, When # type: ignore # pylint: disable=no-name-in-module


HEADERS = {"User-Agent": "My-User-Agent", "From": "youremail@domain.example"}
TIMEOUT = 30

@Given('we connect to the server on port "{port}"')
def step_impl(context, port):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    context.port = port


@When('sending a GET request to "{}"')
def step_impl(context, endpoint):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    response = requests.get(
        f"http://localhost:{context.port}{endpoint}", timeout=TIMEOUT, headers=HEADERS
    )
    context.response = response


@Then('we get a "{}" status code')
def step_impl(context, status_code):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.status_code == int(status_code)


@Then('we get a "{}" status code with the content type of "{}"')
def step_impl(context, status_code, expected_content_type):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.status_code == int(status_code)
    assert context.response.headers["Content-Type"] == expected_content_type


@Then('the body contains "{expected_body}"')
def step_impl(context, expected_body):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.content == expected_body.encode()


@Then("the body contains the user agent")
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.content == "My-User-Agent".encode()

@Given('concurrent GET requests to "/"')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    context.responses = []
    num_requests = 5  # Adjust this number as needed
    for _ in range(num_requests):
        response = requests.get(f"http://localhost:{context.port}/", timeout=TIMEOUT, headers=HEADERS)
        context.responses.append(response)


@Then('we respond with "200" to all the requests')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    for response in context.responses:
        assert response.status_code == 200

@Given('we create a local file called "{}" with the content of "{}"')
def step_impl(_, file_name, file_contents):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(file_contents)

@When('sending a POST request to "{}" with the body contents of "{}"')
def step_impl(context, endpoint, text_body):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    post_response = requests.post(
        f"http://localhost:{context.port}{endpoint}",
        timeout=TIMEOUT,
        headers=HEADERS,
        data=text_body,
    )
    context.response = post_response


@Then('the local file "{}" exists with the content of "{}"')
def step_impl(_, file_name, file_content):  # type: ignore # pylint: disable=function-redefined disable=inconsistent-return-statements
    """Behave"""
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            actual_content = f.read()
            assert actual_content == file_content
        os.remove(file_name)
    else:
        return False
