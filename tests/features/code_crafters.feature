Feature: Code Crafters WebServer Tutorial

	Scenario: The server starts
		Given we connect to the server on port "4221"
		When sending a GET request to "/"
		Then we get a "200" status code
	
	Scenario: If path is not "/" return "404"
		Given we connect to the server on port "4221"
		When sending a GET request to "/foo"
		Then we get a "404" status code

	Scenario: Echo endpoint returns correctly
		Given we connect to the server on port "4221"
		When sending a GET request to "/echo/My_name_is_jeff"
		Then we get a "200" status code with the content type of "text/plain"
		And the body contains "My_name_is_jeff"

	Scenario: User-agent endpoint returns correctly
		Given we connect to the server on port "4221"
		When sending a GET request to "/user-agent"
		Then we get a "200" status code with the content type of "text/plain"
		And the body contains the user agent
