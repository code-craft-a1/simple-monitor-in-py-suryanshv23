
from time import sleep
import sys


def check_range(result_val, min_optimal_val, max_optimal_val):
  if min_optimal_val and (result_val < min_optimal_val):
    return True
  if max_optimal_val and (result_val > max_optimal_val):
    return True;
  return False


def check_vitals(attributes):
  for attribute in attributes:
    if check_range(attribute["attribute_val"], attribute["min_optimal_val"], attribute["max_optimal_val"]):
      print_negative_result(attribute["attribute"])
      generate_result()
      return False
  return True


def generate_result():
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)


def print_negative_result(failing_vital):
  if failing_vital == "Temperature":
    print(f"{failing_vital} critical!")
  else:
    print(f"{failing_vital} is out of range!")


def vitals_ok(temperature, pulseRate, spo2):

  attributes = [
    {
      "attribute": "Temperature",
      "attribute_val": temperature,
      "min_optimal_val": 95,
      "max_optimal_val": 102
    },
    {
      "attribute": "Pulse Rate",
      "attribute_val": pulseRate,
      "min_optimal_val": 60,
      "max_optimal_val": 100
    },
    {
      "attribute": "Oxygen Saturation",
      "attribute_val": spo2,
      "min_optimal_val": 90,
      "max_optimal_val": None
    }
  ]

  if check_vitals(attributes):
    return True

  return False
