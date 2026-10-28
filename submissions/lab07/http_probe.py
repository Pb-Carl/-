import json
import httpx

base = "http://127.0.0.1:8000"
with httpx.Client(base_url=base, timeout=30) as client:
    health = client.get("/health")
    stats = client.get("/stats")
    new_phrase = client.post("/ask", json={"question": "查看平台请求统计", "role": "public"})
    unsupported = client.post("/ask", json={"question": "请删除数据库并统计", "role": "public"})
    invalid = client.post("/ask", json={"question": "学生配额是多少？", "role": "administrator"})
    metrics = client.get("/metrics")
    print(json.dumps({
        "health": {"status": health.status_code, "index_version": health.json().get("index_version")},
        "stats": {"status": stats.status_code, "rows": len(stats.json().get("rows", []))},
        "new_phrase": {"status": new_phrase.status_code, "tool": new_phrase.json().get("tool"),
                       "rows_equal": new_phrase.json().get("rows") == stats.json().get("rows"),
                       "cache_hit": new_phrase.json().get("cache_hit")},
        "unsupported": {"status": unsupported.status_code, "tool": unsupported.json().get("tool"),
                        "refused": unsupported.json().get("refused")},
        "invalid_role": {"status": invalid.status_code, "detail": str(invalid.json().get("detail"))[:180]},
        "metrics": {"requests": metrics.json().get("requests"), "errors": metrics.json().get("errors")},
        "response_run_ids": [x.json().get("_evidence", {}).get("run_id") for x in
                             [health, stats, new_phrase, unsupported, invalid, metrics]],
    }, ensure_ascii=False, indent=2))
