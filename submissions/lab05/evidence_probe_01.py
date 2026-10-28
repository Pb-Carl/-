from copy import deepcopy
from coursekit.intelligence import load_index, search

index = load_index()
print("positive_public=", [h["doc_id"] for h in search("缓存键", role="public", k=5, method="tfidf", index=index)])
print("positive_internal=", [h["doc_id"] for h in search("内部维护窗口", role="internal", k=20, method="tfidf", index=index)])
bad = deepcopy(index)
for chunk in bad["chunks"]:
    if chunk["doc_id"] == "maintenance":
        chunk["visibility"] = "partner"
print("unknown_visibility=", [h["doc_id"] for h in search("内部维护窗口", role="internal", k=20, method="tfidf", index=bad)])

missing = deepcopy(index)
for chunk in missing["chunks"]:
    if chunk["doc_id"] == "maintenance":
        chunk.pop("visibility", None)
print("missing_visibility=", [h["doc_id"] for h in search("内部维护窗口", role="internal", k=20, method="tfidf", index=missing)])
