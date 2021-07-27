## @file
## @brief functional code generator

import os, sys, re

## base Object (hyper)Graph node
class Object:
    def __init__(self,V):
        self.value = V
        self.nest = []

    def box(self,that):
        if isinstance(that,Object): return that
        raise TypeError(['box',that])

    ## @name dump

    def __repr__(self): return self.dump()

    def dump(self,depth=0,prefix=''):
        return self.head(prefix)

    def head(self,prefix=''):
        gid = f' @{id(self):x}'
        return f'{prefix}<{self.tag()}:{self.val()}>{gid}'

    def tag(self): return self.__class__.__name__.lower()
    def val(self): return f'{self.value}'

    ## @name operator

    def __floordiv__(self,that):
        that = self.box(that)
        self.nest.append(that); return self

class Title(Object): pass

TITLE = Title('functional code generator in Python');print(TITLE)

class IO(Object): pass

class Dir(IO):
    def __init__(self,V):
        super().__init__(V)
        try: os.mkdir(self.value)
        except FileExistsError: pass

class File(IO): pass

class Meta(Object): pass

class Project(Meta):
    def __init__(self,V=None):
        if not V: V = re.sub(r'\.py$','',__file__.split('/')[-1])
        super().__init__(V)
        self.d = Dir(self.value)
        #
        self.vscode()
    def vscode(self):
        self.vscode = Dir('vscode');self.d//self.vscode

## circular implementation
circ = Project()
