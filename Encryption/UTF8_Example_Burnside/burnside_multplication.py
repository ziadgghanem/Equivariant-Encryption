# for product of selection pass list ex: brmult_list(T,M,[0,1,2,3])
def brmult_list(T, L, sel = "none"):
    if sel == "none":
        pass
    else:
        L = L[sel,:]
        
    for l in L:
        if all(l == L[0]): # initialize product
            chi = l
        else:
            temp = np.zeros(len(l))
            for i in range(len(l)):
                for j in range(len(l)):
                    temp+= chi[i]*l[j]*T[i][j]
            chi = temp
            #print("-------------------------------------------------------------")
            #print(chi) 
    return chi