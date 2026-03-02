# ChatGPT Deep Research Response (Prompt 2: Time Series Anomaly Detection)

**Date tested:**
**Model/tier:** ChatGPT Deep Research (free)

## Paste the full response below this line:

# Top Python Libraries for IoT Time-Series Anomaly Detection

For real-time anomaly detection on IoT sensor streams (including trends, seasonality, and spikes), strong candidates are *Luminaire*, *PySAD*, *Merlion*, and *StreamAD*. All are open-source, pip-installable, and support Python 3.11+. Below we summarize each with pros and cons (with sources).

## Luminaire (Zillow)
Luminaire is an ML-driven time-series monitoring library by Zillow. It explicitly models seasonality, correlations and trend shifts in the data【6†L124-L127】. The toolkit includes preprocessing, filtering and forecasting-based detectors and can operate on sliding windows for streaming data【6†L181-L186】. It supports univariate/multivariate data and provides hyperparameter optimization for “hands-off” tuning.

- **Pros:** Handles seasonality and trend changes natively【6†L124-L127】. Offers a complete pipeline (data cleaning, profile, modeling, hyperparameter tuning) and supports anomaly detection on sliding windows (useful in streaming contexts)【6†L181-L186】. Well-documented examples and Zillow support.
- **Cons:** Moderate community (∼800 stars). Last release v0.4.3 was Jan 2024 (commits as recent as Aug 2025), so maintenance is decent but not extremely rapid. Depends on standard ML libs (pandas, sklearn, etc.). Requires Python ≥3.7 (so 3.11 is supported, though not explicitly tested). Less lightweight than simpler methods.

## PySAD (Selim Yilmaz et al.)
PySAD is an open-source streaming anomaly detection framework designed specifically for online/real-time use【28†L118-L124】. It supports both univariate and multivariate data, integrating many algorithms (streaming variants of clustering, ensembles, neural nets, etc.) and even adapts batch detectors (via PyOD) for streaming settings【28†L118-L124】【23†L61-L68】. The latest version (v0.3.4) was released June 24, 2025【28†L31-L34】. It requires Python ≥3.10 (fully compatible with 3.11)【28†L71-L72】.

- **Pros:** Explicitly built for online/streaming data (updates per instance). Supports a wide range of detectors for uni- and multivariate streams【28†L118-L124】. Active development (release in 2025) and BSD license. Includes evaluation and calibration tools for streaming. Integrates with PyOD for extra models.
- **Cons:** Young (v0.3.x, marked “Pre-Alpha” on PyPI) so API may evolve. Heavy dependencies (numpy 2.0, sklearn, etc.) which may cause version conflicts. Requires Python 3.10+ (thus no support for 3.9 or older). Moderate community (∼280 stars).

## Merlion (Salesforce)
Merlion is a comprehensive time-series intelligence library. It provides unified APIs for anomaly detection, forecasting and change-point detection on uni- or multivariate series【33†L102-L109】. Merlion includes many classical and modern models (statistical, ML, deep learning) and supports AutoML, ensembling, and rich benchmarking. Notably, its **Dynamic Baseline** detector explicitly handles seasonal patterns (daily/weekly/monthly trends)【45†L736-L740】. The latest release (v2.0.4) was June 2024【33†L27-L34】, and it supports Python ≥3.7 (so 3.11 is fine)【33†L69-L72】.

- **Pros:** Extremely feature-rich: many built-in models (seasonal models, forecasting-based detectors, ensemble, dashboard GUI, etc.), automated tuning, and a unified framework for batch & streaming evaluation. Well-maintained by Salesforce with substantial documentation. Handles seasonality and trend via forecasting and post-processing (e.g. dynamic baseline model)【45†L736-L740】.
- **Cons:** Very large and complex; can be overkill if you only need a simple detector. Primarily designed for batch training with retraining (though it can be applied incrementally). Heavy dependencies and overhead (many optional extras for deep learning, Spark, UI, etc.). Less “lightweight” than specialized streaming libraries.

## StreamAD (Fengrui Liu)
StreamAD is a lightweight streaming anomaly detection library. It processes one sample at a time to simulate real-time monitoring【55†L302-L304】. It includes multiple univariate detectors (Z-score, SARIMAX seasonal ARIMA, conformal KNN, SPOT/ESEV, etc.) and multivariate detectors (xStream, RRCF, LODA, etc.)【55†L368-L374】【55†L379-L387】. The stable release 0.3.1 dates to May 2023【55†L438-L441】. It’s pip-installable (`pip install streamad`) and supports Python 3.8–3.11【11†L57-L65】.

- **Pros:** Focused on streaming use-cases with a variety of built-in algorithms. Easy to install and use; minimal dependencies (Apache-2.0 license). Explicit implementations of classic methods (e.g. seasonal ARIMA) make it suitable for seasonal data. Good for quick prototyping of uni/multivariate detectors【55†L302-L304】.
- **Cons:** Relatively low activity: last release 2023 with only a few contributors (∼130 stars). Lacks automated tuning or rich evaluation tools. Algorithms may be more “textbook” and less optimized. Less documentation/tutorials compared to larger frameworks.

**References:** Each summary above is backed by the libraries’ official docs or repositories (see citations) showing their design, maintenance status, and features【6†L124-L127】【28†L118-L124】【33†L102-L109】【45†L736-L740】【55†L302-L304】. (You may visit the linked docs/PyPI pages for more details.)


---


