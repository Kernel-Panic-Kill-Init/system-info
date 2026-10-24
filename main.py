    ### 1. wyświetl nazwę systemu ✔️
    ### 2. wyświetl wersję systemu ❌
    ### 3. wyświetl kernel ✔️
    ### 4. wyświetl architekturę CPU ❌
    ### 5. zakończ program ❌
    ### 6. hostname ✔️
    ### 7. nazwa komputera ❌
    ### 8. ilość RAM ❌
    ### 9. użycie RAM ❌
    ### 10. CPU ❌
    ### 11. liczba rdzeni ❌
    ### 12. liczba wątków ❌
    ### 13. dyski ❌
    ### 14. wolne miejsce ❌
    ### 15. Ładnie sformatowany raport. ❌

import platform
import os




def collect_system_info():
    os_info = platform.freedesktop_os_release()

    os_name = platform.system()
    kernel = platform.release()
    os_distribution = os_info['PRETTY_NAME']
    architecture = platform.machine()
    hostname = platform.node()

    system_info={
        "OS Name" : os_name,
        "Kernel" : kernel,
        "OS Distribution" : os_distribution,
        "Architecture" : architecture,
        "Hostname" : hostname,

    }
    return system_info

system_info = collect_system_info()



def display_report(system_info):
    separator = 104*"="
    title = 41*"=" + " System Snapshot Tool " + 41*"="
    print(title)
    print(f"{'OS Name:':<25}{system_info["OS Name"]}")
    print(f"{'Kernel:':<25}{system_info["Kernel"]}")
    print(f"{'OS Distribution:':<25}{system_info["OS Distribution"]}")  #[LINUX]
    print(f"{'System Architecture:':<25}{system_info["Architecture"]}")
    print(f"{'Hostname:':<25}{system_info["Hostname"]}")
    print(separator)

display_report(system_info)
