import re

with open("vault-acesso-exclusivo.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add keyframes fadeInUp if not present
if "fadeInUp" not in html:
    css = """        @keyframes fadeInUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }"""
    html = html.replace("</style>", css + "\n    </style>")

with open("vault-acesso-exclusivo.html", "w", encoding="utf-8") as f:
    f.write(html)
