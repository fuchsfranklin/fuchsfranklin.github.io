---
title: 'Breaking Deep Research: Where Retail User LLM Search Agents Fail and Why Verification Still Falls on You'
date: 2025-02-12
permalink: /posts/2025/02/breaking-deep-research-where-llm-search-agents-fail/
excerpt: "Deep research tools from OpenAI, Google, and Perplexity promise source-grounded synthesis, but their reliability depends heavily on what they are searching. Professional tools connected to peer-reviewed databases like PubMed have a built-in quality gate: the barrier to publication is literally peer review. But for code repositories, blog posts, and other sources with no editorial barrier, deep research inherits every error, exaggeration, and fabrication in the source material. Digging into some of the recent literature myself, it looks like studies often find citation accuracy as low as 40% and fabricated references. I tested all three tools on the same code-type deep research question as a small experiment to show how they can fail (a la proof by contradiction). The issue of AI-generated content infiltrating peer review itself is a separate and important problem, but not within the scope of this post."
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

I use deep research tools regularly (ChatGPT's Deep Research, Gemini, Perplexity Pro), and they are genuinely useful for getting up to speed on unfamiliar topics. But the more I use them for anything technical, especially code or quantitative claims, the more I notice a pattern: these tools are confidently wrong in ways that are hard to catch unless you already know the answer. Deep research cannot execute code in a GitHub repo or verify that the claims a README makes are true.

Their reliability depends fundamentally on what they are searching. Connect an LLM to PubMed or a curated legal database, and the source material has already passed through peer review. The barrier to publication is itself a quality gate. The tool can still misinterpret, but at least the underlying sources have been vetted by domain experts. Professional connectors restricted to these databases are, for this reason, substantially more reliable than open web search.

But most of what retail-facing deep research tools search is not peer-reviewed. Code repositories, blog posts, Stack Overflow answers, documentation pages: none of these have a publication barrier. Anyone can push a README claiming state-of-the-art performance. And deep research cannot tell the difference, because it reads text, not code, and cannot execute anything to verify claims independently.

This post explores *why* deep research fails in these unvetted domains, grounded in recent literature, with a small experiment to illustrate the problem firsthand. This is not a takedown of these tools, but understanding where the quality gate exists (and where it does not) matters if you use them for anything important. The separate issue of AI-generated content infiltrating peer review itself (fabricated citations in accepted papers, LLM-written reviews, etc.) is a growing concern but not within scope here.

---

## Overview

1. [**What Deep Research Actually Does (and Does Not Do)**](#what-deep-research-actually-does-and-does-not-do) - The retrieval-synthesis pipeline and its blind spots
2. [**The Citation Problem**](#the-citation-problem) - Fabricated references, broken URLs, and misattributed claims
3. [**The Code Verification Gap**](#the-code-verification-gap) - Why deep research cannot verify what code actually does
4. [**Why Connectors and RAG Do Not Fully Solve This**](#why-connectors-and-rag-do-not-fully-solve-this) - Hallucinations accumulate across the research trajectory
5. [**Experiment: One Question, Three Tools, Ground Truth**](#experiment-one-question-three-tools-ground-truth) - Testing ChatGPT, Gemini, and Perplexity against a real GitHub repo
6. [**What This Means for You**](#what-this-means-for-you) - Practical implications
7. [**References**](#references) - Sources

---

### What Deep Research Actually Does (and Does Not Do)

Deep research tools work roughly as follows: you give the model a question, it formulates a search plan, retrieves documents from the web (or from specified sources), reads through them, and synthesizes a long-form report with citations. OpenAI's version browses autonomously for 5 to 30 minutes. Gemini and Perplexity follow similar patterns with their own retrieval backends.

What these tools do well: they aggregate information across many sources faster than any human could. They produce structured, readable reports. They cite their sources (sometimes).

What they do not do: they do not execute code. They do not verify that a dataset contains what its documentation claims. They do not check whether a function's output matches its docstring. They do not run statistical analyses to confirm reported numbers. They do not cross-reference a paper's abstract against its actual results tables. They read text and generate text. That is the entire operation.

This distinction matters more than most users realize. When you ask deep research a question about a GitHub repository, it reads the README, maybe some issues, maybe a blog post about the repo. It does not clone the repo, install dependencies, and run the test suite. It cannot tell you if the code is broken, if the results are reproducible, or if the README is lying. It takes documentation at face value, which is exactly what a careful researcher would not do.

---

### The Citation Problem

The most well-documented failure mode of deep research tools is citation fabrication and misattribution. This is not a fringe issue. It has been measured repeatedly, at scale, and the numbers are not good.

A 2025 study by the Tow Center for Digital Journalism at Columbia University evaluated eight AI search tools by feeding them real excerpts from published news articles and asking them to identify the source. Over 60% of responses contained incorrect or misleading information. ChatGPT provided false citations 134 times out of 200 responses and signaled a lack of confidence only 15 times. It never declined to answer (Tow Center, 2025). The tools did not say "I don't know." They said the wrong thing with full confidence.

A landmark BBC and European Broadcasting Union study analyzed over 3,000 responses from ChatGPT, Gemini, Copilot, and Perplexity on current news topics. 45% of responses contained at least one significant issue. 31% had serious sourcing problems. 20% had major accuracy issues including hallucinated details and outdated information. When accounting for minor errors, 81% of responses had some form of problem. Gemini was the worst performer, with significant issues in 76% of its responses (BBC/EBU, 2025).

Perhaps most striking: a study analyzing papers accepted at NeurIPS 2025, one of the most prestigious AI conferences in the world, found 100 fabricated citations across 51 accepted submissions (GPTZero, 2025). These were not student projects. These were peer-reviewed papers at a top venue, and the fabricated references slipped through. This is an example of AI-generated content infiltrating the peer review process itself, which as noted in the rationale is a separate and important problem. For our purposes here, it illustrates that even the peer-review quality gate is not immune to AI-era challenges, though it remains a far stronger filter than no gate at all.

The DeepTRACE audit framework (Venkit et al., 2025) from Salesforce and Microsoft Research evaluated deep research agents specifically. Their findings: citation accuracy ranged from 40% to 80% across systems. Deep research configurations reduced overconfidence compared to standard search, but still produced large fractions of statements unsupported by their own listed sources. Even when the tools cited a source, the source often did not actually support the claim being made.

A separate study published in JMIR Mental Health found that across 176 AI-generated citations, 35 were completely fabricated, 64 of the real ones contained errors, and only 77 (44%) were both real and accurate. Hallucination rates increased on specialized or less-covered topics (Gravel et al., 2025).

The pattern is consistent across studies: these tools fabricate sources, misattribute claims, link to broken URLs, and do all of this without expressing uncertainty. The user has no way to distinguish a real citation from a hallucinated one without manually checking every single reference.

---

### The Code Verification Gap

This is where things get particularly interesting for anyone using deep research for coding or technical questions. The fundamental issue: deep research tools read *about* code but never *run* code. This creates a verification gap that is structurally impossible to close within the current architecture.

The CodeHalu benchmark (Tian et al., 2024) systematically studied code hallucinations in LLMs and identified four distinct types: mapping hallucinations (misunderstanding the task), naming hallucinations (referencing nonexistent APIs or variables), resource hallucinations (using unavailable external resources), and logic hallucinations (producing code that is syntactically valid but logically wrong). The key finding: LLMs generate code that *looks* correct and often compiles without errors, but fails to produce expected outputs when actually executed.

This problem extends beyond generating code to a more insidious issue: recommending code that does not exist. A large-scale study analyzing 576,000 code samples generated by 16 widely used LLMs found that approximately 440,000 of the package dependencies referenced were "hallucinated," meaning the packages did not exist in any public repository (Spracklen et al., 2025). This phenomenon, now called "slopsquatting," has become a real supply chain security threat. Malicious actors can register these hallucinated package names and fill them with malware, knowing that developers using LLM-generated code will install them. In roughly 20% of examined cases, the recommended packages were entirely fictional.

Now consider what happens when you ask a deep research tool about a specific GitHub repository. The tool reads the README, which might say "this library implements a transformer-based model for time series forecasting with state-of-the-art accuracy on the ETTh1 benchmark." Deep research will report this claim as fact. But it cannot:

- Clone the repo and check if the code actually runs
- Verify that the reported benchmark numbers are reproducible
- Determine if the implementation matches the paper it claims to implement
- Check whether the "state-of-the-art" claim was true at the time of writing, let alone now
- Identify if the code has known bugs in its core logic that invalidate the results

The README is treated as ground truth. For well-maintained, widely-used repositories, this is often fine. For the long tail of research code, personal projects, and less-scrutinized libraries, it is a significant source of error. And deep research has no mechanism to distinguish between the two.

---

### Why Connectors and RAG Do Not Fully Solve This

A common response to these concerns is: "Just use domain-specific connectors." If you are researching medical literature, connect the LLM to PubMed. If you need legal information, connect it to a legal database. This is the premise behind Retrieval-Augmented Generation (RAG), and it is worth distinguishing where this works and where it does not.

For peer-reviewed literature, connectors genuinely help. When a tool is restricted to searching PubMed, Scopus, or a curated legal database, the source material has already cleared a quality gate: peer review, editorial oversight, or institutional vetting. The LLM can still misinterpret or misattribute what it reads, but the underlying claims have at least been scrutinized by domain experts. This is a meaningful advantage. A PubMed-connected tool hallucinating a citation is bad, but the *real* citations it retrieves are far more likely to be accurate than a random blog post or GitHub README. The barrier to publication does real work here.

The problem is that most deep research queries do not stay within peer-reviewed territory. Code repositories have no publication barrier. Anyone can create a package, write a README claiming anything, and push it to GitHub or PyPI. Blog posts, Stack Overflow answers, documentation pages, and forum threads are similarly unvetted. When deep research tools search the open web, they are pulling from a mix of high-quality and low-quality sources with no reliable way to distinguish between them. The tool treats a well-maintained library's documentation and a student's abandoned side project with equal authority.

Even within the RAG framework, connectors do not solve the deeper issue. The "Why Your Deep Research Agent Fails?" paper (Zhan et al., 2025), presented at ICML, introduced a critical insight: hallucinations in deep research agents do not just occur at the retrieval step. They accumulate across the entire research trajectory. The authors proposed the PIES taxonomy, categorizing hallucinations along two dimensions: functional component (Planning vs. Summarization) and error property (Explicit vs. Implicit). Their experiments on six state-of-the-art deep research agents revealed that no system achieved robust reliability, and critically, flawed *planning* (deciding what to search for and how to structure the research) was a major source of errors that existing benchmarks completely missed.

In other words, even if you give the model perfect sources, it can still:

- Formulate a flawed research plan that misses key aspects of the question
- Selectively attend to information that confirms its initial framing
- Misinterpret or oversimplify technical content during synthesis
- Propagate an early error through the entire report

The DeepTRACE study confirmed this: deep research agents frequently produced one-sided, highly confident responses on debatable topics, even when their own cited sources contained nuance or counterarguments. The problem is not just "bad retrieval." It is that the synthesis step introduces its own distortions.

So the picture is: connectors to peer-reviewed databases improve *input* quality substantially, and for literature-based research questions they are the right approach. But they do nothing about *processing* quality. And for code-related questions, where the source material has no publication barrier and verification requires execution rather than reading, even perfect retrieval of documentation does not substitute for running the code.

---

### Experiment: One Question, Three Tools, Ground Truth

To move beyond citing other people's findings, I wanted to test this myself. The setup is simple: ask ChatGPT Deep Research, Gemini, and Perplexity the same technical question about a real GitHub repository, then score their responses against the actual code.

**The Question:**

I chose a question that requires understanding actual code behavior, not just reading documentation. The specific question, repository, and methodology will be documented in the companion GitHub repo once the experiment is complete. The key criteria for the question:

1. It must be about a real, public repository with verifiable ground truth
2. The answer must require understanding code logic, not just reading the README
3. The correct answer must be unambiguous and confirmable by running the code
4. The README or documentation should not directly state the answer (forcing the tools to reason about code)

**Scoring Rubric:**

Each response is scored on five dimensions (0-2 points each, 10 total):

| Dimension | 0 | 1 | 2 |
|-----------|---|---|---|
| **Factual Accuracy** | Major factual errors | Partially correct | Fully correct |
| **Code Understanding** | Did not understand the code logic | Surface-level understanding | Demonstrated actual comprehension |
| **Source Quality** | Fabricated or irrelevant sources | Some valid sources, some issues | All sources valid and relevant |
| **Uncertainty Calibration** | Confident and wrong | Mixed signals | Appropriately confident or appropriately uncertain |
| **Completeness** | Missed key aspects | Addressed some aspects | Comprehensive |

**Results:**

*[This section will be populated once I run the experiment across all three tools. I will include the exact question asked, verbatim excerpts from each tool's response, the ground truth answer verified by running the code, and the scores. The companion repo will contain the full responses and verification code.]*

I will update this section and link to the full experiment data on [GitHub](https://github.com/fuchsfranklin) once complete. The goal is not to declare a "winner" among the three tools, but to illustrate the verification gap in practice: even the best-performing tool may get things wrong in ways that are invisible without independent verification.

---

### What This Means for You

None of this means deep research tools are useless. They are genuinely useful for getting oriented on a new topic, generating leads for further reading, and drafting initial summaries. The problem is the gap between what they *appear* to do (rigorous, source-grounded research) and what they *actually* do (probabilistic text synthesis with retrieval augmentation).

A few practical takeaways:

**For coding questions:** If a deep research tool tells you about a library, a function, or a code pattern, verify it by actually running the code. The tool cannot do this for you. README claims are not ground truth.

**For citations:** Check every reference manually if the stakes matter. The fabrication rates documented in the literature (20-60% depending on the study and domain) are too high to trust blindly. If a citation looks plausible but you cannot find it, it may not exist.

**For technical claims:** Be especially skeptical of quantitative claims (benchmarks, performance numbers, statistical results). Deep research tools have no mechanism to verify numbers against source data. They report what text says, and text can be wrong.

**For connectors and RAG:** If your question is about peer-reviewed literature, domain-specific connectors (PubMed, legal databases, etc.) are meaningfully more reliable because the source material has cleared a quality gate. Use them when available. But for code, open web sources, and anything without a publication barrier, the synthesis step still introduces its own errors. Treat outputs with appropriate skepticism regardless.

The irony is not lost on me: the people most likely to catch deep research errors are the people who least need the tool (because they already know the domain). The people who benefit most from the tool (newcomers to a topic) are the least equipped to catch its mistakes. This is the fundamental tension, and it does not have a clean solution yet.

---

## References

### Academic Papers and Benchmarks

**Tian, H., Lu, W., Li, T. O., Tang, X., Cheung, S., Klein, J., & Bissyandé, T. F.** (2024). CodeHalu: Investigating Code Hallucinations in LLMs via Execution-based Verification. *arXiv preprint arXiv:2405.00253*.  
[https://arxiv.org/abs/2405.00253](https://arxiv.org/abs/2405.00253)

**Spracklen, J., Neupane, A., & Challagundla, S.** (2025). We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs. *arXiv preprint arXiv:2406.10279*.  
[https://arxiv.org/abs/2406.10279](https://arxiv.org/abs/2406.10279)

**Venkit, P. N., Laban, P., Zhou, Y., Huang, K.-H., Mao, Y., & Wu, C.-S.** (2025). DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence. *arXiv preprint arXiv:2509.04499*.  
[https://arxiv.org/abs/2509.04499](https://arxiv.org/abs/2509.04499)

**Zhan, Y. et al.** (2025). Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory. *Proceedings of the International Conference on Machine Learning (ICML)*. arXiv:2601.22984.  
[https://arxiv.org/abs/2601.22984](https://arxiv.org/abs/2601.22984)

### Industry Studies

**Tow Center for Digital Journalism, Columbia University.** (2025). AI Search and News Citation Accuracy Study.  
[https://www.cjr.org/tow_center](https://www.cjr.org/tow_center)

**BBC & European Broadcasting Union.** (2025). AI Assistants and News Accuracy: An International Study. Analysis of 3,000+ responses across ChatGPT, Gemini, Copilot, and Perplexity.  
[https://www.bbc.co.uk/rd/publications](https://www.bbc.co.uk/rd/publications)

**GPTZero.** (2025). A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025. *arXiv preprint arXiv:2602.05930*.  
[https://arxiv.org/abs/2602.05930](https://arxiv.org/abs/2602.05930)

### Additional Sources

**Gravel, J. et al.** (2025). Citation Hallucination in Large Language Models: A Study of AI-Generated Bibliographic References. *JMIR Mental Health*.

**Frontiers in AI.** (2025). Survey and Analysis of Hallucinations in Large Language Models: Attribution to Prompting Strategies or Model Behavior.  
[https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full)
