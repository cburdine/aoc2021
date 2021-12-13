#!/bin/env python3

import sys



def search(graph, start, end, marks, p):
    if start == end:
        print(p + ['end'])
        return 1

    result = 0
    adj_smalls = set(marks.keys())
    for adj in (graph[start] - adj_smalls):
        if adj.islower():
            result += search(graph, adj, end, (marks | {adj: 1} ), p+[adj])
        else:
            result += search(graph, adj, end, marks, p+[adj])
    
    if max(marks.values()) <= 1:
        for adj in (graph[start] & adj_smalls):
            if adj not in ['start','end']:
                result += search(graph, adj, end, (marks | {adj:2} ), p+[adj])


    return result

def main():
    lines = sys.stdin.readlines()
    graph = {}
    
    for line in lines:
        tokens = line.split('-')
        a = tokens[0].strip()
        b = tokens[1].strip()
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

    
    n_paths = search(graph, 'start','end',{'start':1},p=['start'])
    print('#paths: ', n_paths)

if __name__ == '__main__':
    main()
