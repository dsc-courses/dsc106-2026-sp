---
layout: assignment
title: 'Project 3: Interactive Visualization'
parent: '📝 Projects'
released: true
nav_order: 4
---

# Project 3: Interactive Visualization

For this assignment, you will explore the issues involved in implementing interactive visualizations. You will build a visualization that enables interactive exploration of a scientific or environmental dataset and deploy it on the web.

One goal of this assignment is to gain familiarity with implementing interaction
techniques for visualizations. For example, the [zipdecode][link] and
[NameGrapher][link1] applications apply the interactive technique of dynamic
queries – as explored in the earlier [HomeFinder][link2] application – to the
problem of uncovering patterns in zip codes and baby names.

Similarly, [treemaps][link3] were originally developed to display hierarchical
file structures and were later adapted to the problem of interactively depicting
a [map of the stock market][link4]. We have seen many other examples of
interactive visualization techniques in class. In the same spirit, your goal is to extend these ideas to modern Earth and climate data, such as global temperature projections, atmospheric patterns, or satellite imagery. Interactivity will be essential to help viewers explore spatial and temporal variation in these complex datasets.

We have seen many examples of interactive visualization techniques in class. The goal of this assignment is not only for you to gain hands-on implementation experience, but also for you to think critically about how effective specific techniques are for your chosen data domain—for instance, how zooming, filtering, or time sliders support insight into environmental change.

One challenge is to **scope the assignment so that you can finish it within two
weeks**. Focus on designing a limited yet compelling visualization that enables
interactive exploration along a few critical dimensions. The
[NameGrapher][link1] application is a nice example that uses a simple but
elegant interaction design to enable engaging explorations. **A tightly focused,
well-implemented interactive graphic is much preferred to a sprawling design
that attempts too much!**

[link]: http://benfry.com/zipdecode/
[link1]: https://namerology.com/baby-name-grapher/
[link2]: http://www.cs.umd.edu/hcil/spotfire/
[link3]: http://www.cs.umd.edu/hcil/treemap/
[link4]: http://www.bewitched.com/marketmap.html

## Team Registration

For this assignment, you should work in teams of **3-4 students**. You might
want to find project partners that you will continue to work with for the final
project.

As soon as you have formed a team and chosen a dataset, complete the team formation submission on GradeScope.
Your submission must include a **concise title for your interactive visualization** (we will get the UCSD email and names of your groupmates from the group submission!). 
The visualization title need not be exact, **just a rough title should be a good start**. If you are looking for project partners,
please post to Piazza to find classmates with similar interests! **You should
submit your team registration by Friday 5/01, 11:59 pm.** Please ensure that the
team has been finalized before filling the form, and that the details are
correct.

You will submit your interactive prototype as a webpage hosted on GitHub Pages,
just like you did for your Project 2 and the labs.

{: .important}
If you don't fill out the team registration form before the deadline, we will randomly assign you to a group.

[link5]: https://docs.google.com/forms/d/e/1FAIpQLSf8RiGZy_xFD8gZVP7yiPPZi1t3ceEtwXE0j9vlxHxco0lytg/viewform?usp=dialog

## Deliverables

Design an interactive graphic aimed at enabling understanding of a compelling
question. You must use one of the datasets listed below. To determine what
subset of the data and which interactive options are most promising, you may
want to perform additional exploratory analysis. What aspects of the data reveal
the most interesting discoveries or stories? **Do not feel obligated to try to
convey everything about the data: focus on a compelling subset.**

Your graphic must include interactions that enable exploration. Possible
techniques include panning, zooming, brushing, details-on-demand (e.g.,
tooltips), dynamic query filters, and selecting different measures to display.
You are free to also consider highlights, annotations, or other narrative
features intended to draw attention to particular items of interest and provide
additional context.

Implement your interactive graphic and deploy it to the web. You may **use only
D3.js** for this project. **Vega-lite/Plotly/Altair/any other high-level
plotting library or tool** are **strictly not allowed** for this project. You
can use other non-plotting related JavaScript libraries, e.g. Lodash, Svelte,
Moment, etc. Your graphic should not require customized server-side support; you
should simply load data from a static data file or public web API.

