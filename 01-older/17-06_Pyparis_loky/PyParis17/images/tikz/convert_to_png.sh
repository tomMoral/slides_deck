for i in {1..8}; do 
    echo $i
    f=$(ls $i_*.pdf)
    nf=$(echo $f | sed 's/.pdf/.png/')
    echo $f $nf
    convert -density 150 $f -quality 90 images/$nf; 
    # rm $f; 
done
