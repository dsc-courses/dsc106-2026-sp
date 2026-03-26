---
layout: page
title: 📺 Final Project Showcase
description: Showcase of student final projects from Spring 2026.
nav_order: 1
nav_exclude: true
---

# Final Project Showcase

Coming at the end of the quarter!

{% for project in site.data.projects %}
{% include project-showcase-card.html project=project %}
{% endfor %}
