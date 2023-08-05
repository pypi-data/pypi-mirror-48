from terrarium import constants as C
from uuid import uuid4


def make_hash(*args, sep="-"):
    """Returns a hash string composed of several tokens"""
    return sep.join([str(_) for _ in args])


def external_aft_hash(aft):
    if not aft["field_type_id"]:
        return str(uuid4())
    return make_hash(
        aft[C.MODEL_CLASS],
        aft["object_type_id"],
        aft["sample_type_id"],
        aft["field_type"]["part"] is True,
    )


def internal_aft_hash(aft):
    return make_hash(aft[C.MODEL_CLASS], aft["field_type"]["parent_id"])


def edge_hash(pair):
    h = "{}->{}".format(external_aft_hash(pair[0]), external_aft_hash(pair[1]))
    return make_hash(
        pair[0]["field_type"]["parent_id"], h, pair[1]["field_type"]["parent_id"]
    )
