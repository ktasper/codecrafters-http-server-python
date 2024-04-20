[![progress-banner](https://backend.codecrafters.io/progress/http-server/cc4c94c4-4d41-497c-8c81-f930a1d2ba23)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

Given I have passed the initial challenge, I wanted to add `behave` tests and then refactor the code.


# Tests
- The tester will send you a request of the form GET /user-agent, and it'll include a User-Agent header.
    Your program will need to respond with a 200 OK response. The response should have a content type of text/plain, and it should contain the user agent value as the body.
- In this stage, your server will need to handle multiple concurrent connections.
    The tester will send you multiple requests at the same time. Your server will need to respond to all of them
- In this stage, your server will need to return the contents of a file.
    The tester will execute your program with a --directory flag like this:
    ./your_server.sh --directory <directory>
    It'll then send you a request of the form GET /files/<filename>.
    If <filename> exists in <directory>, you'll need to respond with a 200 OK response. The response should have a content type of application/octet-stream, and it should contain the contents of the file as the body.
- In this stage, your server will need to accept the contents of a file in a POST request and save it to a directory.
    Just like in the previous stage, the tester will execute your program with a --directory flag like this:
    ./your_server.sh --directory <directory>
    It'll then send you a request of the form POST /files/<filename>. The request body will contain the contents of the file.
    You'll need to fetch the contents of the file from the request body and save it to <directory>/<filename>. The response code returned should be 201.
