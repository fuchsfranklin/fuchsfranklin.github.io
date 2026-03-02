# ChatGPT Deep Research Response

**Date tested:**
**Model/tier:** ChatGPT Deep Research (free)

## Paste the full response below this line:

OpenAI:

# Comparison of Open-Source AutoML Libraries for Tabular Data

The five libraries differ significantly in upkeep, community, and technical capabilities. **auto-sklearn** is a scikit-learn–based AutoML framework that “takes care of … encoding of categorical parameters and missing values”【51†L123-L126】. It is a drop-in replacement for an sklearn estimator【51†L109-L117】. However, its development has slowed: the latest PyPI release is version 0.15.0 (Sep 2022)【74†L31-L34】, with few recent updates. **TPOT** (Tree-based Pipeline Optimization Tool) uses genetic programming to evolve sklearn pipelines. It integrates natively with sklearn pipelines and can include preprocessing steps, but it does *not* automatically impute missing values or encode categories – these must be handled by pipeline steps. TPOT is actively maintained: version 1.1.0 was released July 3, 2025【76†L29-L34】, and the project has ~10k GitHub stars, indicating strong community use.

**H2O AutoML** (part of H2O-3) is a mature platform (Java backend) accessible via Python. It natively supports categorical data and missing values: for example, H2O’s tree-based models treat missing and unseen categories as a special “NA” category【80†L130-L138】. H2O AutoML does not fit directly into sklearn pipelines (data must be converted to an H2OFrame or pandas). Its maintenance is very active – H2O-3 had multiple patch releases in 2024–2025 (latest 3.46.0.9 on Nov 24, 2025)【22†L1-L4】. H2O has a large ecosystem (enterprise support, forums) and 7.5k GitHub stars. **FLAML** (by Microsoft) is a lightweight Python AutoML library with strong sklearn compatibility. It automatically preprocesses data: continuous features have NaNs imputed by median, and categorical NaNs are replaced with a special `"__NAN__"` category【48†L67-L75】. It can also be inserted into a scikit-learn `Pipeline` (e.g. as a transformer)【57†L39-L42】. FLAML is actively maintained (v2.5.0 in Jan 2025)【24†L239-L247】 and has ~4.3k stars.

**AutoGluon** (by AWS) is a broad AutoML toolkit covering tabular, image, text, and time-series data. Its TabularPredictor handles missing and categorical data internally. (In fact, AutoGluon “does not perform generic missing value imputation; instead it sends missing values to each model, and each model has different custom handling”【82†L469-L475】.) As of late 2023 it gained a scikit-learn–compatible API (classes like `TabularClassifier`)【64†L194-L202】, so it can be integrated into sklearn pipelines. AutoGluon is under very active development: v1.5.0 was released Dec 2025【67†L27-L35】, and it has ~10k stars. It requires more resources (sometimes GPU, deep-learning libraries) but achieves state-of-art results in benchmarks【28†L922-L931】.

## Technical Feature Support

- **Scikit-learn pipeline integration:** auto-sklearn, TPOT, FLAML, and AutoGluon (via its new sklearn API【64†L194-L202】) all support use in sklearn pipelines. H2O AutoML does **not** plug into sklearn pipelines without wrappers.
- **Categorical features:** auto-sklearn, H2O, FLAML, and AutoGluon all natively handle categorical data. (auto-sklearn “takes care about … encoding of categorical parameters”【51†L123-L126】; H2O uses native factor columns【80†L130-L138】; FLAML auto-encodes dataframes’ object/category columns; AutoGluon’s models ingest categorical features directly.) TPOT requires the user to include encoders (e.g. `OneHotEncoder`) in the pipeline.
- **Missing values:** FLAML automatically imputes NaNs (median for numeric, placeholder for categorical)【48†L67-L75】. H2O’s algorithms treat missing as a category【80†L130-L138】. AutoGluon leaves missing values in raw data and relies on each learner’s handling【82†L469-L475】. auto-sklearn internally uses sklearn imputers during preprocessing【51†L123-L126】. TPOT requires manual imputation (it offers preprocessing templates but does not auto-impute on its own).
- **Tasks supported:** All five handle classification and regression. AutoGluon extends to multi-modal (text, image, etc.), and H2O has time-series extensions.
- **Licenses:** AutoGluon (Apache-2), FLAML (MIT/Apache), auto-sklearn (BSD3)【74†L61-L64】, TPOT (LGPLv3)【76†L59-L66】, H2O (Apache-2). All are open-source.

