# -*- coding: utf-8 -*-
html = []
html.append('<!DOCTYPE html><html lang="pt"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Mini Mateuzinho</title><style>')
html.append('*{margin:0;padding:0;box-sizing:border-box}body{background:#0a0a1a;color:#fff;font-family:sans-serif;min-height:100vh;display:flex;justify-content:center;align-items:center}.hidden{display:none!important}')
html.append('.card{background:#1a1a3e;border-radius:20px;padding:30px;text-align:center;max-width:400px;border:1px solid rgba(255,107,157,.3)}')
html.append('h1{font-size:1.8em;background:linear-gradient(45deg,#ff6b9d,#c44dff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:10px 0}')
html.append('.btn{display:block;width:100%;padding:14px;margin:8px 0;border-radius:15px;border:none;cursor:pointer;font-size:1em;color:#fff}')
html.append('.btn-pink{background:rgba(255,107,157,.2);border:2px solid #ff6b9d}.btn-pink:hover{background:rgba(255,107,157,.4)}')
html.append('.btn-purple{background:rgba(196,77,255,.2);border:2px solid #c44dff}.btn-purple:hover{background:rgba(196,77,255,.4)}')
html.append('.btn-green{background:#25d366;margin-top:15px;font-weight:bold;animation:glow 2s infinite}')
html.append('@keyframes glow{0%,100%{box-shadow:0 0 10px rgba(37,211,102,.3)}50%{box-shadow:0 0 25px rgba(37,211,102,.6)}}')
html.append('.chat{position:fixed;top:0;left:0;width:100%;height:100%;background:#0a0a1a;display:flex;flex-direction:column}')
html.append('.chat-msgs{flex:1;overflow-y:auto;padding:15px;display:flex;flex-direction:column;gap:8px}')
html.append('.msg{max-width:80%;padding:10px 14px;border-radius:16px;font-size:.85em;line-height:1.4}')
html.append('.msg.bot{background:#1a1a3e;align-self:flex-start;border-left:3px solid #c44dff}')
html.append('.msg.user{background:linear-gradient(135deg,#ff6b9d,#c44dff);align-self:flex-end}')
html.append('.input-row{display:flex;gap:8px;padding:10px;background:#111133}')
html.append('.input-row input{flex:1;padding:10px;border-radius:20px;border:1px solid rgba(196,77,255,.3);background:#0d0d25;color:#fff;outline:none}')
html.append('.input-row button{background:linear-gradient(45deg,#ff6b9d,#c44dff);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer}')
html.append('.modal{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.85);z-index:200;display:flex;align-items:center;justify-content:center;padding:20px}')
html.append('.modal-card{background:#111133;border-radius:20px;padding:25px;text-align:center;max-width:400px;width:100%;border:2px solid #25d366;max-height:90vh;overflow-y:auto}')
html.append('.servico{display:block;width:100%;background:#25d366;color:#fff;border:none;padding:10px;border-radius:12px;cursor:pointer;margin:4px 0;font-size:.9em}')
html.append('.servico:hover{background:#128c7e}')
html.append('.admin-btn{background:transparent;border:none;color:#222;font-size:10px;margin-top:15px;cursor:default}')
html.append('</style></head><body>')
with open('c:/projetos/novoprojeto/mini.html','w',encoding='utf-8') as f:
    for l in html: f.write(l+'\n')
print("CSS+Head done")

