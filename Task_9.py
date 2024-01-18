import os

def common_substring(list):
    common_substring = os.path.commonprefix(list)
    return common_substring

print(common_substring(["flower","flow","flight"]))
print(common_substring(["dog","racecar","car"]))
