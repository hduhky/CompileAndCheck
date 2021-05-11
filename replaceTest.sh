#!/bin/bash

FilePath="$1"
TargetText="$2"
ReplaceText="$3"
sed -i '' s/${TargetText}/${ReplaceText}/ ${FilePath}




