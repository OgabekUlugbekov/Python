
import threading


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_primes(start, end, primes):
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)


def threaded_prime_checker(start, end, num_threads):
    primes = []
    threads = []
    chunk_size = (end - start + 1) // num_threads
    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, primes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    primes.sort()
    print("Prime numbers:", primes)


# Test Exercise 1
threaded_prime_checker(1, 100, 4)

# Exercise 2: Threaded File Processing
import threading
from collections import Counter


def count_words(lines, word_counts):
    local_counts = Counter()
    for line in lines:
        words = line.strip().split()
        local_counts.update(words)
    with threading.Lock():
        word_counts.update(local_counts)


def threaded_file_processing(file_path, num_threads):
    with open(file_path, "r") as file:
        lines = file.readlines()

    word_counts = Counter()
    threads = []
    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        chunk_start = i * chunk_size
        chunk_end = chunk_start + chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[chunk_start:chunk_end], word_counts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word counts:", dict(word_counts))


threaded_file_processing("large_file.txt", 4)