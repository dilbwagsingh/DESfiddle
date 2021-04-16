from binascii import hexlify, unhexlify
from random import sample, shuffle
from typing import List, Tuple

def permute(s: str, arr: List[int], n: int) -> str:
  """Shuffle a string using an 1-indexed array and resizing it to size n. This function is used to resize and apply a specific permutation to a string during various iterations of DES"""
  final = ""
  for i in range(n):
    final += s[arr[i] - 1]
  return final

def xor(a: str, b: str) -> str:
  """Perform poistionwise xor of the arguments. This function is used to implement the xor operation between the round keys and plaintext block in DES"""
  res = ""
  for i in range(len(a)):
    if (a[i] == b[i]):
      res += '0'
    else:
      res += '1'
  return res

def shift_left(k: str, shift: int) -> str:
  """Shift a string k by shift units to the left. This is used while generating round keys in DES."""
  s =  k[shift:] + k[:shift]
  return s  

def txt_to_hex(txt: str) -> str:
  """Convert ASCII string to hexadecimal string. Useful for preprocessing the key and plaintext in different settings."""
  return hexlify(txt.encode()).decode()

def hex_to_txt(txt: str) -> str:
  """Convert hexadecimal string to ASCII string.Useful for preprocessing the key and plaintext in different settings."""
  return unhexlify(txt.encode()).decode()

def hex_to_bin(txt: str) -> str:
  """Convert hexadecimal string to binary string.Useful for preprocessing the key and plaintext in different settings."""
  return bin(int(txt,16))[2:]

def bin_to_hex(txt: str) -> str:
  """Convert binary string to ASCII string.Useful for preprocessing the key and plaintext in different settings."""
  return hex(int(txt,2))[2:]

def calc_diff(arr1: List[List[str]], arr2: List[List[str]]) -> List[int]:
  """Calculate positionwise difference of two List of List of iterables(eg. List of List of strings). This is used for plotting the avalanche effect induced during each round of DES."""
  diff = []
  for i in range(len(arr1[0])):
    cnt = 0
    for j in range(len(arr1)):
      for (c,d) in zip(arr1[j][i], arr2[j][i]):
        if(c != d):
          cnt += 1
    diff.append(cnt)
  return diff

def generate_PC_1(size: int) -> List[int]:
  """A non-classical DES function used to generate Permuted Choice 1 array of a given size. This array is used to drop parity bits of the key in DES."""
  arr = [x for x in range(1,size+1) if x%8 != 0]
  shuffle(arr)
  return arr

def generate_PC_2(size: int, n: int) -> List[int]:
  """A non-classical DES function used to generate the Permuted Choice 2 array of length (size - n). This array is used to generate an equivalent length round key as the plaintext block in the round function of DES. It returns an 1-indexed array."""
  pos = sample(range(size),n)
  arr = []
  for i in range(size):
    if(i not in pos):
      arr.append(i+1)
  shuffle(arr)
  return arr

def generate_initial_perm(size: int) -> List[int]:
  """A non-classical DES function used to generate 1-indexed initial permutation array of a given size. The generated array is used to permute the plaintext before a round of DES. Returns an 1-indexed array."""
  arr = [x for x in range(1,size+1)]
  shuffle(arr)
  return arr

def generate_expansion(size: int, n: int) -> List[int]:
  """A non-classical DES function used to generate expansion array of a length (size + n). This function is used to increase the length of plaintext block to match the size of the roundkey in DES. Returns an 1-indexed array."""
  arr = [x for x in range(1,size+1)]
  pos = sample(range(1,size+1),n)
  for i in pos:
    arr.append(i)
  shuffle(arr)
  return arr

def generate_permutation(size: int) -> List[int]:
  """A non-classical DES function used to generate permutation array of a given size. The returned array is used to permute the output of the S-box in a round of DES. Returns an 1-indexed array."""
  arr = [x for x in range(1,size+1)]
  shuffle(arr)
  return arr

def generate_final_perm(size: int) -> List[int]:
  """A non-classical DES function used to generate final permutation array of a given size. The returned array is used to permute rouond ciphertexts produced before applying the inverse initial permutation. Returns an 1-indexed array."""
  arr = [x for x in range(1,size+1)]
  shuffle(arr)
  return arr

