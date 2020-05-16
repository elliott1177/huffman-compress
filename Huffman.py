class Node:
  def __init__(self, freq, char):
    self.freq = freq
    self.char = char
    self.left = None
    self.right = None
    
 class HuffmanCodes:
  # Returns dictionary of chars and their frequencies in the string. 
  def __freqdict__(self, string):
    str_len = len(string)
    char_dict = {}
    for char in string:
      if char in char_dict:
        char_dict[char] = char_dict[char] + 1
      else:
        char_dict[char] = 1
      # Go through every value in the key dict and divide by string length. 
      # The dictionary now contains every char and it's frequency.
      for key in char_dict:
        char_dict[key] = char_dict[key] / str_len
