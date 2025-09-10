---
title: Update Site Statistics
section: Extend:Update Sites
---

<style>
#controls {
  margin: 0 auto;
  padding-bottom: 2em;
  width: fit-content;
}
#controls .grid {
  display: grid;
  grid-template-columns: 150px 1fr;
  gap: 0.2em 0.2em;
  align-items: start;
}
#controls .grid label.heading {
  font-weight: bold;
  text-align: right;
}
#controls .grid div.widgets {
  display: flex;
  gap: 2px;
  flex-wrap: wrap;
  width: 100%;
}
#controls .grid div.widgets select {
  flex: 1;
}
#controls label, #controls select {
  padding-right: 0.4em;
}
#loading {
  display: none;
  font-style: italic;
  color: #666;
  text-align: center;
  margin-top: 15px;
}
.error {
  color: #d32f2f;
  font-weight: bold;
  padding: 20px;
  text-align: center;
}
</style>

<div id="controls">
<div class="grid">
  <label class="heading">Update Site:</label>
  <div class="widgets">
    <select id="sort" onchange="updateSiteList()">
      <option value="alpha">Sort: A-Z</option>
      <option value="ips">Sort: Most Used</option>
      <option value="date">Sort: Newest</option>
    </select>
    <select id="site" onchange="updateChart()"></select>
  </div>

  <label class="heading">Compare To:</label>
  <div class="widgets">
    <select id="op" onchange="updateCompareMode(); updateChart()">
      <option value=""></option>
      <option value="+" selected>+</option>
      <option value="/">/</option>
      <option value="%">%</option>
    </select>
    <select id="site2" onchange="updateChart()"></select>
  </div>

  <label class="heading">Time Window:</label>
  <div class="widgets">
    <label><input type="radio" id="time-daily" name="timeWindow" value="daily" checked onchange="updateChart()"> Daily</label>
    <label><input type="radio" id="time-monthly" name="timeWindow" value="monthly" onchange="updateChart()"> Monthly</label>
    <label><input type="radio" id="time-yearly" name="timeWindow" value="yearly" onchange="updateChart()"> Yearly</label>
    <label><input type="radio" id="time-ever" name="timeWindow" value="ever" onchange="updateChart()"> Ever/Cumulative</label>
  </div>

  <label class="heading">Count Type:</label>
  <div class="widgets">
    <label><input type="radio" id="count-unique" name="countType" value="unique" checked onchange="updateChart()"> Unique IPs</label>
    <label><input type="radio" id="count-total" name="countType" value="total" onchange="updateChart()"> Total Checks</label>
  </div>

  <label class="heading">Options:</label>
  <div class="widgets">
    <label for="rolling-average"><input type="checkbox" id="rolling-average" checked onchange="updateChart()"> 7-day rolling average</label>
  </div>
</div>

<div id="loading">Loading data...</div>
</div>

<div id="stats-chart" style="width: 100%"></div>

