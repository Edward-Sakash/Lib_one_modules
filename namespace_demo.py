global_var = "This is a global variable"

def outer_function():
    outer_var = "This is an outer variable"
    
    def inner_function():
        inner_var = "This is an inner variable"
        print("Inside inner_function:")
        print("global_var:", global_var)
        print("outer_var:", outer_var)
        print("inner_var:", inner_var)
    
    print("Inside outer_function:")
    print("global_var:", global_var)
    print("outer_var:", outer_var)
    inner_function()

def nonlocal_demo():
    outer_count = 10
    
    def inner_increment():
        nonlocal outer_count  # Declare that we're using the outer_count variable from the outer scope
        inner_count = 5
        print("Before increment:")
        print("outer_count:", outer_count)
        print("inner_count:", inner_count)
        
        outer_count += 1
        inner_count += 1
        
        print("After increment:")
        print("outer_count:", outer_count)
        print("inner_count:", inner_count)
    
    inner_increment()

print("In global scope:")
print("global_var:", global_var)

outer_function()

print("Calling nonlocal_demo:")
nonlocal_demo()
