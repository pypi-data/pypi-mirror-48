# xmind2Excel  
    xmind2Excel 是用来将xmind转为xmind的通用工具

## 最近更新
    初始发布...


    ############################
    Last update time: 2018-11-13 
    By： 8034.com

# 使用说明：
    1） 安装：
    pip install xmind2Excel
    2） 执行
    Python -c "from xmind2Excel.main import  Main; Main()" 
    3） 按模板xmind格式要求，编写用例
    4） 运行工具，把xmind转化为xls、xlsx格式的文件

    注： 为方便后期操作方便 
    可以 把上面的 运行命令放到bat或shell文件中，下次直接双击运行 

########################################################
# 源码打包
    ## 打包 检查
    python setup.py check 
    ## 打包 生成
    python setup.py sdist
    ## 上传
    twine upload dist/*
    ## 使用
    pip install xmind2Excel 
    ## 更新
    pip install --upgrade xmind2Excel
    ## 卸载
    pip uninstall -y xmind2Excel 

########################################################

## MANIFEST.in 
    include pat1 pat2 ...   #include all files matching any of the listed patterns
    exclude pat1 pat2 ...   #exclude all files matching any of the listed patterns
    recursive-include dir pat1 pat2 ...  #include all files under dir matching any of the listed patterns
    recursive-exclude dir pat1 pat2 ... #exclude all files under dir matching any of the listed patterns
    global-include pat1 pat2 ...    #include all files anywhere in the source tree matching — & any of the listed patterns
    global-exclude pat1 pat2 ...    #exclude all files anywhere in the source tree matching — & any of the listed patterns
    prune dir   #exclude all files under dir
    graft dir   #include all files under dir
