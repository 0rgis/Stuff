cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname) $(uname -r)"
echo "-------------------------------"
echo "CPU => $((cpu/1000))'C"
