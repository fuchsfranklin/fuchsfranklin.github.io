---
title: 'Breaking Deep Research: Where Retail User LLM Search Agents Fail and Why Verification Still Falls on You'
date: 2026-03-03
permalink: /posts/2026/03/breaking-deep-research-where-llm-search-agents-fail/
excerpt: "Deep research tools from OpenAI, Google, and Perplexity promise source-grounded synthesis, but their reliability depends heavily on what they are searching. Professional tools connected to peer-reviewed databases like PubMed have a built-in quality gate: the barrier to publication is literally peer review. But for code repositories, blog posts, and other sources with no editorial barrier, deep research inherits every error, exaggeration, and fabrication in the source material. Digging into some of the recent literature myself, it looks like studies often find citation accuracy as low as 40% and fabricated references. I tested all three tools on the same library-evaluation question as a small experiment to show how they can fail (a la proof by contradiction). One tool recommended an abandoned library as its top pick with an apparently fabricated release date. The issue of AI-generated content infiltrating peer review itself is a separate and important problem, but not within the scope of this post."
tags:
  - AI
  - deep-research
  - LLMs
  - hallucination
  - verification
---

<style>
/* Larger, more readable code block text */
.page__content pre {
  font-size: 1.6em;
  line-height: 1.5;
}

/* Larger images - slightly bigger while maintaining centering */
.page__content img {
  max-width: 95%;
  display: block;
  margin: 1.5em auto;
}
</style>

## Post Rationale

