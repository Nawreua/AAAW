gamedata = ""

with open('another_astonishingly_anguished_.bitsy', 'r') as file:
    gamedata = file.read()
    gamedata = gamedata.replace('Another Astonishingly Anguished Worker',
'''"""
Another Astonishingly Anguished Worker
By Nawreua
Live your life to the fullest !
But for 20 seconds ! (js "setTimeout(function() { window.location.reload(); }, 20000);")
"""''')

with open('index_to_process.html', 'r') as file:
    filedata = file.read()

    filedata = filedata.replace('[gamedata]', gamedata)

    with open('index.html', 'w') as index:
        index.write(filedata)