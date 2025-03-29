from pprint import pprint
import typing
from pyfsig.constants import FileSignatureDict


def _process_file_signature_test_hex(test_hex: str) -> list[int | None]:
    """Converts from the wikipedia format to a list of utf-8 ordinals"""
    test_hex_list = test_hex.strip().split(" ")
    return [ord(bytes.fromhex(x)) if x != "nn" else None for x in test_hex_list]


SIGNATURES: list[FileSignatureDict] = []

new_signatures = []
for sig in SIGNATURES:
    file_ext = sig["file_extension"]

    new_hex = _process_file_signature_test_hex(sig["hex"])
    new_string = "".join([chr(x) if x is not None else "." for x in new_hex])
    new_printable_string = "".join([x if x.isprintable() else "." for x in new_string])

    new_signatures.append(
        {
            "display_string": new_printable_string,
            "description": sig["description"],
            "file_extension": sig["file_extension"],
            "hex": new_hex,
            "offset": sig["offset"],
        }
    )

pprint(new_signatures, indent=4, width=120)
