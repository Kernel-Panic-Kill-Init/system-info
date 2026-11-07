#System Snapshot Tool

System Snapshot Tool (SST) is a Python-based system diagnostics tool designed to collect, organize and present operating system and hardware information in a structured and readable format.

The project aims to provide a consistent overview of a computer's system configuration across different operating systems, while accounting for platform-specific differences in available information and collection methods.

Originally inspired by tools such as neofetch, SST is being developed towards a more structured diagnostic utility with future support for saving and comparing system snapshots.

##Project Goals

- Collect relevant operating system and hardware information.
- Provide a consistent information structure across supported platforms.
- Handle platform-specific differences and unavailable information gracefully.
- Present collected data in a clear and readable format.
- Provide a foundation for saving and comparing system snapshots.
- Maintain a modular and extensible architecture.

##Supported Platforms

Cross-platform compatibility is one of the main design goals of this project.

###The planned target platforms are:

- Linux
- Windows
- macOS
- Android

*Platform support is being implemented and verified progressively. Feature availability may vary depending on the operating system, hardware, permissions and available system interfaces.*

##Current Features

The current implementation provides the following functionality:

###System Information

- Operating system identification
- Kernel identification
- Linux distribution identification
- Operating system version retrieval
- System architecture detection
- Hostname retrieval

###CPU Information

- CPU model identification
- Physical core count
- Logical processor count

###Memory Information

- Total RAM
- Available RAM
- RAM usage percentage

###Storage Information

- Total disk space
- Used disk space
- Available disk space
- Storage usage percentage

*Storage information currently covers the root filesystem ("/"). Individual disk and partition reporting is planned for future development*.

###Report Generation

- Structured terminal output
- Information grouped into dedicated sections:
  - System
  - CPU
  - RAM
  - Disk
- Human-readable memory and storage values

###Technologies

- Python 3.12+
- "platform" – operating system and system information
- "psutil" – CPU, memory and storage information
- Standard Python libraries

**Requirements**
>- Python 3.12 or newer
>- "psutil"

**Install the required dependency:**

>python3 -m pip install psutil

###Usage

**Clone the repository:**

>git clone https://github.com/Kernel-Panic-Kill-Init/system-info.git
>cd system-info

**Run the application:**

>python3 main.py


###Project Architecture and Development Direction

SST is intended to use a modular approach that separates system information collection from data presentation.

###The long-term design focuses on:

- Platform-specific information collection.
- Consistent data structures regardless of the operating system.
- Separation of collection logic and presentation logic.
- Graceful handling of unavailable or unsupported information.
- Extensibility for future output formats and interfaces.

**Planned Features**

- Expanded CPU and hardware information.
- Individual disk and partition identification.
- Device and computer identification.
- Improved error handling and fallback mechanisms.
- Verified Windows, macOS and Android support.
- Structured snapshot storage.
- Snapshot comparison to identify configuration and measurement changes.
- Additional output formats.
- Graphical user interface.

**Current Limitations**

- The current implementation relies on Linux-specific interfaces, including "/proc/cpuinfo" and "platform.freedesktop_os_release()".
- CPU model detection currently uses "/proc/cpuinfo".
- Storage usage currently reports the root filesystem ("/") rather than all available disks and partitions.
- Cross-platform collectors and platform-specific fallback mechanisms are still under development.
- Snapshot storage and comparison are not implemented yet.

**License**

*This project is licensed under the MIT License. See the "LICENSE" (LICENSE) file for details.*

**Project Status**

Work in progress.

System Snapshot Tool is an actively developed personal project. Features, platform compatibility and architectural improvements are introduced progressively and documented according to their implementation status.


*Ale tam, gdzie stanął Adanos, ani Innos, ani Beliar nie mieli żadnej władzy*
