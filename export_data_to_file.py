# Export data to file
# Notice: All inputs are hexadecimal
# https://github.com/qux-bbb/ghidra-scripts
# @author qux-bbb
# @category export
# @keybinding
# @menupath Tools.Export Data To File
# @toolbar

choice = askChoice(
    "Export data to file",
    "method",
    [
        "1. start_addr, data_len",
        "2. start_addr, end_addr",
        "3. current_addr, data_len",
        "4. current_addr, end_addr",
        "5. selected data",
    ],
    "1. start_addr, data_len",
)

if choice == "1. start_addr, data_len":
    data_start = askAddress("start_addr", "Data start address(hex)")
    data_len = int(askString("data_len", "Data length(hex)"), 16)
elif choice == "2. start_addr, end_addr":
    data_start = askAddress("start_addr", "Data start address(hex)")
    data_end = askAddress("end_addr", "Data end address(hex)")
    data_len = data_end.getOffset() - data_start.getOffset()
elif choice == "3. current_addr, data_len":
    data_start = currentAddress
    data_len = int(askString("data_len", "Data length(hex)"), 16)
elif choice == "4. current_addr, end_addr":
    data_start = currentAddress
    data_end = askAddress("end_addr", "Data end address(hex)")
    data_len = data_end.getOffset() - data_start.getOffset()
elif choice == "5. selected data":
    data_start = currentSelection.getMinAddress()
    data_end = currentSelection.getMaxAddress()
    data_len = data_end.getOffset() - data_start.getOffset() + 1
else:
    # No this choice
    exit(1)

filepath = askFile("file_path", "Save data").absolutePath


data = getBytes(data_start, data_len)

the_file = open(filepath, "wb")
the_file.write(data)
the_file.close()
