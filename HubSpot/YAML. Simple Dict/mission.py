def yaml(a):
    rs = {}
    for it in a.split("\n"):
        if len(it) == 0: continue
        k, v = it.split(":")
        v = v.strip()
        rs[k] = int(v) if v.isdigit() else v
    return {k: v for k, v in sorted(rs.items())}


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}

    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
