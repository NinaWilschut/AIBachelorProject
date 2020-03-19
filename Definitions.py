def cut(files):
    for file in files:
        value = check(file)
        return value

def check(file):
    #with open('example.txt') as f:
        #file = f.readlines()
    for line in file:
        if '<|endoftext|>' in line:
            return True
    return False  # Because you finished the search without finding