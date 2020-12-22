DEST_LIB=$HOME/.local/lib/website-skel
DEST_EXEC=$HOME/.local/bin

mkdir -p $DEST_LIB

rsync -rmv cli $DEST_LIB 
rsync -rmv skel $DEST_LIB 

echo "creating sym link "
ln -v -s -T $DEST_LIB/cli/main.py $DEST_EXEC/webskel
chmod +x $DEST_LIB/cli/main.py