# Get max substring with char repetition.

def get_sub_string(strg):
    largest = ""
    for i in range(0, len(strg)):
        sec_largest = ""
        for j in range(i, len(strg)):
            largest = sec_largest if len(largest) < len(sec_largest) else largest
            if strg[j] not in sec_largest:
                sec_largest = sec_largest + strg[j]
            else:
                sec_largest = ""

    return largest



print(get_sub_string("abcadfrgthy"))