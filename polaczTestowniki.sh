outdir="out_testownik"
indir="out_testownik"

for dir in `ls "$indir"`
do
    echo "$dir"
    mv "$indir/$dir"/* "$outdir"
    rmdir "$indir/$dir"
done

echo "Połączono!"