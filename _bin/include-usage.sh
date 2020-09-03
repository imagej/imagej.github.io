#!/bin/sh

if [ $# -gt 0 ]
then
  for t in $@
  do
    grep -oh "{% *include  *$t [^%]*%}" _pages/*
  done
else
  # List counts of all unfinished templates.
  for include in _includes/*
  do
    grep -q TODO "$include" || continue
    short=${include#_includes/}
    echo "$(git grep "{% *include *$short[% ]" | wc -l) :: $include"
  done | sort -n
fi
