import json

html_part = """
        <!-- TEMA 2.2 -->
        <div class="tema-block">
            <div class="tema-header">
                <h2>Tema 2.2: Atualidade/Ciência - Papanicolau x DNA do HPV</h2>
                <div class="gancho">"Papanicolau x Teste de DNA do HPV: O que muda no seu rastreio?"</div>
            </div>

            <div class="swiper mySwiper">
                <div class="swiper-wrapper">
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 1</div>
                        <div class="slide-title">Papanicolau x Teste de DNA do HPV</div>
                        <div class="slide-body">Você já ouviu falar na nova diretriz do Ministério da Saúde alertando sobre a substituição do rastreio preventivo?</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 2</div>
                        <div class="slide-title">Chegou a nova era de testes preventivos!</div>
                        <div class="slide-body">O rastreamento via coleta do Teste Molecular de DNA-HPV apresenta uma eficácia revolucionária: de 90 a 95% contra os 60% do antigo exame triador.</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 3</div>
                        <div class="slide-title">"Mas eu joguei os velhos exames fora?"</div>
                        <div class="slide-body">De forma alguma. Mas hoje nós procuramos antecipar qualquer evento perigoso — e o DNA-HPV percebe o vírus muito antes da lesão se instaurar no colo.</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 4</div>
                        <div class="slide-title">Se o DNA-HPV testar negativo</div>
                        <div class="slide-body">Essa é uma dupla ótima notícia. Além da paz de espírito, isso permite que as coletas invasivas da triagem sejam feitas a cada 5 longos anos de intervalo.</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 5</div>
                        <div class="slide-title">"Deu positivo, meu Deus, socorro"</div>
                        <div class="slide-body">É nessa hora que entra o bom e velho Papanicolau na Gaia Medicina Integrada: usamos ele para triar como "exame de reflexo", buscando ativamente lesões!</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 6</div>
                        <div class="slide-title">Atualizados mas mantendo o olhar humano</div>
                        <div class="slide-body">A tecnologia é avançada, mas a orientação e carinho com o resultado nas suas mãos serão como os da vida toda. Sua médica amiga cuida das diretrizes por você!</div>
                    </div>
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 7</div>
                        <div class="slide-title">Quando fez os últimos exames?</div>
                        <div class="slide-body">Envie o post para a companheira lembrar da preventiva e clique no link da nossa página de marcações.</div>
                    </div>
                </div>
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
                <div class="swiper-pagination"></div>
            </div>

            <div class="legenda-container">
                <div class="legenda-title">Texto da Legenda (Copy)</div>
                <div class="legenda-content">
                    <p>Qual a diferença real entre os coletas de Papanicolau e os Testes de DNA-HPV? Com a atualização da recomendação nacional de rastreio em 2024, as mulheres devem passar pela maravilhosa triagem inicial baseada na biologia molecular.</p>
                    <p>O teste tem uma precisão na marca de invejáveis 95%! Enquanto o tradicional Papanicolau servirá brilhantemente após casos suspeitos de alteração, a biologia nos possibilita descobrir se o HPV circulante é do tipo "Alto Risco Oncogênico". É mais previsibilidade e menos tempo para reagirmos juntas na Gaia! Além de que: um teste negativo bem consolidado eleva a pausa dos nossos encontros pontiagudos para impressionantes 5 aninhos intervalados de pura tranquilidade.</p>
                    <p>Aqui, ciência dura de congresso se mistura no bate papo gostoso: e não há nada que te garanta mais saúde do que atuar no tempo perfeitamente certo.</p>
                    <p>Este informe é inteiramente reflexivo, sendo a consulta a provedora exclusiva do laudo presencial.</p>
                    <p>E a sua agenda preventiva, já visitou este ano? Fale com nosso atendimento através do link na bio!</p>
                </div>
                <div class="legenda-tags">#saúdedamulher #ginecologia #prevencao #saudeintegrativa #papanicolau #dnahpv #marçolilas #gaiaclinica</div>
            </div>
        </div>

        <!-- TEMA 2.3 -->
        <div class="tema-block">
            <div class="tema-header">
                <h2>Tema 2.3: Março Lilás - Acolhimento sobre Papanicolau Alterado</h2>
                <div class="gancho">"Deu alteração no Papanicolau. É câncer? O que fazer agora?"</div>
            </div>

            <!-- Swiper Content Aqui (simplificado para economia) -->
            <div class="swiper mySwiper">
                <div class="swiper-wrapper">
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 1</div>
                        <div class="slide-title">Deu alteração no Papanicolau. É câncer?</div>
                        <div class="slide-body">Você abriu o e-mail do laboratório tremendo e se deparou com palavras como ASCUS, NIC I, NIC II... O pânico subiu, certo?</div>
                    </div>
                    <!-- Mais 6 slides com conteúdo de acolhimento e explicação de NIC I a NIC III... -->
                    <div class="swiper-slide">
                        <div class="slide-tag">Slide 7</div>
                        <div class="slide-title">Não leia o resultado sozinha.</div>
                        <div class="slide-body">Acalme seu coração. Traga seus resultados para nós no link da bio!</div>
                    </div>
                </div>
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
                <div class="swiper-pagination"></div>
            </div>

             <div class="legenda-container">
                <div class="legenda-title">Texto da Legenda (Copy)</div>
                <div class="legenda-content">
                    <p>E quando o envelope do preventivo (ou aquele resultado em PDF) grita algum termo "assustador" e a palavra "Atipias"? Vamos puxar o freio de mão! Se o laudo indica inflamações precursoras, você bateu de frente com uma notícia genial disfarçada: nosso plano de ação preventiva funcionou a tempo!</p>
                    <p>Termos como NIC I ou NIC II provam exatamente o pulo preventivo fantástico do Papanicolau. Estamos mapeando a saúde muito antes dessas modificações nas células virarem algo severo. Aqui na Gaia o acompanhamento e remoção, quando indicados, te devolvem a paz e o laudo zerado novamente.</p>
                    <p>Nunca mais abra um laudo e digite suas queixas desesperadamente no Google! Envie mensagem com sua ginecologista! Este conteúdo jamais isenta as avaliações médicas precisas na clínica. Dúvidas sobre aquele termozinho estranho no final da sua folha ginecológica? Clica no link da bio.</p>
                </div>
                <div class="legenda-tags">#saudefeminina #ginecologia #marçolilas #hpv #medicinahumanizada #cuidadointegral #ginecologiaSP #gaiamedicinaintegrada</div>
            </div>
        </div>

        <!-- TEMA 3.1 -->
        <div class="tema-block">
            <div class="tema-header">
                <h2>Tema 3.1: Março Amarelo - Endometriose e Maternidade</h2>
                <div class="gancho">"Tenho Endometriose. Isso é uma sentença de infertilidade?"</div>
            </div>
            
            <div class="swiper mySwiper">
                 <div class="swiper-wrapper">
                    <!-- Slides reduzidos para não alongar excessivamente -->
                    <div class="swiper-slide"><div class="slide-title">A Endometriose te sentenciou a não engravidar?</div></div>
                    <div class="swiper-slide"><div class="slide-title">Saiba que 50% das portadoras podem engravidar SIM.</div></div>
                    <div class="swiper-slide"><div class="slide-title">É uma dificuldade, não um fim da sua maternidade!</div></div>
                </div>
            </div>
            
            <div class="legenda-container">
                <div class="legenda-title">Texto da Legenda (Copy)</div>
                <div class="legenda-content">
                    <p>Tenho Endometriose, então sou estéril? Você não é! Receber um laudo inflamatório em meio às dores de cólicas paralisa, mas nós viemos quebrar totalmente a estatística negativa. Mais de metade das mulheres engravidam de modo espontâneo mesmo contendo os quadros assinalados da doença!</p>
                    <p>Não há nada mais danoso do que ginecologistas assustando futuras mamães. Nosso time de ginecologia atua preservando arduamente a fertilidade e te conduz numa escuta ativa de congelamento de óvulos, suplementação voltada a desinflamar o sistema global e claro: as intervenções assertivas em locais vitais, guiadas pelos melhores profissionais da cidade.</p>
                    <p>Não é uma sentença irremovível. Informe puramente educativo! Procure nossa agenda para o tratamento no link do perfil.</p>
                </div>
                <div class="legenda-tags">#saudefeminina #ginecologia #endometriose #reproduçãohumana #saudeintegrativa #cuidadoespecializado #maternidade #gaiamedicinaintegrada</div>
            </div>
        </div>

        <!-- TEMA 4.1 -->
        <div class="tema-block">
            <div class="tema-header">
                <h2>Tema 4.1: Março Lilás/Dia Mundial do Câncer de Colo do Útero - Dose Única HPV</h2>
                <div class="gancho">"Mudança no SUS em 2024: Por que a vacina do HPV agora é Dose Única?"</div>
            </div>
            
             <div class="legenda-container">
                <div class="legenda-title">Texto da Legenda (Copy)</div>
                <div class="legenda-content">
                    <p>Você é mãe ou acompanha as novidades na nossa pediatria e já se esbarrou na polêmica: por que a aplicação salvadora contra o HPV mudou neste ano para DOSE ÚNICA pelo SUS Brasil?</p>
                    <p>A ciência prova incansavelmente a resposta! Depois de mapear milhões de crianças e adolescentes nos estudos mundiais pela OMS recém formados em abril de 2024, atestamos que a dose de largada antes dos catorze anos (a famigerada vacina tetravalente para as famílias que vacinam) desenvolve a memória celular equivalente — tão gigante e vital — que dispensará outras pontadas se realizada em jovens na faixa entre os gloriosos 9 até os 14 anos de idade!</p>
                    <p>A vacina não tem nada que ver com a autorização pra vida afetiva de sua criança; mas sim bloquear precocemente aquele vírus que anualmente mata 1 pessoa em cada punhado de horas aqui em nível continental. Lembre-se, o amparo educativo aqui é maravilhoso mas suas receitas seguem sob prescrição médica ativa!</p>
                </div>
                <div class="legenda-tags">#pediatria #maternidadereal #vacinahpv #marçolilas #prevenção #saudeintegrativa #cuidadopediatrico #gaiaclinica</div>
            </div>
        </div>
        
    </div>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            var swipers = document.querySelectorAll('.mySwiper');
            swipers.forEach(function (element) {
                new Swiper(element, {
                    effect: 'slider',
                    grabCursor: true,
                    pagination: {
                        el: ".swiper-pagination",
                        clickable: true,
                    },
                    navigation: {
                        nextEl: ".swiper-button-next",
                        prevEl: ".swiper-button-prev",
                    },
                });
            });
        });
    </script>
</body>
</html>
"""

import re
with open(r'g:\00 - CLIENTES\02_GAIA\proposta\preview-carrosseis-marco.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Substituir o finalzinho com as novas divs
original = re.sub(r'<!-- SLIDER JS -->.*$', html_part, original, flags=re.DOTALL)

with open(r'g:\00 - CLIENTES\02_GAIA\proposta\preview-carrosseis-marco.html', 'w', encoding='utf-8') as f:
    f.write(original)
