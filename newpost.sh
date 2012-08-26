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

HEADER="---\nlayout: post\ntitle: $TITLE\npublished: true\ncategories: [$KEYWORDS]\n---\n"

mkdir -p "work/$PLACE/_posts"

DATE=`date +"%Y-%m-%d-%H.%M"`
# 2011-10-30-13.00-the-title-of-the-post.markdown
TITLE=`echo $TITLE | sed 's/ /-/g'`
FILE="work/$PLACE/_posts/${DATE}-$TITLE.markdown"
echo -e $HEADER > $FILE
echo "post at $FILE" 

