# Al-Folio Migration Package for Franklin Fuchs

> This file contains ALL content and configuration from the old academicpages site,
> structured for migration to al-folio. Open the cloned al-folio-dev repo in Kiro
> and paste this file in. Then tell Kiro: "Use MIGRATION_PACKAGE.md to set up my site."

---

## 1. SITE CONFIGURATION

```yaml
# Key values for _config.yml
first_name: Franklin
last_name: Fuchs
email: fuchs.franklin@gmail.com
location: NYC
employer: Mondelēz
description: >
  Business Intelligence and Forecasting Manager working on optimization, LLM systems, and decision-making under uncertainty.
url: https://fuchsfranklin.github.io
baseurl: ""  # leave empty

# Social
github_username: fuchsfranklin
linkedin_username: franklin-fuchs-aab0a6306

# Theme
theme_color: dark

# No Google Scholar, ORCID, or Twitter currently
```

---

## 2. ABOUT PAGE (Homepage)

Current bio from `_pages/about.md`:

> I am currently working at Mondelēz as a Business Intelligence and Forecasting Manager in the
> Insights and Analytics Group under Ryan Grum and closely with Matthew Kullmann, where I focus on consumer research
> and providing product portfolio insights using methods in Algorithmic Marketing, alongside
> automating analytical workflows and model deployment through cloud computing at scale.
>
> The areas and ideas I (personally) think about a lot often relate to fat tailed distributions,
> or more accessibly thought of as black swan type phenomena. I also like learning about concepts
> in psychology, especially behavioural science and mental health. In my free time I like to exercise.

---

## 3. CV DATA

### Education
- Johns Hopkins University — ScM in Biostatistics (2021-2023)
- University of Nevada, Reno — Honors BS in Mathematics (Statistics Emphasis), Minor in Big Data (2017-2021)

### Skills
- Programming Languages: R, Python, SQL, C++, C, MATLAB
- Software: GCP, AWS, Databricks, BigQuery, Dataiku, Docker, Singularity, SLURM, Markdown, Shiny, LaTeX, Linux Shell, Office Suite, Git, and GitHub
- Modeling and Computing: Multi-Objective Optimization, Classification, Regression, Time Series Forecasting, Predictive Analytics, Feature Engineering, Variable Selection, Data Wrangling, Exploratory Data Analysis, High-Performance/Cluster Computing, Containerization, Database Design and Implementation, Web-Application Development, Interactive Data Visualization, LLM Infrastructure Testing/Development

### Work Experience

1. **Mondelēz Insights and Analytics Group** — Business Intelligence and Forecasting Manager (Apr. 2026 - Present)

2. **Mondelēz Insights and Analytics Group** — Data Science Manager (Jun. 2025 - Apr. 2026)

3. **Pfizer Digital Client Partners** — Data Scientist - DRP Associate (Jun. 2024 - Jun. 2025)
   - Multi-Objective Optimization for target product profile support (Evolutionary Algorithms, RL, Robust Portfolio Optimization)
   - Interactive D3/Python/R visualizations for unmet needs analysis, AWS deployments
   - LLM-enhanced data APIs, RAG systems with source citation, disease evidence map generation

3. **Pfizer AI/ML/Analytics Enterprise Architecture** — Software/Solution Engineer - DRP Associate (Jun. 2023 - Jun. 2024)
   - Prototyped Vector Databases and RAG for internal LLM with enterprise scalability (AWS)
   - Enterprise Architecture CityMap tool in Python
   - Evaluation framework documentation for Architecture Data/Analytics Platform
   - Interactive dashboards (Power BI, Tableau, Python, Excel)

4. **Pfizer Machine Learning and Computational Science Group** — Data Scientist Intern (Jun. 2022 - Aug. 2022)
   - MySQL database for proteomics data (Chemical Biology Group)
   - R Shiny UI for experiment/data management
   - Extended MSstats R package for proteomics

5. **Pfizer Simulation and Modeling Science Group** — Software Development Intern (Jun. 2021 - Aug. 2021)
   - Automated data pipeline in R for computational proteomics cloud (SevenBridges)
   - R Shiny General User Interface

6. **UNR Visual Perception Lab** — Student Researcher, HURA Award (Jan. 2021 - May 2021)
   - Sleep classification algorithms (R to MATLAB port)
   - Arduino-based wrist-wearable for circadian rhythm measurement (C/C++)

7. **Nevada INBRE** — Student Researcher, INBRE UROP Award (Jan. 2020 - Jan. 2021)
   - R Shiny web-app for TBI prediction model deployment
   - Docker/Singularity containerized parallelized analyses on HPC
   - Pediatric TBI predictive modeling (supervised ML + traditional statistics)

8. **UNR Department of Mathematics** — Statistics Research Assistant (Aug. 2019 - Jan. 2020)
   - Bayesian regression analyses for UNR medical school curriculum evaluation

