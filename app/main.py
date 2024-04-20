import argparse
import os
import socket
import sys
import threading

"""
Use argpasre to get the directory arg
CD into it
Ten try to get the file name from the client
then try and get the file
Return the file with a 200 and apllication/octet-stream
Else If the file doesn't exist, return a 404.

os.path.exists(path) -> bool
"""

HOST = "localhost"
PORT = 4221




def server(server_socket):
  """Listens for connections and creates threads to pass to the handlers"""
  while True:
    conn, _ = server_socket.accept()
    # Create a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()


def handle_client(conn):
  """Handles a single client connection."""
  print(f"Connected:")
  with conn:
    try:
      data = conn.recv(1024)
      data = data.split(b" ")
      print(f"Data: {data}")
      path = data[1]
      print(f"path: {path}")
      path_vals: list[bytes] = path.split(b"/")
      print(f"path vals: {path_vals}")

      if path == b"/":
        conn.send("HTTP/1.1 200 OK\r\n\r\n".encode())

      elif b"echo" in path_vals[1]:
        content = f"{path_vals[2].decode()}/{path_vals[3].decode()}"
        print(f"content: {content}")
        conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: text/plain\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())

      elif b"files" in path_vals[1]:
        file_name = f"{path_vals[2].decode()}/{path_vals[3].decode()}"
        if not os.path.exists(file_name):
          conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        with open(file_name, 'r') as f:
          content = f.read()
          conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: application/octet-stream\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())

      elif b"user-agent" in path_vals[1]:
        print("Hit user agent")
        if b"User-Agent" in data[3]:
          content = data[4].decode()
          content = content.split('\r')
          content = content[0]
          print(f"content: {content}")
          conn.send(f"HTTP/1.1 200 Ok\r\nContent-Type: text/plain\r\nContent-Length:{len(content)}\r\n\r\n{content}".encode())
        else:
          conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
      else:
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
    except ConnectionError:
      print(f"Client disconnected unexpectedly")



def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--directory", dest="dir")
  args = parser.parse_args()
  print (f"ARGS = {args}")
  if args.dir:
    os.chdir(args.dir)
    print (f"Changed to {args.dir}")
  server_socket = socket.create_server((HOST, PORT), reuse_port=True)
  server(server_socket)


if __name__ == "__main__":
  main()
