class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list = []

    def next(self, val: int) -> float:
      self.list.append(val)
      temp_sum = 0
      if len(self.list) < self.size:
        for i in range(len(self.list)):
          temp_sum += self.list[i]
        return temp_sum / len(self.list)
      else:
        for i in range(self.size):
          temp_sum += self.list[len(self.list) - self.size + i]
        return temp_sum / self.size