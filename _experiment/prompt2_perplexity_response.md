# Perplexity Deep Research Response (Prompt 2: Time Series Anomaly Detection)

**Date tested:**
**Model/tier:** Perplexity (free)

## Paste the full response below this line:

Here is my evaluation of the top open-source Python libraries for time series anomaly detection tailored to your IoT manufacturing pipeline.

***

## Recommended Libraries: Head-to-Head Comparison

| Feature | **STUMPY** | **Merlion** | **PyOD** | **PySAD** |
|---|---|---|---|---|
| **GitHub Stars** | ~3.6k | ~3.3k | ~8.5k | ~400 |
| **Latest Release** | v1.14.1 (Feb 2026) | v2.0.2 (Feb 2023) | v2.0.6 (Dec 2025) | v0.3.4 (Jun 2025) |
| **Actively Maintained** | ✅ Very active | ⚠️ Stale releases | ✅ Very active | ✅ Active |
| **Python 3.11+** | ✅ | ✅ (works) | ✅ | ✅ (3.10+) |
| **pip install** | `pip install stumpy` | `pip install salesforce-merlion` | `pip install pyod` | `pip install pysad` |
| **Univariate** | ✅ | ✅ | ✅ | ✅ |
| **Multivariate** | ✅ (mstump) | ✅ | ✅ (native) | ✅ |
| **Streaming/Online** | ✅ (stumpi) | ⚠️ Batch-oriented | ❌ Batch only | ✅ (purpose-built) |
| **Seasonality Handling** | ✅ (implicit via MP) | ✅ (STL, ETS, etc.) | ❌ Manual | ❌ Manual |
| **Dependency Weight** | Light (numpy, scipy, numba) | Medium-Heavy (JDK, OpenMP) | Light (numpy, sklearn) | Light (numpy, sklearn, pyod) |

***

## 1. STUMPY — Best Overall for Your Use Case

STUMPY computes the *matrix profile*, which is an exact, training-free technique that identifies the nearest-neighbor distance for every subsequence in a time series. The global maximum of the matrix profile directly reveals the most anomalous subsequence (discord), while the minimum reveals the most common motif.[1][2][3]

**Why it fits your IoT pipeline:**

- **Streaming-native via `stumpy.stumpi`**: Incrementally updates the matrix profile as each new sensor reading arrives, with constant-time updates per data point — ideal for near-real-time monitoring.[4]
- **Multivariate support**: `stumpy.mstump` handles multi-dimensional time series (temperature + vibration + pressure jointly).[2]
- **No training required**: Works out-of-the-box — no labeled data, no hyperparameter tuning, no model fitting. You choose a window size (e.g., one machine cycle length) and it works.
- **Handles seasonal patterns implicitly**: The matrix profile naturally captures repeating patterns as motifs and flags deviations as discords, so seasonal behavior is handled without explicit decomposition.
- **Scalable**: GPU acceleration (`gpu_stump`), Dask distributed computing (`stumped`), and Numba JIT compilation for CPU parallelism.[2]
- **Minimal dependencies**: Only numpy, scipy, and numba — no dependency conflicts on Python 3.11+.
- **Very actively maintained**: Released v1.14.1 in February 2026, with regular releases throughout 2025.[5]

**Pros:** Exact results (no false positives from model drift), zero training time, streaming support, excellent tutorials, peer-reviewed (JOSS publication), battle-tested in industrial anomaly detection research.[6]

**Cons:** Requires choosing a window size `m` (the expected pattern length). Not a full ML framework — you get anomaly scores but need to build your own thresholding/alerting logic. Discord discovery is powerful for subsequence anomalies but requires wrapping for point-level spike detection.

```python
import stumpy
import numpy as np

stream = stumpy.stumpi(initial_data, m=window_size)
for new_point in sensor_stream:
stream.update(new_point)
if stream.P_.max() > threshold: # discord score
alert("Anomaly detected!")
```

***

## 2. PyOD — Best Algorithm Breadth & Maturity

PyOD is the most widely adopted Python anomaly detection library, with 50+ algorithms and over 26 million downloads. Version 2 (released 2024–2025) adds 12 deep learning models via PyTorch and LLM-powered automated model selection.[7][8]

**Why it fits your IoT pipeline:**

- **Massive algorithm library**: Isolation Forest, LOF, ECOD, AutoEncoder, Deep SVDD, and many more — lets you experiment rapidly across classical, ensemble, and neural approaches.[7]
- **Multivariate-native**: Designed from the ground up for multivariate tabular data, so correlating temperature/vibration/pressure is straightforward.
- **scikit-learn API**: `fit()`, `predict()`, `decision_function()` — integrates seamlessly into existing pipelines.
- **Actively maintained**: v2.0.6 released December 2025, with ongoing research publications.[9]
- **Lightweight dependencies**: numpy, scipy, scikit-learn, numba, joblib — no exotic system-level requirements.

