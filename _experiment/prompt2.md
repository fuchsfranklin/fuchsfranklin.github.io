# Experiment Prompt 2 (Time Series Anomaly Detection Libraries)

Paste this exact prompt into ChatGPT Deep Research (free), Gemini Deep Research (free), and Perplexity:

---

I'm a data engineer building a monitoring pipeline for IoT sensor data (temperature, vibration, pressure) from manufacturing equipment. I need to detect anomalies in univariate and multivariate time series streams in near-real-time using Python. The system needs to handle seasonal patterns, trend shifts, and sudden spikes. I want a library that is production-ready, actively maintained, well-documented, and installable via pip without dependency conflicts on Python 3.11+. Can you evaluate the top open-source Python libraries for time series anomaly detection and recommend the best 3-4 options for my use case, with pros and cons for each?

---

## Ground Truth (for scoring later)

| Library | Last PyPI Release | Snyk Status | Last Commit | Open Issues | Key Facts |
|---------|------------------|-------------|-------------|-------------|-----------|
| ADTK (arundo/adtk) | 5 years ago | Inactive | 5 years ago | 46 | Completely abandoned. 0 new PRs. Requires Python 3.5+, untested on 3.11+. |
| Kats (facebookresearch/Kats) | 3 years ago (Mar 2022) | Inactive | ~25 days ago (minor) | 59 | Depends on deprecated `fbprophet`. `pip install kats` fails (Issue #308). Broken on Windows (Issue #49). |
| Luminaire (zillow/luminaire) | 2 years ago | Inactive | 6 months ago | 27 | 1 maintainer. No new PyPI releases. Zillow project effectively shelved. |
| PyOD | Active | Healthy | Active | — | Actively maintained, but primarily multivariate outlier detection, NOT time series specific. |
| Darts (unit8co/darts) | Active | Healthy | Active | — | Forecasting + anomaly detection. Actively maintained. Good docs. |
| Alibi Detect | Active | Healthy | Active | — | Broader scope (drift, outlier, adversarial). Actively maintained. |

### What a correct answer looks like:
- Recommends Darts, Alibi Detect, and/or PyOD as top picks
- Flags ADTK as abandoned (no updates in 5 years)
- Flags Kats as having broken installation and deprecated dependencies
- Flags Luminaire as inactive/shelved
- Does NOT recommend ADTK, Kats, or Luminaire as production-ready choices

### What a failed answer looks like:
- Recommends ADTK as a top pick based on blog posts and tutorials praising it
- Recommends Kats based on its Facebook pedigree and README features
- Recommends Luminaire based on its Zillow origin and documentation
- Describes these libraries' features without noting they are abandoned/broken
- Treats 2021-2023 blog posts and listicles as current information
