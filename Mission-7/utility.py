import search

filename = input ("Spécifiez le nom de fichier: ")
index = search.create_index ( filename )
while True:
  words = input ("Spécifiez les mots a rechercher, en utilisant des espaces entre les mots: ")
  lines = search.get_lines ( words.strip().split(), index )
  print("Les mots se retrouvent dans ces lignes:")
  for line in lines:
    print(line)