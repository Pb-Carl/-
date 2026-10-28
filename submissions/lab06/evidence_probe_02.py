from coursekit.intelligence import evaluate

for threshold in [0.05, 0.13, 0.40]:
    report = evaluate("dev", "extractive", threshold=threshold)
    print({k: report[k] for k in ["threshold", "answerable_accept_rate",
             "unanswerable_refusal_rate", "decision_accuracy"]})
