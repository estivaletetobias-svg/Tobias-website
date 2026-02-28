import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Vault
new_vault = """                <!-- Acesso Restrito Form -->
                <div class="w-full max-w-2xl flex flex-col items-center justify-center p-12 lg:p-16 text-center border border-stone-300/60 bg-white/50 backdrop-blur-sm rounded-[24px] shadow-sm relative overflow-hidden z-20 mx-auto mb-10">
                    <!-- Sutil noise ou gradiente -->
                    <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#F9F9F8]"></div>
                    <div class="relative z-10 w-full">
                        <i data-lucide="lock" class="w-6 h-6 mx-auto mb-6 text-stone-400"></i>
                        <h3 class="font-serif text-2xl text-[#1c1917] mb-3">Acesso Restrito</h3>
                        <p class="font-sans text-[14px] text-stone-500 mb-8 max-w-md mx-auto leading-relaxed">Vault em atualização quinzenal. O repositório base das minhas estruturas e sistemas pagos. Em breve destravado via aplicação.</p>
                        
                        <form action="#" class="w-full relative flex items-center relative z-20 pointer-events-auto shadow-sm">
                            <input type="email" placeholder="O seu melhor e-mail" required class="w-full bg-[#EAEAE5] border border-stone-300/50 rounded-full pl-6 pr-32 py-4 font-sans text-[14px] text-[#1c1917] focus:outline-none focus:bg-white focus:shadow-md transition-all duration-300 placeholder:text-stone-400">
                            <button type="submit" class="absolute right-2 top-1/2 -translate-y-1/2 bg-[#1c1917] text-[#EAEAE5] text-[10px] uppercase tracking-widest font-bold px-6 py-2.5 rounded-full hover:bg-stone-700 transition-colors">Aplicar</button>
                        </form>
                    </div>
                </div>"""

# Substituir Controle Customizado e Vault-Grid
html = re.sub(r'<!-- Controle Customizado.*?</button>\s*</div>\s*<!-- Open Ecosystem GPTs Grid.*?</div>\s*</div>', new_vault, html, flags=re.DOTALL)

# 2. Update Contato Select
old_contato = """<input type="text" id="subject" name="subject" required
                                placeholder="Ex: Arquitetura Sistêmica, Consultoria..."
                                class="w-full bg-[#F9F9F8] border border-white/80 shadow-[0_4px_10px_rgba(0,0,0,0.02)] rounded-[20px] px-6 py-[18px] font-sans text-[14px] text-[#1c1917] placeholder-[#A8A29E]/60 focus:outline-none focus:bg-white focus:shadow-[0_8px_20px_rgba(0,0,0,0.04)] transition-all duration-500">"""
new_contato = """<div class="relative w-full">
                                <select id="subject" name="subject" required
                                    class="w-full bg-[#F9F9F8] border border-white/80 shadow-[0_4px_10px_rgba(0,0,0,0.02)] rounded-[20px] px-6 py-[18px] font-sans text-[14px] text-[#1c1917] placeholder-[#A8A29E]/60 focus:outline-none focus:bg-white focus:shadow-[0_8px_20px_rgba(0,0,0,0.04)] transition-all duration-500 appearance-none cursor-pointer">
                                    <option value="" disabled selected class="text-stone-400">Selecione o motivo da conversa...</option>
                                    <option value="Quero evoluir minha performance">Quero evoluir minha performance</option>
                                    <option value="Preciso de sistemas e inteligência para meu negócio">Preciso de sistemas e inteligência para meu negócio</option>
                                    <option value="Parcerias e Convites Especiais">Parcerias e Convites Especiais</option>
                                </select>
                                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-6 text-[#A8A29E]">
                                    <i data-lucide="chevron-down" class="w-4 h-4"></i>
                                </div>
                            </div>"""
html = html.replace(old_contato, new_contato)

# 3. Update Projetos 
card_replacements = [
    (
        '<span\n                                    class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Inteligência</span>\n                            </div>',
        '<span\n                                    class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Inteligência</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-[#1c1917] text-[#EAEAE5] text-[8px] rounded uppercase tracking-widest inline-block">Ativo</span>\n                            </div>'
    ),
    (
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Autoridade\n                                    Assíncrona</span>\n                            </div>',
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Autoridade\n                                    Assíncrona</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-stone-300 text-stone-800 text-[8px] rounded uppercase tracking-widest inline-block">Waitlist</span>\n                            </div>'
    ),
    (
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Evolução\n                                    Biológica</span>\n                            </div>',
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Evolução\n                                    Biológica</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-stone-300 text-stone-800 text-[8px] rounded uppercase tracking-widest inline-block">Em lançamento</span>\n                            </div>'
    ),
    (
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Sistema\n                                    Digital</span>\n                            </div>',
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Sistema\n                                    Digital</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-stone-300 text-stone-800 text-[8px] rounded uppercase tracking-widest inline-block">Waitlist</span>\n                            </div>'
    ),
    (
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Performance\n                                    Real</span>\n                            </div>',
        '<span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Performance\n                                    Real</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-stone-700 text-white text-[8px] rounded uppercase tracking-widest inline-block">Vagas Limitadas</span>\n                            </div>'
    )
]

# Apply badge replacements
for old_s, new_s in card_replacements:
    html = html.replace(old_s, new_s)

# Apply CTAs 
# Using regex for paragraphs inside the left column
pattern_p = r'(<p class="text-\[#78716C\].*?)</p>'

new_ctas = [
    r'\1</p>\n                            <div class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">Acessar Plataforma <i data-lucide="arrow-right" class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>',
    r'\1</p>\n                            <div class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">Aplique antecipadamente <i data-lucide="arrow-right" class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>',
    r'\1</p>\n                            <div class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">Acompanhar Lançamento <i data-lucide="arrow-right" class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>',
    r'\1</p>\n                            <div class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">Aplique antecipadamente <i data-lucide="arrow-right" class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>',
    r'\1</p>\n                            <div class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">Consultar Vagas Abertas <i data-lucide="arrow-right" class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>',
]

paragraphs = re.findall(pattern_p, html, flags=re.DOTALL)
count = 0 
for p in paragraphs:
    if "Sistema de acompanhamento" in p or "Presença e autoridade" in p or "Sistema inteligente que" in p or "Estrutura digital personalizada" in p or "Treinamento aplicado" in p:
        # replace just this instance
        old_block = p + "</p>"
        html = html.replace(old_block, new_ctas[count].replace(r'\1', p), 1)
        count += 1
        
    if count >= 5:
        break


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully!")
