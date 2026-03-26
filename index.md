---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

<!-- [Jump to the current week](#week-9-code-sklearn-code-pipelines-generalization-and-cross-validation){: .btn } -->

<!-- [Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