f.write('''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Central Mini Mateuzinho</title><style>
*{margin:0;padding:0;box-sizing:border-box}body{font-family:Segoe UI,Tahoma,sans-serif;background:#0a0a1a;color:#fff;min-height:100vh;overflow-x:hidden}.hidden{display:none!important}
.particles-bg{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}
.particle{position:absolute;border-radius:50%;animation:floatUp 8s linear infinite;opacity:.3}
@keyframes floatUp{0%{transform:translateY(110vh) scale(0)}10%{opacity:.6}90%{opacity:.6}100%{transform:translateY(-10vh) scale(1.5);opacity:0}}
.portal{display:flex;justify-content:center;align-items:center;min-height:100vh;padding:20px;z-index:1}
.portal-card{background:linear-gradient(145deg,#1a1a3e,#0d0d2b);border:1px solid rgba(255,107,157,.3);border-radius:30px;padding:40px 30px;text-align:center;max-width:450px;box-shadow:0 0 80px rgba(138,43,226,.2);animation:fadeIn 1s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.portal-logo{font-size:60px;margin-bottom:10px}.portal-title{font-size:1.2em;color:#aaa;font-weight:300}
.portal-brand{font-size:2.5em;background:linear-gradient(45deg,#ff6b9d,#c44dff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:10px 0}
.portal-sub{color:#888;font-size:.9em;margin:15px 0}.portal-btns{display:flex;flex-direction:column;gap:12px}
.btn-client{display:flex;align-items:center;gap:12px;padding:18px 22px;border-radius:20px;border:none;cursor:pointer;text-align:left;transition:all .3s}
.btn-sasa{background:rgba(255,107,157,.15);border:2px solid #ff6b9d;color:#fff}.btn-sasa:hover{box-shadow:0 0 30px rgba(255,107,157,.4)}
.btn-kael{background:rgba(196,77,255,.15);border:2px solid #c44dff;color:#fff}.btn-kael:hover{box-shadow:0 0 30px rgba(196,77,255,.4)}
.btn-icon{font-size:2em;flex-shrink:0}.btn-label{flex:1;font-size:.95em}
''')
f.write('''.chat-screen{position:fixed;top:0;left:0;width:100%;height:100%;z-index:10;background:#0a0a1a;display:flex;flex-direction:column}
.chat-top{padding:12px 15px;background:#111133;border-bottom:1px solid rgba(255,107,157,.15);font-size:.85em;color:#aaa;flex-shrink:0;display:flex;justify-content:space-between}
.chat-top .online{color:#2ecc71}.chat-msgs{flex:1;overflow-y:auto;padding:15px;display:flex;flex-direction:column;gap:8px}
.msg{max-width:80%;padding:10px 14px;border-radius:16px;font-size:.85em;line-height:1.4;animation:slideIn .3s ease;word-wrap:break-word}
.msg.bot{background:#1a1a3e;color:#ddd;align-self:flex-start;border-bottom-left-radius:4px;border-left:3px solid #c44dff}
.msg.user{background:linear-gradient(135deg,#ff6b9d,#c44dff);color:#fff;align-self:flex-end;border-bottom-right-radius:4px}
@keyframes slideIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.typing{padding:8px 15px;color:#888;font-size:.75em;font-style:italic}
.dots span{animation:bounce 1.4s infinite;font-size:1.3em}.dots span:nth-child(2){animation-delay:.2s}.dots span:nth-child(3){animation-delay:.4s}
@keyframes bounce{0%,60%,100%{opacity:.3}30%{opacity:1}}
.chat-bottom{flex-shrink:0;background:#111133;padding:10px 12px}
.quick-btns{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
.qbtn{background:rgba(196,77,255,.12);border:1px solid rgba(196,77,255,.3);color:#c44dff;padding:7px 12px;border-radius:15px;cursor:pointer;font-size:.72em}.qbtn:hover{background:rgba(196,77,255,.25)}
.chat-input-row{display:flex;gap:6px;align-items:center}
.chat-input{flex:1;padding:10px 14px;border-radius:20px;border:1px solid rgba(196,77,255,.3);background:#0d0d25;color:#fff;outline:none;font-size:.85em}.chat-input:focus{border-color:#c44dff}
.btn-send{background:linear-gradient(45deg,#ff6b9d,#c44dff);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:1em;flex-shrink:0}
.btn-humano{width:100%;margin-top:6px;background:linear-gradient(135deg,#25d366,#128c7e);border:none;color:#fff;padding:10px;border-radius:15px;cursor:pointer;font-size:.78em;font-weight:bold;animation:glow 2s infinite}
@keyframes glow{0%,100%{box-shadow:0 0 8px rgba(37,211,102,.3)}50%{box-shadow:0 0 20px rgba(37,211,102,.6)}}
.btn-voltar{width:100%;margin-top:4px;background:rgba(255,0,0,.1);border:1px solid rgba(255,0,0,.3);color:#f66;padding:8px;border-radius:12px;cursor:pointer;font-size:.7em}
.games-area{padding:10px 15px;background:#0d0d25;border-top:1px solid rgba(196,77,255,.15);display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0}
.game-btn{background:rgba(255,107,157,.15);border:1px solid #ff6b9d;color:#ff6b9d;padding:6px 12px;border-radius:12px;cursor:pointer;font-size:.7em}.game-btn:hover{background:rgba(255,107,157,.3)}
.game-popup{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.85);z-index:200;display:flex;align-items:center;justify-content:center;padding:20px}
.game-card{background:#111133;border-radius:20px;padding:25px;text-align:center;max-width:380px;width:100%;border:1px solid rgba(196,77,255,.3);animation:pop .4s ease;max-height:80vh;overflow-y:auto}
@keyframes pop{from{transform:scale(.8);opacity:0}to{transform:scale(1);opacity:1}}
.board{display:grid;grid-template-columns:repeat(3,60px);gap:4px;justify-content:center;margin:10px 0}
.cell{width:60px;height:60px;background:#0d0d25;border:1px solid rgba(196,77,255,.3);border-radius:8px;font-size:1.5em;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff}.cell:hover{background:#1a1a3e}
.heart-area{position:relative;height:180px;background:#0d0d25;border-radius:10px;overflow:hidden;margin:10px 0}
.click-heart{position:absolute;font-size:32px;cursor:pointer;animation:pop .3s ease}
.mem-grid{display:grid;grid-template-columns:repeat(4,55px);gap:4px;justify-content:center;margin:10px 0}
.mem-card{width:55px;height:55px;background:linear-gradient(45deg,#ff6b9d,#c44dff);border-radius:8px;cursor:pointer;font-size:1.4em;display:flex;align-items:center;justify-content:center;color:#fff}
.mem-card.flipped{background:#fff;color:#333;border:2px solid #ff6b9d}.mem-card.matched{background:#2ecc71;pointer-events:none}
.quiz-opt{display:block;width:100%;background:#0d0d25;border:1px solid rgba(196,77,255,.3);color:#ccc;padding:8px;border-radius:12px;cursor:pointer;margin:4px 0;font-size:.8em}
.quiz-opt.correct{background:#2ecc71;color:#fff}.quiz-opt.wrong{background:#e74c3c;color:#fff}
.btn-close{background:rgba(255,0,0,.2);border:1px solid rgba(255,0,0,.4);color:#f66;padding:8px 20px;border-radius:15px;cursor:pointer;margin-top:10px}
.btn-sm{background:linear-gradient(45deg,#ff6b9d,#c44dff);color:#fff;border:none;padding:6px 14px;border-radius:12px;cursor:pointer;font-size:.75em;margin-top:8px}
.status{color:#c44dff;font-weight:bold;font-size:.8em;margin:6px 0}
.wp-modal{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.85);z-index:300;display:flex;align-items:center;justify-content:center;padding:20px}
.wp-card{background:#111133;border-radius:25px;padding:25px;text-align:center;max-width:400px;border:2px solid #25d366;animation:pop .5s ease;max-height:90vh;overflow-y:auto}
.servicos{display:flex;flex-direction:column;gap:6px;margin:12px 0}
.servico-btn{background:#25d366;color:#fff;border:none;padding:10px;border-radius:15px;cursor:pointer;font-size:.85em}.servico-btn:hover{background:#128c7e}
.btn-cancel{background:transparent;border:1px solid rgba(255,255,255,.2);color:#888;padding:8px 20px;border-radius:15px;cursor:pointer;font-size:.75em}
@media(min-width:600px){.chat-screen{max-width:450px;margin:0 auto;border-left:1px solid rgba(255,107,157,.2);border-right:1px solid rgba(255,107,157,.2)}}
</style>
''')
print("OK2")

