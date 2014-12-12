Unison backup script generator
----------------

This is the script I use to generate a backup bash script from the `.prf` files in my `.unison` folder.

Usage: `generate-backup-script.py -w <unison_working_dir> -u <path_to_unison> [-f <filter>]`

Example: `generate-backup-script.py -w "/home/hlfernandez/.unison" -u "/usr/bin/unison"`

If in my `.unison` folder I have two configuration files called `thunderbird.prf` and `eclipse.prf` the script will generate the following bash script:

```bash
#!/bin/bash
#Unison working directory:  /home/hlfernandez/.unison
#Log file is:  /home/hlfernandez/.unison/last.log
#Path to unison: /usr/bin/unison
echo Unison backup script
echo
echo Options:
echo -e "	0) ALL"
echo -e "	1) thunderbird"
echo -e "	2) eclipse"

echo Type an option and press enter:
read option
echo

rm /home/hlfernandez/.unison/last.log
touch /home/hlfernandez/.unison/last.log

if [[ "$option" -eq "1" || "$option" -eq "0" ]]; then
	echo Synchronizing thunderbird
	echo
	/usr/bin/unison thunderbird -batch &>> /home/hlfernandez/.unison/last.log
fi

if [[ "$option" -eq "2" || "$option" -eq "0" ]]; then
	echo Synchronizing eclipse
	echo
	/usr/bin/unison eclipse -batch &>> /home/hlfernandez/.unison/last.log
fi
```


