---
layout: page
title: 📺 Final Project Showcase
description: Showcase of student final projects from Spring 2026.
nav_order: 1
---

# Final Project Showcase

This page lists final projects from Spring 2026's offering of DSC 106.
Projects are listed with the permission of the student teams.

There were two kinds of awards given to student submissions:

1. The Best Project Award was given to the top 4 submissions out of 69 (top 6%) based on
   overall project quality, as determined by the instructor and course staff.
1. The Honorable Mention Award was given to the next 3 submissions, bringing
   the recognized group to the top 7 submissions (top 10%).

{% for project in site.data.projects %}
{% include project-showcase-card.html project=project %}
{% endfor %}
