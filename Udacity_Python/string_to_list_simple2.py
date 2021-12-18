cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
cat_list = cat_string.split(', ')
cat_list = [cat.strip('--') for cat in cat_list]
print(cat_list)
"""
['Whiskers', 'Spot', 'Meowmeow', 'Tiger', 'Kitty', 'Henry', 'Mr.Paws']
"""
