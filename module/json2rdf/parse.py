# -*- coding:utf-8 -*-

import json
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

# create a graph
g = Graph()
donna = BNode()

g.add((donna, RDF.type, FOAF.Person))
g.add((donna, FOAF.nick, Literal('donna', lang='foo')))
g.add((donna, FOAF.name, Literal('Donna Fales')))
g.add((donna, FOAF.mbox, URIRef('mailto:donna@example.org')))

for s, p, o in g:
    print((s, p, o))

for person in g.subjects(RDF.type, FOAF.Person):
    for mbox in g.objects(person, FOAF.mbox):
        print(mbox)

g.bind('dc', DC)
g.bind('foaf', FOAF)