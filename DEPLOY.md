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

**Four AAAA records** on `@`, for IPv6:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**One CNAME record** for `www`:

```
pat-testa.github.io
```

Note the CNAME target is the bare `github.io` host — it does **not** include
the repository name.

Delete any existing A or CNAME records for `@` and `www` that point at Wix,
otherwise they conflict.

> These values were checked against GitHub's documentation on 2026-08-02:
> <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>

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

## Domain registration and transfer

`patrickatesta.com` is bundled with the Wix Premium plan, so it must be
transferred out before that plan lapses or it can be forfeited.

Registration facts (RDAP, checked 2026-08-02):

| | |
|---|---|
| Registrar of record | Network Solutions, LLC (Wix resells through them) |
| Registered | 2017-10-14 |
| **Expires** | **2026-10-14** |
| Status | `clientTransferProhibited` (locked) |
| Nameservers | `NS0.WIXDNS.NET`, `NS1.WIXDNS.NET` |

**Deadline: initiate the transfer by mid-September 2026.** Transfers take
about 5–7 days and registrars refuse them close to expiry. An ICANN gTLD
transfer includes a mandatory 1-year renewal, so ~$10–15 to the new registrar
pushes the expiry to October 2027 — you are not paying twice for the same year.

Transferring does **not** disturb the live site: the nameservers stay on
`WIXDNS` throughout, so Wix keeps serving until DNS is repointed deliberately.

### Order of operations

1. **Unlock at Wix** and request the EPP/auth code (lifts
   `clientTransferProhibited`). Disable WHOIS privacy if it blocks the code.
2. **Initiate the transfer** at the new registrar using that code. Wait for it
   to complete. Site unaffected throughout.
3. **Repoint DNS** at the new registrar per the section above. This is the
   moment the site cuts over from Wix to GitHub Pages.
4. **Verify** using the checklist above.
5. **Turn off Wix auto-renew** so the plan is not billed again on 2026-10-14.

Chosen registrar: **Porkbun** (Namecheap equivalent). Deliberately not
Cloudflare Registrar — Cloudflare requires nameservers to move to them before
it will accept a registration transfer, which forces the DNS cutover to happen
first. Porkbun keeps the two steps independent: registration moves while
nameservers stay on Wix, so the live site is untouched until step 3.

During the transfer, do **not** change nameservers and do **not** cancel the
Wix plan. Either can cause the transfer to fail.

The auth/EPP code is a credential — it goes into the registrar's transfer form
and nowhere else.
