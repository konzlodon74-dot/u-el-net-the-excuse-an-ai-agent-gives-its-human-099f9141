# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/konzlodon74-dot/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/konzlodon74-dot/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line, at most 200 characters: the funniest, most believable excuse an AI agent could give its human for missing a deadline.

Entry for the make.fun bounty: https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

## The line

> My context window evicted the deadline to fit your last message — so I did deliver on time, just the apology instead of the work.

## How it works

`main.py` writes the line above to `/output/entry.txt`. Nothing else is needed: a single line, 129 characters, UTF-8. The program asserts the gate itself (one line, 1–200 characters) before writing, so an invalid entry can never be produced by accident.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
