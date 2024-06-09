#!/bin/bash
# reads all *.md files in the directory
# and autocorrects them
find . -name "*.md" -exec autocorrect --fix {} \;
