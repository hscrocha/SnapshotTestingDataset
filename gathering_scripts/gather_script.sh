#!/bin/bash -ex

# arguments:
# owner/repo = $1
# token = $2

#FNAME will convert slash to underscore to save a tar file
FNAME=${1////_}
#echo $FNAME
wget --header="Authorization: token ${2}" --header="Accept:application/vnd.github.v3.raw" -O - https://api.github.com/repos/${1}/tarball > $FNAME.tar.gz