<script src="https://cdn.jsdelivr.net/npm/pako@2.1.0/dist/pako.min.js"></script>
<script type="text/javascript">
  // Data cache to avoid refetching
  window.statsCache = {};

  // Available sites - will be populated from initial discovery
  window.availableSites = [];

  function getSelectedValues() {
    const site = document.getElementById('site').value;
    const op = document.getElementById('op').value;
    const site2 = document.getElementById('site2').value;
    const timeWindow = document.querySelector('input[name="timeWindow"]:checked').value;
    const countType = document.querySelector('input[name="countType"]:checked').value;
    const rollingAverage = document.getElementById('rolling-average').checked;

    return { site, op, site2, timeWindow, countType, rollingAverage };
  }

  function updateSiteList() {
    const sortMode = document.getElementById('sort').value;
    const siteSelect = document.getElementById('site');
    const site2Select = document.getElementById('site2');

    // Remember current selections
    const currentSite = siteSelect.value;
    const currentSite2 = site2Select.value;

    // Sort sites according to selected mode
    let sortedSites = [...window.availableSites];

    switch (sortMode) {
      case 'alpha':
        sortedSites.sort();
        break;
      case 'ips':
        sortedSites.sort((a, b) => {
          const ipsA = window.sitesMetadata[a]?.total_unique_ips || 0;
          const ipsB = window.sitesMetadata[b]?.total_unique_ips || 0;
          return ipsB - ipsA; // Descending
        });
        break;
      case 'date':
        sortedSites.sort((a, b) => {
          const dateA = window.sitesMetadata[a]?.date_range?.start || '00000000';
          const dateB = window.sitesMetadata[b]?.date_range?.start || '00000000';
          return dateB.localeCompare(dateA); // Newest first
        });
        break;
    }

    // Clear and repopulate dropdowns
    siteSelect.innerHTML = '';
    site2Select.innerHTML = '';

    for (const siteName of sortedSites) {
      const siteOption = new Option();
      const site2Option = new Option();
      siteOption.value = site2Option.value = siteName;

      // Add metadata to option text if available
      const metadata = window.sitesMetadata[siteName];
      if (metadata && metadata.total_unique_ips) {
        siteOption.innerHTML = site2Option.innerHTML =
          `${siteName} (${metadata.total_unique_ips.toLocaleString()})`;
      } else {
        siteOption.innerHTML = site2Option.innerHTML = siteName;
      }

      siteSelect.appendChild(siteOption);
      site2Select.appendChild(site2Option);
    }

    // Restore selections if possible
    if (sortedSites.includes(currentSite)) {
      siteSelect.value = currentSite;
    } else if (sortedSites.length > 0) {
      siteSelect.selectedIndex = 0;
    }

    if (sortedSites.includes(currentSite2)) {
      site2Select.value = currentSite2;
    } else if (sortedSites.includes('Java-8')) {
      site2Select.value = 'Java-8';
    } else if (sortedSites.length > 1) {
      site2Select.selectedIndex = 1;
    }

    // Update chart with new selection
    updateChart();
  }

  function updateCompareMode() {
    const op = document.getElementById('op').value;
    const site2Select = document.getElementById('site2');

    if (op === '') {
      // Single site mode
      site2Select.disabled = true;
      site2Select.style.opacity = '0.5';
    } else {
      // Comparison mode
      site2Select.disabled = false;
      site2Select.style.opacity = '1';
    }
  }

  function updateRollingAverageState() {
    const { timeWindow } = getSelectedValues();
    const checkbox = document.getElementById('rolling-average');
    const label = document.querySelector('label[for="rolling-average"]');

    if (timeWindow === 'daily') {
      checkbox.disabled = false;
      label.style.color = '';
    } else {
      checkbox.disabled = true;
      checkbox.checked = false;
      label.style.color = '#999';
    }
  }

  function buildStatsUrl(site, timeWindow, countType) {
    const filename = `stats-${countType}-${timeWindow}.txt.gz`;
    return `https://sites.imagej.net/${site}/${filename}`;
  }

  function getCacheKey(site, timeWindow, countType) {
    return `${site}-${timeWindow}-${countType}`;
  }

  function parseDate(dateStr, timeWindow) {
    if (timeWindow === 'daily' || timeWindow === 'ever') {
      // YYYYMMDD format
      const year = parseInt(dateStr.substring(0, 4));
      const month = parseInt(dateStr.substring(4, 6)) - 1; // JS months are 0-based
      const day = parseInt(dateStr.substring(6, 8));
      return new Date(year, month, day);
    } else if (timeWindow === 'monthly') {
      // YYYYMM format
      const year = parseInt(dateStr.substring(0, 4));
      const month = parseInt(dateStr.substring(4, 6)) - 1;
      return new Date(year, month, 1);
    } else if (timeWindow === 'yearly') {
      // YYYY format
      const year = parseInt(dateStr);
      return new Date(year, 0, 1);
    }
  }

  function fillDateGaps(data, timeWindow) {
    if (!data || data.length === 0) return data;

    // Sort data by date
    data.sort((a, b) => a[0] - b[0]);

    const filled = [];
    const startDate = new Date(data[0][0]);
    const endDate = new Date(data[data.length - 1][0]);

    // Create a map for quick lookup
    const dataMap = new Map();
    for (const [date, value] of data) {
      dataMap.set(date.getTime(), value);
    }

    let current = new Date(startDate);
    let lastCumulativeValue = 0;

    while (current <= endDate) {
      const currentTime = current.getTime();

      if (dataMap.has(currentTime)) {
        const value = dataMap.get(currentTime);
        filled.push([new Date(current), value]);
        if (timeWindow === 'ever') {
          lastCumulativeValue = value;
        }
      } else {
        // Fill gap
        if (timeWindow === 'ever') {
          // For cumulative data, use the last known value
          filled.push([new Date(current), lastCumulativeValue]);
        } else {
          // For other data types, use 0
          filled.push([new Date(current), 0]);
        }
      }

      // Increment current date based on time window
      if (timeWindow === 'daily' || timeWindow === 'ever') {
        current.setDate(current.getDate() + 1);
      } else if (timeWindow === 'monthly') {
        current.setMonth(current.getMonth() + 1);
      } else if (timeWindow === 'yearly') {
        current.setFullYear(current.getFullYear() + 1);
      }
    }

    return filled;
  }

  function combineForStackedChart(data1, data2) {
    if (!data1 || !data2) return data1 || data2 || [];

    // Create maps for efficient lookup
    const map1 = new Map(data1.map(([date, value]) => [date.getTime(), value]));
    const map2 = new Map(data2.map(([date, value]) => [date.getTime(), value]));

    // Get all unique dates from both datasets
    const allDates = new Set([...map1.keys(), ...map2.keys()]);
    const result = [];

    for (const dateKey of Array.from(allDates).sort()) {
      const date = new Date(dateKey);
      const val1 = map1.get(dateKey) || 0;
      const val2 = map2.get(dateKey) || 0;

      // Format: [date, site1_value, site2_value]
      result.push([date, val1, val2]);
    }

    return result;
  }

  function combineDataSets(data1, data2, operation) {
    if (!data1 || !data2) return data1 || data2 || [];

    // Create maps for efficient lookup
    const map1 = new Map(data1.map(([date, value]) => [date.getTime(), value]));
    const map2 = new Map(data2.map(([date, value]) => [date.getTime(), value]));

    // Get all unique dates from both datasets
    const allDates = new Set([...map1.keys(), ...map2.keys()]);
    const result = [];

    for (const dateKey of Array.from(allDates).sort()) {
      const date = new Date(dateKey);
      const val1 = map1.get(dateKey) || 0;
      const val2 = map2.get(dateKey) || 0;

      let combinedValue;
      switch (operation) {
        case '/':
          combinedValue = val2 === 0 ? 0 : val1 / val2;
          break;
        case '%':
          combinedValue = (val1 + val2) === 0 ? 0 : (val1 / (val1 + val2)) * 100;
          break;
        default:
          combinedValue = val1;
      }

      result.push([date, combinedValue]);
    }

    return result;
  }

  async function fetchStatsData(site, timeWindow, countType) {
    const cacheKey = getCacheKey(site, timeWindow, countType);

    if (window.statsCache[cacheKey]) {
      return window.statsCache[cacheKey];
    }

    const url = buildStatsUrl(site, timeWindow, countType);

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      // Handle pre-compressed .gz files (browser won't auto-decompress these)
      const arrayBuffer = await response.arrayBuffer();
      const decompressed = pako.inflate(new Uint8Array(arrayBuffer), { to: 'string' });
      const text = decompressed;
      const lines = text.trim().split('\n');
      const data = [];

      for (const line of lines) {
        if (line.trim()) {
          const parts = line.trim().split(/\s+/);
          if (parts.length >= 2) {
            const dateStr = parts[0];
            const countStr = parts[1];
            const date = parseDate(dateStr, timeWindow);
            const count = parseInt(countStr);
            if (!isNaN(count) && date instanceof Date && !isNaN(date.getTime())) {
              data.push([date, count]);
            }
          }
        }
      }

      // Cache the parsed data
      window.statsCache[cacheKey] = data;
      return data;

    } catch (error) {
      console.error(`Failed to fetch stats for ${site} (${timeWindow}/${countType}):`, error);
      throw error;
    }
  }

  async function updateChart() {
    const { site, op, site2, timeWindow, countType, rollingAverage } = getSelectedValues();

    if (!site) return;

    // Update rolling average state
    updateRollingAverageState();

    // Show loading indicator
    document.getElementById('loading').style.display = 'block';

    try {
      // Fetch data for primary site
      const rawData1 = await fetchStatsData(site, timeWindow, countType);
      let data = fillDateGaps(rawData1, timeWindow);
      let chartTitle = site;
      let yLabel = `${countType === 'unique' ? 'Unique IP Addresses' : 'Total Update Checks'}`;

      // Configuration for chart
      let chartConfig = {
        rollPeriod: rollingAverage && timeWindow === 'daily' ? 7 : 1,
        labels: ['Date', `${countType === 'unique' ? 'Unique IPs' : 'Total Checks'}`],
        ylabel: yLabel,
        title: `${chartTitle} - ${timeWindow.charAt(0).toUpperCase() + timeWindow.slice(1)} ${countType === 'unique' ? 'Unique' : 'Total'} Statistics`
      };

      // Set X-axis formatting based on time window
      if (timeWindow === 'yearly') {
        chartConfig.axes = {
          x: {
            axisLabelFormatter: function(d) {
              return d.getFullYear().toString();
            },
            ticker: function(a, b, pixels, opts, dygraph, vals) {
              // Generate yearly ticks
              const startYear = new Date(a).getFullYear();
              const endYear = new Date(b).getFullYear();
              const ticks = [];
              for (let year = startYear; year <= endYear; year++) {
                ticks.push({v: new Date(year, 0, 1).getTime(), label: year.toString()});
              }
              return ticks;
            }
          }
        };
      } else if (timeWindow === 'monthly') {
        chartConfig.axes = {
          x: {
            axisLabelFormatter: function(d) {
              return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0');
            }
          }
        };
      }

      // If comparison mode is enabled and site2 is selected
      if (op && site2 && site2 !== site) {
        const rawData2 = await fetchStatsData(site2, timeWindow, countType);
        const filledData2 = fillDateGaps(rawData2, timeWindow);

        if (op === '+') {
          // For sum, create stacked chart with both series
          data = combineForStackedChart(data, filledData2);
          chartTitle = `${site} + ${site2}`;
          chartConfig.labels = ['Date', site, site2];
          chartConfig.stackedGraph = true;
          chartConfig.fillGraph = true;
          chartConfig.colors = ['#1f77b4', '#ff7f0e'];
        } else {
          // For other operations, combine into single series
          data = combineDataSets(data, filledData2, op);
          switch (op) {
            case '/':
              chartTitle = `${site} / ${site2}`;
              yLabel = `Ratio (${site}/${site2})`;
              break;
            case '%':
              chartTitle = `${site} as % of (${site} + ${site2})`;
              yLabel = `Percentage (%)`;
              break;
          }
        }

        chartConfig.title = `${chartTitle} - ${timeWindow.charAt(0).toUpperCase() + timeWindow.slice(1)} ${countType === 'unique' ? 'Unique' : 'Total'} Statistics`;
        chartConfig.ylabel = yLabel;
      }

      new Dygraph(document.getElementById("stats-chart"), data, chartConfig);

    } catch (error) {
      document.getElementById("stats-chart").innerHTML =
        `<div class="error">
          <p>Error loading data: ${error.message}</p>
        </div>`;
    } finally {
      // Hide loading indicator
      document.getElementById('loading').style.display = 'none';
    }
  }

  // Initialize the page
  async function initializePage() {
    try {
      // Fetch site list and metadata from sites.json
      const response = await fetch('https://sites.imagej.net/sites.json');
      if (!response.ok) {
        throw new Error(`Failed to fetch sites list: ${response.status} ${response.statusText}`);
      }

      const sitesData = await response.json();
      window.sitesMetadata = sitesData;

      // Extract site names (will be sorted by updateSiteList)
      window.availableSites = Object.keys(sitesData);

      // Set default selections
      const siteSelect = document.getElementById('site');
      const site2Select = document.getElementById('site2');

      // Populate and sort site lists
      updateSiteList();

      // Set initial selections after population
      if (window.availableSites.includes('Fiji')) {
        siteSelect.value = 'Fiji';
      }
      if (window.availableSites.includes('Java-8')) {
        site2Select.value = 'Java-8';
      }

      // Initialize compare mode state and chart
      updateCompareMode();
      updateChart();

    } catch (error) {
      console.error('Failed to initialize page:', error);
      // Fallback to hardcoded list if sites.json fails
      window.availableSites = ['Java-8', 'Fiji'];
      window.sitesMetadata = {}; // Empty metadata for fallback

      const siteSelect = document.getElementById('site');
      const site2Select = document.getElementById('site2');

      updateSiteList();

      // Set fallback selections
      if (window.availableSites.includes('Fiji')) {
        siteSelect.value = 'Fiji';
      }
      if (window.availableSites.includes('Java-8')) {
        site2Select.value = 'Java-8';
      }

      updateCompareMode();
      updateChart();
    }
  }

  // Initialize when page loads
  document.addEventListener('DOMContentLoaded', initializePage);

  // Also initialize immediately in case DOMContentLoaded already fired
  if (document.readyState === 'loading') {
    // Still loading, wait for DOMContentLoaded
  } else {
    // Already loaded
    initializePage();
  }