print("OK1")

f.write('''</head><body>
<div class="particles-bg" id="bg"></div>
<div class="portal" id="portalScreen"><div class="portal-card">
<div class="portal-logo">🏢</div><h1 class="portal-title">Bem-vindo à Central de Ajuda</h1>
<h2 class="portal-brand">Mini Mateuzinho</h2><p class="portal-sub">Selecione seu perfil:</p>
<div class="portal-btns">
<button class="btn-client btn-sasa" onclick="entrar(\'sasa\')"><span class="btn-icon">🌸</span><span class="btn-label">Você é <b>mei mei</b>?<br><small>Clique aqui</small></span></button>
<button class="btn-client btn-kael" onclick="entrar(\'kael\')"><span class="btn-icon">✨</span><span class="btn-label">Você é <b>kael</b>?<br><small>Clique aqui</small></span></button>
</div><button onclick="abrirAdmin()" style="background:transparent;border:none;color:#222;font-size:10px;margin-top:20px">💜</button>
</div></div>
<div class="chat-screen hidden" id="chatScreen">
<div class="chat-top"><span id="chatTitle">💬 Central</span><span class="online">● Online</span></div>
<div class="chat-msgs" id="chatMsgs"></div>
<div class="typing hidden" id="typing">Mini Mateuzinho digitando<span class="dots"><span>.</span><span>.</span><span>.</span></span></div>
<div class="games-area"><button class="game-btn" onclick="abrirJogo(\'velha\')">🎯 Velha</button><button class="game-btn" onclick="abrirJogo(\'coracao\')">💗 Corações</button><button class="game-btn" onclick="abrirJogo(\'memoria\')">🧠 Memória</button><button class="game-btn" onclick="abrirJogo(\'quiz\')">💭 Quiz</button></div>
<div class="chat-bottom"><div class="quick-btns"><button class="qbtn" onclick="quick(\'Oi\')">💬 Oi</button><button class="qbtn" onclick="quick(\'Quero jogar!\')">🎮 Jogar</button><button class="qbtn" onclick="quick(\'Novidade!\')">✨ Novidade</button></div>
<div class="chat-input-row"><input class="chat-input" id="chatInput" placeholder="Digite..." onkeypress="if(event.key===\'Enter\')enviar()"><button class="btn-send" onclick="enviar()">➤</button></div>
f.write('''<div class="game-popup hidden" id="gamePopup"><div class="game-card" id="gameContent"></div></div>
<div class="wp-modal hidden" id="wpModal"><div class="wp-card">
<div style="font-size:45px">🤖➡️💜</div><h2>Conectando ao Mini Mateuzinho...</h2><p id="wpMsg"></p>
<div class="servicos" id="wpServicos"></div>
<div class="chat-msgs" id="humanoMsgs" style="max-height:180px;overflow-y:auto;margin:8px 0;text-align:left"></div>
<div class="chat-input-row"><input class="chat-input" id="humanoInput" placeholder="Digite..." onkeypress="if(event.key===\'Enter\')enviarHumano()"><button class="btn-send" onclick="enviarHumano()">➤</button></div>
<button class="btn-cancel" onclick="fecharWP()">Voltar ao bot</button></div></div>
<div class="wp-modal hidden" id="adminPanel"><div class="wp-card" style="border-color:#ff6b9d">
<div style="font-size:40px">💜</div><h2 style="color:#ff6b9d">Painel do Mateuzinho</h2>
<p style="color:#aaa;font-size:.75em">Cliente: <b id="adminCliente">---</b></p>
<div class="chat-msgs" id="adminMsgs" style="max-height:250px;overflow-y:auto;margin:10px 0;text-align:left;background:#0d0d25;border-radius:10px;padding:10px"></div>
<div class="chat-input-row"><input class="chat-input" id="adminInput" placeholder="Responder..." onkeypress="if(event.key===\'Enter\')enviarAdmin()"><button class="btn-send" onclick="enviarAdmin()">➤</button></div>
<button class="btn-cancel" onclick="fecharAdmin()">Fechar</button>
<button class="btn-cancel" onclick="limparChat()" style="margin-top:4px">🗑️ Limpar</button></div></div>
<script>
(function(){const c=["#ff6b9d","#c44dff","#ff9ff3","#54a0ff"];setInterval(()=>{const p=document.createElement("div");p.className="particle";p.style.left=Math.random()*100+"%";p.style.width=p.style.height=Math.random()*6+3+"px";p.style.background=c[Math.floor(Math.random()*4)];p.style.animationDuration=Math.random()*6+6+"s";document.getElementById("bg").appendChild(p);setTimeout(()=>p.remove(),10000)},400)})();
let cliente="";
function entrar(c){
cliente=c;document.getElementById("portalScreen").classList.add("hidden");
document.getElementById("chatScreen").classList.remove("hidden");
document.getElementById("chatTitle").textContent="💬 Central - "+c;
document.getElementById("chatMsgs").innerHTML="";typing(true);
setTimeout(()=>{typing(false);
if(c==="sasa"){addBot("Oii mei mei! 💖 Bem-vinda à <b>Central Mini Mateuzinho</b>! 🏢");
setTimeout(()=>addBot("Sou o Mini Mateuzinho! Pode falar comigo ou clicar no botão verde para falar comigo de verdade! 💚"),700)}
else{addBot("Oii kael! ✨ Bem-vinda à <b>Central Mini Mateuzinho</b>! 🏢");
setTimeout(()=>addBot("Sou o <b>robô</b> do Mini Mateuzinho 🤖... pode conversar à vontade!"),700);
setTimeout(()=>addBot("💡 <b>Quer falar com o Mini de verdade?</b> Clica no botão verde 📞!"),1400)}},1200)}
function voltar(){document.getElementById("chatScreen").classList.add("hidden");document.getElementById("portalScreen").classList.remove("hidden");document.getElementById("chatMsgs").innerHTML=""}
function addBot(m){const d=document.createElement("div");d.className="msg bot";d.innerHTML=m;document.getElementById("chatMsgs").appendChild(d);scrollMsgs()}
function addUser(m){const d=document.createElement("div");d.className="msg user";d.textContent=m;document.getElementById("chatMsgs").appendChild(d);scrollMsgs()}
function scrollMsgs(){const m=document.getElementById("chatMsgs");m.scrollTop=m.scrollHeight}
function typing(s){document.getElementById("typing").classList.toggle("hidden",!s)}
function enviar(){const i=document.getElementById("chatInput");const m=i.value.trim();if(!m)return;addUser(m);i.value="";typing(true);setTimeout(()=>{typing(false);addBot(responder(m))},800+Math.random()*1200)}
function quick(m){addUser(m);typing(true);setTimeout(()=>{typing(false);addBot(responder(m))},600+Math.random()*800)}
function responder(m){const t=m.toLowerCase();const ik=cliente==="kael";
if(t.includes("oi")||t.includes("ola"))return ik?"Oii kael! 💜 Sou o robô! Quer falar com o Mini de verdade? 📞":"Oii mei mei! 💖";
if(t.includes("tudo bem"))return ik?"Tudo ótimo! (robô 😄) Quer o Mini real? 📞":"Tudo ótimo! Melhor falando com você! 😊";
if(t.includes("amor")||t.includes("amo"))return ik?"O Mini real vai amar! Fala com ele no 📞!":"Awnn! Te amo demais! 💖";
if(t.includes("jogar")||t.includes("jogo"))return "Olha os joguinhos ali em cima! 🎯💗🧠💭";
if(t.includes("novidade"))return "Novidade: o Mini Mateuzinho quer falar com você! 💚 Clica no botão verde!";
if(t.includes("saudade"))return ik?"O Mini real também! Fala com ele! 🥺💚":"Também estou com saudade! 🥺💗";
if(t.includes("obrigad"))return ik?"Por nada! 🤖💜 (O Mini real agradece! 📞)":"Por nada! 🥰💜";
if(t.includes("beijo")||t.includes("bj"))return ik?"😘 O Mini real vai adorar! Chama ele! 💚":"Muitos beijinhos! 😘😘😘";
return ik?"Sou robô, tá? 🤖 Se quiser o Mini de verdade, clica no 📞 verde! 💜":"Pode falar o que quiser! 💜✨"}
''')
print("OK4")
f.write('''let chatHumano=[];
function salvarCH(){localStorage.setItem("ch_"+cliente,JSON.stringify(chatHumano))}
function carregarCH(){const d=localStorage.getItem("ch_"+cliente);if(d)chatHumano=JSON.parse(d);else chatHumano=[]}
function addMsgH(de,msg){chatHumano.push({de,msg,h:new Date().toLocaleTimeString()});salvarCH();renderHM();renderAM()}
function renderHM(){const e=document.getElementById("humanoMsgs");if(!e)return;e.innerHTML=chatHumano.map(m=>"<div class=\\"msg "+(m.de==="cliente"?"user":"bot")+"\\" style=\\"font-size:.72em\\"><b>"+(m.de==="cliente"?"Você":"Mateuzinho")+":</b> "+m.msg+"<br><small>"+m.h+"</small></div>").join("");e.scrollTop=e.scrollHeight}
function renderAM(){const e=document.getElementById("adminMsgs");if(!e)return;e.innerHTML=chatHumano.map(m=>"<div class=\\"msg "+(m.de==="cliente"?"user":"bot")+"\\" style=\\"font-size:.72em\\"><b>"+(m.de==="cliente"?"Cliente":"Você")+":</b> "+m.msg+"<br><small>"+m.h+"</small></div>").join("");e.scrollTop=e.scrollHeight}
function falaraComHumano(){document.getElementById("wpModal").classList.remove("hidden");document.getElementById("wpMsg").innerHTML="<b>Boa tarde! Me chamo Mini Mateuzinho das empresas Mini Mateuzinho, tuturututu! 🎵</b><br>Como podemos ajudar?";document.getElementById("wpServicos").innerHTML="<button class=servico-btn onclick=pedirServico(\\"Tiração de caucinha 🩰\\")>🩰 Tiração de caucinha</button><button class=servico-btn onclick=pedirServico(\\"Beijinho na boca 💋\\")>💋 Beijinho na boca</button><button class=servico-btn onclick=pedirServico(\\"Fuki fuki 🌬️\\")>🌬️ Fuki fuki</button><button class=servico-btn onclick=pedirServico(\\"Copo de água 💧\\")>💧 Copo de água</button>";carregarCH();renderHM();document.getElementById("humanoInput").value=""}
function pedirServico(s){document.getElementById("humanoInput").value=s;enviarHumano()}
function enviarHumano(){const i=document.getElementById("humanoInput");const m=i.value.trim();if(!m)return;addMsgH("cliente",m);i.value=""}
function fecharWP(){document.getElementById("wpModal").classList.add("hidden")}
function abrirAdmin(){document.getElementById("adminPanel").classList.remove("hidden");document.getElementById("adminCliente").textContent=cliente||"---";carregarCH();renderAM();setInterval(()=>{carregarCH();renderAM()},2000)}
function enviarAdmin(){const i=document.getElementById("adminInput");const m=i.value.trim();if(!m)return;addMsgH("mateuzinho",m);i.value=""}
function fecharAdmin(){document.getElementById("adminPanel").classList.add("hidden")}
function limparChat(){chatHumano=[];salvarCH();renderHM();renderAM()}
''')
print("OK5")


<button class="btn-humano" onclick="falaraComHumano()">📞 Falar com Mini Mateuzinho humano</button>
<button class="btn-voltar" onclick="voltar()">🚪 Sair</button></div></div>
f.write('''function abrirJogo(t){const g=document.getElementById("gameContent");document.getElementById("gamePopup").classList.remove("hidden");if(t==="velha"){g.innerHTML=vh();rv()}if(t==="coracao"){g.innerHTML=ch()}if(t==="memoria"){g.innerHTML=mh();im()}if(t==="quiz"){g.innerHTML=qh();nq()}}
function fecharJogo(){document.getElementById("gamePopup").classList.add("hidden")}
let vb=["","","","","","","","",""],vt="❤️",vo=false;
function vh(){return "<h3>🎯 Jogo da Velha</h3><div class=board>"+Array(9).fill().map((_,i)=>"<div class=cell onclick=jv("+i+")></div>").join("")+"</div><p class=status id=vs>Vez: ❤️</p><button class=btn-sm onclick=rv()>🔄</button> <button class=btn-close onclick=fecharJogo()>Fechar</button>"}
function jv(i){if(vo||vb[i]!=="")return;vb[i]=vt;rv2();const w=cv();if(w){document.getElementById("vs").textContent=w+" venceu!";vo=true;return}if(!vb.includes("")){document.getElementById("vs").textContent="Empate!";vo=true;return}vt=vt==="❤️"?"🌸":"❤️";document.getElementById("vs").textContent="Vez: "+vt}
function cv(){const w=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];for(const[a,b,c]of w)if(vb[a]&&vb[a]===vb[b]&&vb[a]===vb[c])return vb[a];return null}
function rv2(){document.querySelectorAll("#gameContent .cell").forEach((c,i)=>{c.textContent=vb[i]})}
function rv(){vb=["","","","","","","","",""];vt="❤️";vo=false;rv2();const s=document.getElementById("vs");if(s)s.textContent="Vez: ❤️"}
let ca=false,cc=0,ct=null;
function ch(){return "<h3>💗 Clique Corações</h3><div class=heart-area id=ha></div><p class=status id=hs>Corações: 0 | 15s</p><button class=btn-sm onclick=sc()>▶ Iniciar</button> <button class=btn-close onclick=fecharJogo()>Fechar</button>"}
function sc(){if(ca)return;ca=true;cc=0;let t=15;ct=setInterval(()=>{t--;document.getElementById("hs").textContent="Corações: "+cc+" | "+t+"s";if(t<=0){clearInterval(ct);ca=false;document.getElementById("hs").textContent="Fim! "+cc+" ❤️"}},1000);sp()}
function sp(){if(!ca)return;const a=document.getElementById("ha");const h=document.createElement("span");h.className="click-heart";h.textContent=["❤️","💕","💗","💖","💘"][Math.floor(Math.random()*5)];h.style.left=Math.random()*80+"%";h.style.top=Math.random()*70+"%";h.onclick=()=>{cc++;h.remove()};a.appendChild(h);setTimeout(()=>{if(h.parentNode)h.remove()},1500);if(ca)setTimeout(sp,Math.random()*500+300)}
let mc=[],mf=[],mm=0,ml=false;
function mh(){return "<h3>🧠 Memória</h3><div class=mem-grid id=mg></div><p class=status id=ms>Pares: 0/6</p><button class=btn-sm onclick=im()>🔄</button> <button class=btn-close onclick=fecharJogo()>Fechar</button>"}
function im(){const e=["❤️","🌸","💖","💕","✨","💗"];mc=[...e,...e].sort(()=>Math.random()-.5);mf=[];mm=0;ml=false;const g=document.getElementById("mg");if(!g)return;g.innerHTML="";mc.forEach((em,i)=>{const c=document.createElement("div");c.className="mem-card";c.textContent="?";c.onclick=()=>fm(c,i,em);g.appendChild(c)});const s=document.getElementById("ms");if(s)s.textContent="Pares: 0/6"}
function fm(card,i,em){if(ml||card.classList.contains("flipped")||card.classList.contains("matched"))return;card.classList.add("flipped");card.textContent=em;mf.push({card,em});if(mf.length===2){ml=true;const[a,b]=mf;if(a.em===b.em){a.card.classList.add("matched");b.card.classList.add("matched");mm++;const s=document.getElementById("ms");if(s)s.textContent="Pares: "+mm+"/6";mf=[];ml=false;if(mm===6&&s)s.textContent="🎉 Completou! 💑"}else{setTimeout(()=>{a.card.classList.remove("flipped");a.card.textContent="?";b.card.classList.remove("flipped");b.card.textContent="?";mf=[];ml=false},800)}}}
let qs=0;const qq=[{q:"Apelido que o Mini mais usa?",o:["mei mei","amor","vida","fofa"],a:0},{q:"O que ele mais gosta?",o:["Games","Filme","Tudo junto!","Dormir"],a:2},{q:"Ele te ama?",o:["Sim","Muito","Demais","Infinitamente!!!"],a:3}];
function qh(){return "<h3>💭 Quiz</h3><p id=qq></p><div id=qo></div><p class=status id=qs2>Pontos: 0</p><button class=btn-close onclick=fecharJogo()>Fechar</button>"}
function nq(){const q=qq[Math.floor(Math.random()*3)];document.getElementById("qq").textContent=q.q;const o=document.getElementById("qo");o.innerHTML="";q.o.forEach((opt,i)=>{const b=document.createElement("button");b.className="quiz-opt";b.textContent=opt;b.onclick=()=>{Array.from(o.children).forEach(x=>x.style.pointerEvents="none");if(i===q.a){b.classList.add("correct");qs++;document.getElementById("qs2").textContent="Pontos: "+qs}else{b.classList.add("wrong");o.children[q.a].classList.add("correct")}setTimeout(nq,1500)};o.appendChild(b)})}
</script></body></html>''')
f.close()
print("ARQUIVO GERADO COM SUCESSO!")

''')
print("OK3")
