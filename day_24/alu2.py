#!/bin/env python3

import sys

def extract_dab_vals(instrs, ops):
    """
        loop takes the form of:
            w -> w' := w
            x -> x' := ((z % 26)+a != w)
            y -> y' := (x'*(w+b))
            z -> z' := (z//d)*(25*x' + 1) + y'
            
            where only the d,a,b variables vary in each iteration            
            
            note that the return values of x and y are
            discarded after each loop iteration
    """

    dab_vals = []
     
    for p in range(0,len(instrs),18):
        assert(instrs[p+0] == 'inp')
        
        assert(instrs[p+4] == 'div' and ops[p+4][0] == 'z')
        d = ops[p+4][1]

        # extract a value:
        assert(instrs[p+5] == 'add' and ops[p+5][0] == 'x')
        a = ops[p+5][1]
        
        # extract b value:
        assert(instrs[p+15] == 'add' and ops[p+15][0] == 'y')
        b = ops[p+15][1]

        dab_vals.append((d,a,b))

    return dab_vals


def search(dab_vals, z=0, n=0, cache={}):
    if n >= len(dab_vals):
        if z == 0:
            return []
        return None
    
    if (n,z) in cache:
        return cache[(n,z)]        
        
    d, a, b = dab_vals[n]
    print('solving: ', n, z)
    for w in range(9,0,-1):
        z_next = z//d
        
        # note: this condition is met when d == 1
        if w != (z%26) + a:
            z_next *= 26
            z_next += (w+b)
            
            if d != 1:
                continue 
        
        if (res := search(dab_vals,z_next, n+1,cache)) != None:
            return [w] + res
    
    cache[(n,z)] = None    
    return None
    
def main():   

    lines = sys.stdin.readlines()
    instrs = []
    ops = []
    
    for line in lines:
        tokens = line.strip().split(' ')
        instrs.append(tokens[0])
        op = tuple( 
               t if t in 'wxyz' else int(t) 
               for t in tokens[1:] 
             )
        ops.append(op)

    dab_vals = extract_dab_vals(instrs, ops)
    print('d/a/b values: ', dab_vals)
    
    result = search(dab_vals)
    print('largest result: ', ''.join(map(str,result)))

if __name__ == '__main__':
    main()
