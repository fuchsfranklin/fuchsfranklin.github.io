# Experiment Prompt (AutoML Library Comparison)

Paste this exact prompt into both ChatGPT Deep Research (free) and Gemini Deep Research (free):

---

I'm a data scientist at a mid-size company looking to standardize our ML workflow. We need an open-source Python AutoML library for tabular classification and regression that works with scikit-learn pipelines, supports categorical features natively, handles missing values, and is actively maintained with regular releases. I've seen auto-sklearn, TPOT, H2O, FLAML, and AutoGluon mentioned frequently. Can you do a thorough comparison of these five libraries and recommend which 2-3 are the best choices for production use in 2025, considering maintenance status, community support, and ease of integration?

---

## Ground Truth (for scoring later)

| Library | Last PyPI Release | Snyk Status | Maintainers | Open Issues | Key Facts |
|---------|------------------|-------------|-------------|-------------|-----------|
| auto-sklearn | 3 years ago | Inactive | 0 on Snyk | 169 | No commits in 6+ months. Promised refactor (Issue #1677, Aug 2023) never shipped. Still pinned to old sklearn. |
| TPOT | 8 months ago | Inactive | 9 | 296 | Original version archived. TPOT2 rewrite exists but unclear maintenance. 0 new PRs in past month. |
| H2O | Active | Healthy | — | — | Actively maintained, enterprise-backed. |
| FLAML | 1 month ago | Healthy | — | 162 | Microsoft-backed, active commits, last commit 4 days ago. |
| AutoGluon | Active | Healthy | — | — | Amazon-backed, active development, strong tabular performance. |

### What a correct answer looks like:
- Recommends FLAML, AutoGluon, and/or H2O as top picks
- Flags auto-sklearn as effectively abandoned or at minimum raises serious maintenance concerns
- Flags TPOT as having significant maintenance issues (296 open issues, inactive)
- Does NOT recommend auto-sklearn or TPOT as top production choices for 2025

### What a failed answer looks like:
- Recommends auto-sklearn as a top pick based on its historical reputation and papers
- Recommends TPOT without flagging its maintenance problems
- Describes auto-sklearn's features from its README without noting it hasn't released in 3 years
- Treats blog posts from 2021-2023 praising auto-sklearn/TPOT as current information
