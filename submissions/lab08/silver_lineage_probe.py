from pathlib import Path
from tempfile import TemporaryDirectory
from coursekit.common import DATA
from coursekit.governance import silver_lineage_check

print("POSITIVE", silver_lineage_check())
with TemporaryDirectory(prefix="bdp08-silver-") as folder:
    altered = Path(folder) / "events.parquet"
    altered.write_bytes((DATA / "silver/events.parquet").read_bytes() + b" ")
    try:
        silver_lineage_check(silver_path=altered)
        raise AssertionError("altered file passed")
    except ValueError as error:
        print("EXPECTED_FAILURE", str(error))
