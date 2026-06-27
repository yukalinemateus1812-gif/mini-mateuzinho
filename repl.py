f=open("c:/projetos/novoprojeto/amor.html",encoding="utf-8")
c=f.read();f.close()
r={"[HEART]":"❤️","[HEART2]":"💕","[HEART3]":"💗","[HEART4]":"💖","[SPARKLE]":"✨","[FLOWER]":"🌸","[BUILDING]":"🏢","[CHAT]":"💬","[DOT]":"●","[ARROW]":"➤","[PHONE]":"📞","[DOOR]":"🚪","[GREENHEART]":"💚","[IDEA]":"💡","[ROBOT]":"🤖","[STAR]":"🌟","[KISS]":"💋","[MUSIC]":"🎵","[SHOES]":"🩰","[WIND]":"🌬️","[DROP]":"💧","[HUG]":"🤗","[HAIR]":"💆","[TICTACTOE]":"🎯","[HEARTS]":"💗","[BRAIN]":"🧠","[QUIZ]":"💭","[PARTY]":"🎉","[HAND]":"🤝","[TRASH]":"🗑️"}
for k,v in r.items():c=c.replace(k,v)
f=open("c:/projetos/novoprojeto/amor.html","w",encoding="utf-8")
f.write(c);f.close()
print("EMOJIS OK")
