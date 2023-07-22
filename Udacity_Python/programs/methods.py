greeting = "Hello world! "
 
greeting.find('lo')   # 3 (-1 if not found)
greeting.replace('llo', 'y')  # => "Hey world!"
greeting.startswith('Hell')  # => True
greeting.isalpha()           # => False (due to '!')
 
greeting.lower()  # => "hello world! "
greeting.title()  # => "Hello World! "
greeting.upper()  # => "HELLO WORLD! "
 
greeting.strip()  # => "Hello world!"
greeting.strip('dH !')  # => "ello worl"
 
