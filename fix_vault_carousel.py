import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Ajustar a visibilidade (blur e opacidade) e o container
# Reduzindo o blur e aumentando a opacidade do carrossel
html = html.replace('opacity-40 blur-[3px]', 'opacity-60 blur-[1px]')

# 2. Corrigir o problema de renderização do lado direito e loop infinito
# Atualmente o container está com classes relativas que clipam ou a animação não é contínua o suficiente
# Vamos reconstruir a div do carrossel para garantir preenchimento em toda a largura usando duplicação

old_carousel_start = """                <!-- Aperitivo Visual (Atrás do Bloqueio) -->
                <div class="absolute inset-0 w-[100vw] left-1/2 -translate-x-1/2 overflow-hidden mask-fade flex items-center z-0 pointer-events-none">
                    <div
                        class="flex items-center gap-6 opacity-60 blur-[1px] pointer-events-none select-none animate-[scrollAnim_30s_linear_infinite]">"""

# If the replace above didn't catch the exact string, try the old one
html = html.replace('opacity-40 blur-[3px]', 'opacity-60 blur-[1px]')

# To make the infinite scroll actually work properly across the whole screen width,
# we need to duplicate the ghost cards so there is never empty space on the right.
# Let's completely replace the ghost cards block with a properly structured marquee.

# Find the start and end of the Aperitivo Visual block
start_idx = html.find('<!-- Aperitivo Visual (Atrás do Bloqueio) -->')
end_idx = html.find('</div> <!-- Fim do Wrapper Relativo -->')

if start_idx != -1 and end_idx != -1:
    old_block = html[start_idx:end_idx]
    
    # New marquee structure with two sets of identical cards to seamlessly loop
    card_template = """
                        <div class="flex-shrink-0 w-[280px] h-[320px] bg-white border border-stone-200/80 rounded-[20px] p-6 flex flex-col justify-between shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
                            <div class="w-10 h-10 bg-stone-100/80 rounded-lg flex items-center justify-center mb-4">
                                <div class="w-5 h-5 bg-stone-300/80 rounded-sm"></div>
                            </div>
                            <div>
                                <div class="h-4 bg-stone-200/80 rounded w-[75%] mb-3"></div>
                                <div class="h-3 bg-stone-100/80 rounded w-full mb-1"></div>
                                <div class="h-3 bg-stone-100/80 rounded w-[85%]"></div>
                            </div>
                            <div class="w-full h-[1px] bg-stone-200/60 mt-4"></div>
                        </div>"""

    # We need 10 cards total (5 in first set, 5 in second set) to ensure it fills any wide screen
    cards_html = (card_template * 5)
    
    # The marquee needs exactly two identical wrappers inside a container
    new_block = """<!-- Aperitivo Visual (Atrás do Bloqueio) -->
                <div class="absolute inset-0 w-[100vw] left-1/2 -translate-x-1/2 overflow-hidden mask-fade flex items-center z-0 pointer-events-none">
                    <!-- Wrapper animado principal -->
                    <div class="flex items-center gap-6 w-max opacity-60 blur-[1px] pointer-events-none select-none animate-[scrollAnim_40s_linear_infinite] px-3">
                        """ + cards_html + """
                        """ + cards_html + """
                    </div>
                </div>
                
                """
    
    html = html.replace(old_block, new_block)

# Fix the CSS animation to slide precisely half of its width (the exact duplicate point)
css_old = """        @keyframes scrollAnim {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); } /* Halfway point for seamless loop if duplicated */
        }"""
css_new = """        @keyframes scrollAnim {
            from { transform: translateX(0); }
            to { transform: translateX(calc(-50% - 12px)); } /* 50% shift minus half the gap for perfect loop */
        }"""
html = html.replace(css_old, css_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully!")
