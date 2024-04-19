import socket
import threading

max_threads = 5
def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    for thr in range(0, max_threads):
        print (thr)

    server(server_socket)


def server(server_socket):
        conn, _ = server_socket.accept()
        with conn:
            print ("connected")
            data = conn.recv(1024)
            data = data.split(b" ")
            print (f"Data: {data}")
            path = data[1]
            print (f"path: {path}")
            path_vals: list[bytes] = path.split(b"/")
            print (f"path vals: {path_vals}")

            if path == b"/":
                conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            elif b"echo" in path_vals[1]:
                content = f"{path_vals[2].decode()}/{path_vals[3].decode()}"
                print (f"content: {content}")
                conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: text/plain\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())

            elif b"user-agent" in path_vals[1]:
                print("Hit user agent")
                if b"User-Agent" in data[3]:
                    content = data[4].decode()
                    content = content.split('\r')
                    content = content[0]
                    print (f"content: {content}")
                    conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: text/plain\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())
                else:
                    conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            else:
                conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
if __name__ == "__main__":
    main()
