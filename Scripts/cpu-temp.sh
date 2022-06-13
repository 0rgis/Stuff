cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
echo "\e[33m $(date) @ $(hostname) $(uname -r)\e[0m"
echo "\e[34m-------------------------------\e[0m"
echo "\e[38;5;82mCPU => $((cpu/1000))'C\e[0m"
echo "\e[34m-------------------------------"
