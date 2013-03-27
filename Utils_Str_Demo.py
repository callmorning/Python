#isEmpty
def isEmpty(Str=None):
    if Str == None:
        return True
    elif isinstance(Str, str):
        Str = Str.strip()
        if len(Str) == 0:
            return True
        else :
            return False
    else :
        return None

#isNotEmpty
def isNotEmpty(Str=None):
    if Str == None:
        return False
    elif isinstance(Str, str):
        Str = Str.strip()
        if len(Str) == 0:
            return False
        else :
            return True
    else :
        return None

#strip -> 去左右空格
def strip(Str=None):
    if isNotEmpty(Str):
        return Str.strip()
    else :
        return None

#is -> 引用相等
def isOneQuote(Str1=None, Str2=None):
    if isNotEmpty(Str1) and isNotEmpty(Str2):
        return Str1 is Str2
    else :
        return False

#equalHeap -> 值相等 去空格，忽略大小写
def idEqual(Str1=None, Str2=None, withOutStrip=False, withOutIgnoreCase=False):
    if isNotEmpty(Str1) and isNotEmpty(Str2):
        if withOutStrip:
            Str1 = strip(Str1)
            Str2 = strip(Str2)
            if withOutIgnoreCase:
                return Str1.lower() == Str2.lower()
            else :
                return Str1 == Str2
        else :
            if withOutIgnoreCase:
                return Str1.lower() == Str2.lower()
            else :
                return Str1 == Str2
    else :
        return False

#indexOf -> 索引
def indexOf(Str=None, indexStr=None, startPos=0, endPos=0):
    if isNotEmpty(Str):
        if not indexStr:
            return Str.indexStr(indexStr)
    return number

#contains -> 比较是否存在
def contains(Str=None, indexStr=None, ignoreCase=False):
    return True

#substring -> 截取
def subStr(Str=None, subFromStr=None, subToStr=None, start=None, end=None, length=None):
    return str

#split -> 分割
def subStr(Str=None, separatorChars=','):
    return [1,2,3,4]

#remove -> 移除
def remove(Str=None, removeStr=None):
    return str

#replace -> 替换

#repeat -> 重复
def repeat(Str=None, times=0):
    return str

#countMatches -> 计数
def countMatches(Str=None, sub=None):
    return int

#isNumeric -> 判断是否是数字
def isNumeric(Str=None):
    return True

# reverse -> 反序
def reverse(Str=None):
    a = "a"
    return str
