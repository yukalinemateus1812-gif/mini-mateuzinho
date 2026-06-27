// ===== PARTÍCULAS DE FUNDO =====
(function(){
    const bg=document.getElementById('particlesBg');
    const colors=['#ff6b9d','#c44dff','#ff9ff3','#54a0ff','#ff6b6b'];
    setInterval(()=>{
        const p=document.createElement('div');
        p.className='particle';
        p.style.left=Math.random()*100+'%';
        p.style.width=p.style.height=Math.random()*8+3+'px';
        p.style.background=colors[Math.floor(Math.random()*colors.length)];
        p.style.animationDuration=Math.random()*6+6+'s';
        bg.appendChild(p);
        setTimeout(()=>p.remove(),10000);
    },300);
})();

let currentClient='';

// ===== ENTRAR NO CHAT =====
function enterChat(client){
    currentClient=client;
    document.getElementById('portalScreen').classList.add('hidden');
    document.getElementById('chatScreen').classList.remove('hidden');
    document.getElementById('clientName').textContent=client==='sasa'?'🌸 sasa':'✨ kael';
    document.getElementById('sidebarClient').querySelector('strong').textContent=client==='sasa'?'sasa':'kael';
    document.getElementById('chatMessages').innerHTML='';
    showTyping();
    setTimeout(()=>{
        hideTyping();
        addBotMsg(`Bem-vinda à <strong>Empresas Super Mini Mateuzinho</strong>! 💼✨`);
        setTimeout(()=>{
            if(client==='sasa'){
                addBotMsg(`Oii sasa! Que bom ter você aqui! 💖 Já sabe como funciona, né? Sou o Mini Mateuzinho e estou 100% dedicado a você! O que deseja hoje? 🥰`);
                setTimeout(()=>addBotMsg(`Use os botões abaixo ou digite o que quiser! E se precisar de mim de verdade, é só clicar no botão verde ali na esquerda 📞💚`),800);
            }else{
                addBotMsg(`Oii kael! Tudo bem com você? ✨`);
                setTimeout(()=>{
                    addBotMsg(`Só pra te avisar: <strong>este é um Mini Mateuzinho robô</strong> 🤖... eu respondo automaticamente, tá? Mas fique à vontade pra conversar e explorar!`);
                    setTimeout(()=>{
                        addBotMsg(`💡 <strong>Gostaria de conversar com o Mini Mateuzinho de verdade?</strong> É só clicar no botão verde <strong>"📞 Falar com Mini Mateuzinho (humano)"</strong> ali na esquerda! Ele vai te atender pessoalmente! 💚`);
                    },1000);
                },600);
            }
        },600);
    },1500);
}

// ===== VOLTAR AO PORTAL =====
function voltarPortal(){
    document.getElementById('chatScreen').classList.add('hidden');
    document.getElementById('portalScreen').classList.remove('hidden');
    document.getElementById('chatMessages').innerHTML='';
}

// ===== CHAT =====
function addBotMsg(msg){
    const d=document.createElement('div');
    d.className='chat-msg bot';
    d.innerHTML=msg;
    document.getElementById('chatMessages').appendChild(d);
    scrollChat();
}

function addUserMsg(msg){
    const d=document.createElement('div');
    d.className='chat-msg user';
    d.textContent=msg;
    document.getElementById('chatMessages').appendChild(d);
    scrollChat();
}

function scrollChat(){
    const m=document.getElementById('chatMessages');
    m.scrollTop=m.scrollHeight;
}

function showTyping(){
    document.getElementById('typingIndicator').classList.remove('hidden');
}

function hideTyping(){
    document.getElementById('typingIndicator').classList.add('hidden');
}

function handleChatEnter(e){
    if(e.key==='Enter')sendMessage();
}

function sendMessage(){
    const input=document.getElementById('chatInput');
    const msg=input.value.trim();
    if(!msg)return;
    addUserMsg(msg);
    input.value='';
    showTyping();
    setTimeout(()=>{
        hideTyping();
        const r=getSmartResponse(msg);
        addBotMsg(r);
    },1000+Math.random()*1500);
}

function sendQuickEmoji(emoji){
    addUserMsg(emoji);
    showTyping();
    setTimeout(()=>{hideTyping();addBotMsg(getEmojiResponse(emoji));},600);
}
// ===== QUICK REPLIES =====
function sendQuickReply(msg){
    addUserMsg(msg);
    showTyping();
    setTimeout(()=>{
        hideTyping();
        const r=getSmartResponse(msg);
        addBotMsg(r);
    },800+Math.random()*1000);
}