## Community & Maintenance

- **Active development:** TPOT, FLAML, AutoGluon, and H2O show frequent updates in 2024–2025. For example, TPOT 1.1.0 (Jul 2025) and FLAML 2.5.0 (Jan 2025)【76†L29-L34】【24†L239-L247】 were released recently. AutoGluon 1.5.0 arrived Dec 2025【67†L27-L35】. H2O-3 has monthly patches (3.46.x series) through late 2025【22†L1-L4】. In contrast, auto-sklearn’s last stable release (0.15.0) was Sep 2022【74†L31-L34】, suggesting slower momentum.
- **Community size:** AutoGluon, TPOT, and auto-sklearn each have ~10k, ~10k, and ~8k GitHub stars respectively; H2O-3 has ~7.5k stars【52†L13-L20】. FLAML has ~4.3k stars. These reflect user adoption. All projects have active issue trackers or forums (H2O also offers enterprise support and a public forum).
- **Support channels:** AutoGluon and FLAML have community discussions (Discord, GitHub Discussions). H2O maintains a community forum and chat. TPOT has a mailing list/Google group. auto-sklearn has community help via GitHub issues and mailing lists.

## Integration & Production Considerations

- **Deployment:** H2O AutoML can export models as “MOJO” (Java artifacts) for low-latency scoring and production; other frameworks deploy as Python libraries/models. AutoGluon and FLAML models can be saved via Python pickle or their own save methods. auto-sklearn and TPOT produce sklearn models which can be exported (e.g. to ONNX) but typically run in Python.
- **Resource footprint:** FLAML is lightweight (designed for speed/efficiency). TPOT can be compute-heavy (evolutionary search). AutoGluon may require GPUs for its largest presets. H2O can be memory-intensive (runs a JVM cluster by default). auto-sklearn runs on CPU with moderate resources.
- **Compatibility:** All support Linux/Mac/Windows. H2O requires Java for its core. Required Python versions: all support 3.7+ up through 3.13 (some even 3.13 on dev versions)【67†L27-L35】【76†L29-L34】.
- **Ease of use:** auto-sklearn, FLAML, and AutoGluon provide simple `.fit()` APIs. TPOT requires specifying generations or time budgets. H2O AutoML is similarly easy via its API but less “Pythonic” (because of H2OFrame usage).

## Recommendations for 2025

Considering active maintenance, broad community, and the stated requirements, the top choices are **AutoGluon, FLAML,** and **TPOT** (or H2O AutoML in some cases):

- **AutoGluon** – Best overall for production. It is under active development (v1.5.0 in 2025)【67†L27-L35】, handles categorical/missing data natively【82†L469-L475】, and now offers a sklearn-compatible API【64†L194-L202】. Its tabular module leads benchmarks【28†L922-L931】. The AWS backing and large user base make it reliable for production, especially if GPU resources are available.
- **FLAML** – Excellent for mid-size deployments. Actively maintained (v2.5.0 in Jan 2025)【24†L239-L247】, it natively encodes missing/categorical data【48†L67-L75】 and integrates easily into sklearn pipelines【57†L39-L42】. Its lightweight design means it runs quickly and is easy to embed in existing Python ML workflows.
- **TPOT** – Good choice if an evolutionary/pipeline-oriented approach is desired. Recent updates (v1.1.0, Jul 2025)【76†L29-L34】 and a large community indicate it’s production-ready. It requires manual handling of missing/categorical data, so make sure to add imputers/encoders in the pipeline.
- **H2O AutoML** – Also a strong candidate for production. It is heavily maintained【22†L1-L4】 and robust in handling messy data (categoricals and missing)【80†L130-L138】. It excels when a JVM-based solution or MOJO exporting is needed. However, it’s heavier and less seamless in pure Python pipelines.
- **auto-sklearn** – Solid academically, but its slower release cadence (last release 2022)【74†L31-L34】 and smaller team make it a less optimal choice in 2025 compared to the above.

In summary, **AutoGluon** and **FLAML** stand out for production use in 2025, with **TPOT** (or **H2O AutoML**) as additional options depending on specific needs. All cited sources support these conclusions and the detailed comparisons above【67†L27-L35】【24†L239-L247】【76†L29-L34】【51†L123-L126】.

**Sources:** Official docs and release notes for each library【51†L123-L126】【74†L31-L34】【76†L29-L34】【24†L239-L247】【22†L1-L4】【48†L67-L75】【82†L469-L475】. These highlight recent versions, feature support, and integration details.

---