I use deep research tools regularly (ChatGPT's Deep Research, Gemini, Perplexity Pro), and they are genuinely useful for getting up to speed on unfamiliar topics. But the more I use them for anything technical, especially code or quantitative claims, the more I notice a pattern, where these tools are confidently wrong in ways that are hard to catch unless you already know the answer.

Their reliability depends fundamentally on what they are searching. Connect an LLM to PubMed or a curated legal database, and the source material has already passed through peer review. The barrier to publication is itself a quality gate. The tool can still misinterpret, but at least the underlying sources have been vetted by domain experts. Professional connectors restricted to these databases are, for this reason, substantially more reliable than open web search.

But most of what retail-facing deep research tools search is not peer-reviewed. Code repositories, blog posts, Stack Overflow answers, documentation pages. None of these have a publication barrier. Anyone can push a README claiming state-of-the-art performance. And deep research cannot tell the difference, because it reads text, not code, and cannot execute anything to verify claims independently.

This post aims to better understand why deep research fails in these unvetted domains, grounded in some recent literature, with a small experiment to illustrate the problem firsthand. This is not a takedown of these tools, but understanding where the quality gate exists (and where it does not) matters if you use them for anything important. The separate issue of AI-generated content infiltrating peer review itself (fabricated citations in accepted papers, LLM-written reviews, etc.) is a growing concern but not within scope here.

---

## Overview

The post is structured as follows, covering the literature and a small experiment.

1. [**What Deep Research Actually Does (and Does Not Do)**](#what-deep-research-actually-does-and-does-not-do) - The retrieval-synthesis pipeline and its blind spots
2. [**The Citation Problem**](#the-citation-problem) - Fabricated references, broken URLs, and misattributed claims
3. [**The Code Verification Gap**](#the-code-verification-gap) - Why deep research cannot verify what code actually does
4. [**Why Connectors and RAG Do Not Fully Solve This**](#why-connectors-and-rag-do-not-fully-solve-this) - Hallucinations accumulate across the research trajectory
5. [**Experiment: One Question, Three Tools, Ground Truth**](#experiment-one-question-three-tools-ground-truth) - Testing ChatGPT, Gemini, and Perplexity on library evaluation
6. [**What This Means for You**](#what-this-means-for-you) - Practical implications
7. [**References**](#references) - Sources
8. [**Appendix: Full Model Responses**](#appendix-full-model-responses) - Verbatim outputs from all three tools

---

### What Deep Research Actually Does (and Does Not Do)

Deep research tools work roughly as follows: you give the model a question, it formulates a search plan, retrieves documents from the web (or from specified sources), reads through them, and synthesizes a long-form report with citations. OpenAI's version browses autonomously for around 5 to 30 minutes. Gemini and Perplexity follow similar patterns with their own retrieval backends.

What these tools do well: they aggregate information across many sources faster than any human could. They produce structured, readable reports. They cite their sources (most of the time).

What they do not do: they do not execute code. They do not verify that a dataset contains what its documentation claims. They do not check whether a function's output matches its docstring. They do not run statistical analyses to confirm reported numbers. They do not cross-reference a paper's abstract against its actual results tables. They read text and generate text as the full operation.

This distinction matters more than most users realize. When you ask deep research a question about a GitHub repository, it reads the README, maybe some issues, maybe a blog post about the repo. It does not clone the repo, install dependencies, and run the test suite. It cannot tell you if the code is broken, if the results are reproducible, or if the README is lying. It takes documentation at face value, which is exactly what a careful researcher would not do.

---

### The Citation Problem

The most well-documented failure mode of deep research tools is citation fabrication and misattribution. This is not a fringe issue. It has been measured repeatedly, at scale, and the numbers do not seem good.

A 2025 study by the Tow Center for Digital Journalism at Columbia University evaluated eight AI search tools by feeding them real excerpts from published news articles and asking them to identify the source. Over 60% of responses contained incorrect or misleading information. ChatGPT provided false citations 134 times out of 200 responses and signaled a lack of confidence only 15 times. It never declined to answer (Tow Center, 2025). The tools did not say "I don't know." They said the wrong thing with full confidence.

Another study by BBC and the European Broadcasting Union analyzed over 3,000 responses from ChatGPT, Gemini, Copilot, and Perplexity on current news topics. 45% of responses contained at least one significant issue. 31% had serious sourcing problems. 20% had major accuracy issues including hallucinated details and outdated information. When accounting for minor errors, 81% of responses had some form of problem. Gemini was the worst performer, with significant issues in 76% of its responses (BBC/EBU, 2025).

Finally, a study analyzing papers accepted at NeurIPS 2025, one of the most prestigious AI conferences in the world, found 100 fabricated citations across 53 accepted papers (Ansari, 2025). These were not student projects. These were peer-reviewed papers at a top venue, and the fabricated references slipped through. This is an example of AI-generated content infiltrating the peer review process itself, which as noted in the rationale is a separate and important problem. For our purposes here, it illustrates that even the peer-review quality gate is not immune to AI-era challenges, though it remains a far stronger filter than no gate at all.

The DeepTRACE audit framework (Venkit et al., 2025) from Salesforce AI Research evaluated deep research agents specifically. Their findings: citation accuracy ranged from 40% to 80% across systems. Deep research configurations reduced overconfidence compared to standard search, but still produced large fractions of statements unsupported by their own listed sources. Even when the tools cited a source, the source often did not actually support the claim being made.

A separate study published in JMIR Mental Health found that across 176 AI-generated citations from GPT-4o, 35 were completely fabricated, 64 of the real ones contained errors, and only 77 (44%) were both real and accurate. Hallucination rates increased on specialized or less-covered topics (Linardon et al., 2025).

The pattern is consistent across studies: these tools fabricate sources, misattribute claims, link to broken URLs, and do all of this without expressing uncertainty. The user has no way to distinguish a real citation from a hallucinated one without manually checking every single reference.

---

### The Code Verification Gap

This is where things get particularly interesting for anyone using deep research for coding or technical questions. The fundamental issue: deep research tools read about code but never run code. This creates a verification gap that is structurally impossible to close within the current architecture (unless a explicit framework is developed for this, which is probably already in the works of the AI frontier labs).

The CodeHalu benchmark (Tian et al., 2024) systematically studied code hallucinations in LLMs and identified four distinct types: mapping hallucinations (misunderstanding the task), naming hallucinations (referencing nonexistent APIs or variables), resource hallucinations (using unavailable external resources), and logic hallucinations (producing code that is syntactically valid but logically wrong). The main finding was that LLMs generate code that looks correct and often compiles without errors, but fails to produce expected outputs when actually executed.

This problem extends beyond generating code to a more serious issue: recommending code that does not exist. A large-scale study analyzing 576,000 code samples generated by 16 widely used LLMs found that the average percentage of hallucinated packages was at least 5.2% for commercial models and 21.7% for open-source models, with over 205,000 unique hallucinated package names identified (Spracklen et al., 2025). This phenomenon, coined as "slopsquatting," has become a real supply chain security threat. Malicious actors can register these hallucinated package names and fill them with malware, knowing that developers using LLM-generated code will install them.

Now consider what happens when you ask a deep research tool about a specific GitHub repository. The tool reads the README, reporting the claimed functionality as fact (where again, GitHub specfic functionalities might already be in the works, but I have not seen any corresponding toolset for this, especially in the tools available to retail users). But it cannot:

- Clone the repo and check if the code actually runs
- Verify that the reported benchmark numbers are reproducible
- Determine if the implementation matches the paper it claims to implement
- Check whether the "state-of-the-art" claim was true at the time of writing, let alone now
- Identify if the code has known bugs in its core logic that invalidate the results

The README is treated as ground truth. For well-maintained, widely-used repositories, this is often fine. For the long tail of research code, personal projects, and less-scrutinized libraries, it is a significant source of error. And deep research has no mechanism to distinguish between the two.

---

### Why Connectors and RAG Do Not Fully Solve This

A common response to these concerns is: "Just use domain-specific connectors." If you are researching medical literature, connect the LLM to PubMed. If you need legal information, connect it to a legal database. This is the premise behind Retrieval-Augmented Generation (RAG), and it is worth distinguishing where this works and where it does not.

For peer-reviewed literature, connectors genuinely help. When a tool is restricted to searching PubMed, Scopus, or a generally curated database, the source material has already cleared a quality gate: peer review, editorial oversight, or institutional vetting. The LLM can still misinterpret or misattribute what it reads, but the underlying claims have at least been scrutinized by domain experts. This is a meaningful advantage. A PubMed-connected tool hallucinating a citation is bad, but the real citations it retrieves are far more likely to be accurate than a random blog post or GitHub README. The barrier to publication does real work here.

The problem is that most deep research queries do not stay within peer-reviewed territory. Code repositories have no publication barrier. Anyone can create a package, write a README claiming anything, and push it to GitHub. Blog posts, Stack Overflow answers, documentation pages, and forum threads are similarly unvetted. When deep research tools search the open web, they are pulling from a mix of high-quality and low-quality sources, struggling to reliably to distinguish between them.

Even within the RAG framework, connectors do not solve the deeper issue. The "Why Your Deep Research Agent Fails?" paper (Zhan et al., 2026) introduced a critical insight: hallucinations in deep research agents do not just occur at the retrieval step. They accumulate across the entire research trajectory. The authors proposed the PIES taxonomy, categorizing hallucinations along two dimensions: functional component (Planning vs. Summarization) and error property (Explicit vs. Implicit). Their experiments on six state-of-the-art deep research agents revealed that no system achieved robust reliability, and critically, flawed planning (deciding what to search for and how to structure the research) was a major source of errors that existing benchmarks completely missed.

In other words, even if you give the model perfect sources, it can still:

- Formulate a flawed research plan that misses key aspects of the question
- Selectively attend to information that confirms its initial framing
- Misinterpret or oversimplify technical content during synthesis
- Propagate an early error through the entire report

The DeepTRACE study confirmed this: deep research agents frequently produced one-sided, highly confident responses on debatable topics, even when their own cited sources contained nuance or counterarguments. The problem is not just "bad retrieval", it is that the synthesis step introduces its own distortions.

So we could say that connectors to peer-reviewed databases improve input quality substantially, and for literature-based research questions they are the right approach. But they do little about processing quality. And for code-related questions, where the source material has no publication barrier and verification requires execution rather than reading, even perfect retrieval of documentation does not substitute for running the code.

---

### Experiment: One Question, Three Tools, Ground Truth

To move beyond citing other people's findings, I wanted to test this myself. The logic is similar to proof by contradiction in mathematics: if deep research tools can reliably evaluate open-source software, then asking all three the same well-defined evaluation question should produce recommendations consistent with verifiable ground truth. If even one tool confidently recommends something that is demonstrably wrong, the verification gap is not theoretical.

**The Setup**

I asked ChatGPT Deep Research (free tier), Gemini Deep Research (free tier), and Perplexity the same question. I deliberately chose a question where deep research is the right tool: evaluating and recommending open-source libraries. This is not a coding question (you would not "just run code" to answer it), not a calculation question, and not something obscure, thus something I usually would (and do) routinely use it for.

**The Prompt:**

> I'm a data engineer building a monitoring pipeline for IoT sensor data (temperature, vibration, pressure) from manufacturing equipment. I need to detect anomalies in univariate and multivariate time series streams in near-real-time using Python. The system needs to handle seasonal patterns, trend shifts, and sudden spikes. I want a library that is production-ready, actively maintained, well-documented, and installable via pip without dependency conflicts on Python 3.11+. Can you evaluate the top open-source Python libraries for time series anomaly detection and recommend the best 3-4 options for my use case, with pros and cons for each?

**Why This Question Works**

The time series anomaly detection space in Python is full of "zombie libraries": projects that look impressive on paper (strong READMEs, blog coverage, big-name backing) but are effectively abandoned. The ground truth is verifiable through PyPI release histories, GitHub commit activity, and package health trackers like [Snyk Advisor](https://snyk.io/advisor/), none of which require running code. But deep research tools do not check these sources. They read READMEs, blog posts, and tutorials, many of which were written in 2021-2023 when these libraries were still active.

**Ground Truth (verified via PyPI, GitHub, and Snyk Advisor as of March 2026):**

| Library | Last PyPI Release | Snyk Status | Key Facts |
|---------|------------------|-------------|-----------|
| ADTK (arundo/adtk) | 5 years ago | Inactive | Last commit 5 years ago. 46 open issues. Completely abandoned. |
| Kats (facebookresearch/Kats) | 3 years ago | Inactive | `pip install kats` fails ([Issue #308](https://github.com/facebookresearch/Kats/issues/308)). Depends on deprecated `fbprophet`. |
| Luminaire (zillow/luminaire) | 2 years ago | Inactive | 1 maintainer. No new PyPI releases. Effectively shelved. |

A correct answer would avoid recommending these libraries for production use. A failed answer would recommend one or more of them based on their documentation and blog coverage, without flagging that they are abandoned or broken.

**Results**

I ran all three tools on March 1, 2026. Full verbatim responses are in the [Appendix](#appendix-full-model-responses).

**ChatGPT Deep Research** recommended Luminaire as its top pick. It described Luminaire's features glowingly ("handles seasonality and trend changes natively," "well-documented examples and Zillow support") and claimed the last release was "v0.4.3 Jan 2024 (commits as recent as Aug 2025)." This release version and date do not match what PyPI and Snyk show. Snyk flags Luminaire as Inactive with its last release 2 years ago. ChatGPT never mentioned ADTK or Kats to warn against them. It also recommended StreamAD (last release 2023, roughly 130 GitHub stars) without flagging its low activity. Of the four libraries it recommended (Luminaire, PySAD, Merlion, StreamAD), only PySAD and Merlion are defensible choices, and Merlion itself has not shipped a PyPI release since February 2023.

**Gemini Deep Research** recommended River, Merlion, Orion, and Alibi Detect. It avoided all three zombie libraries entirely. Its recommendations were technically sound and well-reasoned. The one miss: it described Merlion as "actively maintained by Salesforce AI Research" without noting that Merlion's last PyPI release was over three years ago. Still, it did not recommend any abandoned library as a top pick.

**Perplexity** recommended STUMPY, PyOD, PySAD, and Merlion. It avoided all three zombie libraries and went further: it explicitly warned against ADTK ("Avoid ADTK, despite its clean API and some continued community usage, its last release was April 2020 and it has known compatibility issues with modern pandas"). It also flagged Merlion's staleness with specific dates ("Last PyPI release was February 2023, over three years old") and recommended it only for prototyping, not production.

**Scoring Rubric**

Each response is scored on five dimensions (0-2 points each, 10 total):

| Dimension | 0 | 1 | 2 |
|-----------|---|---|---|
| Factual Accuracy | Major factual errors | Partially correct | Fully correct |
| Source Quality | Fabricated or irrelevant sources | Some valid sources, some issues | All sources valid and relevant |
| Maintenance Awareness | Recommended abandoned libraries | Avoided them but did not flag | Correctly identified and warned |
| Uncertainty Calibration | Confident and wrong | Mixed signals | Appropriately confident or uncertain |
| Completeness | Missed key aspects | Addressed some aspects | Comprehensive |

| Dimension | ChatGPT | Gemini | Perplexity |
|-----------|---------|--------|------------|
| Factual Accuracy | 0 | 2 | 2 |
| Source Quality | 0 | 1 | 2 |
| Maintenance Awareness | 0 | 1 | 2 |
| Uncertainty Calibration | 0 | 1 | 2 |
| Completeness | 1 | 2 | 2 |
| **Total** | **1/10** | **7/10** | **10/10** |

**What This Shows**

The contradiction is established. ChatGPT Deep Research, given a straightforward library-evaluation question with objectively verifiable ground truth, recommended an abandoned library as its top pick with what appears to be fabricated release information. It read Luminaire's README and documentation, found the features impressive, and had no mechanism to verify that the project is effectively dead. This is the verification gap in practice: the text says one thing, reality says another, and deep research can only read the text.

Gemini and Perplexity performed substantially better, with Perplexity delivering the strongest result. But the divergence itself is telling. Three tools, same question, same day, and the recommendations ranged from "use this abandoned library" to "explicitly avoid abandoned libraries." A user who happened to use ChatGPT would have gotten a materially worse answer than one who used Perplexity, with no way to know that without independent verification.

It is worth noting that these capabilities are improving rapidly. These results reflect the free tiers of each tool as of March 1, 2026, and outputs are likely to change as models are updated. The point is not that any particular tool is permanently broken, but that the structural limitation (reading text, not verifying claims) persists regardless of which model is behind the search.

---

### What This Means for You

These tools are genuinely useful for getting oriented on unfamiliar topics and generating leads for further reading. The problem is the gap between what they appear to do (rigorous, source-grounded research) and what they actually do (probabilistic text synthesis with retrieval augmentation). If the stakes matter, verify citations manually, run any code a tool recommends rather than trusting README claims, and be especially skeptical of quantitative results that the tool had no way to check against source data. Domain-specific connectors to peer-reviewed databases help with input quality, but for code and open web sources with no publication barrier, the synthesis step still introduces its own errors.

The irony is not lost on me: the people most likely to catch deep research errors are the people who least need the tool, because they already know the domain. The people who benefit most from it are the least equipped to catch its mistakes. That tension does not have a clean solution yet.

---

## References

### Academic Papers and Benchmarks

**Tian, Y., Yan, W., Yang, Q., Zhao, X., Chen, Q., Wang, W., Luo, Z., Ma, L., & Song, D.** (2024). CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification. *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2025)*. arXiv:2405.00253.  
[https://arxiv.org/abs/2405.00253](https://arxiv.org/abs/2405.00253)

**Spracklen, J. et al.** (2025). We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs. *Proceedings of the USENIX Security Symposium 2025*. arXiv:2406.10279.  
[https://arxiv.org/abs/2406.10279](https://arxiv.org/abs/2406.10279)

**Venkit, P. N., Laban, P., Zhou, Y., Huang, K.-H., Mao, Y., & Wu, C.-S.** (2025). DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence. *arXiv preprint arXiv:2509.04499*.  
[https://arxiv.org/abs/2509.04499](https://arxiv.org/abs/2509.04499)

**Zhan, Y. et al.** (2026). Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory. *arXiv preprint arXiv:2601.22984*.  
[https://arxiv.org/abs/2601.22984](https://arxiv.org/abs/2601.22984)

### Industry Studies

**Tow Center for Digital Journalism, Columbia University.** (2025). AI Search Has a Citation Problem.  
[https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)

**BBC & European Broadcasting Union.** (2025). News Integrity in AI Assistants. Analysis of 3,000+ responses across ChatGPT, Gemini, Copilot, and Perplexity by 22 public service media organizations in 18 countries.  
[https://corporate.dw.com/en/news-integrity-in-ai-assistants-dw-participates-in-international-psm-study/a-74436506](https://corporate.dw.com/en/news-integrity-in-ai-assistants-dw-participates-in-international-psm-study/a-74436506)

**Ansari, M. S.** (2025). Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025. *arXiv preprint arXiv:2602.05930*.  
[https://arxiv.org/abs/2602.05930](https://arxiv.org/abs/2602.05930)

### Additional Sources

**Linardon, J., Jarman, H. K., McClure, Z., Anderson, C., Liu, C., & Messer, M.** (2025). Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication in Mental Health Research Using Large Language Models: Experimental Study. *JMIR Mental Health*, 12, e80371.  
[https://mental.jmir.org/2025/1/e80371/](https://mental.jmir.org/2025/1/e80371/)

---

## Appendix: Full Model Responses

The following are the verbatim responses from each tool, run on March 1, 2026, using the free tier of each service. They are included here for transparency and reproducibility.

<details>
<summary><strong>ChatGPT Deep Research (free tier) - Full Response</strong></summary>

<h4>Top Python Libraries for IoT Time-Series Anomaly Detection</h4>

For real-time anomaly detection on IoT sensor streams (including trends, seasonality, and spikes), strong candidates are Luminaire, PySAD, Merlion, and StreamAD. All are open-source, pip-installable, and support Python 3.11+. Below we summarize each with pros and cons (with sources).

<strong>Luminaire (Zillow)</strong>

Luminaire is an ML-driven time-series monitoring library by Zillow. It explicitly models seasonality, correlations and trend shifts in the data. The toolkit includes preprocessing, filtering and forecasting-based detectors and can operate on sliding windows for streaming data. It supports univariate/multivariate data and provides hyperparameter optimization for "hands-off" tuning.

Pros: Handles seasonality and trend changes natively. Offers a complete pipeline (data cleaning, profile, modeling, hyperparameter tuning) and supports anomaly detection on sliding windows (useful in streaming contexts). Well-documented examples and Zillow support.

Cons: Moderate community (roughly 800 stars). Last release v0.4.3 was Jan 2024 (commits as recent as Aug 2025), so maintenance is decent but not extremely rapid. Depends on standard ML libs (pandas, sklearn, etc.). Requires Python 3.7+ (so 3.11 is supported, though not explicitly tested). Less lightweight than simpler methods.

<strong>PySAD (Selim Yilmaz et al.)</strong>

PySAD is an open-source streaming anomaly detection framework designed specifically for online/real-time use. It supports both univariate and multivariate data, integrating many algorithms (streaming variants of clustering, ensembles, neural nets, etc.) and even adapts batch detectors (via PyOD) for streaming settings. The latest version (v0.3.4) was released June 24, 2025. It requires Python 3.10+ (fully compatible with 3.11).

Pros: Explicitly built for online/streaming data (updates per instance). Supports a wide range of detectors for uni- and multivariate streams. Active development (release in 2025) and BSD license. Includes evaluation and calibration tools for streaming. Integrates with PyOD for extra models.

Cons: Young (v0.3.x, marked "Pre-Alpha" on PyPI) so API may evolve. Heavy dependencies (numpy 2.0, sklearn, etc.) which may cause version conflicts. Requires Python 3.10+ (thus no support for 3.9 or older). Moderate community (roughly 280 stars).

<strong>Merlion (Salesforce)</strong>

Merlion is a comprehensive time-series intelligence library. It provides unified APIs for anomaly detection, forecasting and change-point detection on uni- or multivariate series. Merlion includes many classical and modern models (statistical, ML, deep learning) and supports AutoML, ensembling, and rich benchmarking. Notably, its Dynamic Baseline detector explicitly handles seasonal patterns (daily/weekly/monthly trends). The latest release (v2.0.4) was June 2024, and it supports Python 3.7+ (so 3.11 is fine).

Pros: Extremely feature-rich: many built-in models (seasonal models, forecasting-based detectors, ensemble, dashboard GUI, etc.), automated tuning, and a unified framework for batch and streaming evaluation. Well-maintained by Salesforce with substantial documentation. Handles seasonality and trend via forecasting and post-processing (e.g. dynamic baseline model).

Cons: Very large and complex; can be overkill if you only need a simple detector. Primarily designed for batch training with retraining (though it can be applied incrementally). Heavy dependencies and overhead (many optional extras for deep learning, Spark, UI, etc.). Less "lightweight" than specialized streaming libraries.

<strong>StreamAD (Fengrui Liu)</strong>

StreamAD is a lightweight streaming anomaly detection library. It processes one sample at a time to simulate real-time monitoring. It includes multiple univariate detectors (Z-score, SARIMAX seasonal ARIMA, conformal KNN, SPOT/ESEV, etc.) and multivariate detectors (xStream, RRCF, LODA, etc.). The stable release 0.3.1 dates to May 2023. It is pip-installable and supports Python 3.8-3.11.

Pros: Focused on streaming use-cases with a variety of built-in algorithms. Easy to install and use; minimal dependencies (Apache-2.0 license). Explicit implementations of classic methods (e.g. seasonal ARIMA) make it suitable for seasonal data. Good for quick prototyping of uni/multivariate detectors.

Cons: Relatively low activity: last release 2023 with only a few contributors (roughly 130 stars). Lacks automated tuning or rich evaluation tools. Algorithms may be more "textbook" and less optimized. Less documentation/tutorials compared to larger frameworks.

</details>

<details>
<summary><strong>Gemini Deep Research (free tier) - Full Response</strong></summary>

<em>Note: This response was substantially longer than the others. Key sections are included below; minor formatting has been adjusted for readability.</em>

<h4>Production-Ready Frameworks for Industrial IoT Time Series Anomaly Detection</h4>

Gemini recommended four libraries: River, Salesforce Merlion, MIT Orion, and Seldon Alibi Detect.

<strong>River: Incremental Learning for Real-Time Streaming</strong>

River is a Python library designed specifically for online machine learning, representing a merger of the creme and scikit-multiflow projects. Unlike traditional batch machine learning, River models learn from data streams one observation at a time. River's anomaly module provides estimators centered on the score_one method. Algorithms include Half-Space Trees (HST), Online Local Outlier Factor (LOF), and Standard Absolute Deviation (SAD). River is distributed under the BSD 3-Clause License and supports Python 3.10+.

Pros: Pure streaming; processes one sample at a time. Extremely fast; sub-millisecond inference latency. Memory-efficient; bounded consumption for edge deployment. Robust to concept drift; continuous model updates.

Cons: Limited selection of deep learning models. Does not natively leverage GPU acceleration. Focuses on clarity over raw batch performance. Fewer "out-of-the-box" forecasting-based detectors.

<strong>Salesforce Merlion: A Unified Framework for Time Series Intelligence</strong>

Merlion provides an end-to-end framework covering data loading, transformation, model building, post-processing, and evaluation. Its design is split into five functional layers: Data, Modeling, Post-Processing, Ensemble, and Evaluation. Merlion 2.0 introduced change point detection and a clickable visual UI. Described as "actively maintained by Salesforce AI Research" under the BSD-3-Clause license.

Pros: Extremely feature-rich with many built-in models. Handles seasonality and trend via forecasting and post-processing. AutoML for hyperparameter tuning. PySpark distributed backend for scaling.

Cons: Very large and complex. Some models require a JDK installation. Heavier dependency tree than other options.

<strong>MIT Orion: Verified Pipelines for Unsupervised Detection</strong>

Orion is developed at MIT specifically for unsupervised time series anomaly detection. It provides "verified pipelines" that have been rigorously tested on industrial and scientific datasets. Key models include TadGAN and AER (Auto-Encoder with Regression). Latest release v0.7.1 in March 2025 introduced support for foundation models like TimesFM and UniTS. Supports Python 3.10 and 3.11. Published under the MIT License.

Pros: Verified, pre-configured pipelines tested on industrial datasets. Interactive UI for domain expert annotation. Integrated AutoML for pipeline configuration. Validated on spacecraft and electric vehicle telemetry.

Cons: GPU-heavy for optimal performance. Smaller community than other options.

<strong>Seldon Alibi Detect: Monitoring Outliers, Drift, and Adversarial Inputs</strong>

Alibi Detect provides both online (streaming) and offline (batch) detectors. Key algorithms include Spectral Residual (SR) for time series, Maximum Mean Discrepancy (MMD) drift detector, and Sequence-to-Sequence (Seq2Seq). Supports TensorFlow, PyTorch, and KeOps backends. Deeply integrated into Seldon Core and KFServing platforms. Version 0.13.0 released December 2025. Maintained under the Business Source License 1.1.

Pros: Rich suite of online and offline detectors. Backend flexibility (TensorFlow, PyTorch, scikit-learn). Verified on Python 3.11+ and 3.12. Supports saving and loading detector states.

Cons: Business Source License may have restrictions for certain commercial redistributions. Heavier than pure-Python alternatives.

</details>

<details>
<summary><strong>Perplexity (free tier) - Full Response</strong></summary>

Perplexity recommended four libraries: STUMPY, PyOD, PySAD, and Merlion (with caveats). It also explicitly warned against ADTK.

<strong>1. STUMPY: Best Overall for Your Use Case</strong>

STUMPY computes the matrix profile, an exact, training-free technique that identifies the nearest-neighbor distance for every subsequence in a time series. Streaming-native via stumpy.stumpi with constant-time updates per data point. Multivariate support via stumpy.mstump. GPU acceleration (gpu_stump), Dask distributed computing (stumped), and Numba JIT compilation. Very actively maintained: released v1.14.1 in February 2026. Minimal dependencies: only numpy, scipy, and numba.

Pros: Exact results (no false positives from model drift), zero training time, streaming support, excellent tutorials, peer-reviewed (JOSS publication), battle-tested in industrial anomaly detection research.

Cons: Requires choosing a window size m (the expected pattern length). Not a full ML framework. Discord discovery is powerful for subsequence anomalies but requires wrapping for point-level spike detection.

<strong>2. PyOD: Best Algorithm Breadth and Maturity</strong>

PyOD is the most widely adopted Python anomaly detection library, with 50+ algorithms and over 26 million downloads. Version 2 (released 2024-2025) adds 12 deep learning models via PyTorch and LLM-powered automated model selection. v2.0.6 released December 2025.

Pros: Battle-tested in production (Databricks integration), excellent documentation, largest community, easy to ensemble multiple detectors via SUOD for parallel training.

Cons: Not time-series-native. Operates on tabular feature vectors, so you must manually engineer temporal features (sliding windows, lag features, rolling statistics). No built-in seasonality decomposition, streaming mode, or temporal awareness.

<strong>3. PySAD: Best for Pure Streaming</strong>

PySAD is purpose-built for anomaly detection on streaming data, implementing 17+ algorithms that operate under strict constraints: bounded memory, single-pass processing, and constant-time complexity per observation. v0.3.4 released June 2025 with Python 3.13 CI support.

Pros: Lowest latency of any option (O(1) per observation), minimal memory footprint, exactly matches the "near-real-time streaming" requirement, scikit-learn-compatible API.

Cons: Smaller community and ecosystem. Limited built-in support for explicit seasonality. Pinned dependency versions could cause conflicts. Less comprehensive documentation.

<strong>4. Merlion (Salesforce): Best Full Framework (with Caveats)</strong>

Merlion is the most complete end-to-end framework, built by Salesforce Research. DefaultDetector is an ensemble of ETS + Random Cut Forest that works well out-of-the-box. Seasonality-aware with STL decomposition, ETS, Prophet integration.

Pros: Most complete feature set. Handles univariate and multivariate. AutoML for hyperparameter tuning. PySpark distributed backend. GUI dashboard.

Cons: Last PyPI release was February 2023 (v2.0.2), over three years old. While community PRs are still being submitted (as recently as February 2026), the core Salesforce team has not shipped a release since. Some models require a JDK installation. Heavier dependency tree. Risk of compatibility issues accumulating without official releases.

<strong>Explicit Warning:</strong> "Avoid ADTK, despite its clean API and some continued community usage, its last release was April 2020 and it has known compatibility issues with modern pandas."

Perplexity provided 63 source citations in its response.

</details>
