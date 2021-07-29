---
title: Update Site Statistics
section: Extend:Update Sites
---

<div id="controls" style="left: auto; right: auto; text-align: center">
<b>Update Site:</b> <select id="site" onchange="updateChart()"></select>
<br>
<b>Granularity:</b>
<input type="radio" id="daily" name="mode" value="daily" checked onchange="updateChart()"><label for="daily">Daily</label>
<input type="radio" id="weekly" name="mode" value="weekly" onchange="updateChart()"><label for="weekly">Weekly</label>
<input type="radio" id="monthly" name="mode" value="monthly" onchange="updateChart()"><label for="monthly">Monthly</label>
</div>

<div id="stats-chart" style="width: 100%;"></div>
<script type="text/javascript">
  function updateChart() {
    var site = document.getElementById('site').value;
    var data = [];
    for (var ds in window.siteStats[site]) {
      data.push([new Date(ds), window.siteStats[site][ds]])
    }
    var days = 1;
    if (document.getElementById('weekly').checked) days = 7;
    else if (document.getElementById('monthly').checked) days = 30;
    new Dygraph(
      document.getElementById("stats-chart"),
      data,
      { rollPeriod: days }
    );
  }
  fetch('https://sites.imagej.net/stats.json')
    .then(response => response.json())
    .then(json => {
      window.siteStats = json;
      // Sort site names.
      var siteNames = []
      for (var site in json) siteNames.push(site);
      siteNames.pop(); // remove '_until'
      siteNames.sort();

      // Add sites as options to dropdown list.
      var siteSelect = document.getElementById('site');
      for (var i in siteNames) {
        var siteOption = new Option();
        siteOption.value = siteOption.innerHTML = siteNames[i];
        if (siteNames[i] === 'Java-8') siteOption.selected = true;
        siteSelect.appendChild(siteOption);
      }

      updateChart();
    });
</script>

You can download the raw data from:

{% include link-banner url='https://sites.imagej.net/stats.json' %}
