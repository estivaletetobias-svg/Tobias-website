import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the button transformation that was done halfway
old_btn = r"""                <!-- Projeto 3 (Liberado) -->
                <button type="button" onclick="openProjectModal('athena-protocol')"
                    class="group border-b border-stone-300 bg-\[#EAEAE5\] hover:bg-white transition-colors duration-500 cursor-pointer overflow-hidden block reveal-up text-left w-full">
                    <div
                        class="max-w-\[1400px\] mx-auto grid grid-cols-1 md:grid-cols-12 min-h-\[320px\]">
                            <div
                                class="col-span-1 md:col-span-5 p-8 md:p-12 lg:p-16 border-r border-stone-300/0 md:border-stone-300 flex flex-col justify-center">"""

new_btn = """                <!-- Projeto 3 (Liberado) -->
                <button type="button" onclick="openProjectModal('athena-protocol')"
                    class="group border-b border-stone-300 bg-[#EAEAE5] hover:bg-white transition-colors duration-500 cursor-pointer overflow-hidden block reveal-up text-left w-full">
                    <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-12 min-h-[320px]">
                        <div class="col-span-1 md:col-span-5 p-8 md:p-12 lg:p-16 border-r border-stone-300/0 md:border-stone-300 flex flex-col justify-center">"""

html = re.sub(r'<!-- Projeto 3 \(Em Breve\) -->(.*?)<!-- Projeto 4 \(Em Breve\) -->', r"""<!-- Projeto 3 (Liberado) -->
                <button type="button" onclick="openProjectModal('athena-protocol')"
                    class="group border-b border-stone-300 bg-[#EAEAE5] hover:bg-white transition-colors duration-500 cursor-pointer overflow-hidden block reveal-up text-left w-full">
                    <div class="max-w-[1400px] mx-auto grid grid-cols-1 md:grid-cols-12 min-h-[320px]">
                        <div class="col-span-1 md:col-span-5 p-8 md:p-12 lg:p-16 border-r border-stone-300/0 md:border-stone-300 flex flex-col justify-center">
                            <div class="flex items-center gap-3 mb-6">
                                <span class="text-xs font-mono text-stone-500">03</span>
                                <div class="h-px w-8 bg-stone-300"></div>
                                <span class="text-[10px] font-bold uppercase tracking-widest text-[#1c1917]">Evolução Biológica</span><span
                                    class="ml-3 mt-[-2px] px-2 py-0.5 bg-[#1c1917] text-[#EAEAE5] text-[8px] rounded uppercase tracking-widest inline-block">Ativo</span>
                            </div>
                            <h4
                                class="text-3xl md:text-4xl lg:text-5xl font-medium tracking-tight mb-6 text-[#1c1917] group-hover:translate-x-3 transition-transform duration-500 font-serif">
                                Protocolo Athena
                            </h4>
                            <p class="text-[#78716C] text-[15px] leading-relaxed max-w-sm font-light">
                                Sistema inteligente que conecta mente, performance e resultados reais — para mulheres
                                que querem otimizar a cognição e proteger a saúde cardiovascular.
                            </p>
                            <div
                                class="mt-8 flex items-center font-mono text-[10.5px] uppercase tracking-[0.15em] text-[#1c1917]/50 group-hover:text-[#1c1917] transition-all font-semibold">
                                Detalhes e Aplicação <i data-lucide="arrow-right"
                                    class="w-3 h-3 ml-2 group-hover:translate-x-1 transition-transform"></i></div>
                        </div>
                        <div
                            class="col-span-1 md:col-span-7 relative overflow-hidden block h-[260px] md:h-auto border-t border-stone-300 md:border-t-0">
                            <div class="absolute inset-0 bg-stone-100 flex items-center justify-center p-0">
                                <img src="assets/img/1.png" alt="Protocolo Athena" loading="lazy"
                                    class="w-full h-full object-cover object-top grayscale opacity-80 group-hover:scale-105 group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-[800ms] ease-out">
                            </div>
                        </div>
                    </div>
                </button>

                <!-- Projeto 4 (Em Breve) -->""", html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
