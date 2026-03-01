# MANUAL DO ARQUITETO DE INTERFACES COM IA 🏗️⚡

Este guia documenta o método exato utilizado para construir a estrutura de alta performance do projeto **Tobias Estivalete**. Ele serve como um roteiro de engenharia reversa para replicar esse sucesso em novos projetos, unindo design de elite e automação inteligente.

---

## 🚀 PASSO 0: O SETUP DO PODER (Antigravity & VS Code)

O sucesso de qualquer projeto de IA não começa no código, mas na **organização do ambiente**.

1.  **Pasta Raiz:** Crie uma pasta clara no seu computador (ex: `/Projetos/MeuNovoSite`).
2.  **VS Code:** Abra essa pasta no Visual Studio Code.
3.  **Ignite Antigravity:** Inicie o seu agente de IA (Antigravity) dentro deste contexto.
4.  **O "Prompt" de Intencionalidade:** Não peça apenas "faça um site". Diga: 
    > *"Você é meu Engenheiro de Software Sênior. Vamos construir uma plataforma de alta conversão, estética premium (Glassmorphism), focada em performance e automação. Leia meus arquivos de referência e proponha a melhor arquitetura."*

---

## 🏗️ PASSO 1: A COLHEITA DE REFERÊNCIAS (Engenharia Reversa)

Nós não inventamos o design do zero. Nós **curamos** os melhores do mundo.

1.  **Identificação:** Encontre sites que possuem a "vibe" que você deseja (ex: sites da Apple, Linear, ou os templates do curso como *Digital Architect*).
2.  **Captura (Download):** Use ferramentas como a extensão **Save Page WE** (Chrome) ou o comando **HTTrack** para baixar o site completo para o seu computador.
3.  **Pasta de Templates:** Crie uma pasta dentro do seu projeto chamada `assets/templates/` e coloque os sites baixados lá.
4.  **Instrução para a IA:** Peça para a IA ler esses arquivos:
    > *"Leia o arquivo `assets/templates/site-referencia/index.html`. Eu quero que você use o sistema de cores e as fontes dele, mas com o layout de botões do `assets/templates/outro-site/design-system.html`."*

---

## 🎨 PASSO 2: O LABORATÓRIO (Design System)

Antes de montar a "casa" (Index), nós testamos os "tijolos".

1.  **Criação do Design System:** Peça para a IA criar um arquivo `design-system.html`.
2.  **O Teste de Estresse:** Neste arquivo, peça para ela renderizar:
    *   Sistemas de Tipografia (H1, H2, P).
    *   Paleta de Cores (Primária, Secundária, Transparências).
    *   Componentes de UI: Botões com hover, Cards de vidro, Menus Mobile.
3.  **Validação:** Só leve para a `index.html` aquilo que você olhar e disser: **"Isso é nível Apple"**.

---

## ⚙️ PASSO 3: O MOTOR DE PERFORMANCE (GSAP & Lenis)

O que separa um site amador de um site de elite é o **movimento**.

1.  **Lenis Scroll:** Instalamos o script de "Smooth Scroll" para que a rolagem do mouse seja amanteigada.
2.  **GSAP (GreenSock):** O motor de animação de Hollywood. Usamos para fazer os elementos "surgirem" (Reveal) conforme o usuário rola a tela.
3.  **O Comando Mágico:** 
    > *"Instale o GSAP e o Lenis no meu projeto. Configure uma animação de 'Fade In Up' para todas as seções que possuem a classe `.reveal-up`."*

---

## 📊 PASSO 4: BANCO DE DADOS SEM CÓDIGO (Google Sheets)

Atualize seu site sem abrir o VS Code, apenas mexendo em uma planilha.

1.  **Google Sheets:** Crie uma planilha, preencha os dados e vá em *Arquivo > Compartilhar > Publicar na Web* (escolha formato CSV).
2.  **PapaParse:** Peça para a IA instalar a biblioteca PapaParse.
3.  **A Conexão:** 
    > *"Use o link CSV da minha planilha do Google para alimentar dinamicamente os cards da minha página `vault.html`. Se eu mudar um nome na planilha, o site deve atualizar sozinho."*

---

## 🤖 PASSO 5: AUTOMAÇÃO DE LEADS (Brevo)

Capture e-mails e entregue arquivos automaticamente 24h por dia.

1.  **Brevo (ex-Sendinblue):** Crie uma conta e um formulário simples (apenas campo E-mail).
2.  **Captura Invisível (Assíncrona):** Peça para a IA pegar o código HTML simples do Brevo e "escondê-lo" dentro do seu design de vidro, usando `fetch` para enviar o e-mail sem recarregar a página.
3.  **Workflow:** Configure no Brevo para: *"Sempre que alguém entrar na lista X, envie o E-mail de Boas Vindas com o link do Vault"*.

---

## 🌐 PASSO 6: DEPLOY (GitHub & Vercel)

Tire o projeto do seu computador e jogue para o mundo.

1.  **Git Init:** `git init`, `git add .`, `git commit -m "First Blood"`.
2.  **GitHub:** Crie um repositório e faça o `git push`.
3.  **Vercel/Netlify:** Conecte o repositório do GitHub. A partir de agora, cada vez que eu fizer um commit, o seu site atualiza na URL oficial em segundos.

---

*Manual criado em parceria com Antigravity por Tobias Estivalete. Última atualização: Março de 2026.*
