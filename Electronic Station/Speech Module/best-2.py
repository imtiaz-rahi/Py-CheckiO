# https://py.checkio.org/mission/speechmodule/publications/veky/python-3/first/
# migrated from python 2.7
def checkio(number):
    l=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
    d=dict(enumerate(l))
    d.update({30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"})
    h=number//100
    if h:
        return (d[h]+" hundred "+checkio(number%100)).strip()
    if number in d:
        return d[number]
    return d[number//10*10]+" "+d[number%10]

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print('All ok')
