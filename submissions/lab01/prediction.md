# 实验 01 运行前预测

这份预测由 AI 助手协助起草，提交者须对照实际运行结果自行核验。

1. 仅把对象键从 `shared/raw/demo.json` 改成带已登记学号的前缀，`payload` 字节不变，因此 `source_sha256` 和 `downloaded_sha256` 预计都不变，`equal` 仍为 `true`。
2. 将 `payload` 中的 `tokens` 从 `120` 改为 `121`，序列化后的字节改变，因此两个摘要预计同步改变，但上传与下载内容仍一致，`equal` 仍为 `true`。
3. 无效 endpoint `http://127.0.0.1:1` 预计导致连接失败；恢复默认临时 Moto 服务后，完整往返和哈希校验预计重新成功。
