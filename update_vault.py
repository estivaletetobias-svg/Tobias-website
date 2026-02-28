import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Vault Content
vault_content_to_insert = """
                <!-- Aperitivo Visual (Atrás do Bloqueio) -->
                <div class="w-full relative mx-auto mt-4 overflow-hidden mask-fade">
                    <div class="flex items-center gap-6 opacity-40 blur-[2px] pointer-events-none select-none animate-[scrollAnim_30s_linear_infinite]">
                        
                        <!-- Ghost Card 1 -->
                        <div class="flex-shrink-0 w-[280px] h-[320px] bg-white border border-stone-300 rounded-[20px] p-6 flex flex-col justify-between">
                            <div class="w-10 h-10 bg-stone-100 rounded-lg flex items-center justify-center mb-4">
                                <div class="w-5 h-5 bg-stone-300 rounded-sm"></div>
                            </div>
                            <div>
                                <div class="h-4 bg-stone-200 rounded w-3/4 mb-3"></div>
                                <div class="h-3 bg-stone-100 rounded w-full mb-1"></div>
                                <div class="h-3 bg-stone-100 rounded w-5/6"></div>
                            </div>
                            <div class="w-full h-[1px] bg-stone-200 mt-4"></div>
                        </div>

                        <!-- Ghost Card 2 -->
                        <div class="flex-shrink-0 w-[280px] h-[320px] bg-white border border-stone-300 rounded-[20px] p-6 flex flex-col justify-between">
                            <div class="w-10 h-10 bg-stone-100 rounded-lg flex items-center justify-center mb-4">
                                <div class="w-5 h-5 bg-stone-300 rounded-sm"></div>
                            </div>
                            <div>
                                <div class="h-4 bg-stone-200 rounded w-2/3 mb-3"></div>
                                <div class="h-3 bg-stone-100 rounded w-full mb-1"></div>
                                <div class="h-3 bg-stone-100 rounded w-4/5"></div>
                            </div>
                            <div class="w-full h-[1px] bg-stone-200 mt-4"></div>
                        </div>

                        <!-- Ghost Card 3 -->
                        <div class="flex-shrink-0 w-[280px] h-[320px] bg-white border border-stone-300 rounded-[20px] p-6 flex flex-col justify-between">
                            <div class="w-10 h-10 bg-stone-100 rounded-lg flex items-center justify-center mb-4">
                                <div class="w-5 h-5 bg-stone-300 rounded-sm"></div>
                            </div>
                            <div>
                                <div class="h-4 bg-stone-200 rounded w-4/5 mb-3"></div>
                                <div class="h-3 bg-stone-100 rounded w-full mb-1"></div>
                                <div class="h-3 bg-stone-100 rounded w-full"></div>
                            </div>
                            <div class="w-full h-[1px] bg-stone-200 mt-4"></div>
                        </div>

                         <!-- Ghost Card 4 -->
                         <div class="flex-shrink-0 w-[280px] h-[320px] bg-white border border-stone-300 rounded-[20px] p-6 flex flex-col justify-between">
                            <div class="w-10 h-10 bg-stone-100 rounded-lg flex items-center justify-center mb-4">
                                <div class="w-5 h-5 bg-stone-300 rounded-sm"></div>
                            </div>
                            <div>
                                <div class="h-4 bg-stone-200 rounded w-3/4 mb-3"></div>
                                <div class="h-3 bg-stone-100 rounded w-full mb-1"></div>
                                <div class="h-3 bg-stone-100 rounded w-5/6"></div>
                            </div>
                            <div class="w-full h-[1px] bg-stone-200 mt-4"></div>
                        </div>

                    </div>
                </div>
"""

# Insert CSS rules for mask fade
css_to_insert = """
        .mask-fade {
            mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
        }
        @keyframes scrollAnim {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); } /* Halfway point for seamless loop if duplicated */
        }
"""

# Apply modifications
if "mask-fade" not in html:
    html = html.replace("</style>", css_to_insert + "\n    </style>")

if "Ghost Card 1" not in html:
    # Anchor point
    anchor = "</div>\n                </div>\n\n            </div>\n        </section>\n\n        <!-- SEÇÃO SOBRE -->"
    html = html.replace("</div>\n                </div>\n\n            </div>\n        </section>\n\n        <!-- SEÇÃO SOBRE -->", 
                       "</div>\n                </div>\n" + vault_content_to_insert + "\n            </div>\n        </section>\n\n        <!-- SEÇÃO SOBRE -->")


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Files updated successfully")
