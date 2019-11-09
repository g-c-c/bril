### python to bril
# Takes python code and outputs 

import ast


getnode = lambda fname: ast.parse(open(fname).read()) # get node from python filename 'yourfile.py'


#class (ast.NodeTransformer):
#    def makeblock(self, node):
#        return 0





def walk(node):
    b = []
    for s in ast.walk(node):




def writebril(stuff,fname):
    f = open(fname + '.bril', 'w')
    # maybe write python code as comment at top?
    
    f.write('main { \n')
    for s in stuff:
        f.write(s)
    f.write('}')


if __name__ == '__main__':
    ast.dump(ast.parse("print('hello')"))


    colo = open("colors.py").read()
    c = ast.parse(colo)
    ast.dump(c)




### eof
