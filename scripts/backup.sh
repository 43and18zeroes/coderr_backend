echo "Database Backup started"
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BACKUP_NAME="db-backup__`date "+%F__%H:%M"`.db"
cp $SCRIPT_DIR/../db.sqlite3 $BACKUP_NAME
echo "Uploading file:  $BACKUP_NAME"

echo "
 verbose
 open w01c0cb4.kasserver.com
 user f01748c0 fav0r4!M1nt
 bin
 cd coderr
 put $BACKUP_NAME
 bye
" | ftp -n > ftp_$$.log
echo "Backup successful"

rm $BACKUP_NAME
rm ftp_$$.log