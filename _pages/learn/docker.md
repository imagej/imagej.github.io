---
title: Docker
---

{% include img src='logos/docker' align='right' width=150 caption='**Docker:** enabling containerized applications for reproducibility.' %}

[Docker](https://www.docker.com/whatisdocker/) provides a platform for
distribution of application state. This facilitates the highest level of
scientific [reproducibility](/develop/architecture#reproducible-builds):
a Docker image can bundle operating system, Java version, update site and
plugin state, and even sample data. These Docker images can then be reused
by remote users and scientists worldwide, with no dependency concerns
beyond Docker itself.

The [Fiji](/software/fiji) distribution of ImageJ is available via Docker;
for details, please see:

{% include link-banner url="https://github.com/fiji/dockerfiles#readme" %}
