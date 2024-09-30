import queue
import time
import random


def generate_request(requests, request_number):
    requests.put(f'Request {request_number}')
    print(f'Added request to queue: {request_number}')


def process_request(requests):
    if not requests.empty():
        request = requests.get()
        print(f'Processing: {request}')
    else:
        print('Queue is empty')


def main():
    requests = queue.Queue()
    request_number = 1
    try:
        while True:
            time.sleep(1)
            if random.choice([True, False]):
                generate_request(requests, request_number)
                request_number += 1
            if random.choice([True, False]):
                process_request(requests)
    except KeyboardInterrupt:
        print('Good bye!')


if __name__ == '__main__':
    main()
