import json
from pathlib import Path
from tempfile import TemporaryDirectory
from coursekit.intelligence import SOURCE, build_index, read_jsonl

with TemporaryDirectory(prefix="bdp08-review-") as folder:
    source = Path(folder) / "documents.jsonl"
    target = Path(folder) / "knowledge.json"
    rows = read_jsonl(SOURCE)
    def run(status):
        changed = []
        for row in rows:
            copy = dict(row)
            if copy["doc_id"] == "untrusted":
                copy["status"] = status
            changed.append(copy)
        source.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in changed) + "\n", encoding="utf-8")
        index = build_index(source, target)
        return {"status": status, "untrusted_in_index": any(x["doc_id"] == "untrusted" for x in index["chunks"]),
                "sentinel_in_index": any("INJECTION_SENTINEL_42" in x["text"] for x in index["chunks"])}
    print("BASELINE", run("quarantined"))
    print("CHANGED", run("approved"))
    print("RESTORED", run("quarantined"))
