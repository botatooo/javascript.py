

# ----- Functions -----
def function(name, *args):
    fn = list(args).pop()
    if name.lower() == 'anon':
        return exec(f'def {name}({", ".join(args)}):\n{fn}')
    exec(f'global {name}\ndef {name}({", ".join(args[:-1])}):\n\t{fn}')

# ----- Console -----
class console (object):
    def log(*args):
        print(*args)
    
    def debug(*args):
        print(*args)
    
    def error(*args):
        raise Exception(*args)
    
    def clear(*args):
        print('\n'*100)

# ----- Object -----
def new(obj: str):
    return eval(obj)

# ----- Array -----
class Array (list):
    def __init__(self, array):
        self.array = array
        
        length = len(self.array)
        push = super().append

    def map(self, func):
        return map(self.array, func)


# ----- String -----
class String (str):
    pass

# ----- Integer -----
def parseInt()

# ----- Boolean -----
true = True
false = False

#  ----- None -----
null = None
