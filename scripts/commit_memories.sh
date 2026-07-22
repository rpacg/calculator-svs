#!/bin/bash

echo "Adding changes under ./scripts and ./memories..."
git add ./scripts ./memories
if git diff --cached --quiet; then
  echo "No staged changes in ./scripts or ./memories. Nothing to commit."
  exit 0
fi

git commit -m 'memories update'
if [ $? -ne 0 ]; then
  echo "Commit failed."
  exit 1
fi

git push
