from DESfiddle import *

plaintext = "0101010101010101010101010101010101010101010101010101010101010101"
key = "1111111111111111111111111111111100000000000000000000000000000000"
# plaintext = "This is so cool"
# key = "Yesss"
nor = 16
halfwidth = 32
hamming_dist = 1

def __pretty_print(RoundKeys):
    s = "Number of unique roundkeys: " + str(len(set(RoundKeys))) + "\n"
    for i in range(len(RoundKeys)):
            s += "Round "+str(i+1)+":\t"+str(RoundKeys[i])+"\n"
    return s.strip()

# Preprocessing when input in ASCII
# plaintext = txt_to_hex(plaintext)
# plaintext = hex_to_bin(plaintext)
# key = txt_to_hex(key)
# key = hex_to_bin(key)

# Ham the plaintext
ref_pt_arr = preprocess_plaintext(plaintext, halfwidth)
pt_arr = preprocess_plaintext(plaintext, halfwidth, hamming_dist)
key = preprocess_key(key, halfwidth)
rkb,rkh = generate_round_keys(key,nor, halfwidth)
ref_ciphertext, ref_round_ciphert
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
output = __pretty_print(rkh)

print(output, "\n", diff);


# Ham the key
pt_arr = preprocess_plaintext(plaintext, halfwidth)
ref_key = preprocess_key(key,halfwidth)
key = preprocess_key(key, halfwidth, hamming_dist)
ref_rkb, ref_rkh = generate_round_keys(ref_key, nor, halfwidth)
rkb,_ = generate_round_keys(key, nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(pt_arr, ref_rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
output = __pretty_print(rkh)

print(output, "\n", diff);