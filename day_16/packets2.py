#!/bin/env python3

import sys

def apply_op(op, params):
    if op == 0:
        return sum(params)
    if op == 1:
        p = 1
        for v in params:
            p *= v
        return p
    if op == 2:
        return min(params)
    if op == 3:
        return max(params)
    if op == 5:
        return int(params[0] > params[1])
    if op == 6:
        return int(params[0] < params[1])
    if op == 7:
        return int(params[0] == params[1])
    assert(False)

def hex_to_bits(h):
    bits = []
    for ch in h:
        b = format(int(ch,16),'04b')
        bits.extend(b)
    return bits

def bits_to_int(bstr):
    return int(''.join(bstr),2)

def decode_packets(bits):
    assert(bits)
    v = bits_to_int(bits[:3])
    t = bits_to_int(bits[3:6])
    print('version: ', v)
    print('type: ', t)
    print('bits: ', ''.join(bits))
    val = 0
    ptr = 6

    if t == 4:
        num = [] 
        while bits[ptr] != '0':
            num.extend(bits[ptr+1:ptr+5])
            ptr += 5
        num.extend(bits[ptr+1:ptr+5])
        
        val = int(''.join(num),2)
        print('base packet: ', val)
        return val, bits[ptr+5:]

    else:
        I = bits[ptr]
        ptr += 1
        if I == '0':
            pkts_len = bits_to_int(bits[ptr:ptr+15])
            print(bits[ptr:ptr:15])
            print('pkts_len: ', pkts_len)
            ptr += 15
            subpkts = bits[ptr:ptr+pkts_len]
            subvals = []
            while subpkts:
                subval, subpkts = decode_packets(subpkts) # len
                subvals.append(subval)
            ptr += pkts_len
                        
            print(subvals)
            return apply_op(t,subvals), bits[ptr:]
        else:
            n_pkts = bits_to_int(bits[ptr:ptr+11])
            print('n_pkts: ', n_pkts)
            ptr += 11
            bits = bits[ptr:]
            subvals = []
            for _ in range(n_pkts):
                subval, bits = decode_packets(bits) # npkts
                subvals.append(subval) 

            print(subvals)
            return apply_op(t,subvals), bits
        
def main():
    pkts = sys.stdin.readlines()[0].strip()
    bits = hex_to_bits(pkts)

    result, _ = decode_packets(bits)
    print('result: ', result)

if __name__ == '__main__':
    main()
