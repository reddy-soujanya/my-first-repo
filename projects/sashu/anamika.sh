laptopprice=80
laptopquantity=20
computerprice=10
computerquantity=10
credit=20
totalbill=$(expr $laptopprice \* $laptopquantity + $computerprice \* $computerquantity - $credit)
echo $totalbill
