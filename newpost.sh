#!/bin/bash

echo "Post title:"
read TITLE

echo "Post Keywords (comma separated list):"
read KEYWORDS

PLACE="default"
echo "Path to post (current: $PLACE):"
read NEWPLACE

if [ "$NEWPLACE" != "" ]
then
    PLACE=$NEWPLACE
fi

HEADER="---
layout: post
title: $TITLE
published: true
categories: [$KEYWORDS]
---"

mkdir -p "work/$PLACE/_posts"

DATE=`date +"%Y-%m-%d-%H.%M"`
# 2011-10-30-13.00-the-title-of-the-post.markdown
TITLE=`echo $TITLE | sed 's/ /-/g'`
echo $HEADER > "work/$PLACE/_posts/${DATE}-$TITLE.markdown"


