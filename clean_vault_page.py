import re

with open("vault-acesso-exclusivo.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Adicionar NOINDEX meta tag para SEO
html = html.replace('<title>Tobias Estivalete | Estratégia e Sistemas</title>',
                   '<title>Vault | Acesso Restrito - Tobias Estivalete</title>\n    <meta name="robots" content="noindex, nofollow">')

# 2. Simplificar a Navbar (Remover links de navegação para parecer página isolada/cofre)
nav_pattern = r'<div class="hidden md:flex items-center gap-10">.*?</div>'
html = re.sub(nav_pattern, '', html, flags=re.DOTALL)

# Remover botão de menu Mobile
mobile_btn_pattern = r'<button class="md:hidden flex flex-col justify-center items-center w-10 h-10.*?</button>'
html = re.sub(mobile_btn_pattern, '', html, flags=re.DOTALL)

# Remover o Overlay Mobile inteiro
mobile_menu_pattern = r'<!-- MOBILE MENU OVERLAY -->.*?</div>\n    </div>'
html = re.sub(mobile_menu_pattern, '', html, flags=re.DOTALL)

# 3. Remover a Seção Home Inteira (Video Hero)
home_pattern = r'<!-- SEÇÃO HOME / OVERVIEW -->.*?</section>'
html = re.sub(home_pattern, '', html, flags=re.DOTALL)

# 4. Remover Projetos
projetos_pattern = r'<!-- SEÇÃO PROJETOS \(List View\) -->.*?</section>'
html = re.sub(projetos_pattern, '', html, flags=re.DOTALL)

# 5. Remover Seção Sobre
sobre_pattern = r'<!-- SEÇÃO SOBRE -->.*?</section>'
html = re.sub(sobre_pattern, '', html, flags=re.DOTALL)

# 6. Remover Contato
contato_pattern = r'<!-- SEÇÃO CONTATO -->.*?</section>'
html = re.sub(contato_pattern, '', html, flags=re.DOTALL)

# 7. Refatorar a Seção do Vault para a versão DESTRANCADA
vault_start = html.find('<!-- SEÇÃO VAULT (YT ENCAPSULADO) -->')
vault_end = html.find('</main>')

if vault_start != -1 and vault_end != -1:
    old_vault = html[vault_start:vault_end]
    
    new_vault_content = """<!-- SEÇÃO VAULT DESTRANCADA -->
        <section id="vault" class="relative z-10 w-full min-h-[100vh] bg-[#F9F9F8] py-32 md:py-40 px-6 md:px-12 flex flex-col items-center text-center">

            <div class="max-w-6xl mx-auto flex flex-col items-center w-full">

                <!-- Cabeçalho de Sucesso/Acesso -->
                <div class="mb-6 flex items-center justify-center gap-2 text-[10px] md:text-xs uppercase font-mono tracking-widest text-[#1c1917]/70">
                    <i data-lucide="unlock" class="w-3.5 h-3.5"></i>
                    Acesso Autenticado
                </div>

                <h1 class="font-serif text-[#1c1917] text-4xl md:text-6xl lg:text-[4.5rem] leading-[1.1] font-normal tracking-tight mb-8">
                    Vault Destrancado.
                </h1>

                <p class="font-sans text-[#78716C] text-[15px] md:text-[17px] max-w-2xl leading-[1.6] font-light mb-16">
                    Mantenha este link salvo. Abaixo estão os ativos gratuitos iniciais para estruturar a sua visão e escalar sua execução. Materiais premium e novos acessos serão notificados na sua caixa de entrada.
                </p>

                <!-- Grid de Materiais (No modelo do Carrossel Antigo, porem Grid Real) -->
                <div class="w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 text-left">
                    
                    <!-- Material 1: Notion -->
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden reveal-up">
                        <div class="absolute top-0 left-0 w-full h-[3px] bg-stone-200 group-hover:bg-[#1c1917] transition-colors duration-500"></div>
                        <div>
                            <div class="w-12 h-12 bg-[#F9F9F8] rounded-xl flex items-center justify-center mb-6">
                                <i data-lucide="layout-template" class="w-5 h-5 text-[#1c1917]"></i>
                            </div>
                            <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-stone-400 mb-2 block">Notion Template</span>
                            <h4 class="font-serif text-2xl text-[#1c1917] mb-3 group-hover:text-black transition-colors">Sistema Pessoal Base</h4>
                            <p class="font-sans text-[13px] text-stone-500 leading-relaxed font-light">Estrutura inicial de organização de tarefas inspirado no Agente de Produção.</p>
                        </div>
                        <div class="mt-8 flex items-center justify-between">
                            <span class="text-[11px] font-sans font-medium uppercase tracking-widest text-[#1c1917]">Duplicar</span>
                            <i data-lucide="external-link" class="w-4 h-4 text-stone-300 group-hover:text-[#1c1917] group-hover:translate-x-1 group-hover:-translate-y-1 transition-all"></i>
                        </div>
                    </a>

                    <!-- Material 2: Ebook/PDF -->
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden reveal-up" style="transition-delay: 100ms;">
                        <div class="absolute top-0 left-0 w-full h-[3px] bg-stone-200 group-hover:bg-[#1c1917] transition-colors duration-500"></div>
                        <div>
                            <div class="w-12 h-12 bg-[#F9F9F8] rounded-xl flex items-center justify-center mb-6">
                                <i data-lucide="book-open" class="w-5 h-5 text-[#1c1917]"></i>
                            </div>
                            <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-stone-400 mb-2 block">Protocolo em PDF</span>
                            <h4 class="font-serif text-2xl text-[#1c1917] mb-3 group-hover:text-black transition-colors">A Lógica da Alta Performance</h4>
                            <p class="font-sans text-[13px] text-stone-500 leading-relaxed font-light">Os 4 pilares físicos e mentais para performar em alto nível sem queimar o motor.</p>
                        </div>
                        <div class="mt-8 flex items-center justify-between">
                            <span class="text-[11px] font-sans font-medium uppercase tracking-widest text-[#1c1917]">Baixar</span>
                            <i data-lucide="download" class="w-4 h-4 text-stone-300 group-hover:text-[#1c1917] group-hover:translate-y-[2px] transition-all"></i>
                        </div>
                    </a>

                    <!-- Material 3: GPT -->
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden reveal-up" style="transition-delay: 200ms;">
                        <div class="absolute top-0 left-0 w-full h-[3px] bg-stone-200 group-hover:bg-[#1c1917] transition-colors duration-500"></div>
                        <div>
                            <div class="w-12 h-12 bg-[#F9F9F8] rounded-xl flex items-center justify-center mb-6">
                                <i data-lucide="bot" class="w-5 h-5 text-[#1c1917]"></i>
                            </div>
                            <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-stone-400 mb-2 block">GPT Customizado</span>
                            <h4 class="font-serif text-2xl text-[#1c1917] mb-3 group-hover:text-black transition-colors">Conselheiro Sintético</h4>
                            <p class="font-sans text-[13px] text-stone-500 leading-relaxed font-light">Prompt estruturado para auxiliar na tomada de decisões complexas de negócios.</p>
                        </div>
                        <div class="mt-8 flex items-center justify-between">
                            <span class="text-[11px] font-sans font-medium uppercase tracking-widest text-[#1c1917]">Conversar</span>
                            <i data-lucide="message-square" class="w-4 h-4 text-stone-300 group-hover:text-[#1c1917] transition-all"></i>
                        </div>
                    </a>

                </div>
                
                <div class="mt-20 flex justify-center">
                    <a href="index.html" class="inline-flex items-center text-[10px] font-mono uppercase tracking-[0.2em] text-[#1c1917]/50 hover:text-[#1c1917] transition-colors">
                        <i data-lucide="arrow-left" class="w-3 h-3 mr-2"></i> Voltar ao site principal
                    </a>
                </div>

            </div>
        </section>
        
        """
    html = html.replace(old_vault, new_vault_content)

# Clean up Modal injections related to the main page since this is just a delivery page
script_pattern = r'<!-- INJEÇÃO DOS MODAIS / MINI LPs \(Exclusivo para Mobile/Tablet\) -->.*?</style>'
html = re.sub(script_pattern, '', html, flags=re.DOTALL)

with open("vault-acesso-exclusivo.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Página do Vault Refatorada com Sucesso")
