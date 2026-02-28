import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# PART 1: Top up to end of Nav
part1 = html.split('<!-- MOBILE MENU OVERLAY -->')[0]

# Adjust title and robots
part1 = part1.replace('<title>Tobias Estivalete | Estruturo performance humana</title>', '<title>Vault | Acesso Restrito - Tobias Estivalete</title>\n    <meta name="robots" content="noindex, nofollow">')
# Fix nav link
part1 = part1.replace('href="#home"', 'href="index.html"')

# Let's remove the extra nav links to be clean
part1 = re.sub(r'<div\s+class="hidden md:flex items-center gap-6 text-\[10px].*?</div>', '', part1, flags=re.DOTALL)
part1 = re.sub(r'<button id="mobile-menu-btn".*?</button>', '', part1, flags=re.DOTALL)

# Clean up any unclosed section tags up there if any
part1 = part1.strip()

# PART 2: The New Vault Section
part2 = """
    <!-- WRAPPER GERAL -->
    <div class="max-w-[1440px] mx-auto border-x border-stone-300 relative bg-[#EAEAE5] shadow-2xl shadow-stone-200">

<!-- SEÇÃO VAULT DESTRANCADA -->
        <section id="vault" class="relative z-10 w-full min-h-[90vh] bg-[#F9F9F8] py-32 px-6 md:px-12 flex flex-col items-center text-center">

            <!-- Fundo dinâmico da área VIP -->
            <div class="absolute inset-0 bg-gradient-to-b from-stone-100 to-[#F9F9F8] z-0 pointer-events-none opacity-50"></div>

            <div class="max-w-6xl mx-auto flex flex-col items-center w-full mt-10 md:mt-24 relative z-10">

                <!-- Cabeçalho de Sucesso/Acesso -->
                <div class="mb-6 flex items-center justify-center gap-2 text-[10px] md:text-xs uppercase font-mono tracking-widest text-emerald-700/80 bg-emerald-50 px-4 py-2 border border-emerald-100 rounded-full shadow-sm">
                    <i data-lucide="unlock" class="w-3.5 h-3.5"></i>
                    Acesso Autenticado
                </div>

                <h1 class="font-serif text-[#1c1917] text-4xl md:text-6xl lg:text-[4.5rem] leading-[1.1] font-normal tracking-tight mb-8">
                    Vault Destrancado.
                </h1>

                <p class="font-sans text-[#78716C] text-[15px] md:text-[17px] max-w-2xl leading-[1.6] font-light mb-16">
                    Abaixo estão os ativos gratuitos iniciais para estruturar a sua visão e escalar sua execução. Materiais premium e novos acessos serão notificados na sua caixa de entrada.
                </p>

                <!-- Grid de Materiais -->
                <div class="w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 text-left relative z-20">
                    
                    <!-- Material 1: Notion -->
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden">
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
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden" style="transition-delay: 100ms;">
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
                    <a href="#" target="_blank" class="group bg-white border border-stone-200 p-8 flex flex-col justify-between min-h-[280px] w-full transition-all duration-500 hover:border-stone-400 hover:shadow-xl hover:shadow-black/5 hover:-translate-y-1 relative overflow-hidden" style="transition-delay: 200ms;">
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
                
                <div class="mt-20 flex justify-center pb-10">
                    <a href="index.html" class="inline-flex items-center text-[10px] font-mono uppercase tracking-[0.2em] text-[#1c1917]/50 hover:text-[#1c1917] transition-colors relative z-20">
                        <i data-lucide="arrow-left" class="w-3 h-3 mr-2"></i> Voltar ao site principal
                    </a>
                </div>

            </div>
        </section>
"""

# PART 3: Footer and Scripts
part3 = """
        <!-- Footer Simplificado -->
        <section class="relative z-10 w-full bg-[#EAEAE5] border-t border-[#d4d4d0]/50 pt-10 pb-12 overflow-hidden flex flex-col items-center">
            
            <a href="mailto:estivaletetobias@gmail.com" class="text-[10px] font-mono uppercase tracking-[0.2em] text-stone-500 hover:text-stone-800 transition-colors mb-20 relative z-20">
                Qualquer dúvida responda por email
            </a>

            <!-- Tipografia Gigante em 2 Linhas -->
            <div class="opacity-[0.08] pointer-events-none select-none overflow-hidden w-full z-0 px-4 md:px-12 max-w-screen-2xl mx-auto flex flex-col items-center">
                <span class="text-[20vw] md:text-[14vw] lg:text-[11.5vw] font-bold font-serif leading-[0.7] tracking-tighter uppercase block w-full text-[#1c1917] text-left">
                    Tobias
                </span>
                <span class="text-[17vw] md:text-[14vw] lg:text-[11.5vw] font-bold font-serif leading-[0.7] tracking-tighter uppercase block w-full text-[#1c1917] text-right mt-1 md:mt-0">
                    Estivalete
                </span>
            </div>
        </section>

    </div> <!-- FIM DO WRAPPER GERAL -->
    
    <!-- SCRIPTS CORE (Somente Lucide para a area restrita) -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            lucide.createIcons();
        });
    </script>
</body>
</html>
"""

final_html = part1 + "\n" + part2 + "\n" + part3

with open("vault-acesso-exclusivo.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Página reconstruída corretamente!")
