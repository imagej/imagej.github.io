---
title: Update Site Statistics
section: Extend:Update Sites
---

<div id="controls" style="left: auto; right: auto; text-align: center">
<b>Update Site:</b> <select id="site" onchange="updateChart()"></select>
<br>
<b>Rolling average:</b>
<input type="radio" id="daily" name="mode" value="daily" checked onchange="updateChart()"><label for="daily">Raw</label>
<input type="radio" id="weekly" name="mode" value="weekly" onchange="updateChart()"><label for="weekly">7-day</label>
<input type="radio" id="monthly" name="mode" value="monthly" onchange="updateChart()"><label for="monthly">30-day</label>
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

## Analyzing the data yourself

You can download the raw data from:

{% include link-banner url='https://sites.imagej.net/stats.json' %}

Here is an example Python script to list all update sites with more than 5000 hits in the year 2022:

```python
import json

year = 2022
cutoff = 5000

with open('stats.json') as f:
    stats = json.load(f)

recent_totals = {
    site: sum(v for date, v in counts.items() if date.startswith(f'{year}-'))
    if isinstance(counts, dict) else 0
    for site, counts in stats.items()
}

popular = dict(sorted(recent_totals.items(), key=lambda x:x[1]))

for site, total in popular.items():
    if total > cutoff:
        print(f"* {site} = {total}")
```
