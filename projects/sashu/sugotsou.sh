breadprice=10
breadquantity=7
butterprice=8
butterquantity=15
totalbill=$(expr $breadprice \* $breadquantity + $butterprice \* $butterquantity)
echo $totalbill

