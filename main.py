
   ### 1. wyświetl nazwę systemu ✔️
    ### 2. wyświetl wersję systemu ✔️
    ### 3. wyświetl kernel ✔️
    ### 4. wyświetl architekturę CPU ✔️
    ### 5. zakończ program ❌
    ### 6. hostname ✔️
    ### 7. nazwa komputera ❌
    ### 8. ilość RAM ✔️
    ### 9. użycie RAM ✔️
    ### 10. CPU ✔️
    ### 11. liczba rdzeni ✔️
    ### 12. liczba wątków ✔️
    ### 13. dyski ❌
    ### 14. wolne miejsce ✔️
    ### 15. Ładnie sformatowany raport. ✔️

import platform
import os
import psutil
##########################################
##########################################
##########################################
def collect_system_info():
    os_info = platform.freedesktop_os_release()
    os_name = platform.system()
    kernel = platform.release()
    os_distribution = os_info['PRETTY_NAME']
    os_version = os_info['VERSION_ID']
    architecture = platform.machine()
    hostname = platform.node()
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    info_ram = psutil.virtual_memory()
    disk_info = psutil.disk_partitions(all=False)
    disk_usage = psutil.disk_usage('/')
    total_disk_space = disk_usage.total
    used_disk = disk_usage.used
    free_disk_space = disk_usage.free
    percent_disk_space = disk_usage.percent
    
    with open('/proc/cpuinfo', 'r') as cpu_file:
        for line in cpu_file:
            if "model name" in line:
                cpu_model = line.split(':', 1)[1].strip()
                break
            
    system_info={
          "OS Name" : os_name,
          "Kernel" : kernel,
          "OS Distribution" : os_distribution,
          "OS Version" : os_version,
          "Architecture" : architecture,
          "Hostname" : hostname,
          "CPU Model" : cpu_model,
          "Physical Cores" : physical_cores,
          "Logical Cores" : logical_cores,
          "Total RAM" : info_ram.total,
          "Available RAM" : info_ram.available,
          "Percent RAM" : info_ram.percent,
          "Disk Info" : disk_info,
          "Total Disk Space" : total_disk_space,
          "Free Disk Space" : free_disk_space,
          "Used Disk Space" : used_disk,
          "Percent Disk Space" : percent_disk_space
          }
        
        
    
    return system_info
system_info = collect_system_info()

##########################################
##########################################
##########################################

def display_report(system_info):

    separator = 104*"="
    title = 41*"=" + " System Snapshot Tool " + 41*"="
    system_module = 47*"=" + "  SYSTEM  " + 47*"="
    cpu_module = 47*"=" + "   CPU    " + 47*"="
    ram_module = 47*"=" + "   RAM    " + 47*"="
    disk_module = 48*"=" + "  DISK  " + 48*"="
    print(title)
    print(separator)
    print(system_module)
    print(f"{'OS Name:':<25}{system_info["OS Name"]}")
    print(f"{'Kernel:':<25}{system_info["Kernel"]}")
    print(f"{'OS Distribution:':<25}{system_info["OS Distribution"]}")  #[LINUX]
    print(f"{'OS Version:':<25}{system_info["OS Version"]}")
    print(f"{'System Architecture:':<25}{system_info["Architecture"]}")
    print(f"{'Hostname:':<25}{system_info["Hostname"]}")
    print(cpu_module)
    print(f"{'CPU Model:':<25}{system_info["CPU Model"]}")
    print(f"{'Physical Cores:':<25}{system_info["Physical Cores"]}")
    print(f"{'Logical Processors:':<25}{system_info["Logical Cores"]}")
    print(separator)
    print(ram_module)
    print(f"{'Total RAM:':<25}{system_info["Total RAM"]/ (1024 ** 3):.2f} GiB")
    print(f"{'Available RAM:':<25}{system_info["Available RAM"] /(1024 ** 3):.2f} GiB")
    print(f"{'RAM Usage':<25}{system_info["Percent RAM"]:.2f}%")
    #print(f"{'Disk Info:':<25}{system_info['Disk Info']}")
    print(separator)
    print(disk_module)
    print(f"{'Total Disk Space:':<25}{system_info['Total Disk Space'] /(1024 **3):.2f} GiB")
    print(f"{"Free Disk Space:":<25}{system_info['Free Disk Space']/(1024 **3):.2f} GiB")
    print(f"{"Used Disk Space:":<25}{system_info['Used Disk Space']/(1024 **3):.2f} GiB")
    print(f"{"Used Disk Space Percent:":<25}{system_info['Percent Disk Space']:.2f}%")

display_report(system_info)

##########################################
##########################################
##########################################



