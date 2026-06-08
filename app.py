import time
import dice


def roll_dice(amount, sides):
    results = []

    for _ in range(amount):
        result = dice.roll(f"1d{sides}")
        results.append(result)

    return results


if __name__ == "__main__":

    launches = roll_dice(amount=5, sides=6)

    for index, result in enumerate(launches, start=1):
        print(
            f"Lanzamiento {index} número obtenido {result}"
        )

        if index < len(launches):
            time.sleep(5)