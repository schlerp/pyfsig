import hashlib
import json

import pyfsig

def test_redundant_file_signatures():
    hmap = {}

    for signature in pyfsig.SIGNATURES:
        hash = hashlib.md5(json.dumps(signature).encode("utf-8")).hexdigest()
        if hash in hmap:
            print(f"Found two colliding hashes ({hash}):\n{hmap[hash]} &\n{signature}")
        else:
            hmap[hash] = signature


def test_known_file_header_matches():
    file_header = bytearray([237, 171, 238, 219])
    print(file_header)
    matches = pyfsig.find_matches_for_file_header(file_header)
    assert matches
    assert len(matches) == 1
    assert matches[0].file_extension == "rpm"


def test_unknown_file_header_doesnt_match():
    file_header = bytearray([123, 123, 123, 123, 123, 123, 123])
    print(file_header)
    matches = pyfsig.find_matches_for_file_header(file_header)
    assert not matches


def test_known_file_header_matches_with_offset():
    file_header = bytearray([0, 0, 0, 0, 102, 116, 121, 112, 51, 103])
    matches = pyfsig.find_matches_for_file_header(file_header)
    assert matches
    file_exts = [match.file_extension for match in matches]
    assert "3gp" in file_exts
    assert "3g2" in file_exts


def test_empty_file_header_doesnt_match():
    file_header = bytearray()
    matches = pyfsig.find_matches_for_file_header(file_header)
    assert not matches

