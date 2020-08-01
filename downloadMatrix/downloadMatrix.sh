#!/bin/bash
while read line; do 
link="https://suitesparse-collection-website.herokuapp.com/MM"$line".tar.gz"; 
echo  $link;
wget -qO- $link | tar --transform 's/^dbt2-0.37.50.3/dbt2/' -xvz --strip-components 1 -C HB/;
done < HB.txt

