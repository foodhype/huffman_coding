from bitlist import bitlist
from collections import Counter, OrderedDict
import heapq
from HuffmanTree import HuffmanTree

def compress(text):
  timestamp = 0
  heap = []
  counter = OrderedDict(sorted(Counter(text).items()))

  for char, frequency in counter.items():
    node = HuffmanTree(frequency, timestamp, char)
    heapq.heappush(heap, node)
    timestamp += 1

  while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    node = HuffmanTree(left.priority + right.priority, timestamp, None)
    node.left = left
    node.right = right
    heapq.heappush(heap, node)
    timestamp += 1
  
  huffman_tree = heapq.heappop(heap)
  huffman_codes = {}
  traverse(huffman_tree, bitlist(), huffman_codes)

  compressed = bitlist()
  for char in text:
    compressed += huffman_codes[char]

  return compressed, huffman_tree

def traverse(tree, path, codes):
  if tree is not None:
    traverse(tree.left, path + bitlist(0, 1), codes)
    if tree.value is not None:
      codes[tree.value] = path
    traverse(tree.right, path + bitlist(1, 1), codes)
