'''
def main(name):
    
    for l in name:
        l = "*"
        print(l)

main('Brendan')
'''

def mask(name):
    li = ""
    for l in name:
        li += " " if l == " " else "*"
    return li
print(mask("Brendan Cormier"))