9. **Swiss Armed Forces NBC Defense School** — Biology Laboratory Specialist (Jul. 2016 - Dec. 2016)
   - Microbiological hazard identification, BSL-3 laboratory work

### Teaching
- JHU Bloomberg School of Public Health — Teaching Assistant (Aug. 2022 - May 2023)
- UNR Honors College — Honors Peer Coach and Teaching Assistant (Aug. 2019 - May 2021)
- UNR Department of Mathematics — Statistics Grader (Jan. 2020 - May 2020)
- UNR Department of Computer Science — Computer Science Teaching Fellow (Jan. 2018 - Apr. 2019)

### Awards
- Honors Undergraduate Research Award (HURA) — $1,500 + $500 mentor stipend (2021)
- Nevada INBRE UROP — $6,000 + $1,000 mentor stipend (2020)
- 1st Place, 2019 Capstone Statistical Computing Project Competition (2019)


---

## 4. PUBLICATION (BibTeX)

```bibtex
@article{fuchs2025adiponectin,
  title     = {Association of serum adiponectin and leptin levels with inner retinal thickness among individuals with or without elevated HbA1c},
  journal   = {Scientific Reports},
  year      = {2025},
  url       = {https://www.nature.com/articles/s41598-025-93562-9},
  selected  = {true}
}
```

Note: The author field was listed as "Co-Authored" on the old site. Franklin should fill in the full author list.

---

## 5. PROJECTS (migrate to `_projects/`)

### Project 1: Multi-Agentic Oncology Value Scorecard Creation with LLMs
- **GitHub**: https://github.com/fuchsfranklin/multi-agentic-scorecard-creation
- **Description**: Replicating established oncology value frameworks (ISPOR Scorecard, ASCO Value Framework) using LLMs. Compares multi-agent systems, single LLM pipelines, and RAG using ClinicalTrials.gov, PubMed, and OpenFDA. A fourth MOA-based multi-agent framework was later integrated.
- **Collaborators**: Brett South, Ajit Jadhav, Jay Ronquillo, Jon Mauer, Stephen Watt (Pfizer colleagues)
- **Importance**: 1 (flagship)

### Project 2: BaltimoreTrails R Package and Dashboard
- **GitHub**: https://github.com/datatrail-jhu/BaltimoreTrails
- **Live App**: https://fuchsfranklin25.shinyapps.io/shiny-examples/
- **Description**: R package and Shiny dashboard for integrating Baltimore datasets into the DataTrail data science education initiative (JHU Bloomberg School of Public Health). ScM thesis work.
- **Importance**: 2

### Project 3: Survival Analysis Shiny App
- **GitHub**: https://github.com/fuchsfranklin/Survival-Analysis-Project
- **Live App**: https://franklinf.shinyapps.io/Survival-Analysis-Project/
- **Description**: R Shiny web-app introducing survival analysis concepts using a Moderna vaccine dataset. With Tiffany Hsieh and Bowen Chen.
- **Importance**: 3

### Project 4: Pediatric TBI Mortality Prediction Web-Application
- **GitHub**: https://github.com/fuchsfranklin/Pediatric-TBI-Prediction-Application
- **Live App**: https://franklinfuchs.shinyapps.io/Pediatric-TBI-Prediction-Application/
- **Description**: C5.0 decision tree classifier on SMOTE-subsampled data for pediatric TBI mortality prediction. Part of honors thesis. Published at IEEE BIBM (doi: 10.1109/BIBM49941.2020.9313568).
- **Importance**: 2

### Project 5: Metropolis-Hastings Algorithm Visualization
- **GitHub**: https://github.com/fuchsfranklin/MCMC-Visualization-Project
- **Live App**: https://franklinfuchs.shinyapps.io/MCMC_Visual_Project/
- **Description**: Interactive animated visualizations of the Metropolis-Hastings algorithm and MCMC diagnostics in R Shiny.
- **Importance**: 4

### Project 6: Variable Selection Techniques on Simulated Data
- **GitHub**: https://github.com/fuchsfranklin/Regularization-Project
- **Live**: https://rpubs.com/franklinfuchs/Regularization-Project
- **Description**: Simulating multivariate data from Tibshirani (1996) Lasso paper and comparing variable selection methods (AIC, BIC, Adjusted R²).
- **Importance**: 5

### Project 7 (HIDDEN on old site): COVID-19 Modeling
- **GitHub**: https://github.com/fuchsfranklin/Exploratory-Covid-Modeling
- **Description**: COVID-19 pandemic dynamics through healthcare strain, pandemic fatigue, and policy effectiveness. Ensemble methods for ICU utilization prediction.
- **Importance**: 6

### SKIP: Old Shiny Personal Website (portfolio-6) — retired, don't migrate

---

## 6. BLOG POSTS (migrate to `_posts/`)

