cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname) $(uname -r)"
echo "-------------------------------"
echo -e "\e[38;5;82mCPU => $((cpu/1000))'C\e[0m"
echo "-------------------------------"
