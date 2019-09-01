from collections import Counter
import re


def most_wanted(text: str) -> str:
    count = Counter(re.sub(r'[^a-z]', '', text.lower()))
    max_val = max(count.values())
    return sorted([k for k, v in count.items() if v == max_val])


if __name__ == '__main__':
    assert most_wanted("Lorem ipsum dolor sit amet 0000000000000000000") == ["m","o"]
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")
