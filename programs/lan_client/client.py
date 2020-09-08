"""
The client sends messages to the server, with input from the user, and prints
the received message.

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
with open("config_copy.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# server code
FLAG = False


def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break
        send_message = input("")
        clsock.sendall(send_message.encode())


def recieve_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data == "q":
            lg.info("Closing client connection")
            FLAG = True
            break
        lg.info(f"Server: {data}")
        playsound("91926__tim-kahn__ding.wav")


def main():
    # threads = []

    host = "192.168.1.6"
    port = 6789

    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((host, port))
    lg.info("Client is connected to a chat server")

    # t_send = threading.Thread(target=send_to_server, args=(client_socket,))
    # t_recv = threading.Thread(target=recieve_from_server, args=(client_socket,))

    # threads.append(t_send)
    # threads.append(t_recv)

    # t_send.start()
    # t_recv.start()

    # t_send.join()
    # t_recv.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        send_future = executor.submit(send_to_server, client_socket)
        recieve_future = executor.submit(recieve_from_server, client_socket)

    try:
        lg.info(send_future.result())
    except Exception as exc:
        lg.error(exc)

    try:
        lg.info(recieve_future.result())
    except Exception as exc:
        lg.error(exc)

    lg.info("Exiting client")

    sys.exit()


if __name__ == "__main__":
    main()
