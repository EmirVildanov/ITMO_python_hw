import logging
import sys
from multiprocessing import Queue
import time
import codecs
from multiprocessing import Process, Pipe
from threading import Thread

logging.basicConfig(filename="artifacts/interprocess_communication_logs.txt",
                    filemode='a',
                    format='%(asctime)s, %(message)s',
                    datefmt='%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('urbanGUI')

STOP_MESSAGE = "stop"

def A_process_logic(input_queue, output_pipe):
    while True:
        message = input_queue.get().lower()
        logger.info(f"Process_A got  message [{message}] from main.")
        output_pipe.send(message)
        if message == STOP_MESSAGE:
            break
        else:
            time.sleep(5)


def B_process_logic(input_pipe, output_pipe):
    while True:
        message = input_pipe.recv()
        logger.info(f"Process_B got  message [{message}] from Process_A.")
        encoded_msg = codecs.encode(message, 'rot_13')
        output_pipe.send(encoded_msg)
        if message == STOP_MESSAGE:
            break


def print_messages_from_B_pipe(input_pipe):
    while True:
        message = input_pipe.recv()
        logger.info(f"main      got  message [{message}] from Process_B.")
        if codecs.encode(STOP_MESSAGE, 'rot_13') == message:
            break


if __name__ == "__main__":
    parent_to_A_queue = Queue()
    A_to_B_pipe_output, A_to_B_pipe_input = Pipe()
    B_to_main_pipe_output, B_to_main_pipe_input = Pipe()

    A_process = Process(target=A_process_logic, args=(parent_to_A_queue, A_to_B_pipe_input,))
    B_process = Process(target=B_process_logic, args=(A_to_B_pipe_output, B_to_main_pipe_input))

    A_process.start()
    B_process.start()
    main_message_print_thread = Thread(target=print_messages_from_B_pipe, args=(B_to_main_pipe_output,))
    main_message_print_thread.start()

    print("Let's start communication!")
    while True:
        message = str(input("Enter message: ")).rstrip()
        parent_to_A_queue.put(message)
        logger.info(f"main      sent message [{message}] to   A_process.")
        if message == STOP_MESSAGE:
            break

    A_process.join()
    B_process.join()
    main_message_print_thread.join()
