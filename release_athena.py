import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. REMOVE "EM BREVE" BLOCK AND ENABLE CLICK
old_btn = r"""                <!-- Projeto 3 (Em Breve) -->
                <div
                    class="group border-b border-stone-300 bg-[#EAEAE5] transition-colors duration-500 overflow-hidden block reveal-up relative opacity-90 cursor-wait">
                    <!-- Tooltip "Em Breve" -->
                    <div
                        class="absolute inset-0 z-20 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-white/70">
                        <span
                            class="bg-[#1c1917] text-[#EAEAE5] font-mono text-xs uppercase tracking-\[0.2em\] px-6 py-3 rounded-full shadow-2xl translate-y-4 group-hover:translate-y-0 transition-all duration-300 ease-out">Em
                            Breve</span>
                    </div>

                    <div
                        class="max-w-\[1400px\] mx-auto grid grid-cols-1 md:grid-cols-12 min-h-\[320px\] pointer-events-none">"""

new_btn = """                <!-- Projeto 3 (Liberado) -->
                <button type="button" onclick="openProjectModal('athena-protocol')"
                    class="group border-b border-stone-300 bg-[#EAEAE5] hover:bg-white transition-colors duration-500 cursor-pointer overflow-hidden block reveal-up text-left w-full">
                    <div
                        class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-12 min-h-[320px]">"""

html = re.sub(old_btn, new_btn, html)

# 2. UPDATE BADGE (From "Em lançamento" to "Ativo")
old_badge = r"""Inteligência</span><span
                                    class="ml-3 mt-\[-2px\] px-2 py-0.5 bg-stone-300 text-stone-800 text-\[8px\] rounded uppercase tracking-widest inline-block">Em
                                    lançamento</span>"""

new_badge = """Inteligência</span><span
                                    class="ml-3 mt-[-2px] px-2 py-0.5 bg-[#1c1917] text-[#EAEAE5] text-[8px] rounded uppercase tracking-widest inline-block">Ativo</span>"""

html = re.sub(r'Evolução\s*Biológica.*?Em\s*lançamento</span>', 'Evolução Biológica</span><span class="ml-3 mt-[-2px] px-2 py-0.5 bg-[#1c1917] text-[#EAEAE5] text-[8px] rounded uppercase tracking-widest inline-block">Ativo</span>', html, flags=re.DOTALL)

# 3. UPDATE CTA "Acompanhar Lançamento" -> "Acessar Plataforma"
html = re.sub(r'Acompanhar Lançamento <i data-lucide="arrow-right"', 'Acessar Detalhes <i data-lucide="arrow-right"', html)

# 4. REMOVE grayscale opacity-50 and adjust image classes
html = re.sub(r'img src="assets/img/1.png" alt="Protocolo Athena".*?class=".*?grayscale opacity-50(.*?)"', r'img src="assets/img/1.png" alt="Protocolo Athena" loading="lazy"\n                                    class="w-full h-full object-cover object-top grayscale opacity-80\1"', html, flags=re.DOTALL)

# Remove the closing </div> of the old "Em breve" block, replace with </button>
old_end = r"""                            </div>
                        </div>
                    </div>
                </div>

                <!-- Projeto 4 \(Em Breve\) -->"""

new_end = """                            </div>
                        </div>
                    </div>
                </button>

                <!-- Projeto 4 (Em Breve) -->"""

html = re.sub(old_end, new_end, html)

# 5. INJECT MODAL DATA IN JS
athena_data = """            'athena-protocol': {
                tag: '03 / Evolução Biológica',
                title: 'Protocolo Athena',
                img: 'assets/img/1.png',
                desc: `
                <div class="flex flex-col gap-6 text-[#1c1917] font-sans pb-4">
                    <p class="text-xl md:text-2xl font-serif leading-snug tracking-tight">O sistema não foi desenhado para influenciadoras fitness que passam 3 horas na academia.</p>
                    
                    <p class="text-stone-600 font-light leading-relaxed">Ele foi forjado para engenheiras de seu próprio ecossistema. Advogadas, empresárias, fundadoras, médicas e executivas.</p>
                    
                    <p class="text-stone-600 font-light leading-relaxed">Você não precisa de mais cobrança estética.<br>Você precisa de tônus muscular que gere energia real, de higiene do sono que restaure função cognitiva e de protocolos que blindem seu cortisol sem comprometer sua agenda.</p>

                    <p class="text-stone-600 font-light leading-relaxed">O <strong>Protocolo Athena</strong> integra duas décadas de ciência do treinamento com estratégia cardiovascular e inteligência adaptativa de rotina feminina.</p>

                    <h5 class="text-2xl font-serif text-[#1c1917] tracking-tight mt-6">Três Pilares Inegociáveis</h5>
                    <ul class="flex flex-col gap-2 font-light text-stone-600 ml-4 list-disc mb-2">
                        <li>Carga neuro-hormonal ajustada à sua fase de vida</li>
                        <li>Arquitetura muscular funcional que sustenta postura, energia e presença</li>
                        <li>Otimização cognitiva e proteção cardiovascular como prioridade, não como consequência</li>
                    </ul>

                    <div class="bg-[#EAEAE5] border border-stone-300/60 p-6 mt-6 relative overflow-hidden group">
                        <p class="text-stone-600 font-light leading-relaxed relative z-10">Aqui, performance não é estética.</p>
                        <p class="text-lg font-serif tracking-tight text-[#1c1917] mt-3 relative z-10">É clareza mental.<br>É resistência fisiológica.<br>É longevidade executiva.</p>
                    </div>

                    <h5 class="text-2xl font-serif text-[#1c1917] tracking-tight mt-6">O que você recebe</h5>
                </div>`,
                bullets: [
                    '<strong>Dossiê Científico Athena</strong> — Documento estruturado com os fundamentos neurofisiológicos, hormonais e cardiovasculares que sustentam o protocolo.',
                    '<strong>GPT exclusivo do Protocolo Athena</strong> — Um sistema de IA adaptativo configurado para ajustar carga, intensidade e foco conforme sua rotina, energia e fase do ciclo.',
                    'Treinamentos hiperfocados em musculatura estabilizadora, metabolismo feminino e densidade funcional.',
                    'Estrutura de progressão com 0% de decisões aleatórias (você apenas executa).',
                    'Arquitetura de rotina com blindagem de cortisol e preservação de capacidade cognitiva.',
                    'Estratégias de recuperação ativa com foco em proteção cardiovascular e sustentabilidade de longo prazo.'
                ],
                checkoutLink: '#contato'
            },"""

html = html.replace("const projectData = {", "const projectData = {\n" + athena_data)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
