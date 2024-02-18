
# CrazyFrogSound => crazy_frog_sound



def convert_camel_to_snake(text):
    # iterate
    j = 0
    res = ""
    for char in text:
        if char.isupper():
            if j == 0:
                res += char.lower()
            else:
                res += "_" + char.lower()
        else:
            res += char
        j += 1
    return res

s = "CrazyFrogSound"

new_title = convert_camel_to_snake(s)
print(new_title)