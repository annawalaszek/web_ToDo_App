def get_todos(file_patch=r'todo.txt', mood='r', encode='utf8'):
    '''Read data from text file and return list type variable.'''
    with open(file_patch, mood, encoding=encode) as _:
        local_todos = _.readlines()
        return local_todos


def set_todos(file_patch=r'todo.txt', mood='w', encode='utf8', list=[]):
    '''Write data (list) to text file.'''
    with open(file_patch, mood, encoding=encode) as f:
        f.writelines(list)


def created():
    return 'made by annnevvv'


if __name__ == '__main__':
    print('Hello from TDfunction modul')
