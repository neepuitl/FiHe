# 文件帮助器
文件帮助器主要是协助你自动化处理大批量文件，例如文件去重和图片处理。

目前支持: 

- **文件去重**：自动移除目录下的重复文件到目标目录。
- **图片处理**: 将图片文件转换成base64字符串，或者压缩图片等。

## 1. 环境
> 编译器 >= `Python3.6`

> 包管理工具 >= `pip3`

## 2. 安装
> python3 setup.py install

## 3. 用法
### 3.1. 帮助
> fihe -h

### 3.2. 文件去重
- 查看重复文件

    > fihe dedu ls --root-dir="<absolute_root_dir>"
    
    **注意**：`root-dir`是你查看重复文件的根目录。

- 去除重复文件
    
    > fihe dedu rm --root-dir="<absolute_root_dir>" --target-dir="<absolute_target_dir>"
    
    **注意**：`root-dir`是你将要进行文件去重复的目录，`target-dir`是重复文件将要移动到的目标目录。

### 3.3. 图片处理
- 图片编码转换

    > fihe image its --file-path="<absolute_file_path>"

    **注意**：`file-path`是你将要进行编码转换的图片地址。

- 压缩图片

    > fihe image ci --input="<absolute_file_path>" --quality="<quality>"
    **注意**：`input`是你将要进行压缩的图片地址，`quality`是压缩后的图片质量百分比，整数值范围`(0, 100]`。