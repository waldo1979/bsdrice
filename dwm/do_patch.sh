#!/usr/local/bin/bash
#for patch in ../../patches/*; 
#do
	#echo $patch
#	patch -u -V existing < $patch
#done
function patchy {
	echo -e "\e[41;30m$1\e[39;49m"
	patch -uV existing < ../../patches/$1
}

cd ./work/dwm-6.2
#patchy dwm-systray-6.2.diff
patchy dwm-alpha-20180613-b69c870.diff
#patchy dwm-pango-20200428-f09418b.diff
patchy dwm-statuscolors-nopad-systray-20180106-db22360.patch
patchy dwm-fibonacci-20200418-c82db69.diff
patchy dwm-fixborders-6.2.diff
patchy dwm-uselessgap-6.2.diff
patchy robs_config.diff
cp ../../patches/tcl.c .
cd ../../
