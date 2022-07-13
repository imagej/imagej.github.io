// maven.js - scrape a remote Maven repository for details about a component.

function values(element, path, cdata = true) {
  if ('documentElement' in element) {
    // convenience coercion: Document -> Element
    element = element.documentElement;
  }
  if (path.length == 0) return cdata ? element.innerHTML : element;
  var path1 = path.slice();
  var name = path1.shift();
  var result = []
  var children = element.children;
  for (var i = 0; i < children.length; i++) {
    var child = children[i];
    if (child.tagName === name) {
      result = result.concat(values(child, path1, cdata));
    }
  }
  return result;
}

function value(element, path, cdata = true) {
  var vals = values(element, path, cdata);
  return vals.length > 0 ? vals[0] : null;
}

function download(url) {
  /*
  if (response.ok) { // if HTTP-status is 200-299
    // get the response body (the method explained below)
    let json = await response.json();
  } else {
    alert("HTTP-Error: " + response.status);
  }
  */
  // TODO: Handle HTTP response codes.
  return fetch(url)
    .then(response => response.text())
    .then(str => (new window.DOMParser()).parseFromString(str, "text/xml"));
}

function lastModified(url) {
  // TODO: Someone better at JavaScript than me could figure out how to combine
  // this request with the one from download, extracting both the response text
  // and the last modified date in one swoop. But it wasn't obvious to me how
  // to do it due to the asynchronous promises involved.
  return fetch(url).then(response => response.headers.get('Last-Modified'));
}

function gpath(g) {
  return g.replace(/\./g, '/')
}

/* Discern latest release version of an artifact from remote metadata. */
function latestVersion(g, a, repository) {
  return download(`${repository}/${gpath(g)}/${a}/maven-metadata.xml`)
    .then(metadata => value(metadata, ['versioning', 'release']));
}

/* Discern the concrete version string for a given snapshot version. */
function resolveSnapshotVersion(g, a, v, repository) {
  // E.g.: slim-curve:slim_plugin:2.0.0-SNAPSHOT -> 2.0.0-20191015.150518-26
  return download(`${repository}/${gpath(g)}/${a}/${v}/maven-metadata.xml`)
    .then(metadata => {
      var timestamp = value(metadata, ['versioning', 'snapshot', 'timestamp']);
      var buildNumber = value(metadata, ['versioning', 'snapshot', 'buildNumber']);
      return `${v.slice(0, -9)}-${timestamp}-${buildNumber}`;
    });
}

function link(url, label) {
  return url ? `<a href=\"${url}\">${label}</a>` : label;
}

function releaseURL(g, a, v) {
  return `https://maven.scijava.org/index.html#nexus-search;gav~${g}~${a}~${v}~~~kw,versionexpand`;
}

function fill(id, value) {
  var element = document.getElementById(id);
  if (element && !element.classList.contains("manual")) {
    // Value exists and was not manually specified, so it should be filled.
    element.innerHTML = value || '[Unknown]';
  }
}

function fillRole(id, people) {
  var element = document.getElementById(id);
  var ul = document.createElement('ul');
  element.appendChild(ul);
  for (var i in people) {
    var person = people[i];
    var id = person.id;
    var name = person.name;
    var url = person.url;
    if (!name && id) name = id;
    if (!name) continue; // no name or id -- skip this person
    if (!url && id) url = `/people/${id}`;
    var li = document.createElement('li');
    li.innerHTML = url ?
      `<a class="person" href="${url}">${name}</a>` :
      `<span class="person">${name}</span>`;
    ul.appendChild(li);
  }
}

function fillStatus(id, label, description) {
  fill(id, `<span class="tooltip">${label}<span class="tooltiptext" style="left: -90px; bottom: 1.5em; width: 180px">${description}</span></span>`);
}

function catalogRoles(team, id, name, url, roles) {
  for (var i in roles) {
    var role = roles[i];
    if (!(role in team)) team[role] = [];
    team[role].push({'id': id, 'name': name, 'url': url});
  }
}