**Pros:** Battle-tested in production (Databricks integration), excellent documentation, largest community, easy to ensemble multiple detectors via SUOD for parallel training.[7]

**Cons:** **Not time-series-native.** PyOD operates on tabular feature vectors, so you must manually engineer temporal features (sliding windows, lag features, rolling statistics) to feed sensor time series to it. It has no built-in seasonality decomposition, streaming mode, or temporal awareness. This is extra engineering work, but it's a common and well-understood pattern.

```python
from pyod.models.iforest import IForest
# Requires manual windowing: create feature matrix from rolling windows
clf = IForest(contamination=0.01)
clf.fit(X_train_windows)
scores = clf.decision_function(X_test_windows)
```

***

## 3. PySAD — Best for Pure Streaming

PySAD is purpose-built for anomaly detection on streaming data, implementing 17+ algorithms that operate under strict constraints: bounded memory, single-pass processing, and constant-time complexity per observation.[10][11]

**Why it fits your IoT pipeline:**

- **True streaming architecture**: Models update incrementally with each incoming data point — no batching, no retraining. This is exactly what a real-time sensor pipeline needs.
- **Algorithms include**: Half-Space Trees, xStream, LODA, Robust Random Cut Forest, and others designed specifically for data streams.[11]
- **Univariate and multivariate**: Supports both out of the box.[10]
- **Full pipeline toolkit**: Stream simulators, evaluators, preprocessors, statistic trackers, postprocessors, and probability calibrators — covers the full monitoring pipeline.[10]
- **Integrates with PyOD**: Wraps PyOD's batch detectors for use in a streaming context, giving you the best of both worlds.[12]
- **Recently maintained**: v0.3.4 released June 2025 with Python 3.13 CI support and critical bug fixes.[13]

**Pros:** Lowest latency of any option (O(1) per observation), minimal memory footprint, exactly matches the "near-real-time streaming" requirement, scikit-learn-compatible API.[10]

**Cons:** Smaller community and ecosystem compared to PyOD or STUMPY. Limited built-in support for explicit seasonality — streaming algorithms adapt to distributional shifts but don't decompose seasonal components. Pinned dependency versions (e.g., `numpy==2.0.2`, `scikit-learn==1.5.2`) could cause conflicts in some environments. Less comprehensive documentation than the larger libraries.[14]

```python
from pysad.models import HalfSpaceTrees
from pysad.transform.postprocessing import RunningAveragePostprocessor

model = HalfSpaceTrees(window_size=250, n_trees=25)
postprocessor = RunningAveragePostprocessor(window_size=50)
for x in sensor_stream:
score = model.fit_score_partial(x)
smoothed = postprocessor.fit_transform_partial(score)
```

***

## 4. Merlion (Salesforce) — Best Full Framework (with Caveats)

Merlion is the most complete end-to-end framework, built by Salesforce Research originally for monitoring their data center infrastructure — a use case closely analogous to your manufacturing IoT scenario.[15][16]

**Why it fits your IoT pipeline:**

- **Full ML pipeline**: Data loading → preprocessing → model training → post-processing → evaluation → visualization, all in one library.[16]
- **`DefaultDetector`**: An ensemble of ETS + Random Cut Forest that works well out-of-the-box without tuning — great for getting a baseline fast.[17]
- **Seasonality-aware**: Models include STL decomposition, ETS, Prophet integration, and other methods that explicitly handle daily/weekly/seasonal patterns in sensor data.
- **Production evaluation pipeline**: Simulates live deployment with periodic retraining, batch or streaming inference, and TSAD metrics (precision, recall, F1, mean time to detect).[16]
- **Post-processing for false positive reduction**: Industry-inspired calibration rules that convert raw scores into interpretable z-scores — critical for a manufacturing alerting system.[16]
- **GUI dashboard** for rapid prototyping.

**Pros:** Most complete feature set of any option. Handles univariate and multivariate. AutoML for hyperparameter tuning. PySpark distributed backend for scaling to many sensors.[16]

**Cons:** **Last PyPI release was February 2023 (v2.0.2)** — over three years old. While community PRs are still being submitted (as recently as February 2026), the core Salesforce team has not shipped a release since. Some models require a JDK installation, which complicates containerized deployments. Heavier dependency tree than the other options. Risk of compatibility issues accumulating with newer Python/pandas/numpy versions without official releases.[18][19]

***

## Recommendation for Your Architecture

For a production IoT monitoring pipeline handling temperature, vibration, and pressure streams, I'd architect a **layered approach** using two of these libraries:

