import requests
from behave import Given  # type: ignore # pylint: disable=no-name-in-module
from behave import Then, When


@Given('we connect to the server on port "{port}"')
def step_impl(context, port):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    context.port = port


@When('sending a GET request to "{}"')
def step_impl(context, endpoint):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    headers = {
    'User-Agent': 'My-User-Agent',
    'From': 'youremail@domain.example'
    }
    response = requests.get(f'http://localhost:{context.port}{endpoint}', timeout=30, headers=headers)
    context.response = response

@Then('we get a "{}" status code')
def step_impl(context, status_code):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.status_code == int(status_code)


@Then('we get a "{}" status code with the content type of "{}"')
def step_impl(context, status_code, expected_content_type):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.status_code == int(status_code)
    assert context.response.headers['Content-Type'] == expected_content_type


@Then('the body contains "{expected_body}"')
def step_impl(context, expected_body):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.content == expected_body.encode()


@Then('the body contains the user agent')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    """Behave"""
    assert context.response.content == 'My-User-Agent'.encode()

@Given('concurrent connections to the server')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    raise NotImplementedError('STEP: Given concurrent connections to the server')


@Then('we respond to all the concurrent connections')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    raise NotImplementedError('STEP: Then we respond to all the connections')


@Given('a local file called "goblin" exists and has the content on "Foo Bar"')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    raise NotImplementedError('STEP: Given a local file called "goblin" exists and has the content on "Foo Bar"')


@When('sending a POST request to "/files/elf" with the body contents of "HelloWorld!"')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    raise NotImplementedError('STEP: When sending a POST request to "/files/elf" with the body contents of "HelloWorld!"')


@Then('the local file "elf" exists with the contnet of "HelloWorld!')
def step_impl(context):  # type: ignore # pylint: disable=function-redefined
    raise NotImplementedError('STEP: Then the local file "elf" exists with the content of "HelloWorld!')