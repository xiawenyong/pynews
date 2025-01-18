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
    try:
        print("add(3, 5) =", add(3, 5))
        print("subtract(3, 5) =", subtract(3, 5))
        print("multiply(3, 5) =", multiply(3, 5))
        print("divide(3, 5) =", divide(3, 5))
        print("divide(3, 0) =", divide(3, 0))  # 这行代码会引发异常，用于测试异常处理
    except Exception as e:
        print("Error:", e)
