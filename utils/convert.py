import numpy


def is_not_nan(num): return num == num


def is_nan(num): return num != num


# convert any_to_int
def any_to_int(number):
    if is_nan(number):
        return '0'
    elif type(number).__name__ == 'float64':
        number_ = int(number)
        return number_
    elif type(number).__name__ == 'numpy.float64':
        a = numpy.array(number, dtype=numpy.float64)
        number_ = a.astype(numpy.int64)
        return number_
    elif type(number).__name__ == 'numpy.int64':
        a = numpy.int64(number)
        number_ = a.item()
        return number_
    elif type(number).__name__ == 'int64':
        a = numpy.int64(number)
        number_ = a.item()
        return number_
    else:
        return "problem with excel format conversion"


# convert any_to_str
def any_to_str(var):
    if type(var).__name__ == 'str': return var
    if is_nan(var):
        return ''
    if type(var).__name__ == 'float64':
        var_ = str(round(var))
        resultvar = var_.strip(' ')
        return resultvar
    if type(var).__name__ == 'int':
        var_ = str(var)
        resultvar = var_.strip(' ')
        return resultvar


# get digits only from str
def digits(string_):
    result_list = [n for n in string_ if n in '0123456789']
    result_ = ''.join(result_list)
    result2 = str(result_)
    return result2
