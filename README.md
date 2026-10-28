# 云计算与大数据处理实验报告（实验一至实验八）

这是《云计算与大数据处理》的实验提交仓库。课程原始代码在 [BDP 课程仓库](https://gitee.com/ryukinkou/BDP/)，本次使用的课程提交为 `7ffdf1ebc71a62693eabb6f548687194d132135d`。实验 01 的概要在本页；实验 02—08 的报告、代码差异和带学号的原始运行证据见下表。

## 实验 02—08

| 实验 | 主题 | 报告 | 证据与代码 |
|---|---|---|---|
| 02 | 数据湖与质量契约 | [PDF](submissions/lab02/2410311319-24计科3-彭博-实验二.pdf) | [提交目录](submissions/lab02/) |
| 03 | 分布式批处理与性能分析 | [PDF](submissions/lab03/2410311319-24计科3-彭博-实验三.pdf) | [提交目录](submissions/lab03/) |
| 04 | 增量事件处理与故障恢复 | [PDF](submissions/lab04/2410311319-24计科3-彭博-实验四.pdf) | [提交目录](submissions/lab04/) |
| 05 | 规则文档整理与可解释检索 | [PDF](submissions/lab05/2410311319-24计科3-彭博-实验五.pdf) | [提交目录](submissions/lab05/) |
| 06 | 证据查询与结果评价 | [PDF](submissions/lab06/2410311319-24计科3-彭博-实验六.pdf) | [提交目录](submissions/lab06/) |
| 07 | 数据服务部署与可观测性 | [PDF](submissions/lab07/2410311319-24计科3-彭博-实验七.pdf) | [提交目录](submissions/lab07/) |
| 08 | 数据治理与可信发布 | [PDF](submissions/lab08/2410311319-24计科3-彭博-实验八.pdf) | [提交目录](submissions/lab08/) |

这些实验使用课程合成数据，本机运行结果已保留为 JSON、同名 HTML 和浏览器截图。报告和代码有 AI 助手协助，机器预检查状态为等待教师复核。仓库公开，实验 02—08 的报告含姓名和学号。

## 我改了什么

`submissions/lab01/student_object_roundtrip.py` 是从课程附件改出来的。我只动了两处，方便比较结果：

1. 把 `make_key()` 返回的共享对象键换成 `students/<已登记学号>/raw/demo.json`。脚本会读取课程身份登记，不需要在代码里写死学号。
2. 把小型 JSON 中的 `tokens` 从 `120` 改成 `121`，看看内容变了以后 SHA-256 会不会变。

`final_changes.diff` 记录了相对课程附件的改动。

## 怎么重新跑

1. 克隆上方课程仓库，并按其 `docs/Windows环境准备.md` 使用 Python 3.12 安装 `requirements.lock.txt`。
2. 在课程仓库根目录执行 `python -m coursekit identity --student-id <本人学号> --lab 01 --stage start`，再执行 `python -m coursekit seed --rows 20000` 与 `python -m coursekit lab01`。
3. 把本仓库的脚本复制到课程根目录的 `submissions/lab01/student_object_roundtrip.py`，从课程根目录运行它。
4. 运行后按课程手册保存原生记录和截图。报告里比较了原样脚本、改对象键、改 `tokens`、连接失败和恢复后的结果。这里只放结果摘要，不能代替带学号的证据。

## 我在本机看到的结果

| 对照 | 内容 SHA-256 | 上传下载相等 |
|---|---|---|
| 基线 payload，`tokens=120` | `23c0b20c65b4476c7e541044c09c88cd970bb02191681f804daef0b7ba49f0e8` | `true` |
| 仅改对象键，`tokens=120` | `23c0b20c65b4476c7e541044c09c88cd970bb02191681f804daef0b7ba49f0e8` | `true` |
| 再改 payload，`tokens=121` | `1d0f0d28612d93ec866d670eab8876e9dfb64d1c2b2cb84ee24fa60d0ee63bec` | `true` |

主程序生成的文件有 20,102 行，其中 20,000 条有效且不重复、100 条重复、2 条异常。原始文件和下载文件的 SHA-256 都是 `0d93bcd25e28047f804238c220bdb5b1d2dadf328647c07de85ba0104e8e2854`，程序给出 `hash_matches=true` 和 `version_ids_differ=true`。我还把 endpoint 改成 `http://127.0.0.1:1` 试过，得到 `EndpointConnectionError`；改回默认 Moto 服务后又跑通了。

Moto 在这里模拟本机 S3 接口，所以这些结果只能说明本次上传下载的字节一致，不能说明真实云存储的持久性、跨机器容灾或访问权限。报告整理时用到了 AI 助手；上面的数字取自实际运行记录。