1. **STUMPY as the primary real-time detector** — Use `stumpi` for per-sensor streaming anomaly detection. Its zero-training, exact-match approach is robust against the model drift problems that plague ML-based detectors in manufacturing environments where operating conditions change. The matrix profile naturally handles seasonal equipment cycles. Actively maintained with minimal dependencies.

2. **PyOD as the multivariate correlation layer** — Run periodically (e.g., every 5 minutes) on windowed feature vectors combining all three sensor channels. Isolation Forest or ECOD can catch subtle multi-sensor anomalies (e.g., temperature and vibration rising together while pressure drops) that univariate detectors miss. Its maturity and algorithm breadth give you room to iterate.

3. **PySAD as an alternative to STUMPY** if you prefer a more traditional streaming ML approach over the matrix profile paradigm, or if you need probability-calibrated anomaly scores out of the box.

4. **Merlion for prototyping and benchmarking** — Its `DefaultDetector` and evaluation pipeline are excellent for quickly establishing baseline performance. But consider the maintenance risk before committing it to a production deployment.

The key trade-off: STUMPY + PyOD gives you the most actively maintained, lightweight, dependency-conflict-free stack, while PySAD offers the cleanest streaming API at the cost of a smaller community. Avoid ADTK — despite its clean API and some continued community usage, its last release was April 2020 and it has known compatibility issues with modern pandas.[20][21][22]

