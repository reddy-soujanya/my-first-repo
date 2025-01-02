carrotprice=20
carrotquantity=10
beansprice=30
beansquantity=20
credit=40
totalbill=$(expr $carrotprice \* $carrotquantity + $beansprice \* $beansquantity - $credit)
echo $totalbill

