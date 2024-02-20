import python_example
import time

def measure(name, value):
  start_time = time.time()
  for i in range(0, 10000):
    value.name
  end_time = time.time()
  print(name, "time:", end_time - start_time, "seconds")


measure("Small", python_example.SmallEnum.VALUE003)
measure("Medium", python_example.MediumEnum.VALUE100)
measure("Large", python_example.LargeEnum.VALUE999)
