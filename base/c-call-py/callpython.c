#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
 
 
int main(int argc,char **argv)
{
    //初始化，载入python的扩展模块
    Py_Initialize();
    //判断初始化是否成功
    if(!Py_IsInitialized())
    {
        printf("Python init failed!\n");
        return -1;
    }
    //PyRun_SimpleString 为宏，执行一段python代码
    //导入当前路径
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
 
    PyObject *pName = NULL;
    PyObject *pModule = NULL;
    PyObject *pDict = NULL;
    PyObject *pFunc = NULL;
    PyObject *pArgs = NULL;
 
    //加载名为py_add的python脚本
    pName = PyString_FromString("py_add");
    pModule = PyImport_Import(pName);
    if(!pModule)
    {
        printf("Load py_add.py failed!\n");
        getchar();
        return -1;
    }
	
	//获取模块字典属性
    pDict = PyModule_GetDict(pModule);
    if(!pDict)
    {
        printf("Can't find dict in py_add!\n");
        return -1;
    }
     
	//通过字典获取模块中的类
    pFunc = PyDict_GetItemString(pDict,"add");
    if(!pFunc || !PyCallable_Check(pFunc))
    {
        printf("Can't find function!\n");
        getchar();
        return -1;
    }
    /*
    向Python传参数是以元组（tuple）的方式传过去的，
    因此我们实际上就是构造一个合适的Python元组就
    可以了，要用到PyTuple_New，Py_BuildValue，PyTuple_SetItem等几个函数
    */
    pArgs = PyTuple_New(2);
    
    //  PyObject* Py_BuildValue(char *format, ...) 
    //  把C++的变量转换成一个Python对象。当需要从 
    //  C++传递变量到Python时，就会使用这个函数。此函数 
    //  有点类似C的printf，但格式不同。常用的格式有 
    //  s 表示字符串， 
    //  i 表示整型变量， 如Py_BuildValue("ii",123,456)
    //  f 表示浮点数， 
    //  O 表示一个Python对象
    PyTuple_SetItem(pArgs,0,Py_BuildValue("i",123));
    PyTuple_SetItem(pArgs,1,Py_BuildValue("i",321));
 
    //调用python的add函数
    PyObject_CallObject(pFunc,pArgs);
 
    //清理python对象
    if(pName)
    {
        Py_DECREF(pName);
    }
    if(pArgs)
    {
        Py_DECREF(pArgs);
    }
    if(pModule)
    {
        Py_DECREF(pModule);
    }
    
    //关闭python调用
    Py_Finalize();
 
    return 0;
    
}