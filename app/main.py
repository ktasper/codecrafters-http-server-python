import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    with conn:
        print ("connected")
        data = conn.recv(1024)
        data = data.split(b" ")
        path = data[1]
        path_vals: list[bytes] = path.split(b"/")
        if b" / " in data:
            conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        elif b"echo" in path_vals[1]:
            content = path_vals[2]
            conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: text/plain\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())
        else:
            conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())


if __name__ == "__main__":
    main()
