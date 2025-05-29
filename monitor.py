from time import sleep
import sys


def is_below_min(value, min_val):
    return min_val is not None and value < min_val


def is_above_max(value, max_val):
    return max_val is not None and value > max_val


def check_range(value, min_val, max_val):
    return is_below_min(value, min_val) or is_above_max(value, max_val)


def animate_result():
    for _ in range(6):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(1)


def print_negative_result(vital_name):
    message = f"{vital_name} critical!" if vital_name == "Temperature" else f"{vital_name} is out of range!"
    print(message)


def process_vital(attribute):
    if check_range(attribute["attribute_val"], attribute["min_optimal_val"], attribute["max_optimal_val"]):
        print_negative_result(attribute["attribute"])
        animate_result()
        return False
    return True


def check_vitals(attributes):
    return all(process_vital(attr) for attr in attributes)


def vitals_ok(temperature, pulseRate, spo2):
    attributes = [
        {"attribute": "Temperature", "attribute_val": temperature, "min_optimal_val": 95, "max_optimal_val": 102},
        {"attribute": "Pulse Rate", "attribute_val": pulseRate, "min_optimal_val": 60, "max_optimal_val": 100},
        {"attribute": "Oxygen Saturation", "attribute_val": spo2, "min_optimal_val": 90, "max_optimal_val": None},
    ]
    return check_vitals(attributes)
