import re


def is_stressful(subj):
    if bool(re.search(r".*[!]{3,}$", subj)) or subj.isupper():
        return True
    regex = r"(h)+[!.-]?(e)+[!.-]?(l)+[!.-]?(p)+(!.)?|" \
            r"(a)+[!.-]?(s)+[!.-]?(a)+[!.-]?(p)+(!.)*|" \
            r"(u)+[!.-]?(r)+[!.-]?(g)+[!.-]?(e)+[!.-]?(n)+[!.-]?(t)+(!.)*"
    return bool(re.search(regex, subj, re.IGNORECASE))
