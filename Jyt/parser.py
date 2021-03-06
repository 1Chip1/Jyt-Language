from ast import keyword
from lib2to3.pgen2 import token
from operator import truediv


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = []

    def add_node(self, parent, node):
        for a in self.AST:
            if parent in a:
                a[parent].append(node)

    def build_AST(self):
        saved = {}
        parent = {}
        collect = False

        for token in self.tokens:
            if token['id'] == 'label':
                t = {token['value']: []}

                if parent != t:
                    parent = token['value']
                    self.AST.append(t)
            
            elif token['id'] == 'keyword':
                if token['value'] == 'end':
                    t = {token['value']: 0}
                    self.add_node(parent, t)
                else:
                    if collect == False:
                        saved = token
                        collect = truediv
                    else:
                        t = {saved['value']: token['value']}
                        self.add_node(parent,t)
                        collect = False
            
            elif token['id'] == 'char':
                if collect == False:
                    saved = token
                    collect = True
                else:
                    t = {saved['value']: token['value']}
                    self.add_node(parent,t)