// ===== FALAR COM HUMANO =====
function chamarHumano(){
    addBotMsg('🔔 <strong>Mini Mateuzinho</strong> será notificado! Conectando você ao atendimento humano... 💜');
    document.getElementById('whatsappModal').classList.remove('hidden');
    // Configura o link do WhatsApp - ALTERE AQUI SEU NÚMERO:
    const numero='5547997457157'; // Mateuzinho
    const msg=encodeURIComponent('Oi Mini Mateuzinho! Vim pela Central de Ajuda 💜');
    document.getElementById('btnWhatsApp').onclick=()=>{
        window.open('https://wa.me/'+numero+'?text='+msg,'_blank');
    };
}

function abrirWhatsApp(){
    const numero='5547997457157'; // Mateuzinho
    const msg=encodeURIComponent('Oi Mini Mateuzinho! Vim pela Central de Ajuda 💜');
    window.open('https://wa.me/'+numero+'?text='+msg,'_blank');
    fecharWhatsAppModal();
}

function fecharWhatsAppModal(){
    document.getElementById('whatsappModal').classList.add('hidden');
}
    setTimeout(()=>{
        hideTyping();
        addBotMsg(getEmojiResponse(emoji));
    },600);
}

function getEmojiResponse(emoji){
    if(emoji==='❤️')return 'Awnnn! O Mini Mateuzinho também te ama! 💕💕💕';
    if(emoji==='🌸')return 'Que linda! Flores pra você também! 🌸🌷🌺🌻';
    if(emoji==='😊')return 'Seu sorriso ilumina tudo! 😊✨💫';
    return 'Que fofo! 💝';
}

function getSmartResponse(msg){
    const m=msg.toLowerCase();
    const isKael=currentClient==='kael';
    if(m.includes('oi')||m.includes('ola')||m.includes('olá'))
        return isKael?'Oii kael! 💜 Lembrando: sou o robô do Mini Mateuzinho! Quer falar com ele de verdade? Clica no botão verde 📞':'Oiiii sasa! Que bom ter você aqui! 💖';
    if(m.includes('tudo bem')||m.includes('como vai'))
        return isKael?'Tudo ótimo por aqui! (Mesmo sendo robô 😄) E você? Se quiser uma conversa mais real, chama o Mini Mateuzinho no botão verde! 💚':'Tudo ótimo! Ainda melhor agora falando com você! 😊 E você?';
    if(m.includes('amor')||m.includes('amo')||m.includes('te amo'))
        return isKael?'Awnn! 💖 O Mini Mateuzinho de verdade vai AMAR ouvir isso! Quer mandar pra ele pelo WhatsApp? Clica no 📞':'Awnn! O Mini Mateuzinho te ama demais, sasa! 💖💖💖';
    if(m.includes('saudade'))
        return isKael?'O Mini Mateuzinho também deve estar com saudade! Fala com ele pelo botão verde ali! 🥺💚':'Também estou com saudade! Mas agora estamos conectados! 🥺💗';
    if(m.includes('jogo')||m.includes('jogar')||m.includes('joguinhos'))
        return 'Ótima ideia! Clique em 🎮 Joguinhos ali no menu lateral pra gente se divertir! 🎯';
    if(m.includes('surpresa')||m.includes('presente'))
        return 'Temos surpresas especiais! Clique em 🎁 Surpresas no menu! ✨';
    if(m.includes('obrigad')||m.includes('brigad')||m.includes('valeu'))
        return isKael?'Por nada! 🤖💜 (Mas se quiser agradecer o Mini Mateuzinho pessoalmente, já sabe: 📞 botão verde!)':'Por nada, sasa! Estou sempre aqui pra você! 🥰💜';
    if(m.includes('lind')||m.includes('bonit'))
        return isKael?'Você é linda demais! ✨ O Mini Mateuzinho de verdade com certeza concorda! Quer ouvir dele? 📞💚':'Você que é a pessoa mais linda do universo, sasa! 🌟';
    if(m.includes('beijo')||m.includes('bj'))
        return isKael?'😘💋 O Mini Mateuzinho vai adorar receber esse beijo pessoalmente! Chama ele no WhatsApp! 💚':'Muitos beijinhos pra você! 😘😘😘💋';
    if(m.includes('humano')||m.includes('verdade')||m.includes('real')||m.includes('whatsapp'))
        return 'É só clicar no botão verde 📞 <strong>"Falar com Mini Mateuzinho (humano)"</strong> ali na esquerda! Ele vai te atender! 💚';
    return isKael?'Sou o robô do Mini Mateuzinho, tá? 🤖 Mas pode falar o que quiser! Se preferir falar com ele de verdade, clica no 📞 verde ali na esquerda! 💜':'Sou todo ouvidos, sasa! Pode falar o que quiser, estou aqui pra você! 💜✨';
}