### Post 1: Pure Indexing, Factor Tilts, Three-Fund Portfolio
- **Date**: 2025-12-27
- **Old permalink**: /posts/2025/12/pure-indexing-factor-tilts-three-fund-portfolio/
- **Tags**: investing, index-funds, factor-investing, bogleheads, personal-finance
- **Images needed**: vti_vxus_mix_growth.png, vti_dfus_growth.png, vxus_dfax_growth.png
- **Code files needed**: vti_vxus_mix_comparison.py, vti_dfus_comparison.py, vxus_dfax_comparison.py, factor_regression_analysis.py
- **External code repo**: https://github.com/fuchsfranklin/balancing-priorities-project
- **Note**: Contains custom CSS for larger code blocks and images — will need al-folio equivalent or can be dropped (al-folio handles this natively)

### Post 2: Breaking Deep Research — Where LLM Search Agents Fail
- **Date**: 2026-03-03
- **Old permalink**: /posts/2026/03/breaking-deep-research-where-llm-search-agents-fail/
- **Tags**: AI, deep-research, LLMs, hallucination, verification
- **Images needed**: none (tables only)
- **Note**: Contains HTML `<details>` blocks for appendix — al-folio supports these natively. Also has custom CSS that can be dropped.

---

## 7. IMAGES TO COPY

From old repo `images/` → new repo `assets/img/`:
- `profile.png` → `prof_pic.jpg` (or keep as .png, al-folio supports both)
- `vti_vxus_mix_growth.png`
- `vti_dfus_growth.png`
- `vxus_dfax_growth.png`
- `tbi_prediction_webapp.png`

---

## 8. FILES TO COPY

From old repo `files/` → new repo `assets/`:
- `files/blog/factor_regression_analysis.py` → `assets/code/factor_regression_analysis.py`
- `files/blog/vti_dfus_comparison.py` → `assets/code/vti_dfus_comparison.py`
- `files/blog/vti_vxus_mix_comparison.py` → `assets/code/vti_vxus_mix_comparison.py`
- `files/blog/vxus_dfax_comparison.py` → `assets/code/vxus_dfax_comparison.py`
- `files/paper1.pdf`, `paper2.pdf`, `paper3.pdf` → check if these are real papers or template files

---

## 9. NAVIGATION (old site had 3 items)

Old nav:
1. Expanded Resume/CV → /cv/
2. Projects → /portfolio/
3. Data & Daydreams (Blog) → /year-archive/

Suggested al-folio nav (configured in `_data/navigation.yml` or `_config.yml`):
1. About (homepage, default)
2. Projects
3. Publications
4. Blog (keep "Data & Daydreams" as subtitle or description)
5. CV

---

## 10. POSTERS/PRESENTATIONS (from CV, for reference)

These are listed in the CV but don't have dedicated pages:
- "Association of serum adiponectin..." — Scientific Reports 2025 (PUBLICATION, handled above)
- "Enhancing DataTrail..." — ScM Thesis (2023) (PROJECT, handled above)
- "ProtIOT" — Pfizer MLCS group talk (2022)
- "Standardized Proteomics Pipeline" — Pfizer SMS/MI demos (2021)
- "Low-Cost Arduino-Based Wearable" — UNR Symposium (2021)
- "Pediatric TBI Survival Prediction" — IEEE BIBM + UNLV Symposium (2020) (doi: 10.1109/BIBM49941.2020.9313568)
- "Intuitive Introduction to Metropolis-Hastings" — Personal Project (2020)
- "Bayesian Regression Model" — UNR Capstone Competition (2019)
- "Comparing Regularization Techniques" — Personal Project (2019)

---

## 11. DARK THEME SETUP

In al-folio's `_config.yml`, set:
```yaml
# Theme
theme_color: dark
```

This enables the dark theme globally. Users can toggle between light/dark via the sun/moon icon in the navbar.

To default to dark and still allow toggling, this is the default behavior when `theme_color: dark` is set.

---

## 12. LOCAL DEVELOPMENT

```bash
# Option A: Docker (recommended)
docker compose pull
docker compose up
# Visit http://localhost:8080

# Option B: VS Code Dev Container
# Just open the repo in VS Code, accept the Dev Container prompt

# Option C: Native Ruby (if you have it)
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

---

## 13. DEPLOYMENT CHECKLIST (when ready to go live)

1. Rename current `fuchsfranklin.github.io` repo → `old-site-backup`
2. Rename `al-folio-dev` → `fuchsfranklin.github.io`
3. In `_config.yml`, confirm `url: https://fuchsfranklin.github.io` and `baseurl: ""`
4. In repo Settings → Actions → General → Workflow permissions → Read and write
5. Push to main branch
6. Wait for "Deploy site" GitHub Action (~4 min)
7. In repo Settings → Pages → set branch to `gh-pages`
8. Wait for `pages-build-deployment` action (~45s)
9. Visit https://fuchsfranklin.github.io