You will use [GitHub pages to host your visualization][link7] from your project
repository. **Make sure that you make your repository "Public"**. We recommend
keeping everything (development files and website) in your master branch: either
serve your website from the root folder or the "/docs" folder. Your repo must
also contain the (unobfuscated) source code for your visualization.

Your deployed web page should also include a write-up with the following
components:

- A rationale for your design decisions. How did you choose your particular
  visual encodings and interaction techniques? What alternatives did you
  consider and how did you arrive at your ultimate choices?

- An overview of your development process. Describe how the work was split among
  the team members. Include a commentary on the development process, including
  answers to the following questions: Roughly how much time did you spend
  developing your application (in people-hours)? What aspects took the most
  time?

You can either include your write-up on the same page as your visualization or
link to a separate file.

[link7]: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Rubric

The assignment is out of 14 points possible. Submissions that squarely meet the project requirements (Satisfactory column) will get 11/14 points.

| Component                    | Excellent                                                                                                                                                            | Satisfactory                                                                                                                                                                                                                                                      | Not Satisfactory                                                                                                                                                                                                                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Visual Encodings             | The visualization does not violate the expressiveness criteria and the design choices (marks and encoding channels) are clear, evocative, and effective. (+3 points) | The visualization does not violate the expressiveness criteria, but another set of design choices (marks and encoding channels) could have been more effective (e.g. using the area visual channel instead of position when possible). (+2 points)                | The visualization violates the expressiveness criteria (e.g. heavy overplotting, encodings that imply incorrect readings, etc.), and these violations are not addressed using the available interactions (e.g. overplotting that cannot be filtered or zoomed into). (+1 points) |
| Data Transformations         |                                                                                                                                                                      | The visualization uses appropriate data transformations (e.g. filtering, aggregating) and clearly describes the transformations to the reader (e.g. in the subtitle of the plot). (+2 points)                                                                     | The visualization used an inappropriate set of data transformations (e.g. filtering out important outliers), or did not clearly describe these transformations to the reader. (+1 point)                                                                                         |
| Interaction (Implementation) | The interactive elements of the plot are polished and are almost completely bug-free. (+3 points)                                                                    | The interactive elements of the plot are functional, but some bugs impede the viewing experience (+2 points)                                                                                                                                                      | The interactive elements have major bugs that preclude use. (+1 point)                                                                                                                                                                                                           |
| Interaction (Design)         | The interactive elements guide the reader to quickly and easily discover interesting patterns in the data that would not be apparent in a static plot. (+3 points)   | The interactive elements enable the reader to discover interesting patterns in the data, but a static plot (perhaps with a different encoding) could have conveyed the same information just as effectively. (+2 points)                                          | The plot would have been substantially more effective as a static plot without the interaction. (+1 point)                                                                                                                                                                       |
| Writeup                      |                                                                                                                                                                      | The writeup clearly describes the motivation for the visualization and the rationale for its design decisions (e.g. the visual encodings, data transformations, color palette, etc.). It also contains an overview of the team’s development process. (+3 points) | One or more required elements of the writeup has major issues (e.g. rationale misses important parts of the visualization design), is missing, or is clearly generated by an AI tool. (+2 points)                                                                                |
| Creativity and Originality   | The submission exceeds the assignment requirements, with original insights or particularly engaging visualizations. (+1 bonus point)                                 | The submission meets the assignment requirements. (+0 points)                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |

## Submission Details

### Team Registration

Submit your team submission form on GradeScope by **Friday 5/01, 11:59 PM**.

### Checkpoint Submission

The submission must be made on gradescope by **Tue 05/05, 11:59 PM**. For this submission, submit an **mp4** video no longer than 2 minutes with the following details:

1. Name of your team and team members
2. Dataset chosen. Explain the aspects of the datasets you plan to use.
3. 5-6 exploratory graphs you have come up with (static/dynamic) that lead you to choose the (below) question.
4. Title of your graph / the question you are aiming to answer.
5. Current progress on the final dynamic graph.

