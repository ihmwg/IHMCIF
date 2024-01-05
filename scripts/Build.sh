#!/bin/bash -f

if [ "$1" == "" ]; then
    echo "Usage:  $0 <dict_name> <generator_type development|master|local>
    "
    echo "Example:  $0 mmcif_ma local"
    exit 1
fi
dict=$1
genType=$2

TOPDIR="$( builtin cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
echo $TOPDIR

dictname=$dict.dic
outdir=$TOPDIR/dist
outdict=$outdir/$dictname
basedir=$TOPDIR/base
archivedir=$TOPDIR/archive

if [ "$genType" == "master" ]; then
   generator=$basedir/$dict'-generator-master.dic'
elif [ "$genType" == "development" ]; then
   generator=$basedir/$dict'-generator-development.dic'
elif [ "$genType" == "local" ]; then
   generator=$basedir/$dict'-generator-local.dic'
fi

if [ ! -e $generator ]; then
    echo "Missing configuration file $generator"
    exit 1
fi

if [ ! -e $outdir ]; then
    mkdir $outdir
fi
if [ ! -e $archivedir ]; then
    mkdir $archivedir
fi

rm -f $outdict
build_dict_cli --op build --input_dict_path $generator --output_dict_path $outdict --cleanup
version=`build_dict_cli --op get_version --input_dict_path $outdict`
#
archivefile=$archivedir/$dict-v$version'.dic'
cp $outdict $archivefile

echo "Completed generation of $dictname"
exit 0
