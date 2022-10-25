#!/usr/bin/env bash

KATA_NAME=$1

mkdir "$KATA_NAME" && touch "$KATA_NAME/$KATA_NAME.md" "$KATA_NAME/$KATA_NAME.py"

echo -e "def $KATA_NAME():\n\tpass" >"$KATA_NAME/$KATA_NAME.py"
echo -e "# $KATA_NAME" >"$KATA_NAME/$KATA_NAME.md"
