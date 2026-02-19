To build resources quickly, you can do these two commands:

```
cd package
python package.py ../lzh/resources
```

Note that the output directory is `../versions/prereleases`. However, once if you fork this respo, you'll find that this directory isn't exist because it was ignored by git. So if you want to build this pack, you should create a folder named prereleases yourself or you can edit the output directory manually. 