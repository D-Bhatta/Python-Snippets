"""
A server script.The server waits for a message from the client and lg.infos
it. On receiving the message ‘q’ it quits. It takes input from the user and
sends it to the client.

Attributions:

S: ding.wav by tim.kahn ( paypal.me/pools/c/83tOZtfkXU) -- https://freesound.org/s/91926/ -- License: Attribution
S: buttonchime02up.wav by JustinBW -- https://freesound.org/s/80921/ -- License: Attribution
"""
import concurrent.futures
import logging
import logging.config
import sys
import threading
from json import load as jload
from socket import *  # pylint: disable=unused-wildcard-import

from playsound import playsound

# Configure logger lg with config for appLogger from config.json["logging"]
with open("config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# server code
flag = False


def receive_from_client(conn):
    global flag
    try:
        while True:
            if flag == True:
                break
            message = conn.recv(1024).decode()

            if message == "q":
                conn.send("q".encode())
                lg.info("Closing connection")
                conn.close()

                flag = True
                break
            lg.info(f"Client: {message}")
            playsound("80921__justinbw__buttonchime02up.wav")

    except:
        conn.close()


def send_to_client(conn):
    global flag
    try:
        while True:
            if flag == True:
                break
            send_message = input("")

            if send_message == "q":
                conn.send("q".encode())
                lg.info("Closing connection")
                conn.close()

                flag = True
                break
            conn.send(send_message.encode())
    except:
        conn.close()


def main():
    # threads = []

    global flag

    host = "192.168.1.6"

    server_port = 6789
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, server_port))

    server_socket.listen(1)

    lg.info("The server is ready to connect to a chat client")

    connection_socket, _ = server_socket.accept()

    lg.info("The server is connected to a chat client")

    # t_rcv = threading.Thread(target=receive_from_client, args=(connection_socket,))
    # t_snd = threading.Thread(target=send_to_client, args=(connection_socket,))

    # threads.append(t_rcv)
    # threads.append(t_snd)

    # t_rcv.start()
    # t_snd.start()

    # t_rcv.join()
    # t_snd.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        recieve_future = executor.submit(
            receive_from_client, connection_socket
        )
        send_future = executor.submit(send_to_client, connection_socket)

    try:
        lg.info(send_future.result())
    except Exception as exc:
        lg.error(exc)

    try:
        lg.info(recieve_future.result())
    except Exception as exc:
        lg.error(exc)

    lg.info("Server: exiting")

    server_socket.close()

    sys.exit()


if __name__ == "__main__":
    main()
