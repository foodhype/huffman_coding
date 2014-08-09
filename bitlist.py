class bitlist:
  def __init__(self, bits = 0, length = 0):
    self.current = 0
    self.bits = bits
    self.length = length

  def append(self, bit):
    self.bits = (self.bits << 1) + bit
    self.length += 1

  def __add__(self, other):
    newbits = (self.bits << len(other)) + other.bits
    newlength = len(self) + len(other)
    return bitlist(newbits, newlength)

  def __iter__(self):
    return self

  def next(self):
    if self.current >= len(self):
      raise StopIteration
    else:
      self.current += 1
      return self[self.current - 1]

  def __len__(self):
    return self.length

  def __getitem__(self, index):
    return 1 if self.bits & (1 << (len(self) - index - 1)) else 0

  def __setitem__(self, index, value):
    if value == 0:
      self.bits &= ~(1 << index)
    else:
      self.bits |= (1 << index)

  def __str__(self):
    return bin(self.bits)[2:].zfill(self.length)
