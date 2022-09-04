import numpy as np
import json
import os

import burnside_encryption as bse
import burnside_multplication as bsm

# read multiplication table file
infile = [np.asarray(json.loads(line)) for line in open(os.path.abspath(os.pardir) + '\z2_s4_001.json', 'r')]
mixer_index = infile[0]
M = infile[1] #multipliers
T = infile[2] #multiplication table

assert T.shape[0] == T.shape[1] == T.shape[2]
len_T = T.shape[0]
print("Number of conjugacy classes: {}" .format(len_T))


assert M.shape[1] == len_T
len_M = M.shape[0]
print("Number of multipliers: {}" .format(len_M))

#print("Multiplier Indices: {}" .format(M))

def run():
    print('---------------------------------------------------')
    msg = input("Enter your message \n")
    print('---------------------------------------------------')
    msg_utf = bse.encode_msg(msg) + bse.set_mixer(mixer_index, "123567")
    print("UTF-8 representation of your message:  \n {}" .format(msg_utf))
    multiplier = bse.brmult_list(T,M)
    encryption = bse.brmult_list(T,[msg_utf,multiplier])
    print('---------------------------------------------------')
    print("UTF-8 representation of encrypted message:  \n {}" .format(encryption))
    decrypt_utf = bse.brmult_list(T,[encryption,multiplier])
    #decrypt = np.char.decode(np.string_(decrypt_utf),'utf-8')
    print('---------------------------------------------------')
    #print("Your decrypted message:  \n {}" .format(decrypt))

run()
