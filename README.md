TRACE: Trusted Return-Path Authentication via Context and Lightweight Encryption
TRACE is a lightweight control flow integrity (CFI) mechanism designed to defend against Return-Oriented Programming (ROP) attacks in embedded systems. TRACE dynamically binds return addresses to the unique function call path, making it difficult for attackers to hijack control flow by exploiting buffer overflows and other memory corruption vulnerabilities. This project uses the PRESENT cipher for lightweight encryption of return addresses and provides a defense mechanism that can be easily integrated with embedded applications.

--------------------------------------Project Structure--------------------------------------
The project contains the following components:

libmodbus-2.9.3/: This folder contains the Modbus protocol stack used for testing the vulnerabilities in embedded systems.

TRACE_CFI.py: The main defense script that provides the return-path authentication mechanism.

baseline.py: The baseline script with no defense mechanisms, used to test the system without protection for comparison.

canshu.txt: A configuration file that includes the encryption key and counter seed used in the defense mechanism.

scripts/: Contains the automation scripts.

automated_run.py: The automation script used to run experiments, either with or without defense.

exp.py: The exploit script used to perform the attack.

README.md: This file, containing the project documentation and instructions.

--------------------------------------Requirements--------------------------------------
GDB: GNU Debugger, used for running the target program and injecting the defense logic.

Python 3: Required for running the automation and attack scripts.

To install the necessary dependencies, you can run: sudo apt-get install gdb python3

--------------------------------------Setup and Running the Experiment--------------------------------------
1. Clone the repository:
git clone https://github.com/your_username/TRACE.git
cd TRACE

2. Configure the experiment:
In automated_run.py, set the ENABLE_TRACE variable to True or False to control whether the defense mechanism (TRACE) is enabled:
Enable Defense (TRACE):
Set ENABLE_TRACE = True to enable return-path authentication (TRACE defense mechanism)
Disable Defense (Baseline):
Set ENABLE_TRACE = False to run the experiment without any defense (baseline)

3. Running the experiment:
To run the experiment, simply execute the automation script automated_run.py. It will launch the target server, either with or without the TRACE defense, and execute the attack payload (exp.py):python3 scripts/automated_run.py
This will:
1.Start GDB with or without TRACE defense based on the ENABLE_TRACE setting.
2.Launch the unit-test-server program.
3.Wait for the attack payload (exp.py) to be executed.
4.If the attack is successful (i.e., control flow is hijacked), the experiment will execute shellcode.

--------------------------------------Attack Reproduction--------------------------------------
To reproduce the attack, the exploit script (exp.py) needs to be configured with the correct return address that points to the shellcode. Since the return address is highly dependent on the specific memory layout of the target system, you must replace the return address in the exp.py script with the address of the shellcode in your environment.
Modifying the Return Address in exp.py：
1.Identify the shellcode address:The shellcode address can be obtained by inspecting the memory layout of the target program. This is typically done by using GDB to inspect the memory.
2.Modify exp.py:In exp.py, locate the section where the return address is set (usually where the stack or buffer overflow is triggered). Replace the placeholder return address with the actual address of your shellcode.
3.Run the attack:python3 exp.py

--------------------------------------Important Notes--------------------------------------
Ensure that your shellcode is properly placed in memory and accessible at the specified address. This may require debugging and analysis using GDB.

The exact method for obtaining the return address will depend on the target system, so memory inspection tools like GDB are essential.

The address you use must be aligned with the specific layout of the program being tested, including any stack adjustments or randomization mechanisms in place.

--------------------------------------How the Defense Works--------------------------------------
The TRACE defense mechanism uses a dynamic path-sensitive approach to bind the return address to a unique function call path. This is achieved by:

1.Path state encoding: The current execution path is encoded using a state vector that is updated during function calls.
2.Encryption: The return address and its path context are encrypted using the PRESENT cipher.
3.Return address verification: Upon returning from a function, the integrity of the return address is verified by decrypting it and comparing it with the expected value.

If the return address does not match the expected value, the program execution is aborted, preventing the control flow hijacking.

--------------------------------------License--------------------------------------
This project is licensed under the MIT License - see the LICENSE file for details.








