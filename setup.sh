#!/bin/bash

set -eo pipefail

(cd ./python && ./setup.sh)

(cd ./scala && sbt clean assembly)