import hashlib
import sys


def witness_to_hex(witness: list[str], size=4):
    ints = map(int, witness)
    return b''.join(map(lambda x: x.to_bytes(size, byteorder='big'), ints))


def pad(hexstr: str, size=32):
    byts = bytes.fromhex(hexstr)
    padded = byts.rjust(size, bytes.fromhex("00"))
    assert(len(padded) == size)
    return padded


def sha256(value):
    h = hashlib.sha256()
    h.update(value)
    return h.digest()


def hash_for_proof(hexstr: str):
    padded = pad(hexstr)
    return sha256(padded)


def split_to_ints(value: str, elem_bytes_len=4):
    return [int(value[i:i+elem_bytes_len].hex(), 16) 
            for i in range(0, len(value), elem_bytes_len)]


if __name__ == "__main__":
    arg = sys.argv[1]
    arg_lst = split_to_ints(pad(arg))
    print("secretValue:", ' '.join(map(str, arg_lst)))

    h = hash_for_proof(arg)
    spl = split_to_ints(h)
    spl = list(map(str, spl))
    print("publicHash:", ' '.join(map(str, spl)))
