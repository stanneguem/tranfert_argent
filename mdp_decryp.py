import hashlib
from mdp_protect import hash_mdp


def verif_mdp(hashe, mdp) -> bool:
    mdp1 = hash_mdp(mdp)

    if mdp1 == hashe:
        return True
    else:
        return False