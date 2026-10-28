from pathlib import Path
from tempfile import TemporaryDirectory
from coursekit.intelligence import SOURCE, build_index, validate_index, StaleIndexError

with TemporaryDirectory(prefix="bdp05-") as folder:
    source = Path(folder) / "documents.jsonl"
    target = Path(folder) / "index.json"
    source.write_bytes(SOURCE.read_bytes())
    old = build_index(source, target)
    source.write_bytes(source.read_bytes() + b"\n")
    try:
        validate_index(source, target)
        raise AssertionError("stale index was accepted")
    except StaleIndexError as error:
        print("EXPECTED_FAILURE", error)
    new = build_index(source, target)
    print("version_changed=", old["index_version"] != new["index_version"])
    print("RECOVERED", validate_index(source, target)["index_version"])
