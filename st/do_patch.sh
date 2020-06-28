#!/usr/local/bin/bash
function patchy {
        echo -e "\e[41;30m$1\e[39;49m"
        patch -uV existing < ../../patch/$1
}

cd ./work/st-0.8.3
patchy st-scrollback-20200419-72e3f6c.diff
patchy st-scrollback-mouse-20191024-a2c479c.diff
#patchy st-no_bold_colors-20170623-b331da5.diff
#patchy st-solarized-dark-20180411-041912a.diff
patchy st-clipboard-20180309-c5ba9c0.diff
patchy st-alpha-0.8.2.diff
patchy robpref.diff
