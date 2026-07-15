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

#print("OS Name:", platform.system())
#print("OS Version:", platform.version())

separator = "=" * 70

print(separator)
print("System Info")
print(separator)


print(f"{'OS Name:':<15}{platform.system()}")
print(f"{'OS Version:':<15}{platform.release()}")
print(f"{'Architecture:':<15}{platform.machine()}")
print(f"{'Hostname:':<15}{platform.node()}")
print(separator)