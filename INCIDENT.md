# Incident: Leaked PAYMENTS_API_KEY

- **What leaked:** PAYMENTS_API_KEY (fake lab value `sk_test_FAKEVALUEONLY000000000`) was exposed in a screenshot shared in a public Slack channel.
- **Detection:** Reported by a teammate approximately 5 minutes after posting.
- **Revocation:** The key was revoked at the (fictional) payments provider immediately, without waiting to confirm misuse.
- **Rotation:** New keys were issued and set via `gh secret set PAYMENTS_API_KEY --env staging` and `--env production`. The SOPS-encrypted Kubernetes secret was re-encrypted with the new value.
- **Verification:** Pipeline re-ran end-to-end and passed in all environments; the old key returned 401 from the provider.
- **Prevention change:** Enabled gitleaks pre-commit hook and added a rule forbidding secrets in screenshots — use the GitHub Secrets UI instead of chat.
- **Cloud credentials note:** If the leaked credential had been an AWS access key, the OIDC federation from Part 5 would have eliminated this drill entirely — no static key to leak, only short-lived per-run tokens.
