import hashlib


def hash_mdp(mdp) -> str:
    mdp_c = mdp.encode('utf-8')
    hash1 = hashlib.sha256()
    hash1.update(mdp_c)

    return hash1.hexdigest()
