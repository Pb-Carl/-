# 实验08操作前预测

实验05索引若改成其他模式或版本，原测试评价和 HTTP 记录的 index_version 不再匹配，不能直接沿用。服务只重启而数据不变时，进程内缓存会清空，但资料版本不会因此改变。

若仅改动 Silver Parquet，不同步更新清单，新增 silver_lineage 检查应在“实际 Parquet SHA256 与 manifest 的 silver_sha256”这一步失败；即使有人同步改了 manifest，实验04 latest.json 的 source_sha256 仍可抓住未重放的状态。隔离资料的 status 若在临时副本中被改为 approved，预计会进入索引；恢复 quarantined 后不应再进入。

本实验的预测和实现由 AI 助手协助完成，报告以实际检查结果为准。
