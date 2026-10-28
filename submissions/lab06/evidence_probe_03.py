from coursekit.intelligence import answer, read_jsonl, QUESTIONS

questions = {q["qid"]: q for q in read_jsonl(QUESTIONS)}
for qid in ["d01", "d11", "d05"]:
    q = questions[qid]
    result = answer(q["question"], role=q["role"])
    print({"qid": qid, "refused": result["refused"],
           "hit_cosines": [(h["doc_id"], round(h["lexical_cosine"], 3)) for h in result["hits"][:3]],
           "citations": [c["doc_id"] for c in result["citations"]],
           "answer_chars": len(result["answer"]), "citation_exists": result.get("citation_exists")})
