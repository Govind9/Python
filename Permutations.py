all_permutations = set()
def permute (done_str, rem_str):
    if (len(rem_str) == 0):
        all_permutations.add(done_str)
    for i in range(len(rem_str)):
        permute (done_str + rem_str[i], rem_str[:i] + rem_str[i + 1:])
permute ("", "abcda")
