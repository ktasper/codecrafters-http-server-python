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

	Scenario: Concurrent Requests
		Given concurrent connections to the server
		Then we respond to all the concurrent connections

	Scenario: GET files endpoint returns correctly
		Given we connect to the server on port "4221"
		Given a local file called "goblin" exists and has the content on "Foo Bar"
		When sending a GET request to "/files/goblin"
		Then we get a "200" status code with the content type of "application/octet-stream"
		And the body contains "Foo Bar"
		When sending a GET request to "files/troll"
		Then we get a "404" status code

	Scenario: POST files endpoint returns correctly
		Given we connect to the server on port "4221"
		When sending a POST request to "/files/elf" with the body contents of "HelloWorld!"
		Then we get a "201" status code
		And the local file "elf" exists with the content of "HelloWorld!