Sources
[1] Stumpy: unleashing the power of the matrix profile for time series ... https://blog.lambdaclass.com/stumpy-unleashing-the-power-of-the-matrix-profile-for-time-series-analysis/
[2] STUMPY is a powerful and scalable Python library for ... - GitHub https://github.com/stumpy-dev/stumpy
[3] The Matrix Profile — stumpy 1.14.1 documentation https://stumpy.readthedocs.io/en/latest/Tutorial_The_Matrix_Profile.html
[4] Incremental Matrix Profiles for Streaming Time Series Data https://stumpy.readthedocs.io/en/latest/Tutorial_Matrix_Profiles_For_Streaming_Data.html
[5] Releases · stumpy-dev/stumpy - GitHub https://github.com/stumpy-dev/stumpy/releases
[6] A Robust and Explainable Data-Driven Anomaly Detection ... - arXiv https://arxiv.org/abs/2209.11427
[7] pyod · PyPI https://pypi.org/project/pyod/
[8] yzhao062/pyod: A Python Library for Outlier and Anomaly ... - GitHub https://github.com/yzhao062/pyod
[9] Versions | pyod | PyPI - Open Source Insights https://deps.dev/pypi/pyod/0.5.8/versions
[10] Python Streaming Anomaly Detection (PySAD) — PySAD 0.3.4 ... https://pysad.readthedocs.io
[11] PySAD: A Streaming Anomaly Detection Framework in Python - arXiv https://arxiv.org/abs/2009.02572
[12] selimfirat/pysad: Streaming Anomaly Detection Framework in Python ... https://github.com/selimfirat/pysad
[13] Releases · selimfirat/pysad - GitHub https://github.com/selimfirat/pysad/releases
[14] pysad · PyPI https://pypi.org/project/pysad/
[15] Salesforce advances open-source Merlion project for time-series ML ... https://venturebeat.com/ai/salesforce-advances-open-source-merlion-project-for-time-series-ml-analysis
[16] Merlion: A Machine Learning Framework for Time Series ... https://github.com/salesforce/Merlion
[17] Introduction to Time Series Modeling using Machine Learning https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[18] Releases · salesforce/Merlion - GitHub https://github.com/salesforce/Merlion/releases
[19] Pull requests · salesforce/Merlion - GitHub https://github.com/salesforce/Merlion/pulls
[20] arundo/adtk: A Python toolkit for rule-based/unsupervised ... - GitHub https://github.com/arundo/adtk
[21] Performing Real-Time Anomaly Detection with InfluxDB 3 - InfluxData https://www.influxdata.com/blog/real-time-anomaly-detection-influxdb-3/
[22] Releases · arundo/adtk - GitHub https://github.com/arundo/adtk/releases
[23] dtaianomaly: A Python library for time series anomaly ... https://arxiv.org/abs/2502.14381
[24] Timur Bikmukhametov, PhD's Post - LinkedIn https://www.linkedin.com/posts/timurbikmukhametov_top-5-anomaly-detection-libraries-for-time-activity-7307371339634429952-Zc9r
[25] ML-KULeuven/dtaianomaly: A simple-to-use Python tool for ... - GitHub https://github.com/ML-KULeuven/dtaianomaly
[26] 9 Anomaly Detection Tools and Libraries for Time Series Data https://aimodels.org/open-source-ai-tools/anomaly-detection-tools-libraries-time-series-data/
[27] lmmentel/awesome-time-series https://github.com/lmmentel/awesome-time-series
[28] Anomaly Detection in Time Series | The PyCharm Blog https://blog.jetbrains.com/pycharm/2025/01/anomaly-detection-in-time-series/
[29] What libraries I can use for Anomaly detection in Time-series data in ... https://stackoverflow.com/questions/66642332/what-libraries-i-can-use-for-anomaly-detection-in-time-series-data-in-python
[30] Master Time Series: Python Resources https://www.kaggle.com/general/469290
[31] A Practical Toolkit for Time Series Anomaly Detection, Using Python https://towardsdatascience.com/a-practical-toolkit-for-time-series-anomaly-detection-using-python/
[32] Real-time anomaly detection: algorithms, use cases & SQL code https://www.tinybird.co/blog/real-time-anomaly-detection
[33] Related Software - sktime documentation https://www.sktime.net/en/latest/related_software.html
[34] Time Series Projects: Tools, Packages, and Libraries https://neptune.ai/blog/time-series-tools-packages-libraries
[35] yzhao062/anomaly-detection-resources - GitHub https://github.com/yzhao062/anomaly-detection-resources
[36] Top 5 Anomaly Detection Libraries for Timeseries https://careercompassai.io/blogs/top-5-anomaly-detection-libraries-for-timeseries
[37] Welcome to Merlion's documentation! https://opensource.salesforce.com/Merlion/v1.0.0/index.html
[38] Anomaly detection in time series with Python - YouTube https://www.youtube.com/watch?v=qy41dXGbAxY
[39] Building a Monitoring System That Actually Works https://towardsdatascience.com/building-a-monitoring-system-that-actually-works/
[40] pyod 2.0.6 documentation https://pyod.readthedocs.io
[41] How to Download and Install PIP for Python 3.11 (Easy Method) https://www.youtube.com/watch?v=T41ob6zLC_4
[42] Getting Started with Anomaly Detection Toolkit (ADTK) - Cake AI https://docs.cake.ai/docs/getting-started-with-anomaly-detection-toolkit-adtk
[43] How do I install python on alpine linux? - Stack Overflow https://stackoverflow.com/questions/62554991/how-do-i-install-python-on-alpine-linux
[44] (PDF) PySAD: A Streaming Anomaly Detection Framework in Python https://www.academia.edu/94061806/PySAD_A_Streaming_Anomaly_Detection_Framework_in_Python
[45] Install Meridian - Google for Developers https://developers.google.com/meridian/docs/user-guide/installing
[46] Anomaly Detection Toolkit (ADTK) — ADTK 0.6.2 documentation https://adtk.readthedocs.io/en/stable/
[47] google-meridian - PyPI https://pypi.org/project/google-meridian/
[48] In 2024 which library is best for time series forecasting and anomaly ... https://www.reddit.com/r/MachineLearning/comments/1bho0r0/in_2024_which_library_is_best_for_time_series/
[49] pysad · PyPI https://pypi.org/project/pysad/0.1.0/
[50] [REVIEW]: STUMPY: A Powerful and Scalable Python Library for ... https://github.com/openjournals/joss-reviews/issues/1504
[51] Milestones · salesforce/Merlion - GitHub https://github.com/salesforce/Merlion/milestones
[52] Stateless ADTK detector plugin | InfluxDB 3 Enterprise Documentation https://docs.influxdata.com/influxdb3/enterprise/plugins/library/official/stateless-adtk-detector/
[53] Issues · stumpy-dev/stumpy - GitHub https://github.com/TDAmeritrade/stumpy/issues
[54] Activity · salesforce/Merlion - GitHub https://github.com/salesforce/Merlion/activity
[55] User Guide — ADTK 0.6.2 documentation https://arundo-adtk.readthedocs-hosted.com/en/stable/userguide.html
[56] Issues · stumpy-dev/stumpy - GitHub https://github.com/stumpy-dev/stumpy/issues
[57] Python 3.14 Released - Python News for November 2025 https://realpython.com/python-news-november-2025/
[58] Download Python https://www.python.org/downloads/
[59] Welcome to Merlion's documentation! https://opensource.salesforce.com/Merlion/latest/index.html
[60] github.com-salesforce-Merlion_-_2021-09-24_21-07-36 https://archive.org/details/github.com-salesforce-Merlion_-_2021-09-24_21-07-36
[61] pyserial - PyPI Download Stats https://pypistats.org/packages/pyserial
[62] salesforce-merlion - conda-forge - Anaconda.org https://anaconda.org/conda-forge/salesforce-merlion
[63] merlion: Time Series Intelligence https://opensource.salesforce.com/Merlion/latest/merlion.html


---


