# 实验 01 云端数据接口与可复现环境

本仓库保存《云计算与大数据处理》实验 01 的个人代码改动与不含学号的结果摘要。课程运行框架来自 [BDP 课程仓库](https://gitee.com/ryukinkou/BDP/)，本次基于提交 `7ffdf1ebc71a62693eabb6f548687194d132135d`。完整的实名运行 JSON、HTML、截图和实验报告保存在单独提交包中，不在公开仓库暴露学号。

## 代码改动

`submissions/lab01/student_object_roundtrip.py` 在课程附件基础上做了两处用于对照的改动：

1. `make_key()` 从共享对象键改为 `students/<已登记学号>/raw/demo.json`。脚本从课程身份登记读取学号，不在代码中写死个人信息。
2. 小型 JSON 的 `tokens` 从 `120` 改为 `121`，用于检验内容字节改变后的 SHA-256。

`final_changes.diff` 给出相对课程附件的完整差异。

## 在课程工作区复现

1. 克隆上方课程仓库，并按其 `docs/Windows环境准备.md` 使用 Python 3.12 安装 `requirements.lock.txt`。
2. 在课程仓库根目录执行 `python -m coursekit identity --student-id <本人学号> --lab 01 --stage start`，再执行 `python -m coursekit seed --rows 20000` 与 `python -m coursekit lab01`。
3. 把本仓库的脚本复制到课程根目录的 `submissions/lab01/student_object_roundtrip.py`，从课程根目录运行它。
4. 课程脚本会产生带学号、实验号和 `run_id` 的原生运行记录。按课程手册保留基线、改键、改 payload、连接失败与恢复五组证据。不要把公开仓库中的结果摘要当作实名运行证据。

## 本机观测摘要

| 对照 | 内容 SHA-256 | 上传下载相等 |
|---|---|---|
| 基线 payload，`tokens=120` | `23c0b20c65b4476c7e541044c09c88cd970bb02191681f804daef0b7ba49f0e8` | `true` |
| 仅改对象键，`tokens=120` | `23c0b20c65b4476c7e541044c09c88cd970bb02191681f804daef0b7ba49f0e8` | `true` |
| 再改 payload，`tokens=121` | `1d0f0d28612d93ec866d670eab8876e9dfb64d1c2b2cb84ee24fa60d0ee63bec` | `true` |

主运行生成了 20,102 行合成事件（20,000 条有效唯一记录、100 条重复记录、2 条异常记录）；原始与下载文件的 SHA-256 均为 `0d93bcd25e28047f804238c220bdb5b1d2dadf328647c07de85ba0104e8e2854`，`hash_matches=true` 且 `version_ids_differ=true`。无效 endpoint `http://127.0.0.1:1` 得到 `EndpointConnectionError`，恢复默认本机 Moto 服务后重新成功。

Moto 仅模拟本机 S3 HTTP 接口。本实验验证的是本次对象上传下载的字节一致性，没有验证真实云服务的持久性、跨机容灾、访问控制或业务数据质量。分析与文档整理使用了 AI 助手，数值来自实际程序输出。