def generate_inverse(arr: List[int]) -> List[int]:
  """A non-classical DES function used to generate inverse initial permutation array (positionwise inverse) from the initial permutation array. Returns an 1-indexed array."""
  inv = [0 for i in range(len(arr))]
  for i,x in enumerate(arr):
    inv[x-1] = i+1 # Assuming numbers in the array start from 1
  return inv

def mutate(txt: str, hamming_dist: int) -> str:
  """Alter the given txt at some hamming_dist number of positions. This is used to experimentally determine how the avalanche effect varies with hamming distance in DES. """
  length = len(txt)
  random_pos = sample(range(0,length),hamming_dist)
  random_pos.sort() # To ensure the for loop below doesnot increase the length of txt
  mutated_txt = ""
  i = 0
  for pos in random_pos:
    mutated_txt += txt[i:pos]
    i = pos+1
    if(txt[pos] == '1'):
      mutated_txt += '0'
    else:
      mutated_txt += '1'
  
  mutated_txt += txt[i:]
  return mutated_txt

def preprocess_plaintext(plaintext: str, halfwidth: int =32, hamming_dist: int =0) -> List[str]:
  """Left pad the binary plaintext string with 0s and ham the same with the specified hamming distance to make plaintext blocks of appropriate sizes for use in DES."""
  length = 2*halfwidth
  x = len(plaintext)%length
  if(x != 0):
    x = length - x
  plaintext = '0'*x + plaintext

  if(hamming_dist != 0):
    plaintext = mutate(plaintext,hamming_dist)

  # Make 2*halfwidth bit blocks of plaintext
  pt_arr = []
  i=0
  while(i+length <= len(plaintext)):
    pt_arr.append(plaintext[i:i+length])
    i += length
  return pt_arr

def preprocess_key(key: str, halfwidth:int =32, hamming_dist:int =0) -> str:
  """Left pad the binary key string if necessary(useful in ASCII setting) and make the keylength appropriate for DES."""
  if(len(key) > 2*halfwidth):
    key = key[:2*halfwidth]
  key = key.zfill(2*halfwidth)

  if(hamming_dist != 0):
    key = mutate(key,hamming_dist)

  return key

