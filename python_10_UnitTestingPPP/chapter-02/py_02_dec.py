import random
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def run_many_times(n: int=1):
    def dec(func):
        def inner(*args, **kwargs):
            if n < 0:
                raise ValueError('n must be integer and n > 0')
            for _ in range(n):
                func(*args, **kwargs)
        return inner
    return dec

@run_many_times(n=5)
def say_hello(name: str) -> None:
    logging.debug(f'hello {name}')

@run_many_times(n=3)
def calc_square(n: int) -> int:
    logging.debug(n**2)

@run_many_times(n=random.randint(1, 10))
def do_sth() -> None:
    logging.debug('im doing sth..')

if __name__ == "__main__":
    say_hello('cnm')
    calc_square(random.randint(1, 10))
    do_sth()