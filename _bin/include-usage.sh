#!/bin/sh
for include in _includes/*
do
  short=${include#_includes/}
  echo "$(git grep "{% *include *$short[% ]" | wc -l) :: $include"
done | sort -n
