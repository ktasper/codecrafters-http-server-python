import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client = server_socket.accept()[1] # wait for client
    print (client)


if __name__ == "__main__":
    main()
