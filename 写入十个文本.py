# Author :lixinhao

def test_creation():
    path = '/Users/lixh/Desktop/'
    for name in range(1, 11):
        with open(path + str(name) + '.txt', 'w') as text:
            text.write(str(name))
            text.close()
            print('Done')
test_creation()
