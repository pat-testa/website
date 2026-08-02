# Deployment and DNS cutover

The site auto-deploys: every push to `main` triggers
`.github/workflows/publish.yml`, which renders with Quarto and publishes to
GitHub Pages. No manual build step.

Preview URL (before custom domain): <https://pat-testa.github.io/website/>

## Pointing patrickatesta.com at GitHub Pages

Do this only after the preview URL looks correct. Wix keeps serving the old
site until DNS propagates, so there is no downtime window.

### 1. Add DNS records at Wix

In the Wix domain DNS panel, for `patrickatesta.com`:

**Four A records** on the root/apex (`@`), all pointing at GitHub Pages:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**One CNAME record** for `www`:

```
pat-testa.github.io
```

Delete any existing A or CNAME records for `@` and `www` that point at Wix,
otherwise they conflict.

> Verify the four IPs against GitHub's current documentation before entering
> them: <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>

### 2. Re-enable the CNAME file in this repo

```bash
git mv CNAME.pending CNAME
```

Then uncomment the `- CNAME` line under `project: resources:` in `_quarto.yml`,
commit, and push. This tells GitHub Pages the site's canonical hostname.

### 3. Set the custom domain in repo settings

<https://github.com/pat-testa/website/settings/pages> → Custom domain →
`patrickatesta.com` → Save. Then tick **Enforce HTTPS** once the certificate
finishes provisioning (usually well under an hour; the checkbox is greyed out
until it is ready).

### 4. Verify before cancelling Wix

- <https://patrickatesta.com> loads the new site over HTTPS
- <https://www.patrickatesta.com> redirects to the apex
- A few PDF links resolve, e.g. `/files/cv.pdf`
- Old page URLs still work: `/about-me/`, `/research/`, `/data/`,
  `/teaching/`, `/contact/`

Only then cancel the Wix plan.

## Domain registration

Repointing DNS (above) does **not** require transferring the domain away from
Wix. Transfer is only necessary to stop paying Wix entirely.

Before cancelling, check whether the domain was bought separately or came
bundled free with the Premium plan. If bundled, transfer it out *first* —
cancelling may forfeit it. Transfers require unlocking the domain and getting
an EPP/auth code from Wix, and ICANN blocks transfers for 60 days after a
registration or a previous transfer.
