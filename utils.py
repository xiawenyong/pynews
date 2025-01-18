def add(a, b):
    """返回两个数的和"""
    return a + b

def subtract(a, b):
    """返回两个数的差"""
    return a - b

def multiply(a, b):
    """返回两个数的积"""
    return a * b

def divide(a, b):
    """返回两个数的商"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

if __name__ == "__main__":
    print(add(3, 5))
