#font('Comic Sans MS', 100)
#fill(1, 0, 0)
#text('Hello world', (0, 0))

myMargin = 50



#with open('book.txt', encoding='utf-8') as myFile:
#    myText = myFile.read()

myText = '''
Acerio. 9593025 Is mi, ipician dipsam experum quis plisiti atemole cepera nobit aliatqui natemque sum rest et di  235 aceperero ommoluptatet volut et, sinvelici sequiant est as sus, sum, in num id quias nossint, quis 2342 nusdae 1010101 abor sendam nis adit occae excepro dolorehenis delignihilla debit utatet et lisqui odit qui te sequi re nis maionecatqui officabore, officil iquamus audit minulpa rchiliatium, tes doluptasimet estiur aliquid magnat iniento et rectatet ersperum ea as dolut pe pa cuptat od expliquisqui bla dolesero mo blam, tentiat antotatios experia asi asperitaquam velitectota sunt et voluptas volorep taquiamus.
Aperio que poreptae ere, voluptibust, sequas aut rem. Et dolupta vit et quae sanda ipsam, vellita voluptiis alicia velitate verum ratur? Quidiste eumento es sit, ilit hilibusa cullandae nobis eatiunt lacepuda nim re dolestior aut harum quam cus dendis reribus eumquas sendios tibus.
To eliatibus et, quis qui to exeria ducid que diteni il mi, con eiunti omnihit aut ulloribus voluptur, qui acestiis doluptatio. Nam iur soluptatur?
Ribusa dolest, ommos explis resequa spidipsam quo quatemquam rem et ea nossum et aruptaturio. Aceperrovid et verrorernat utemporum sinctus restis magnieni sin nus am que quos unto consedia volupta tureritibus, sin porerum, toremporem acia voluptam, vollit volum, sint.
Molorem ut dolut eos dolorep eribusda numquat emporibus ute si debis millest entem eres sit pos que lam, optatur, sitatiat ut videst reriorepuda aceperciunto bere conecturit velenia ipidel inim facerio. Nam, solorunt ma porerumque rescid eate ni repe nient in reptate dolorrum et et fuga. Bus et ea prent eum, atatur aliquod quiatum quatem exerum aut quo inim desed es rehenec aerferunt, inis as asimi, opta cus, conse vel maximaiorem quae conet et ute del essit quatiat enimolupiet peri volorias erum haris modi conempor reratet que offic te diate nonesti ostios aut ipsuntis nimagnat ute nonecati volupit aturiam aut fugit eum fuga. Et accuptatem la dolupta tiatia venis acerum quam, consed mintia ea conseni musantis rehene labo. Et acepudae vent aut lit quas arciae pa parum hit ad mi, est, con comnihi catur?
Gendaecabore consed que nimolore voluptio volorep ernatur, odit et quia nit oditatio quo dunt, omnimeniet maximpo rporiaero beatendae ni optibuscit que nate pres sum rehenti cus.
Aquas eium rae. Et praeperio vent laborunt ium audit, odit andicatum aut fugia dolupta tiorpos dis molo cum quam aliquam, qui dolo qui doloris es acearum esequam repeles non porum saped ut est laturit praestr uptate landus, comnihi cimillor aliquos exerovide rehendam voluptatur aut ut audaepelit as eatecat emporem sam quaspel igente acepere necta ipidenist, omnimil modia vel iur, optaque dit volendi ut aperovit, quaspel itatur? Giatio occuptas provita testibus event hictur alitat ex eiume reruptinctia cullati animpos animagnam aut quiae. Fugitiis ut poratur alis seque et omnis perrum ut que volupta que res aut doluptios estia excest vid qui unt.

'''


myString = FormattedString(
    myText, 
    font='CondorVariable-VF.ttf', 
    fontSize=35, 
    lineHeight=50, 
    tracking=0, 
    fill=(1, 0, 0),
    openTypeFeatures={'smcp': True, 'onum': True, 'ss01': False},
    fontVariations={'wdth': 100, 'wght': 900, 'ital': 1},
    align="justified",
    )
    

myPageNumber = 1

while myString:
    newPage()
    #rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
    myString = textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
    print(myString)
    fontSize(30)
    font('Georgia')
    fill(0, 1, 0)
    text(str(myPageNumber), (20, 40))
    myPageNumber += 1