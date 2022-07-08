from random import randint
from threading import Thread

nums = []


def rand_nums() -> None:
    for i in range(10_000):
        nums.append(randint(0, 99999))


def sumator(nums: list) -> None:
    print(f"Summary = {sum(nums)}")


def arithmetic_avarage(nums: list) -> None:
    print(f"Arithmetic avarage = {sum(nums) / len(nums)}")


def main():
    t1 = Thread(target=rand_nums)
    t1.start()
    t1.join()
    t2 = Thread(target=sumator, args=(nums,))
    t3 = Thread(target=arithmetic_avarage, args=(nums,))
    t2.start()
    t3.start()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
