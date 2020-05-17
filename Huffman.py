#!/usr/bin/env python
#from bitarray import bitarray
class Node:
  def __init__(self, freq = 0, char = None):
    self.freq = freq
    self.char = char
    self.left = None
    self.right = None

class HuffmanCodes:
  # Returns dictionary of chars and their frequencies in the string sorted
  # in descending frequency order. The dictionary will eventually be turned
  # into a list with nodes but it's easier to determine character frequencies
  # using a dictionary.
 def freqdict(self, string):
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
   return char_dict

 # this function is used for sorting nodes by frequency.
 def listsort(node):
   return node.freq

 def huffmantree(self, string):
   char_dict = freqdict(string)
   # This list will contain a node with every single character and it's freq
   # and will be created with a loop going through the dict returned by freqdict
   queue_list = []
   for key in char_dict:
     # create a new node for every key in our character dictionary and append.
     queue_list.append(Node(char_dict[key], key))
   queue_list.sort(reverse = True, key = listsort)
   # length used to iterate through list.
   length = len(queue_list)-1
   # iterate through entire list.
   for x in range(1,length):
     # The new node only contain a frequency and no char. It is an inner node of
     # the huffman tree and its frequency is the combination of the two nodes
     # below it.
     new_node = Node()
     new_node.left = queue_list.pop()
     new_node.right = queue_list.pop()
     new_node.freq = new_node.left.freq + new_node.right.freq
     # new_node is appended and then the list must be sorted again.
     queue_list.append(new_node)
     queue_list.sort(reverse = True, key = listsort)
   # return completed tree.
   return queue_list.pop()

 # takes in a dictionary and a binary tree and returns a dictionary of all the
 # chars in the binary tree with the value being their corresponding bitstrings.
 def makecodes(self, dict, bin_tree):
   # call making codes with an empty bitarray and root of huffman tree.
   makingcodes(dict, bitarray(), bin_tree)

 # This makes the bitcodes for each char in the huffman tree node (bin_tree). It
 # does this recursively by adding the bitarr input into the dictionary if the
 # bin_tree node is an external node. Otherwise it adds a 1 or 0 to the bitarr
 # and recursively calls the method again with the right and left subtree of
 # bin_tree.
 def makingcodes(self, dict, bitarr, bin_tree):
   # if external node, add bitarr to dictionary.
   if bin_tree.char != None:
     dict[bin_tree.char] = bitarr
   else:
     makingcodes(dict, bitarr.append(0), bin_tree.left)
     makingcodes(dict, bitarr.append(1), bin_tree.right)


if __name__ == '__main__':
    a = HuffmanCodes()
    correct_dict = {}
    tree = a.huffmantree("make this into a bitstring dictaaaaaaaaaaa")
    a.makecodes(correct_dict, tree)
    print(correct_dict)