Please ensure that the video has an associated audio/voiceover rather than just text. The video recording does not need to include all members of the team.

{: .note }

**Only submit one video per team**. It is important to add all members of your team to the submission.

### Final Submission

You must have a working prototype online by **Tue 05/12, 11:59 pm**. Your prototype should be accessible on GitHub pages using a publicly viewable URL.

In addition, **you must submit the URL on Gradescope**. **One submission per team is sufficient**.

Submissions will be reviewed as part of a subsequent peer review assignment, so try to avoid a late submission; assignments submitted late may not be included as part of the peer review and thus not receive peer feedback.

## Data Sources

We’ve provided three datasets for you to use. You must only pick a dataset from the list below.

All datasets contain spatiotemporal environmental data from satellite and climate observation systems, each differing in resolution, time scale, and modality. Time-based analyses are not mandatory, but they allow for exploring temporal patterns and relationships across regions and variables.

### Coupled Model Intercomparison Project (CMIP6)

The CMIP6 dataset contains global climate model simulations produced by research centers around the world under the World Climate Research Programme. These simulations include temperature, precipitation, and greenhouse gas projections across multiple climate scenarios.

Address: [NOAA Public CMIP6 Dataset on Google Cloud Marketplace][link8]

[link8]: https://console.cloud.google.com/marketplace/product/noaa-public/cmip6?project=fluid-script-453604-u5

Data can be accessed through Google Cloud’s public repository. You can subset by region, time, or variable using preprocessed .nc (NetCDF) or .csv files. An example Colab notebook demonstrating data access and processing is linked below.

Example notebook: [CMIP6 Example (updated Nov 8, 2025)][link9]

[link9]: https://github.com/dsc-courses/dsc106-2025-fa/blob/main/lectures/climate-lecture/CMIP%20basic_search_and_load-colab.ipynb

### NOAA Geostationary Operational Environmental Satellite (GOES) Data

The GOES dataset provides real-time satellite imagery from NOAA’s GOES-R series (GOES-16 and GOES-17). These geostationary satellites continuously observe the Western Hemisphere, collecting visible, infrared, and water vapor imagery used for weather, ocean, and climate monitoring.

Address: [NOAA GOES Dataset on AWS Open Data Registry][link10]

[link10]: https://registry.opendata.aws/noaa-goes/

Data is available as cloud-optimized NetCDF and Zarr files that can be accessed via AWS or loaded using Python libraries such as xarray. An example Jupyter notebook demonstrating access and visualization is linked below.

Example notebook 1: [GOES Data Access via Zarr/NetCDF (nbviewer)][link11]

Example notebook 2: [Simple GOES Demo][goes_simple]

[link11]: https://nbviewer.jupyter.org/github/oceanhackweek/ohw-tutorials/blob/OHW20/10-satellite-data-access/goes-cmp-netcdf-zarr.ipynb
[goes_simple]: https://github.com/dsc-courses/dsc106-2025-fa/blob/main/lectures/climate-lecture/Simple%20GOES%20demo.ipynb

### NASA MODIS (MODerate Resolution Imaging Spectroradiometer) Satellite Imagery

The MODIS dataset provides global daily satellite imagery of Earth’s surface and atmosphere collected by NASA’s Terra and Aqua satellites. It includes measurements of vegetation, ocean color, land temperature, and aerosols spanning more than two decades.

Address: [NASA Worldview Application][link12]

[link12]: https://worldview.earthdata.nasa.gov/

The data can be explored through NASA’s Worldview web interface or accessed directly using the GIBS REST API. The API allows downloading imagery or data tiles for specific coordinates, layers, and time ranges.

API documentation: [GIBS REST API Basics][link13]

[link13]: https://nasa-gibs.github.io/gibs-api-docs/access-basics/

Advanced usage: [GIBS Python Access Guide][link14]

[link14]: https://nasa-gibs.github.io/gibs-api-docs/python-usage/

## Acknowledgements

The design of this assignment is largely based on similar assignment from Arvind
Satyanarayan from the Massachusetts Institute of Technology and Jeffrey Heer at
the University of Washington.
