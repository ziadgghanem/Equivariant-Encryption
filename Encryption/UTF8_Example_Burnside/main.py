import numpy as np
import json
import os

import resources 

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

if __name__ == "__main__":
    print('---------------------------------------------------')
    msg = input("Enter your message \n")
    print('---------------------------------------------------')
    msg_utf = resources.encode_msg(msg, len_T) + resources.set_mixer(mixer_index, len_T, "123567")
    print("UTF-8 representation of your message:  \n {}" .format(msg_utf))
    multiplier = resources.brmult_list(T,M)
    encryption = resources.brmult_list(T,[msg_utf,multiplier])
    print('---------------------------------------------------')
    print("UTF-8 representation of encrypted message:  \n {}" .format(encryption))
    print('---------------------------------------------------')
    decrypt_utf = resources.brmult_list(T,[encryption,multiplier])
    print("UTF-8 representation of decrypted message:  \n {}" .format(decrypt_utf))
    #decrypt = np.char.decode(np.string_(decrypt_utf),'utf-8')
    print('---------------------------------------------------')
    #print("Your decrypted message:  \n {}" .format(decrypt))
