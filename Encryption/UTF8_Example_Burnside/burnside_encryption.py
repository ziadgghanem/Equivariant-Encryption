
def set_mixer(mixer_index, phrase):
    '''ba = bitarray.bitarray()
    ba.frombytes(m.encode('utf-8'))'''
    mixer = np.zeros(len_T)
    by = np.asarray(bytearray(phrase,'utf-8'))
    mixer[-len(by):] = by
    return mixer


def encode_msg(m):
    '''ba = bitarray.bitarray()
    ba.frombytes(m.encode('utf-8'))'''
    msg_utf = np.asarray([bytearray(m,'utf-8')[i] for i in range(len(bytearray(m,'utf-8')))])
    msg_utf.resize(len_T, refcheck = False)
    #msg = [msg_utf[i] for i in range(len(msg_utf))]
    return msg_utf