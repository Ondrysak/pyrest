FAIL=0

for i in $(seq $1); do  
./test06.sh &
pidlist="$pidlist $!" 
done

for job in $pidlist; do 
  echo $job     
  wait $job || let "FAIL+=1";
done  



if [ "$FAIL" == "0" ]; then 
  echo "YAY!" 
else 
  echo "FAIL! ($FAIL)" 
fi