</script>

## Analyzing the data yourself

You can download the raw data directly from individual update sites. Each site has 8 different statistics files available, plus a metadata index:

**Data Types:**
- `stats-unique-daily.txt.gz` - Unique IP addresses per day
- `stats-total-daily.txt.gz` - Total update checks per day
- `stats-unique-monthly.txt.gz` - Unique IP addresses per month
- `stats-total-monthly.txt.gz` - Total update checks per month
- `stats-unique-yearly.txt.gz` - Unique IP addresses per year
- `stats-total-yearly.txt.gz` - Total update checks per year
- `stats-unique-ever.txt.gz` - Cumulative unique IP addresses by day
- `stats-total-ever.txt.gz` - Cumulative total checks by day
- `sites.json` - Metadata index with site list and summary statistics

**URL Format:** `https://sites.imagej.net/{SITE_NAME}/{STATS_FILE}`

**Sites Index:** [https://sites.imagej.net/sites.json](https://sites.imagej.net/sites.json)

**Example URLs:**
- [https://sites.imagej.net/Java-8/stats-unique-daily.txt.gz](https://sites.imagej.net/Java-8/stats-unique-daily.txt.gz)
- [https://sites.imagej.net/Fiji/stats-total-monthly.txt.gz](https://sites.imagej.net/Fiji/stats-total-monthly.txt.gz)

**Data Format:** Each line contains a datestamp and count value separated by a space:
```
20250723 458
20250724 672
20250725 543
```

Date formats:
- Daily/Ever: `YYYYMMDD` (e.g., `20250723`)
- Monthly: `YYYYMM` (e.g., `202507`)
- Yearly: `YYYY` (e.g., `2025`)

**Sites Metadata Format:**
The `sites.json` file contains metadata for each update site:
```json
{
  "Java-8": {
    "date_range": {
      "start": "20151220",
      "end": "20250904"
    },
    "total_unique_ips": 12534,
    "total_requests": 89472,
    "days_with_data": 3546,
    "last_generated": "2025-09-05"
  }
}
```

Here is an example Python script to analyze total yearly downloads for a specific site:

```python
import gzip
import urllib.request

def fetch_yearly_stats(site_name, stat_type='total'):
    """Fetch and parse yearly statistics for a site."""
    url = f'https://sites.imagej.net/{site_name}/stats-{stat_type}-yearly.txt.gz'

    with urllib.request.urlopen(url) as response:
        with gzip.open(response, 'rt') as f:
            data = {}
            for line in f:
                if line.strip():
                    year, count = line.strip().split()
                    data[int(year)] = int(count)
    return data

# Example: Get Java-8 yearly download statistics
site = 'Java-8'
yearly_stats = fetch_yearly_stats(site, 'unique')

print(f"Yearly unique IP statistics for {site}:")
for year in sorted(yearly_stats.keys()):
    print(f"  {year}: {yearly_stats[year]:,} unique IPs")

# Find the most popular year
best_year = max(yearly_stats.keys(), key=lambda y: yearly_stats[y])
print(f"\nBest year: {best_year} with {yearly_stats[best_year]:,} unique IPs")

# Example: List all sites sorted by total unique IPs
def get_sites_ranking():
    """Get all sites ranked by total unique IPs."""
    import json

    with urllib.request.urlopen('https://sites.imagej.net/sites.json') as response:
        sites_data = json.load(response)

    # Sort sites by total unique IPs
    ranked_sites = sorted(
        sites_data.items(),
        key=lambda x: x[1]['total_unique_ips'],
        reverse=True
    )

    print("Sites ranked by total unique IPs:")
    for site_name, metadata in ranked_sites:
        print(f"  {site_name}: {metadata['total_unique_ips']:,} unique IPs "
              f"({metadata['days_with_data']} days of data)")

get_sites_ranking()
```
