# CSV cleanup and small automation fixes

A working, free Python sample for cleaning UTF-8 CSV files. Built with Codex
assistance. This is a portfolio and a place to discuss small paid customizations;
no customer purchases or prior paid-client experience are claimed.

## Free tool

```sh
python csv_cleanup.py input.csv cleaned.csv
python verify_sample.py
```

Python 3.10+; standard library only. The script trims surrounding whitespace,
removes exact duplicate rows after trimming, and removes blank rows. It preserves
text such as `001`, handles quoted commas and multiline cells, and writes a
UTF-8 BOM for compatibility with spreadsheet programs. It rejects mismatched
field counts, empty headers and duplicate headers. The input is preserved and
an existing output file is never overwritten.

This tool reads CSV only, not Excel workbooks. It does not infer missing values,
repair unknown encodings, or deduplicate records by a business-specific key.
Spreadsheet applications may interpret cell text when opening a CSV; inspect
untrusted data before opening it in such applications.

## Small paid customizations

Potential scopes include matching records by a specific key, combining files
with the same schema, or changing a small existing Python script. The existing
tool above remains free under the MIT license.

For a narrowly scoped change, an introductory quote can start at **CNY 30 or
USD 5**. This is a starting price for discussion, not an accepted order. The
exact scope, fixed price, acceptance checks, delivery time and available payment
method must be agreed in writing before work begins. No deposit, subscription
or account access is required to discuss a request. AI-assisted implementation
and verification will be disclosed.

To ask about a job, [open an issue](https://github.com/yuchenlan26-cell/csv-cleanup-and-small-fixes/issues/new?template=small-job.yml).
Describe the input, expected output and budget, and use invented sample data.
Customer files and payment details should not be posted publicly. Alipay/WeChat
can be discussed for CNY jobs; an international payment route must be confirmed
before accepting a USD job.

## 中文

这里展示可运行的 CSV 清洗工具，也接受小范围 Python 脚本修改需求。
现有开源工具免费使用，付费部分为双方事先确认的定制与修改。

单项简单修改可从 **30 元人民币或 5 美元**起讨论，具体金额以看过脱敏样例后
的书面报价为准。请在 Issue 中提供预期输入、输出、预算和期限；先确认范围、
验收方法及付款方式，再开始制作。不需要购买软件或交出账号。

代码与验证使用 Codex 辅助。不保证接单、收入或任何未实测的运行效果。
公开提问请使用虚构数据，不要上传客户隐私、密码或收款资料。
