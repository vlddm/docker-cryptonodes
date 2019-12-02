#!/bin/sh

if [ "$1" = "screen" ]; then
  mkdir -p "$NEO_DATA"
  chmod 700 "$NEO_DATA"
  chown -R neo "$NEO_DATA"
  echo "Fixed permission on $NEO_DATA"
fi

exec gosu neo "$@"
