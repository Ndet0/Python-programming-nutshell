def enough(cap, on, wait):
  """
  Return number of passengers that can't fit.
  If there's enough capacity return 0, otherwise return how many can't fit.
  """
  available = cap - on
  return 0 if available >= wait else wait - available


if __name__ == "__main__":
  # quick manual tests
  print(enough(10, 5, 5))    # expected 0
  print(enough(100, 60, 50)) # expected 10
