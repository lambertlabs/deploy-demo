#!/usr/bin/env bash

set -xe

if ! find scripts/ -name "*.sh" -exec "shellcheck" {} \;; then
    exit 1
fi
