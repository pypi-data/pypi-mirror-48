# GDSMerge
Tool for merging cells from multiple GDS files into a single GDS file.

## Install
```sh
git clone [this repo]
cd gdsmerge
python3 setup.py devel --user
```

## Example
```sh
gdsmerge -o /my/output.gds \
    -i ~/my/first/input.gds -i \
    ~/a/whole/directory/*.gds
```