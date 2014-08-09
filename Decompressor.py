import HuffmanTree

def uncompress(encoded, huffman_tree):
  result = ""
  root = huffman_tree

  current = root
  for bit in encoded:
    if current.value is None:
      if bit == 0:
        current = current.left
      elif bit == 1:
        current = current.right
      if current.value is not None:
        result += current.value
        current = root

  return result

