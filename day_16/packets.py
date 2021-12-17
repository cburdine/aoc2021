#!/bin/env python3

import sys

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
    val = 0
    ptr = 6

    if t == 4:
        num = [] 
        while bits[ptr] != '0':
            num.extend(bits[ptr+1:ptr+5])
            ptr += 5
        num.extend(bits[ptr+1:ptr+5])
        
        val = int(''.join(num))
        return v, bits[ptr+5:]

    else:
        I = bits[ptr]
        ptr += 1
        if I == '0':
            pkts_len = bits_to_int(bits[ptr:ptr+15])
            ptr += 15
            subpkts = bits[ptr:ptr+pkts_len]
            while subpkts:
                subval, subpkts = decode_packets(subpkts) # len
                val += subval
            ptr += pkts_len
            
            return val+v, bits[ptr:]
        else:
            n_pkts = bits_to_int(bits[ptr:ptr+11])
            ptr += 11
            bits = bits[ptr:]
            for _ in range(n_pkts):
                subval, bits = decode_packets(bits) # npkts
                val += subval
            
            return val+v, bits
        
def main():
    pkts = sys.stdin.readlines()[0].strip()
    bits = hex_to_bits(pkts)

    vsum, _ = decode_packets(bits)
    print('vsum: ', vsum)

if __name__ == '__main__':
    main()
