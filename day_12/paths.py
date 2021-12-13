#!/bin/env python3

import sys



def search(graph, start,  end, marks):
    if start == end:
        return 1

    result = 0
    for adj in (graph[start] - marks):
        if not adj.isupper():
            result += search(graph, adj, end, (marks | {adj} ))
        else:
            result += search(graph, adj, end, marks)

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

    
    n_paths = search(graph, 'start','end',{'start'})
    print('#paths: ', n_paths)

if __name__ == '__main__':
    main()
