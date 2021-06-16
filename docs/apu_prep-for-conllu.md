# Preparing for fieldwork to Universal Dependencies conllu conversion

The are sentences intended for release in the UD Apurinã-UFPA project.

## The first section features metadata and formats to be preserved in UD
* sentence identifiers `sent_id`
* original texts with segmentation `text_orig`
* texts with standard format `text`
* Portuguese gloses `gloss_pt`
* Portuguese translation `text_pt`
* English translation `text_en`

```
# sent_id = FernandaM2017:TextsII-1-6
# text_orig = Kamasaru: Natuku y-txa? 
# text = Natuku ytxa? 
# gloss_pt = como 3SG.M-ser
# text_pt = ‘Como está?’Q
# text_en = How is he?
Natuku ytxa?

# sent_id = FernandaM2017:TextsII-1-9
# text_orig = Kiripa py-kama? 
# text = Kiripa pykama? 
# gloss_pt = o.quê 2SG-fazer 
# text_pt = ‘O que você tá fazendo?’Q
# text_en = ‘‘
Kiripa pykama?

# sent_id = FernandaM2017:TextsII-1-11
# text_orig = Kamasaru: Ĩthepa-ry ximaky? 
# text = Ĩthepary ximaky? 
# gloss_pt = onde.está-3SG.M.O peixe
# text_pt = Cadê o peixe?
# text_en = Where is the fish?
Ĩthepary ximaky?

# sent_id = FernandaM2017:TextsII-1-12
# text_orig = Aramakary: Kuna ka-iumaã-nu. 
# text = Kuna kaiumaãnu. 
# gloss_pt = não ATRIB-trabalho-1SG.O
# text_pt = Não peguei nada.
# text_en = I didn't take anything.
Kuna kaiumaãnu.

# sent_id = FernandaM2017:TextsII-1-16
# text_orig = Ximaky p-anhi-k-inha-wa. 
# text = Ximaky panhikinhawa. 
# gloss_pt = peixe 2SG-levar-PRED-?ser-REFL
# text_pt = ‘Pode levar o peixe.’
# text_en = You can take the fish.
Ximaky panhikinhawa.

# sent_id = FernandaM2017:TextsII-2-7
# text_orig = Txiiupyryỹry: Kuna wai-kiri-nu nuta. 
# text = Kuna waikirinu nuta. 
# gloss_pt = não aqui-?-1SG.O 1SG 
# text_pt = ‘Eu não sou daqui.’
# text_en = I am not from here
Kuna waikirinu nuta.

# sent_id = FernandaM2017:TextsII-2-8
# text_orig = Txiiakatxi: Nanhikiripa p-yna? 
# text = Nanhikiripa pyna? 
# gloss_pt = de.onde 2SG-vir
# text_pt = ‘De onde você é?’ Lit.: ‘De onde você veio?’Q
# text_en = Where do you come from?
Nanhikiripa pyna?

# sent_id = FernandaM2017:TextsII-2-9
# text_orig = Txiiupyryỹry: Syrywyny n-awa. 
# text = Syrywyny nawa. 
# gloss_pt = Seruini 1SG-existir
# text_pt = ‘Eu sou do Seruini.’Q
# text_en = ‘I'm from Seruini.‘
Syrywyny nawa.

# sent_id = FernandaM2017:TextsII-2-14
# text_orig = Txiiupyryỹry: Kanaiapa ny-nyru. 
# text = Kanaiapa nynyru. 
# gloss_pt = N.PROP 1SG-mãe.de
# text_pt = Minha mãe é a Kanaiapa.
# text_en = My mother is Kanaiapa.
Kanaiapa nynyru.

# sent_id = FernandaM2017:TextsII-2-15
# text_orig = Txiiakatxi: Py-nyru ny-nyru nyrymane u-txa-wa. 
# text = Pynyru nynyru nyrymane utxawa. 
# gloss_pt = 2SG-mãe.de 1SG-mãe.de parente.de 3SG.F-ser-REFL
# text_pt = ‘A sua mãe é parenta da minha mãe.’Q
# text_en = Your mother is my mother's relative
Pynyru nynyru nyrymane utxawa.

# sent_id = FernandaM2017:TextsII-2-16
# text_orig = Txiiupyryỹry: Ãkiri kiripa-ra-i pitha? 
# text = Ãkiri kiriparai pitha?
# gloss_pt = filho.de quem-FOC-2SG.O 2SG
# text_pt = ‘E você é filho de quem?’Q
# text_en = ‘‘
Ãkiri kiriparai pitha?

# sent_id = FernandaM2017:TextsII-2-17
# text_orig = Txiiakatxi: Tutupary ãkiri nhi-txa-wa. 
# text = Tutupary ãkiri nhitxawa.
# gloss_pt = N.PROP filho.de 1SG-ser-REFL
# text_pt = ‘Eu sou filho do Tutupary.’Q
# text_en = ‘‘
Tutupary ãkiri nhitxawa.

# sent_id = FernandaM2017:TextsII-2-18
# text_orig = Txiiupyryỹry: Kerupa p-ynyru? 
# text = Kerupa pynyru? 
# gloss_pt = quem 2SG-mãe.de
# text_pt = ‘Quem é a sua mãe?’Q
# text_en = ‘‘
Kerupa pynyru?

# sent_id = FernandaM2017:TextsII-2-19
# text_orig = Txiiakatxi: Kamĩkiu n-ynyru. 
# text = Kamĩkiu nynyru. 
# gloss_pt = N.PROP 1SG-mãe.de
# text_pt = ‘Minha mãe é a Kamĩkiu.’Q
# text_en = ‘‘
Kamĩkiu nynyru.

# sent_id = FernandaM2017:TextsII-2-20
# text_orig = Txiiupyryỹry: Ataũ-pyty-ka-ra py-sãkire. 
# text = Ataũpytykara pysãkire. 
# gloss_pt = ser.verdade-ENF-PRED-FOC 2SG-falar
# text_pt = ‘Você falou a verdade.’ 
Ataũpytykara pysãkire.

# sent_id = FernandaM2017:TextsII-2-21
# text_orig = Ataũ-pyty-ka-ra pi-txa kutxi n-yry xinhika-pi-ka-ry p-yry. 
# text = Ataũpytykara pitxa kutxi nyry xinhikapikary pyry. 
# gloss_pt = ser.verdade-ENF-PRED-FOC 2SG-ser porque 1SG-pai.de lembrar-HAB-PRED-3SG.M.O 2SG-pai.de
# text_pt = ‘Você disse a verdade, pois meu pai sempre se lembra do seu pai.’Q
# text_en = ‘‘
Ataũpytykara pitxa kutxi nyry xinhikapikary pyry.

# sent_id = FernandaM2017:TextsII-2-22
# text_orig = Kiripa py-wãka? 
# text = Kiripa pywãka? 
# gloss_pt = qual 2SG-nome.de
# text_pt = ‘Qual o seu nome?’Q
# text_en = ‘‘
Kiripa pywãka?

# sent_id = FernandaM2017:TextsII-2-23
# text_orig = Txiiakatxi: Txiiakatxi ny-wãka. 
# text = Txiiakatxi nywãka. 
# gloss_pt = N.PROP 1SG-nome.de
# text_pt = ‘O meu nome é Txiiakatxi.’ 
Txiiakatxi nywãka.

# sent_id = FernandaM2017:TextsII-2-24
# text_orig = Kiripa pitha wãka? 
# text = Kiripa pitha wãka? 
# gloss_pt = qual 2SG nome.de
# text_pt = ‘Qual o seu nome?’Q
# text_en = ‘‘
Kiripa pitha wãka?

# sent_id = FernandaM2017:TextsII-2-25
# text_orig = Txiiupyryỹry: Txiiupyryỹry ny-wãka. 
# text = Txiiupyryỹry nywãka. 
# gloss_pt = N.PROP 1SG-nome.de
# text_pt = ‘O meu nome é Txiiupyryỹry.’Q
# text_en = ‘‘
Txiiupyryỹry nywãka.

# sent_id = FernandaM2017:TextsII-2-26
# text_orig = Txiiakatxi: Ĩka a-ymaruta-kaka-pe-ka. 
# text = Ĩka aymarutakakapeka. 
# gloss_pt = ?então 1PL-conhecer-REC-PFTV-PRED
# text_pt = ‘Então já nos conhecemos.’Q
Ĩka aymarutakakapeka.

# sent_id = FernandaM2017:TextsII-3-1
# text_orig = Lição 3: Natukupa i-txa wai p-awinhi-ã? 
# text = Natukupa itxa wai pawinhiã? 
# gloss_pt = (como-INTERR 3SG.M-ser aqui 2SG-comunidade.de-LOC)
# text_pt = ‘Como é a vida na sua comunidade?’Q
# text_en = ‘‘
 Natukupa itxa wai pawinhiã?

# sent_id = FernandaM2017:TextsII-3-5
# text_orig = Kuriiaty: Ii! Kaiãu-ry parĩka-txi atha-munhi. 
# text = Ii! Kaiãury parĩkatxi athamunhi. 
# gloss_pt = interjeição existir.muito-3SG.M.O trabalho.de-N.POSSD 1PL-DAT
# text_pt = ‘Ii! Tem muito trabalho pra nós!’Q
# text_en = ‘‘
Ii! Kaiãury parĩkatxi athamunhi.

# sent_id = FernandaM2017:TextsII-3-6
# text_orig = Hĩtha-munhi awa parĩka-txi apaka? 
# text = Hĩthamunhi awa parĩkatxi apaka? 
# gloss_pt = 2PL-DAT existir trabalho.de-N.POSSD também
# text_pt = ‘E lá com vocês, é assim também?’ Lit.: ‘Pra vocês também tem trabalho?’Q
# text_en = ‘‘
Hĩthamunhi awa parĩkatxi apaka?

# sent_id = FernandaM2017:TextsII-3-7
# text_orig = Txiakatxi: Ary, awa-pyty-ka. 
# text = Ary, awapytyka. 
# gloss_pt = sim existir-ENF-PRED
# text_pt = ‘É, é assim mesmo.’ Lit.: ‘Sim, tem mesmo.’Q
# text_en = ‘‘
Ary, awapytyka.

# sent_id = FernandaM2017:TextsII-3-8
# text_orig = Kuriiaty: Ki-nha-kary-pa parĩka-txi awa hĩtha-munhi? 
# text = Kinhakarypa parĩkatxi awa hĩthamunhi? 
# gloss_pt = INTERR-ser-REL.S.M-INTERR trabalho.de-N.POSSD existir 2PL-DAT
# text_pt = ‘Que tipo de trabalho vocês fazem?’ Lit.: ‘Que tipo de trabalho tem pra vocês?’Q
# text_en = ‘‘
Kinhakarypa parĩkatxi awa hĩthamunhi?

# sent_id = FernandaM2017:TextsII-3-9
# text_orig = Kutxi atha kyky-ãkinhi a-kama-ry tukury, kumyry amapuruka, katarukyry a-kama, a-ũkatsaãta, ã-aiata, a-txa atha wai. 
# text = Kutxi atha kykyãkinhi akamary tukury, kumyry amapuruka, katarukyry akama, aũkatsaãta, ãaiata, atxa atha wai. 
# gloss_pt = porque 1PL homem-grupo 1PL-fazer-3SG.M.O roçado mandioca arrancar farinha 1PL-fazer 1PL-pescar 1PL-caçar 1PL-fazer 1PL aqui
# text_pt = ‘Nós, os homens, fazemos o roçado, arrancamos a mandioca, fazemos a farinha, pescamos, caçamos... Tudo isso nós fazemos aqui.’Q
# text_en = ‘‘
Kutxi atha kykyãkinhi akamary tukury, kumyry amapuruka, katarukyry akama, aũkatsaãta, ãaiata, atxa atha wai.

# sent_id = FernandaM2017:TextsII-3-10
# text_orig = Txiakatxi: Ywatuku kanera a-txa atha ywaã. 
# text = Ywatuku kanera atxa atha ywaã. 
# gloss_pt = assim ? 1PL-ser 1PL lá
# text_pt = ‘Lá pra nós, também é assim.’ 
Ywatuku kanera atxa atha ywaã.
 
# sent_id = FernandaM2017:TextsII-3-11
# text_orig = Tukury a-kama, katarukyry a-kama, a-ũkatsaã-ta, ã-aiata, aiku a-kama, a-txa apaka. 
# text = Tukury akama, katarukyry akama, aũkatsaãta, ãaiata, aiku akama, atxa apaka. 
# gloss_pt = roçado 1PL-fazer farinha 1PL-fazer 1PL-pescar-VBLZ 1PL-caçar casa 1PL-fazer 1PL-aux também
# text_pt = ‘Nós também fazemos roçado, farinha, pescamos, caçamos, fazemos casa, fazemos isso também.’Q
# text_en = ‘‘
Tukury akama, katarukyry akama, aũkatsaãta, ãaiata, aiku akama, atxa apaka.

# sent_id = FernandaM2017:TextsII-3-13
# text_orig = Txiakatxi: Sytu-waku-ru, kiripa u-kama-ã-ne? 
# text = Sytuwakuru, kiripa ukamaãne? 
# gloss_pt = mulher-PL-F o.quê 3PL.F-fazer-PROGR-3PL.F
# text_pt = ‘E as mulheres, o que elas fazem?’Q
Sytuwakuru, kiripa ukamaãne?

# sent_id = FernandaM2017:TextsII-3-14a
# text_orig = Kuriiaty: Mãka-txi ũ-eruka, nhipuku-ry u-kama, xãmyna u-txirata, ĩparãa ũ-apa-ã-ta, ama-ry-ny u-kipa-ã-ta, tui-txi u-weruka, ama-ry-ny u-inhĩkata, mãka-txi u-iutsaã, ximaky u-iumareta, xinhĩ-txi u-sututa, u-ỹruta-wa-ta, u-ỹruta-ry ximaky, ũ-ỹruta-ry xinhĩ-txi, nhipuku-ry u-ãxitha, tsapyryky u-kama.
# text = Mãkatxi ũeruka, nhipukury ukama, xãmyna utxirata, ĩparãa ũapaãta, amaryny ukipaãta, tuitxi uweruka, amaryny uinhĩkata, mãkatxi uiutsaã, ximaky uiumareta, xinhĩtxi usututa, uỹrutawata, uỹrutary ximaky, ũỹrutary xinhĩtxi, nhipukury uãxitha, tsapyryky ukama.
# gloss_pt = roupa.de-N.POSSD 3SG.F-lavar comida-N.POSSD 3SG.F-fazer lenha 3SG.F-partir água 3SG.F-buscar-PROGR-VBLZ criança-M-PL 3SG.F-dar.banho-PROGR-VBLZ coisa.de-N.POSSD 3SG.F-lavar criança -M-PL 3SG.F-cuidar roupa.de-N.POSSD 3SG.F-costurar peixe 3SG.F-tratar carne.de-N.POSSD 3SG.F-cortar 3SG.F-moquear-refl-vblz 3sg.f-moquear-3sg.m.o peixe 3sg.f-moquear-3SG.M.O carne.de-N.POSSD comida-N.POSS 3SG.F-cozinhar açaí 3SG.F-fazer
# text_pt = ‘Ela lava a roupa, faz comida, parte a lenha, vai buscar água, dá banho nas crianças, lava os pratos, cuida das crianças, costura a roupa, trata o peixe, corta a carne, faz o moqueado, moqueia o peixe, cozinha a comida, faz o açaí.’Q
# text_en = ‘‘
Mãkatxi ũeruka, nhipukury ukama, xãmyna utxirata, ĩparãa ũapaãta, amaryny ukipaãta, tuitxi uweruka, amaryny uinhĩkata, mãkatxi uiutsaã, ximaky uiumareta, xinhĩtxi usututa, uỹrutawata, uỹrutary ximaky, ũỹrutary xinhĩtxi, nhipukury uãxitha, tsapyryky ukama.

# sent_id = FernandaM2017:TextsII-3-14b
# text_orig = Kuriiaty: Ypusatuku ũ-ãkirita-ry ũ-tanyry ama-ry-ny-ky ywasaaky nhipuku-ta a-txa. 
# text = Ypusatuku ũãkiritary ũtanyry amarynyky ywasaaky nhipukuta atxa. 
# gloss_pt = depois 3SG.F-chamar-3SG.M.O 3SG.F-marido.de criança-M-PL-NC.pequeno TEMP comida-VBLZ 1PL-AUX
# text_pt = ‘Depois de pronto, ela chama o marido, as crianças, aí então comemos.’Q
# text_en = ‘‘
Ypusatuku ũãkiritary ũtanyry amarynyky ywasaaky nhipukuta atxa.

# sent_id = FernandaM2017:TextsII-3-15
# text_orig = Txiakatxi: Ama-ry-ny-ky kiripa y-kama-ã-ne? 
# text = Amarynyky kiripa ykamaãne? 
# gloss_pt = criança-M-PL-NC.pequeno o.quê 3PL.M-fazer-PROGR-3PL.M
# text_pt = ‘O que as crianças fazem?’Q
# text_en = ‘‘
Amarynyky kiripa ykamaãne?

# sent_id = FernandaM2017:TextsII-3-16
# text_orig = Kuriiaty: Ama-ry-ny-ky kuna parĩka-wa-ta, y-sarawata-pi-ka-ne. 
# text = Amarynyky kuna parĩkawata, ysarawatapikane. 
# gloss_pt = criança-M-PL-NC.pequeno não trabalho-REFL-VBLZ 3PL.M-brincar-HAB-PRED-3PL.M
# text_pt = ‘As crianças não trabalham, elas apenas brincam.’Q
# text_en = ‘‘
Amarynyky kuna parĩkawata, ysarawatapikane.

# sent_id = FernandaM2017:TextsII-3-17
# text_orig = Kytsyna y-kymataka-ne. 
# text = Kytsyna ykymatakane. 
# gloss_pt = calango 3PL.M-flechar-3PL.M
# text_pt = ‘Flecham calango.’Q
# text_en = ‘‘
Kytsyna ykymatakane.

# sent_id = FernandaM2017:TextsII-3-18
# text_orig = Kytypyryky apaka y-kymataka-ne. 
# text = Kytypyryky apaka ykymatakane. 
# gloss_pt = passarinho também 3PL.M-flechar-3PL.M
# text_pt = ‘Eles também flecham passarinho.’Q
# text_en = ‘‘
Kytypyryky apaka ykymatakane.

# sent_id = FernandaM2017:TextsII-3-19
# text_orig = Ama-ry-ny-ky sytu-waku-ru inha-kany-wa muiana-ta-ru u-nyru-ne. 
# text = Amarynyky sytuwakuru inhakanywa muianataru unyrune. 
# gloss_pt = criança-M-PL-NC.pequeno mulher-PL-F ser-REL.PL-REFL acompanhar-VBLZ-3SG.F.O 3PL.F-mãe.de-3PL.F
# text_pt = ‘As meninas acompanham as mães.’Q
# text_en = ‘‘
Amarynyky sytuwakuru inhakanywa muianataru unyrune.

# sent_id = FernandaM2017:TextsII-3-20
# text_orig = Mãka-txi u-weruk-inhi ama-ry-ny 
# text = Mãkatxi uwerukinhi amaryny 
# gloss_pt = roupa.de-N.POSSD 3SG.F-ajudar-GER criança-M-PL
# text_pt = ‘As crianças ajudam com a roupa’Q
# text_en = ‘‘
Mãkatxi uwerukinhi amaryny

# sent_id = FernandaM2017:TextsII-3-21
# text_orig = u-inhĩkat-inhi tui-txi ũ-weruk-inhi. 
# text = uinhĩkatinhi tuitxi ũwerukinhi. 
# gloss_pt = 3SG.F-lavar-GER coisa.de-N.POSSD 3SG.F-ajudar-GER 
# text_pt = ‘As meninas ajudam a lavar os pratos.’Q
# text_en = ‘‘
uinhĩkatinhi tuitxi ũwerukinhi.

# sent_id = FernandaM2017:TextsII-3-22
# text_orig = Ama-ry-ny axa-piti-ri ywa-kata u-sarawata u-txa-ne. 
# text = Amaryny axapitiri ywakata usarawata utxane. 
# gloss_pt = criança-M-PL ser.pequeno-ENF-3SG.M.O 3SG.M-ASSOC 3SG.F-brincar 3PL.F-AUX-3PL.F
# text_pt = ‘Elas brincam (cuidam das) com as crianças menores.’Q
# text_en = ‘‘
Amaryny axapitiri ywakata usarawata utxane.

# sent_id = FernandaM2017:TextsII-4-1
# text_orig = Lição 4: Katarukyry a-kama
# text = Katarukyry akama
# gloss_pt = farinha 1PL-fazer
# text_pt = ‘Nós fazemos farinha’Q
# text_en = ‘‘
Katarukyry akama

# sent_id = FernandaM2017:TextsII-4-2
# text_orig = Kirama ĩkanũka-panhi-ka ũkytykawa kumyry i-mapik-inhi ĩkapane. 
# text = Kirama ĩkanũkapanhika ũkytykawa kumyry imapikinhi ĩkapane. 
# gloss_pt = N.PROP noite-IPFTV-PRED ?levantar mandioca 3SG.M-descascar-GER com.o.propósito de
# text_pt = ‘O Kirama levantou de manhã cedo pra descascar mandioca.’Q
# text_en = ‘‘
Kirama ĩkanũkapanhika ũkytykawa kumyry imapikinhi ĩkapane.

# sent_id = FernandaM2017:TextsII-4-3
# text_orig = Akiritha-ru Kamĩkiu ĩ-tanyru. 
# text = Akiritharu Kamĩkiu ĩtanyru. 
# gloss_pt = chamar-3SG.F N.PROP 3SG.M-esposa.de
# text_pt = ‘Ele chamou Kamĩkiu, a sua esposa.’Q
# text_en = ‘‘
Akiritharu Kamĩkiu ĩtanyru.

# sent_id = FernandaM2017:TextsII-4-4
# text_orig = Kirama: Kiripa a-kama watxa? 
# text = Kiripa akama watxa? 
# gloss_pt = o.quê 1PL-fazer hoje
# text_pt = ‘O que é que nós vamos fazer hoje?’Q
# text_en = ‘‘
Kiripa akama watxa?

# sent_id = FernandaM2017:TextsII-4-5
# text_orig = Kamĩkiiu: Kumyry a-mapika.
# text = Kumyry amapika.
# gloss_pt = mandioca 1PL-descascar
# text_pt = ‘Nós vamos descascar mandioca.’Q
# text_en = ‘‘
Kumyry amapika.

# sent_id = FernandaM2017:TextsII-4-6
# text_orig = Kirama: Ateeneka. 
# text = Ateeneka. 
# gloss_pt = tá.certo
# text_pt = ‘Tá bom.’Q
# text_en = ‘‘

# sent_id = FernandaM2017:TextsII-4-7
# text_orig = Ĩka amu a-sa-puka. 
# text = Ĩka amu asapuka. 
# gloss_pt = ?então EXORT 1PL-ir-?cedo 
# text_pt = ‘Então vamos logo.’Q
# text_en = ‘‘
Ĩka amu asapuka.
```