def generate_round_keys(key: str, rounds: int =16, halfwidth: int =32) -> Tuple[List[str], List[str]]:
  """Generates the Round keys for DES given appropriate binary key string, number of rounds to be used in DES and the halfwidth of the plaintext and key to be used. This is a function common to both classical and non-classical DES. Returns a list of round keys in binary and hexadecimal format."""
  # shifts for rounds <= 16; else shifted by 1
  shift_table = [ 1, 1, 2, 2, 
                  2, 2, 2, 2, 
                  1, 2, 2, 2, 
                  2, 2, 2, 1 ]

  if(halfwidth == 32):
    # Drop parity bits (Permuted Choice-1)
    PC_1 = [ 57, 49, 41, 33, 25, 17, 9, 
            1, 58, 50, 42, 34, 26, 18, 
            10, 2, 59, 51, 43, 35, 27, 
            19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 
            7, 62, 54, 46, 38, 30, 22, 
            14, 6, 61, 53, 45, 37, 29, 
            21, 13, 5, 28, 20, 12, 4 ]
    # Reduce keysize from 56 to 48 bits (Permuted Choice-2)
    PC_2 = [ 14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]
  else:
    PC_1 = generate_PC_1(2*halfwidth)
    PC_2 = generate_PC_2(len(PC_1), halfwidth//4)
      
  # Applying permuted choice-1 for dropping the parity bits in the key
  key = permute(key, PC_1, len(PC_1))

  # Splitting 
  half = len(key)//2
  left = key[0:half]
  right = key[half:] 

  rkb = [] # RoundKeys in binary
  rkh = [] # RoundKeys in hexadecimal
  for i in range(rounds): 
    #  Shifting (take care of rounds)
    if(i < 16): # Use standard shifting table for upto 16th round
      left = shift_left(left, shift_table[i])
      right = shift_left(right, shift_table[i])
    else: # Use a shift of 1 for rounds more than 16
      left = shift_left(left,1)
      right = shift_left(right,1)

    # Combining 
    combine = left + right 

    # Key Compression 
    RoundKey = permute(combine, PC_2, len(PC_2))
    rkb.append(RoundKey)
    RoundKey = bin_to_hex(RoundKey)
    rkh.append(RoundKey)
  
  return (rkb, rkh)

def encrypt(plaintext_arr: List[str], rkb: List[str], rounds: int =16, halfwidth: int =32) -> Tuple[str, List[str]]:
  """Encrypts plaintext and returns final hexadecimal ciphertext and binary round ciphertexts for calculating avalanche effect."""
  s_box = [
          [ 
            [ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
          ], 
          [ 
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
          ], 
          [ 
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
          ],
          [ 
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]
          ], 
          [ 
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
          ],
          [ 
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]
          ], 
          [ 
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]
          ],
          [ 
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 
          ]
      ]    
  
  if(halfwidth == 32):
    s_box_size = 8
  elif(halfwidth == 16):
    s_box_size = 4
  else:
    s_box_size = 16
  
  if(halfwidth == 32):
    initial_perm = [ 58, 50, 42, 34, 26, 18, 10, 2, 
                  60, 52, 44, 36, 28, 20, 12, 4, 
                  62, 54, 46, 38, 30, 22, 14, 6, 
                  64, 56, 48, 40, 32, 24, 16, 8, 
                  57, 49, 41, 33, 25, 17, 9, 1, 
                  59, 51, 43, 35, 27, 19, 11, 3, 
                  61, 53, 45, 37, 29, 21, 13, 5, 
                  63, 55, 47, 39, 31, 23, 15, 7 ]
    expansion = [ 32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9, 
                8, 9, 10, 11, 12, 13, 
                12, 13, 14, 15, 16, 17, 
                16, 17, 18, 19, 20, 21, 
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1 ] 
    permutation = [ 16, 7, 20, 21, 
                    29, 12, 28, 17, 
                    1, 15, 23, 26, 
                    5, 18, 31, 10, 
                    2, 8, 24, 14, 
                    32, 27, 3, 9, 
                    19, 13, 30, 6, 
                    22, 11, 4, 25 ]
    final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
                39, 7, 47, 15, 55, 23, 63, 31, 
                38, 6, 46, 14, 54, 22, 62, 30, 
                37, 5, 45, 13, 53, 21, 61, 29, 
                36, 4, 44, 12, 52, 20, 60, 28, 
                35, 3, 43, 11, 51, 19, 59, 27, 
                34, 2, 42, 10, 50, 18, 58, 26, 
                33, 1, 41, 9, 49, 17, 57, 25 ]
    inv_initial_perm = generate_inverse(initial_perm)
  else:
    initial_perm = generate_initial_perm(2*halfwidth)
    expansion = generate_expansion(halfwidth,len(rkb[0]) - halfwidth)
    permutation = generate_permutation(halfwidth)
    final_perm = generate_final_perm(2*halfwidth)
    inv_initial_perm = generate_inverse(initial_perm)

  final = ""
  round_ciphertexts = []
  
  for plaintext in plaintext_arr:
    plaintext = permute(plaintext, initial_perm, len(initial_perm))

  for plaintext in plaintext_arr:
    left = plaintext[0:halfwidth]
    right = plaintext[halfwidth:]
    rct = []
    for i in range(rounds): 
      right_expanded = permute(right, expansion, len(expansion)) 
      x = xor(rkb[i], right_expanded) 
      op = ""
      for i in range(s_box_size):
          part = x[i*6:(i+1)*6]
          row = part[0] + part[5]
          row = int(row,2)
          col = part[1:-1]
          col = int(col,2)
          val = s_box[i%8][row][col] # mod 8 because of using same S-boxes circularly for a 64 bit halfwidth
          op += bin(val)[2:].zfill(4)
      
      # Simple permutation
      op = permute(op, permutation, len(permutation))

      # XOR of left and op 
      x = xor(op, left)
      left = x
      
      # Swaping at the end of each round
      if (i != rounds-1): # This ensures that we undo the swapping in the last round
          left, right = right, left
      
      rct.append(str(left+right))
    round_ciphertexts.append(rct)

    # Combine the halves
    combine = left + right
    # Final Permutation 
    ciphertext = permute(combine, final_perm, len(final_perm))
    ciphertext = permute(ciphertext, inv_initial_perm, len(inv_initial_perm))
    final += ciphertext

  final = bin_to_hex(final)
  return (final, round_ciphertexts)