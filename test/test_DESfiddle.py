import unittest
from DESfiddle.utils import *

class Test(unittest.TestCase):
  def test_permute(self):
    expected_result = "eiacfgbdh"
    self.assertEqual(permute("abcdefghi", [5, 9, 1, 3, 6, 7, 2, 4, 8], 9), expected_result)
  
  def test_xor(self):
    expected_result = "1110110"
    self.assertEqual(xor("1010001","0100111"), expected_result)
    
  def test_shift_left(self):
    expected_result = "defghiabc"
    self.assertEqual(shift_left("abcdefghi", 3), expected_result)
  
  def test_txt_to_hex(self):
    expected_result = "444553666964646c65"
    self.assertEqual(txt_to_hex("DESfiddle"), expected_result)
  
  def test_hex_to_txt(self):
    expected_result = "DESfiddle"
    self.assertEqual(hex_to_txt("444553666964646c65"), expected_result)
  
  def test_hex_to_bin(self):
    expected_result = "10001000100010101010011011001100110100101100100011001000110110001100101"
    self.assertEqual(hex_to_bin("444553666964646c65"), expected_result)
  
  def test_bin_to_hex(self):
    expected_result = "444553666964646c65"
    self.assertEqual(bin_to_hex("10001000100010101010011011001100110100101100100011001000110110001100101"), expected_result)

  def test_calc_diff(self):
    expected_result = [3, 0, 1]
    self.assertEqual(calc_diff([["1010", "11", "1011"]], [["0001", "11", "1111"]]), expected_result)
  
  def test_generate_PC_1(self):
    arr = generate_PC_1(64)
    for i in range(8, 80, 8):
      self.assertNotIn(i,arr)

  def test_generate_PC_2(self):
    expected_result = 56
    self.assertEqual(len(generate_PC_2(64, 8)), expected_result)
  
  def test_generate_initial_perm(self):
    expected_result = 64
    self.assertEqual(len(generate_initial_perm(64)), expected_result)

  def test_generate_expansion(self):
    expected_result = 72
    self.assertEqual(len(generate_expansion(64, 8)), expected_result)
  
  def test_generate_permutation(self):
    expected_result = 64
    self.assertEqual(len(generate_permutation(64)), expected_result)
  
  def test_generate_final_perm(self):
    expected_result = 64
    self.assertEqual(len(generate_final_perm(64)), expected_result)
  
  def test_generate_inverse(self):
    arr = [7,2,4,5,1,3,6]
    expected_result = arr
    self.assertEqual(generate_inverse(generate_inverse(arr)), expected_result)
  
  def test_mutate(self):
    expected_result = 4
    s = mutate("101010101", 4)
    cnt = 0
    for c, d in zip(s, "101010101"):
      if (c != d):
        cnt = cnt + 1
    self.assertEqual(cnt, expected_result)

  def test_preprocess_plaintext(self):
    expected_result = ['0000000000010110', '0101010101010011', '0111001001100111']
    self.assertEqual(preprocess_plaintext("1011001010101010100110111001001100111", 8), expected_result)
    
  def test_preprocess_key(self):
    expected_result = "10101101"
    self.assertEqual(preprocess_key("10101101011011111010001000", 4), expected_result)
  
  def test_generate_round_keys(self):
    expected_result = (['100001001110101100010110110001011011010011011001', '101001100110011100000110111010011011011011011001', '011010100001011100000101011110111101011000101011', '010010011001000001111001000111100101110100101110', '100001011100000011111010100011000111100111110100', '101101100100101110000010111000011110101011110001', '001110100011101100000001111100111000111000011011', '000010010011010001011101100111110001011100011110', '000010010110010011011100100111010001011110100110', '010101000100010110111000010111000110101011100101', '110101101000100100100001011100101110100011011101', '100010111010101000000111101000111011010110011011', '001010010011011010001110101011110011011100100011', '011100000001010011101000011111100100101101100110', '110100001100100001110000010101001100100111011110', '100101001110100001110010110001001010110111011100'], ['84eb16c5b4d9', 'a66706e9b6d9', '6a17057bd62b', '4990791e5d2e', '85c0fa8c79f4', 'b64b82e1eaf1', '3a3b01f38e1b', '9345d9f171e', '964dc9d17a6', '5445b85c6ae5', 'd6892172e8dd', '8baa07a3b59b', '29368eaf3723', '7014e87e4b66', 'd0c87054c9de', '94e872c4addc'])
    self.assertEqual(generate_round_keys("1111111111111111111111111111111100000000000000000000000000000000"), expected_result)
  
  def test_encrypt(self):
    plaintext_arr = ["0101010101010101010101010101010101010101010101010101010101010101"]
    key = "1111111111111111111111111111111100000000000000000000000000000000"
    rkb, _ = generate_round_keys(key)
    ciphertext, _ = encrypt(plaintext_arr, rkb)
    expected_result = "41a856e3be1978bc"
    self.assertEqual(ciphertext, expected_result)

if __name__ == "__main__":
  unittest.main()