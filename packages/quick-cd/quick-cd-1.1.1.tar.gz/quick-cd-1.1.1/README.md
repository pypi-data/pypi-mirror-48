# Quick cd
Quick cd is little tool allowing you to save any directory under a label, so you can quickly cd into it with out giving whole path.

## Instalation
```
pip install quick-cd
```

## Usage
To save current location under label "my_location" use  
```
qcd -c my_location
```

You can also, specify relative or absolute path, to save it instead of current directory.
```
qcd -c my_location ../different_dir
```
To cd into saved location, simply give label without any additional arguments
```
qcd my_location
```
To remove previously saved location use
```
qcd -d label
```
To list all saved locations
```
qcd -l
```
