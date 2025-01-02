
bookprice=8
bookquantity=8
penprice=10
penquantity=10
totalbill=$(expr $bookprice \* $bookquantity + $penprice \* $penquantity)
 echo $totalbill

