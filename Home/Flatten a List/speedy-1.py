# https://py.checkio.org/mission/flatten-list/publications/ciel/python-3/translate_py3/
flat_list=lambda array: eval('['+str(array).translate(str.maketrans('','','[]'))+']')
