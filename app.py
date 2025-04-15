import streamlit as st
from PIL import Image

st.set_page_config(page_title="Treino para Condromalácia Patelar", layout="wide")

st.title("🏋️ Treino para Condromalácia Patelar")
st.markdown("Este app guia seu treino na academia com foco na saúde dos joelhos.")

# Lista de exercícios com imagens e descrições
exercicios = [
    {
        "nome": "AQUECIMENTO (8-10min)",
        "serie": "5-7 minutos",
        "descricao": "Pedalar em ritmo confortável (50-60 RPM), sem dor. Ajustar o assento para que o joelho não flexione além de 45° no ponto mais baixo.",
        "dica": "Aqueça até sentir os músculos levemente aquecidos, sem forçar a amplitude.",
        "imagem": "bicicleta.png"
    },
    {
        "nome": "Cadeira Extensora (Quadríceps)",
        "serie": "3x15, carga leve a moderada (iniciar com ~20-30% do peso corporal)",
        "descricao": "Ajustar a máquina para limitar a flexão a 30-45°. Estender as pernas lentamente (2-3 segundos na subida) e retornar controladamente (3 segundos na descida). Parar se houver dor.",
        "dica": "Aumentar a carga gradualmente (5-10% por semana) apenas se não houver desconforto após 48h.",
        "imagem": "cadeira_extensora.jpg"
    },
    {
        "nome": "Cadeira Abdutora (Glúteos)",
        "serie": "3x15, carga leve-moderada",
        "descricao": "Sentar com tronco levemente inclinado para frente (~10-15°), pés alinhados com os joelhos. Abrir as pernas lentamente, focando na ativação do glúteo médio. Evitar inclinação pélvica excessiva.",
        "dica": "Aumentar a carga gradualmente (5-10% por semana) apenas se não houver desconforto após 48h.",
        "imagem": "cadeira-adutora.png"
    },
    {
        "nome": "Elevação de Quadril (Hip Thrust)",
        "serie": "3x12, com peso leve (barra ou anilha, iniciar com 5-10kg)",
        "descricao": "Apoiar a parte superior das costas em um banco, pés afastados na largura dos ombros. Elevar o quadril até formar uma linha reta (ombros-quadril-joelhos), contraindo os glúteos no topo (2 segundos). Manter joelhos alinhados, sem hiperextensão lombar.",
        "dica": "Ativação prévia (opcional): Ponte glútea no solo (3x10, sem peso) antes do hip thrust para acordar os glúteos.",
        "imagem": "hip-thrust.png"
    },
    {
        "nome": "Mesa Flexora (Isquiotibiais)",
        "serie": "3x12-15, carga leve-moderada.",
        "descricao": "Deitado na mesa flexora, flexionar os joelhos lentamente (2-3 segundos) até ~90°, sem levantar o quadril. Retornar controladamente. Ajustar a carga para evitar desconforto no joelho.",
        "dica":"Fortalecer os isquiotibiais ajuda a equilibrar a força com o quadríceps, reduzindo a pressão patelofemoral.",
        "imagem": "mesa-flexora.png"
    },
    {
        "nome": "Agachamento com Bola na Parede (wall squat)",
        "serie": "3x10-12, sem peso.",
        "descricao": "Encostar as costas em uma bola suíça contra a parede, pés afastados ~50cm da parede. Descer até 45-60° de flexão dos joelhos, mantendo o joelho alinhado com o segundo dedo do pé. Subir lentamente. Parar se houver dor.",
        "dica": "Após 4-6 semanas, adicionar mini-agachamentos livres (sem bola) com peso corporal, se não houver dor.",
        "imagem": "wall_squat.jpg"
    },
    {
        "nome": "Cadeira adutora",
        "serie": "2x15, carga leve",
        "descricao": "Sentar com postura ereta, fechar as pernas lentamente, focando nos adutores. Evitar forçar se houver desconforto no joelho.",
        "dica": "Após 4-6 semanas, adicionar mini-agachamentos livres (sem bola) com peso corporal, se não houver dor.",
        "imagem": "cadeira-abdutora.gif"
    },
    {
        "nome": "Equilíbrio Unilateral no Bosu",
        "serie": "2-3 séries de 30-45 segundos por lado",
        "descricao": "Ficar em pé sobre um bosu (lado plano para cima) ou disco, com um pé só, mantendo o core ativado e o joelho levemente flexionado (~10-20°). Olhar para um ponto fixo à frente para facilitar o equilíbrio. Iniciantes podem apoiar uma mão na parede.",
        "dica" : "Nenhuma",
        "imagem": "Bosu.webp"
    },
    {
        "nome": "ALONGAMENTO FINAL (8min)",
        "serie": "Cada alongamento por 30 segundos",
        "descricao": "Quadríceps: Em pé, segurar o pé com uma mão, trazendo o calcanhar em direção ao glúteo. Manter o joelho apontado para baixo."\
            " Isquiotibiais: Sentado, com uma perna esticada e a outra dobrada, alcançar a ponta do pé da perna esticada."\
                "Glúteos e piriforme: Deitado, cruzar uma perna sobre a outra (posição 4) e puxar a coxa de apoio em direção ao peito.",
        "dica": "Fazer os alongamentos de forma suave, sem forçar a amplitude.",
        "imagem": None
    }
]

# Exibição dos exercícios
for ex in exercicios:
    with st.expander(f"✅ {ex['nome']}"):
        cols = st.columns([1, 2])
        if ex["imagem"]:
            try:
                imagem = Image.open(f"data/{ex['imagem']}")
                cols[0].image(imagem, caption=ex["nome"], use_container_width=True)
            except Exception as e:
                cols[0].warning("Imagem não encontrada.")
        cols[1].markdown(f"**Instruções:** {ex['descricao']}")
        cols[1].markdown(f"**Séries:** {ex['serie']}")
        cols[1].markdown(f"**Dica:** {ex['dica']}") 
        cols[1].checkbox("Marcar como concluído", key=ex["nome"])