This is code for setting up typesense on the server side. It is tailored for
search.imagej.net, and would need adjustment for use in other scenarios.

Changes made to `index-sites.py` on the main branch will be picked up by the
search.imagej.net server, which calls it hourly via cron to reindex content.
