import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    with conn:
        print ("connected")
        data = conn.recv(1024)
        if b" / " in data:
            conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        elif b"/echo" in data:
            data = data.split(b" ")
            print (f"Data: {data}")
        else:
            conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
