#!/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict
from itertools import product, permutations

class ScanData:
    
    def __init__(self, data):
        self.data = data
        self.matches = {}

        # compute heuristic kernel:
        self.K = [ defaultdict(lambda: 0) for _ in self.data ]
        for i, d1 in enumerate(self.data):
            for j, d2 in enumerate(self.data):
                if i < j:
                    k = sum((xi-xj)**2 for xi,xj in zip(d1,d2))
                    self.K[i][k] += 1
                    self.K[j][k] += 1
    
    def kernel_overlap_matrix(self, oth):

        # determine overlap kernel:
        matrix = [ [ 0 for _ in oth.data ] for _ in self.data ]
        for i, d in enumerate(self.data):
            for j, od in enumerate(oth.data):
                joint_dists = (set(self.K[i].keys()) & set(oth.K[j].keys()))
                for dist in joint_dists:
                    #if dist in self.K[i] and dist in oth.K[j]:
                    matrix[i][j] += min(self.K[i][dist], oth.K[j][dist])
        
        return matrix

    def kernel_overlap_dist(self,oth):
        return sum(max(row) for row in self.kernel_overlap_matrix(oth))
    
    def data_views(self):
        # TODO: make this correct by only using determinant 1 transformations:
        axis_perms = permutations([0,1,2])
        sgns = [-1,1]
        
        for transform in product(axis_perms,sgns,sgns,sgns):
            p, sx,sy,sz = transform
            yield transform, [
                (d[p[0]]*sx,d[p[1]]*sy,d[p[2]]*sz)
                for d in self.data
            ]
                
    def try_match(self, oth, min_overlap=12):
        self_set = set(self.data)
        K_overlap = self.kernel_overlap_matrix(oth)       
        pt_pairs = list(product(range(len(self.data)),range(len(oth.data))))
        pt_pairs.sort(key=lambda x: -K_overlap[x[0]][x[1]])

        for (i,j) in pt_pairs:
            for transform, oth_view in oth.data_views():
                y0 = self.data[i]
                x0 = oth_view[j]
                oth_x0_set = set(
                    tuple(y0i + (xi-x0i) for xi,x0i,y0i in zip(x, x0, y0))
                    for x in oth_view
                )
                n_matches = len(oth_x0_set & self_set)
                if n_matches >= min_overlap:
                    merge_data = list(oth_x0_set | self_set)
                    return ScanData(merge_data)
 
def generate_matching_order(sd):
    kernel_overlaps = {}
    for i, s1 in enumerate(sd):
        for j, s2 in enumerate(sd):
            if i < j:
                kernel_overlaps[(i,j)] = s1.kernel_overlap_dist(s2)
    return sorted(kernel_overlaps.items(), key=lambda x : -x[1])
    


def main():
    lines = sys.stdin.readlines()
    sd = []
    read_data = []
    
    for line in lines:
        if len(line.strip()) == 0:
            sd.append(ScanData(read_data))
            read_data = []
            continue
        if line[:3] == '---':
            continue

        read_data.append(tuple(
            int(tok) for tok in
            line.strip().split(',')
        ))
    if read_data:
        sd.append(ScanData(read_data))
    
    while len(sd) > 1:
        matching_order = generate_matching_order(sd)
        for (im,jm), _ in matching_order:
            if (result := sd[im].try_match(sd[jm])) != None:
                print('Matched: ', (im,jm))
                sd = [
                    s for k, s in enumerate(sd) 
                    if (k != im and k != jm) 
                ] + [result]
                break            

    print('#beacons: ', len(sd[0].data))


if __name__ == '__main__':
    main()
