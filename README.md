# Ghidra-Scripts

Script install method:  
Download script and put it to a folder for example: D:/ghidra_scripts/  
Window -> Bundle Manager, add the script folder  

You can find it in Window -> Script Manager.  
If a script contains valid `@menupath`, tick the checkbox, then you can execute script by menu item.  
You can also assign key binding for a script.  

## export_data_to_file.py
Export data to file, especially convenient for exporting big data.  
Notice: All inputs are hexadecimal.  
Example input:  
```r
start_addr 400000
data_len   1E00
```
[export_data_to_file.py](export_data_to_file.py)  
