---
title: ImageJ (Experimental)
layout: home
---

<!-- Header -->
{::nomarkdown}
    <section id="header">
        <div class="inner">
            <img src="images/logo/ij_logo_shadow_600dpi.png" alt="ImageJ Logo" class="image-header">
            <h1>Welcome to <strong>ImageJ</strong></h1>
            <p>ImageJ is an open source image processing program designed for scientific
                multidimensional images.
            </p>
            <ul class="actions special">
            <li><a href="/learn" class="button icon solid fa-cogs">Use</a></li>
            <li><a href="/develop" class="button icon solid fa-wrench">Extend</a></li>
            <li><a href="/search" class="button icon solid fa-search">Search</a></li>
        </ul>
        <ul class = "actions special">
            <li><a href="/downloads" class="button icon solid fa-download">Download</a></li>
            </ul>
        </div>
    </section>
{:/}

<!--ImageJ Introduction -->
{::nomarkdown}

<div class="text-center"><h1>Why ImageJ?</h1>
<header class="container-whyij">
  <div class="row-whyij">
    <div class="col-4">
    <div class=" fa-5x text-success"><span class="fas fa-check-circle"></span></div>
    <h2>Easy to Use</h2>
    <p>
    Install ImageJ in one-click, Fiji installs all of its plugins, features an automatic updater, and offers comprehensive documentation.
    </p>
    </div>
    <div class="col-4">
    <div class=" fa-5x text-primary"><span class="fas fa-cogs"></span></div>
    <h2>Powerful</h2>
    <p>
    ImageJ offers robust extensibility, harnessing the power of hundreds of plugins to assist with any of your imaging needs.
    </p>
    </div>
    <div class="col-4">
    <div class=" fa-5x text-danger"><span class="fas fa-heart"></span></div>
    <h2>Free &amp; Open Source</h2>
    <p>
    ImageJ is an <a href="/Open_Source">open source</a> project hosted on <a href="https://github.com/imagej">GitHub</a>, developed and written by the community.
    </p>
    </div>
  </div>
</header>

{:/}

<div class="resources">
  <!-- Developer resources -->

  {% include user-resources %}

  <!-- Developer resources -->

  {% include developer-resources %}
</div>


<div class="col-md-8">
        <div class="card text-center">
          <div class="card-header">
            <ul class="nav nav-tabs card-header-tabs" id="plugin-tabs" role="tablist">
              <!-- dynamically generated from plugins.json -->
            </ul>
          </div>
          <div class="card-body">
            <div class="tab-content" id="plugin-tab-content">
              <!-- dynamically generated from plugins.json -->
            </div>
          </div>
        </div>
      </div>

<!-- Spotlight -->
<!-- Bootstrap core JavaScript
      ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="assets/js/jquery-3.4.1.min.js"></script>
  <script>

    let first = true;
    const MAX_PLUGIN_COUNT = 6; // controls max number of tabs shown

    $.getJSON("/plugins.json", function(json) {
      let plugins = json.plugins;
      // Fisher-Yates shuffle; see: https://javascript.info/task/shuffle
      for (let i = plugins.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i
        [plugins[i], plugins[j]] = [plugins[j], plugins[i]]; // swap elements
      }
      if (plugins.length > MAX_PLUGIN_COUNT){
        plugins = plugins.slice(0,MAX_PLUGIN_COUNT);
      }
      plugins.map(function(val){
        // generating the tab header
        let nameSlug = 'plugin-' + slugify(val.name);
        let tabString = `
          <li class="nav-item">
            <a class="nav-link ${first ? 'active' : ''}" id="${nameSlug}-tab-header" data-toggle="tab" href="#${nameSlug}-tab" role="tab" aria-controls="${nameSlug}" aria-selected="true">${val.name}</a>
          </li>
        `

        // generating the tab panel
        let paneString = `
        <div class="tab-pane fade ${first ? 'show active' : ''}" id="${nameSlug}-tab" role="tabpanel" aria-labelledby="${nameSlug}-tab-header">
          ${val.imgUrl ?
            '<img class="img-fluid img-plugin" alt="image showing ' + val.name + ' in action" src = "' + val.imgUrl + '" /> <hr />'
            : ''
          }
          <h5 class="card-title">${val.name}</h5>
          <p class="card-text">${val.description}</p>
          <a href="${val.link}" class="btn btn-primary">More information</a>
        </div>
        `
        $("#plugin-tabs").append(tabString);
        $("#plugin-tab-content").append(paneString);


        if (first){
          first = false;
        }
      })
    });
  </script>
