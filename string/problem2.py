# Get max substring with char repetition.

def get_sub_string(strg):
    # largest = ""
    # for i in range(0, len(strg)):
    #     sec_largest = ""
    #     for j in range(i, len(strg)):
    #         if strg[j] not in sec_largest:
    #             sec_largest = sec_largest + strg[j]
    #             largest = sec_largest if len(largest) < len(sec_largest) else largest
    #         else:
    #             largest = sec_largest if len(largest) < len(sec_largest) else largest
    #             sec_largest = ""

    largest = ""
    s_largest = ""
    seen = []
    for i in range(0, len(strg)):
        if strg[i] in seen:
            s_largest = strg[i] if i>0 else ""
        else:
            seen.append(strg[i])
            s_largest = s_largest+strg[i]
            largest = s_largest if len(s_largest)>len(largest) else largest

    return largest



print(get_sub_string("abcadhgfdsaefgh"))