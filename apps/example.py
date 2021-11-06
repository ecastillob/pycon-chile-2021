import datetime
import math
from random import choice as choice_random


def my_function(fields):
    last_field = fields[-1]
    counter = 0
    while True:
        counter += 1
        field = choice_random(fields)
        if field == last_field:
            break
    return counter


def run():
    fields = [
        "best_brand",
        "best_model",
        "min_year",
        "max_year",
        "budget_min",
        "budget_max",
    ]
    now = datetime.datetime.now()
    n_attemps = my_function(fields)
    total_time = str(datetime.datetime.now() - now)
    print(
        f"{n_attemps} in {total_time}",
        "\t",
        f"log_2 of {n_attemps} is ",
        math.log2(n_attemps),
    )


if __name__ == "__main__":
    run()
