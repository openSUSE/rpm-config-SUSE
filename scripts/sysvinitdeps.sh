#!/bin/sh

[ "$1" = '-P' -o "$1" = '--provides' ] || {
    cat > /dev/null
    exit 0
}

while read file; do
	case $file in
          */etc/init.d/*)
		provs=`grep '^# *Provides:' $file | sed 's,^.*:,,'`
		for p in $provs; do
			echo "sysvinit($p)"
		done
	  ;;
        esac
done
