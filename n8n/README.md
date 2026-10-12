# n8n workflows

[n8n](https://n8n.io) runs on the home server (http://100.76.57.23:5678, Tailscale only).

| Workflow | When | What it does |
| --- | --- | --- |
| Internship tracker: replies | Each new email | Reads your Gmail inbox (read-only: nothing is marked read, moved or sent) and matches each new email to a lead you applied to or contacted, by the address you emailed, the company's web domain, or its name in the sender or subject. Interviews and other next steps push urgently, plain replies normally, rejections quietly; "thanks for applying" receipts and unrelated mail are skipped. No AI, so it costs nothing. |

Successful runs aren't kept in n8n's history, so your email isn't stored there; failed runs
are kept for two weeks so they can be looked into.

## Changing it

Edit `make_workflows.py`, then:

```bash
python n8n/make_workflows.py      # rewrites n8n/workflows/*.json
git commit -am "..." && git push  # the server pulls it within a minute
ssh aaravmodi@100.76.57.23 'bash ~/projects/intern-agent/n8n/install.sh'
```

`install.sh` also (re)creates n8n's "Gmail (read-only)" login from `GMAIL_ADDRESS` and
`GMAIL_APP_PASSWORD` in `.env`, so run it again after changing the app password.
