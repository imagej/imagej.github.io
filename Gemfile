source 'https://rubygems.org'

# NB: This site uses stock GitHub Pages deployment, as described at:
#
#    https://pages.github.com/versions/
#
# However, builds with Jekyll 4.2 are orders of magnitude faster than with
# Jekyll 3.9, especially on Windows (6x faster) and macOS (3x faster).
#
# Therefore, this Gemfile declares Jekyll 4.2 with a suitable config,
# rather than using the github-pages gem, so that local builds will
# benefit from the superior performance.
#
# When developing functionality for the site, please take care to
# use only features available in Jekyll 3.9 / stock GitHub Pages.

#gem 'github-pages', group: :jekyll_plugins

gem 'jekyll', '~> 4.2'
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

group :jekyll_plugins do
  gem 'jekyll-sitemap'
end
