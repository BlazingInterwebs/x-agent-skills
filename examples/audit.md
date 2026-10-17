# Audit a synthetic dataset

`examples/observations.csv` holds 12 synthetic original posts for a demo
account, all public, organic, 48 hours old, measured as owner-analytics
impressions. No real account is represented.

```bash
python3 -B skills/x-audit/scripts/compare.py examples/observations.csv
```

Post `p12` has 1,600 impressions. Excluding it, the other 11 posts have a
median of 400, so its multiple is 4.0: an **outlier** under the 3x working
threshold in the metrics reference. A reasonable audit line:

> p12, 4.0x median impressions (n=11, target excluded). Hypothesis: TBD by
> reading the post. Limits: impressions only; no replies or profile visits
> supplied; synthetic data.

Next step: the "5 more versions" plan in `x-audit`. Don't credit p12 with
the week's follower change.
