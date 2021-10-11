#!/bin/sh

set -x
set -e
set -u

csv_file=output.csv
png_file_list=pngfilelist
success_csv=ok.csv
success_file=ok.filelist
failed_csv=failed.csv
failed_file=failed.filelist

find ./ -name '*.png' > $png_file_list
sed -i -e 's/^.\///' $png_file_list


IN_FILE=`mktemp`

cat $csv_file | while read line
do
    img_path_in_csv=`echo $line | awk -F',' '{print $4}'`
    cat $png_file_list | while read fileline
    do
	echo 0 > $IN_FILE
	if [ "$fileline" == "$img_path_in_csv" ]
	then
	    echo 1 > $IN_FILE
	    break
	fi
    done
    if [ `cat $IN_FILE` == 1 ]
    then
	echo $line >> $success_csv
	echo $img_path_in_csv >> $success_file
    else
	echo $line >> $failed_csv
	echo $img_patho_in_csv >> $failed_file
    fi
done
		   


