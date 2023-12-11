from ipld import multihash

def lakathash(data: bytes) -> str:
    return multihash(data = data, fn_name = 'sha2_256')