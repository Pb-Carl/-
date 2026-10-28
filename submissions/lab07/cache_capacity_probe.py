import json
import httpx

questions = ["模拟服务的用户配额是多少？", "上传材料有什么要求？", "缓存键应包含什么？", "模拟服务的用户配额是多少？"]
with httpx.Client(base_url="http://127.0.0.1:8000", timeout=30) as client:
    rows = []
    for question in questions:
        response = client.post("/ask", json={"question": question, "role": "public"})
        body = response.json()
        rows.append({"question": question, "status": response.status_code, "cache_hit": body.get("cache_hit"),
                     "refused": body.get("refused"), "run_id": body.get("_evidence", {}).get("run_id")})
    print(json.dumps(rows, ensure_ascii=False, indent=2))