function fillStatsFromPOM(pom) {
  var g = value(pom, ['groupId']) || value(pom, ['parent', 'groupId']);
  var a = value(pom, ['artifactId']);
  var v = value(pom, ['version']) || value(pom, ['parent', 'version']);

  fill('statbox-name', value(pom, ['name']));
  var sourceURL = value(pom, ['scm', 'url']);
  var sourceLabel = 'online';
  if (sourceURL.startsWith('https://github.com/')) sourceLabel = 'on GitHub';
  else if (sourceURL.startsWith('https://gitlab.com/')) sourceLabel = 'on GitLab';
  else if (sourceURL.startsWith('https://bitbucket.org/')) sourceLabel = 'on BitBucket';
  fill('component-source', link(sourceURL, sourceLabel));

  var licenseName = value(pom, ['licenses', 'license', 'name']);
  var licenseURL = value(pom, ['licenses', 'license', 'url']);

  // Standardize/abbreviate known licenses.
  switch (licenseName) {
    case 'Apache 2':                                            licenseName = 'Apache v2';   break;
    case 'Apache License 2':                                    licenseName = 'Apache v2';   break;
    case 'Apache License, Version 2.0':                         licenseName = 'Apache v2';   break;
    case 'Apache Software License, Version 2.0':                licenseName = 'Apache v2';   break;
    case 'BSD 2-Clause "Simplified" License':                   licenseName = 'BSD-2';       break;
    case 'BSD 2-Clause License':                                licenseName = 'BSD-2';       break;
    case 'BSD License Version 3':                               licenseName = 'BSD-3';       break;
    case 'BSD license version 3':                               licenseName = 'BSD-3';       break;
    case 'BSD-2-Clause':                                        licenseName = 'BSD-2';       break;
    case 'BSD3':                                                licenseName = 'BSD-3';       break;
    case 'CC0 1.0 Universal License':                           licenseName = 'CC0';         break;
    case 'CC0 1.0 Universal':                                   licenseName = 'CC0';         break;
    case 'CC0':                                                 licenseName = 'CC0';         break;
    case 'Community Research and Academic Programming License': licenseName = 'CRAPL';       break;
    case 'Eclipse Public License 1.0':                          licenseName = 'EPLv1';       break;
    case 'Eclipse Public License':                              licenseName = 'EPL';         break;
    case 'Eclipse Public License, Version 2.0':                 licenseName = 'EPLv2';       break;
    case 'GNU GPL v3':                                          licenseName = 'GPLv3';       break;
    case 'GNU General Public License (GPL) v3+':                licenseName = 'GPLv3+';      break;
    case 'GNU General Public License v2':                       licenseName = 'GPLv2';       break;
    case 'GNU General Public License v2+':                      licenseName = 'GPLv2+';      break;
    case 'GNU General Public License v2+':                      licenseName = 'GPLv2+';      break;
    case 'GNU General Public License v3':                       licenseName = 'GPLv3';       break;
    case 'GNU General Public License v3+':                      licenseName = 'GPLv3+';      break;
    case 'GNU General Public License v3+':                      licenseName = 'GPLv3+';      break;
    case 'GNU General Public License v3.0':                     licenseName = 'GPLv3';       break;
    case 'GNU General Public License':                          licenseName = 'GPL';         break;
    case 'GNU General Public License, version 2 (GPL-2.0)':     licenseName = 'GPLv2';       break;
    case 'GNU Lesser General Public License v2.1+':             licenseName = 'GPLv2.1+';    break;
    case 'GNU Lesser General Public License v3+':               licenseName = 'GPLv3+';      break;
    case 'GNU Public License v2':                               licenseName = 'GPLv2';       break;
    case 'GPL 2 or later':                                      licenseName = 'GPLv2+';      break;
    case 'GPL-2.0':                                             licenseName = 'GPLv2';       break;
    case 'GPLv2 with Classpath exception':                      licenseName = 'GPLv2 w/CP';  break;
    case 'GPLv2':                                               licenseName = 'GPLv2';       break;
    case 'GPLv3.0':                                             licenseName = 'GPLv3';       break;
    case 'Janelia Farm Research Campus Software Copyright 1.1': licenseName = 'JFRCv1.1';    break;
    case 'MIT License':                                         licenseName = 'MIT';         break;
    case 'Modified BSD License':                                licenseName = 'BSD-3';       break;
    case 'Simplified BSD License':                              licenseName = 'BSD-2';       break;
    case 'Simplified BSD License':                              licenseName = 'BSD-2';       break;
    case 'The Apache Software License, Version 2.0':            licenseName = 'Apache v2';   break;
    case 'The BSD License':                                     licenseName = 'BSD';         break;
    case 'The GNU Lesser General Public License, Version 3.0':  licenseName = 'LGPLv3';      break;
    case 'The MIT License':                                     licenseName = 'MIT';         break;
    case 'The zlib/libpng License':                             licenseName = 'zlib/libpng'; break;
    case 'bsd_2':                                               licenseName = 'BSD-2';       break;
    case 'not licensed yet':                                    licenseName = 'None';        break;
    case 'olefile License':                                     licenseName = 'olefile';     break;
  }

  // Fill in missing license URLs for known licenses.
  if (!licenseURL) {
    switch (licenseName) {
      case 'Apache v2':     licenseURL = '/licensing/apache#apache-license-20'; break;
      case 'BSD':           licenseURL = '/licensing/bsd'; break;
      case 'BSD-2':         licenseURL = '/licensing/bsd#simplified-bsd-license'; break;
      case 'BSD-3':         licenseURL = '/licensing/bsd#modified-bsd-license'; break;
      case 'CC0':           licenseURL = '/licensing/public-domain#creative-commons-zero-10-universal'; break;
      case 'CRAPL':         licenseURL = 'https://matt.might.net/articles/crapl/'; break;
      case 'EPL':           licenseURL = '/licensing/epl'; break;
      case 'EPLv1':         licenseURL = '/licensing/epl#eclipse-public-license-v10'; break;
      case 'EPLv2':         licenseURL = '/licensing/epl#eclipse-public-license-v20'; break;
      case 'GPL':           licenseURL = '/licensing/gpl'; break;
      case 'GPLv2 w/CP':    licenseURL = '/licensing/gpl#gnu-general-public-license-v2'; break;
      case 'GPLv2':         licenseURL = '/licensing/gpl#gnu-general-public-license-v2'; break;
      case 'GPLv2+':        licenseURL = '/licensing/gpl#gnu-general-public-license-v2'; break;
      case 'GPLv2.1+':      licenseURL = '/licensing/gpl#gnu-general-public-license-v2'; break;
      case 'GPLv3':         licenseURL = '/licensing/gpl#gnu-general-public-license-v3'; break;
      case 'GPLv3+':        licenseURL = '/licensing/gpl#gnu-general-public-license-v3'; break;
      case 'LGPL':          licenseURL = '/licensing/lgpl'; break;
      case 'LGPLv2':        licenseURL = '/licensing/lgpl#gnu-lesser-general-public-license-v21'; break;
      case 'LGPLv2.1':      licenseURL = '/licensing/lgpl#gnu-lesser-general-public-license-v21'; break;
      case 'LGPLv3':        licenseURL = '/licensing/lgpl#gnu-lesser-general-public-license-v3'; break;
      case 'MIT':           licenseURL = '/licensing/mit'; break;
      case 'Public domain': licenseURL = '/licensing/public-domain'; break;
      case 'Unlicense':     licenseURL = '/licensing/public-domain#unlicense'; break;
    }
  }

  fill('component-license', link(licenseURL, licenseName));
  fill('component-release', link(releaseURL(g, a, v), v));

  var team = {};
  var developers = values(pom, ['developers', 'developer'], false)
  for (var i in developers) {
    var developer = developers[i];
    var id = value(developer, ['id']);
    var name = value(developer, ['name']);
    var url = value(developer, ['url']);
    var roles = values(developer, ['roles', 'role']);
    catalogRoles(team, id, name, url, roles);
  }
  var contributors = values(pom, ['contributors', 'contributor'], false)
  for (var i in contributors) {
    var contributor = contributors[i];
    var id = value(contributor, ['properties', 'id']);
    var name = value(contributor, ['name']);
    var url = value(contributor, ['url']);
    var roles = values(contributor, ['roles', 'role']);
    if (roles.length == 0) roles.push('contributor');
    catalogRoles(team, id, name, url, roles);
  }

  if ('founder' in team) fillRole('component-team-founders', team.founder);
  if ('lead' in team) fillRole('component-team-leads', team.lead);
  if ('developer' in team) fillRole('component-team-developers', team.developer);
  if ('debugger' in team) fillRole('component-team-debuggers', team.debugger);
  if ('reviewer' in team) fillRole('component-team-reviewers', team.reviewer);
  if ('support' in team) fillRole('component-team-support', team.support);
  if ('maintainer' in team) fillRole('component-team-maintainers', team.maintainer);
  if ('contributor' in team) fillRole('component-team-contributors', team.contributor);

  if ('developer' in team) {
    if (v.startsWith('0.')) {
      fillStatus('component-dev-status', 'Unstable',
        'This project is under heavy development, with ' +
        'unstable API undergoing iterations of refinement.');
    }
    else {
      fillStatus('component-dev-status', 'Active',
        'New features are being actively developed. ' +
        'API breakages are kept as limited as possible.');
    }
  }
  else {
    if (true) { // TODO: How to discern Stable vs. Obsolete?
      fillStatus('component-dev-status', 'Stable',
        'No new features are under development. API is stable.');
    }
    else {
      fillStatus('component-dev-status', 'Obsolete',
        'The project is discontinued.');
    }
  }

  if ('support' in team) {
    if ('debugger' in team) {
      fillStatus('component-support-status', 'Active',
        'Someone will respond to questions on community channels, ' +
        "and addresses issue reports in the project's issue tracker. " +
        'A best effort is made to fix reported bugs within a reasonable time frame.');
    }
    else {
      fillStatus('component-support-status', 'Partial',
        'Someone will respond to questions on community channels, ' +
        "as well as to issue reports in the project's issue tracker. " +
        'But reported bugs may not be addressed in a timely manner.');
    }
  }
  else {
    if ('debugger' in team || 'reviewer' in team || 'maintainer' in team) {
      fillStatus('component-support-status', 'Minimal',
        'There is at least one person pledged to the project in some capacity, ' +
        'but not all roles are filled. ' +
        'Response time to questions and issue reports may be protracted.');
    }
    else {
      fillStatus('component-support-status', 'None',
        'No one is pledged to support the project. ' +
        'Questions and issue reports may be ignored. ');
    }
  }
}

function fillStatsFromURL(url) {
  download(url).then(pom => fillStatsFromPOM(pom));
  lastModified(url).then(date => fill('component-date', date.replace(/(\d{4}) /, "$1<br>")));
}

function fillStatsFromGAV(g, a, v, repository) {
  if (v.endsWith("-SNAPSHOT")) {
    resolveSnapshotVersion(g, a, v, repository).then(sv => {
      fillStatsFromURL(`${repository}/${gpath(g)}/${a}/${v}/${a}-${sv}.pom`);
    });
  }
  else fillStatsFromURL(`${repository}/${gpath(g)}/${a}/${v}/${a}-${v}.pom`);
}

function fillStatsFromArtifact(artifact, repository) {
  if (!repository) repository = 'https://maven.scijava.org/content/groups/public';
  var gav = artifact.split(':');
  var g = gav.length > 0 ? gav[0] : '';
  var a = gav.length > 1 ? gav[1] : '';
  var v = gav.length > 2 ? gav[2] : '';
  if (v) fillStatsFromGAV(g, a, v, repository);
  else latestVersion(g, a, repository).then(lv => fillStatsFromGAV(g, a, lv, repository));
}