// ===== NAVEGAÇÃO DE VIEWS =====
function showChatView(){
    document.getElementById('chatMainView').classList.remove('hidden');
    document.getElementById('gamesView').classList.add('hidden');
    document.getElementById('extrasView').classList.add('hidden');
    updateMenu('menuChat');
    scrollChat();
}

function showGamesView(){
    document.getElementById('chatMainView').classList.add('hidden');
    document.getElementById('gamesView').classList.remove('hidden');
    document.getElementById('extrasView').classList.add('hidden');
    updateMenu('menuGames');
    if(!window._memoryInit){initMemory();window._memoryInit=true;}
}

function showExtrasView(){
    document.getElementById('chatMainView').classList.add('hidden');
    document.getElementById('gamesView').classList.add('hidden');
    document.getElementById('extrasView').classList.remove('hidden');
    updateMenu('menuExtras');
// ===== JOGO DA VELHA =====
let tttBoard=['','','','','','','','',''],tttTurn='❤️',tttOver=false;
function makeMove(idx){
    if(tttOver||tttBoard[idx]!=='')return;
    tttBoard[idx]=tttTurn;renderBoard();
    const w=checkWinnerTTT();
    if(w){document.getElementById('tttStatus').textContent=w+' venceu! 🎉';tttOver=true;return;}
    if(!tttBoard.includes('')){document.getElementById('tttStatus').textContent='Empate! 🤝';tttOver=true;return;}
    tttTurn=tttTurn==='❤️'?'🌸':'❤️';
    document.getElementById('tttStatus').textContent='Vez do: '+tttTurn;
}
function checkWinnerTTT(){
    const wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    for(const[a,b,c]of wins){if(tttBoard[a]&&tttBoard[a]===tttBoard[b]&&tttBoard[a]===tttBoard[c])return tttBoard[a];}
    return null;
}
function renderBoard(){document.querySelectorAll('#board .cell').forEach((c,i)=>{c.textContent=tttBoard[i];});}
function resetTicTacToe(){tttBoard=['','','','','','','','',''];tttTurn='❤️';tttOver=false;renderBoard();document.getElementById('tttStatus').textContent='Vez do: ❤️';}

// ===== JOGO DE CORAÇÕES =====
let heartActive=false,heartClicks=0,heartTimer=null;
function startHeartGame(){
    if(heartActive)return;
    heartActive=true;heartClicks=0;
    document.getElementById('heartScore').textContent='Corações: 0 | Tempo: 15s';
    const area=document.getElementById('heartGameArea');
    area.querySelectorAll('.click-heart').forEach(h=>h.remove());
    let t=15;
    heartTimer=setInterval(()=>{t--;
        document.getElementById('heartScore').textContent='Corações: '+heartClicks+' | Tempo: '+t+'s';
        if(t<=0){clearInterval(heartTimer);heartActive=false;
            area.querySelectorAll('.click-heart').forEach(h=>h.remove());
            document.getElementById('heartScore').textContent='Fim! '+heartClicks+' corações! '+(heartClicks>=10?'Trabalho incrível! 💑':'🎉');}
    },1000);
    spawnHeart();
}
function spawnHeart(){
    if(!heartActive)return;
    const area=document.getElementById('heartGameArea');
    const h=document.createElement('span');h.className='click-heart';
    h.textContent=['❤️','💕','💗','💖','💘'][Math.floor(Math.random()*5)];
    h.style.left=Math.random()*80+'%';h.style.top=Math.random()*70+'%';
    h.onclick=()=>{heartClicks++;h.remove();};
    area.appendChild(h);
    setTimeout(()=>{if(h.parentNode)h.remove();},1500);
    if(heartActive)setTimeout(spawnHeart,Math.random()*600+400);
}

// ===== MEMÓRIA =====
let memoryCards=[],memoryFlipped=[],memoryMatched=0,memoryLocked=false;
function initMemory(){
    const emojis=['❤️','🌸','💖','💕','✨','💗'];
    memoryCards=[...emojis,...emojis].sort(()=>Math.random()-0.5);
    memoryFlipped=[];memoryMatched=0;memoryLocked=false;
    const board=document.getElementById('memoryBoard');board.innerHTML='';
    memoryCards.forEach((emoji,i)=>{
        const card=document.createElement('div');card.className='memory-card';
        card.dataset.index=i;card.dataset.emoji=emoji;card.textContent='?';
        card.onclick=()=>flipMemory(card,i);board.appendChild(card);
    });
    document.getElementById('memoryStatus').textContent='Pares: 0 / 6';
}
function flipMemory(card,idx){
    if(memoryLocked||card.classList.contains('flipped')||card.classList.contains('matched'))return;
    card.classList.add('flipped');card.textContent=memoryCards[idx];
    memoryFlipped.push({card,idx});
    if(memoryFlipped.length===2){memoryLocked=true;
        const[a,b]=memoryFlipped;
        if(a.card.dataset.emoji===b.card.dataset.emoji){
            a.card.classList.add('matched');b.card.classList.add('matched');memoryMatched++;
            document.getElementById('memoryStatus').textContent='Pares: '+memoryMatched+' / 6';
            memoryFlipped=[];memoryLocked=false;
            if(memoryMatched===6)document.getElementById('memoryStatus').textContent='Parabéns! 🎉💑';
        }else{setTimeout(()=>{a.card.classList.remove('flipped');a.card.textContent='?';
// ===== SURPRESAS =====
function showSurprise(tipo){
    const popup=document.getElementById('surprisePopup');
    const content=document.getElementById('surpriseContent');
    const surprises={
        poema:'<h2>📝 Poema Exclusivo</h2><br>Em cada estrela que brilha no céu 🌟<br>Vejo o reflexo do seu olhar ✨<br>Em cada flor que desabrocha 🌸<br>Sinto seu perfume no ar 💕<br><br>O Mini Mateuzinho escreveu:<br>"Você é a razão do meu sorriso<br>E a dona do meu coração 💖<br>Cada momento ao seu lado<br>É minha melhor canção 🎵"',
        playlist:'<h2>🎵 Nossa Playlist</h2><br>💜 Músicas que lembram você:<br><br>🎶 "Amor de Verdade"<br>🎶 "Perfeita Pra Mim"<br>🎶 "Dois Corações"<br>🎶 "Eternamente"<br>🎶 "Você é Tudo"<br>🎶 "Meu Sol"<br><br>✨ Cada música representa um momento especial! 💑',
        carta:'<h2>💌 Carta Aberta</h2><br>Querida '+currentClient+',<br><br>Você entrou na minha vida e transformou tudo em cor e alegria. Cada conversa, cada risada, cada momento ao seu lado é um tesouro que guardo no coração.<br><br>Obrigado por ser exatamente como você é: incrível, especial e única. Prometo estar sempre aqui.<br><br>Com amor,<br><strong>Mini Mateuzinho</strong> 💜',
        galeria:'<h2>🖼️ Galeria do Amor</h2><br>✨ Nosso primeiro "oi" 💬<br>🌸 As primeiras risadas 😂<br>💖 Quando descobri que te amava<br>🌟 Todos os dias desde então<br>💑 Agora, aqui, juntos!<br><br>Cada instante é uma foto eterna 💜',
        promessas:'<h2>🤞 Minhas Promessas</h2><br>✨ Prometo te fazer sorrir todo dia<br>🌸 Prometo estar ao seu lado sempre<br>💖 Prometo te amar cada vez mais<br>🌟 Prometo cuidar de você<br>💑 Prometo ser seu porto seguro<br>🎮 Prometo jogar todos os joguinhos!<br><br>Essas promessas são pra sempre! 💜',
        futuro:'<h2>🌟 Nosso Futuro</h2><br>✨ Vejo a gente viajando juntos 🌍<br>🌸 Vejo nossa casa cheia de amor 🏠<br>💖 Vejo nossos sonhos se realizando<br>🌟 Vejo a gente dançando na chuva<br>💑 Vejo a gente de mãos dadas pra sempre<br>🎉 Vejo MUITOS momentos felizes!<br><br>O futuro é lindo porque você está nele! 💜✨',
    };
    content.innerHTML=surprises[tipo]||'Surpresa especial! 💜';
    popup.classList.remove('hidden');
}
function closeSurprise(){
    document.getElementById('surprisePopup').classList.add('hidden');

﻿
