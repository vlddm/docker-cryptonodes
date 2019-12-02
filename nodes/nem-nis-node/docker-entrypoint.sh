#!/bin/sh
set -e

if [ $(echo "$1" | cut -c1) = "-" ]; then
  echo "$0: assuming arguments for nis"

  set -- ./nis.sh "$@"
fi

if [ $(echo "$1" | cut -c1) = "-" ] || [ "$1" = "java" ]; then
  mkdir -p "$NIS_DATA"
  chmod 700 "$NIS_DATA"
  chown -R nem "$NIS_DATA"
fi

if [ "$1" = "./nis.sh" ] || [ "$1" = "./ncc.sh" ] || [ "$1" = "./harvest.sh" ]; then
  echo
  exec gosu nem "$@"
fi

echo
exec "$@"
