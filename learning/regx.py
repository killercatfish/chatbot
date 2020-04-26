text = 'GameIsOver -> Flabby Daddy (index #) something else'

new_text = text.replace('GameIsOver -> ', '')
end_name = new_text.index('(')
name = new_text[:end_name]

print(name)