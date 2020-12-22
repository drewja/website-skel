DEST_LIB=$HOME/.local/lib/website-skel
DEST_EXEC=$HOME/.local/bin

echo "removing $DEST_LIB"
rm -rv $DEST_LIB
echo "removing symlink $HOME/.local/bin/webskel"
rm -v $DEST_EXEC/webskel