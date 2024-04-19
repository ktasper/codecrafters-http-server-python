import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    with conn:
        print ("connected")
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    



if __name__ == "__main__":
    main()
