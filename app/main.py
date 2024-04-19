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
            path = data[1]
            echo_vals: dict[str] = data.split("/")
            print (f"Data: {data}")
            print (f"Path: {path}")
            print (f"Echo Values: {echo_vals}")
        else:
            conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()
