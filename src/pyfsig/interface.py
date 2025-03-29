from dataclasses import dataclass
from pyfsig.constants import SIGNATURES, FileSignatureDict


@dataclass(slots=True, frozen=True)
class FileSignature:
    """
    A class to represent a file signature.

    Attributes:
    -----------
    display_string : str | None
        The display string for the file signature.
    description : str | None
        The description of the file signature.
    file_extension : str
        The file extension for the file signature.
    hex : List[Optional[int]]
        The hex values for the file signature. None represents a wildcard during matching.
    offset : int
        The offset from the start of the file for the file signature.

    Methods:
    --------
    as_dict() -> FileSignatureDict:
        Returns the file signature as a dictionary.
    """

    file_extension: str
    hex: list[int | None]
    offset: int
    display_string: str | None = None
    description: str | None = None

    def as_dict(self) -> FileSignatureDict:
        ret_dict: FileSignatureDict = {
            "file_extension": self.file_extension,
            "hex": self.hex,
            "offset": self.offset,
            "display_string": None,
            "description": None,
        }

        if self.display_string is not None:
            ret_dict["display_string"] = self.display_string

        if self.description is not None:
            ret_dict["description"] = self.description

        return ret_dict


def check_for_match(
    file_header: bytes, test_hex_array: list[int | None], offset: int
) -> bool:
    """Checks for a match between the file header and the test hex string"""

    # return false for empty file headers
    if not file_header:
        return False

    # if the file header is shorter than the test hex array plus offset
    # we cant match so return false
    if len(file_header) < len(test_hex_array) + offset:
        return False

    # check for a match
    for _loc, _byte in enumerate(test_hex_array):
        if _byte is None:
            continue
        if _byte != file_header[_loc + offset]:
            return False
    return True


def find_matches_for_file_header(
    file_header: bytes, signatures: list[FileSignatureDict] = SIGNATURES
) -> list[FileSignature]:
    """Finds the file signatures that match the provided file header."""
    matches: list[FileSignature] = []
    for test_sig in signatures:
        if check_for_match(
            file_header=file_header,
            test_hex_array=test_sig["hex"],
            offset=test_sig["offset"],
        ):
            matches.append(FileSignature(**test_sig))
    return matches


def find_matches_for_file_path(
    file_path: str,
    max_header: int = 32,
    signatures: list[FileSignatureDict] = SIGNATURES,
) -> list[FileSignature]:
    """Finds the file signatures that match the file header of the provided file path."""
    with open(file_path, "rb") as f:
        file_header = f.read(max_header)
    return find_matches_for_file_header(file_header=file_header, signatures=signatures)
