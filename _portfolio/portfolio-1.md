---
title: "Enhancing DataTrail Data Science Education: The BaltimoreTrails R Package and Dashboard"
excerpt: "An R package and Shiny dashboard that bring Baltimore datasets into [DataTrail](https://www.datatrail.org/), the Johns Hopkins Bloomberg School of Public Health's data science training program, so students can practice on local data. This was my ScM thesis project."
collection: portfolio
---
<br />
[<i class="fa fa-fw fa-link" aria-hidden="true"></i>](https://fuchsfranklin25.shinyapps.io/shiny-examples/) Deployed Web-Application

[<i class="fa fa-fw fa-code" aria-hidden="true"></i>](https://github.com/datatrail-jhu/BaltimoreTrails) GitHub Code Repository

## Project Overview

###### _(R Package and Shiny-based Dashboard)_

[DataTrail](https://www.datatrail.org/) is a data science training program run out of the Johns Hopkins Bloomberg School of Public Health. The idea behind BaltimoreTrails, my ScM thesis project, was that students would get more out of the material if they practiced on local Baltimore data instead of generic examples.

There are two parts. The R package bundles a set of Baltimore datasets with helper functions for loading, wrangling, and plotting them. It's built on dplyr, tidyr, and ggplot2, so it should feel familiar to anyone who has worked through the DataTrail R lessons. The Shiny dashboard puts the same data behind an interactive front end, so students can poke around before writing any code. Both are open source, and the next step we had in mind was a few learnr tutorial chapters that use the package directly.



