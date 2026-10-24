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

#separator = "=" * 70

#print(separator)
#print("System Info")
#print(separator)
#
#os_info = platform.freedesktop_os_release()


#print(f"{'OS Name:':<25}{platform.system()}")
#print(f"{'Kernel:':<25}{platform.release()}")
#print(f"{'OS Distribution:':<25}{os_info['PRETTY_NAME']}")  #[LINUX]
#print(f"{'Architecture:':<25}{platform.machine()}")
#print(f"{'Hostname:':<25}{platform.node()}")
#
#print(separator)


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

print(system_info)
print(system_info["Hostname"])