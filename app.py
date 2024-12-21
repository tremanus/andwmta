from flask import Flask, request, render_template
import re
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return "", 204  # No Content

@app.route("/process", methods=["POST"])
def process():
    start = time.time()
    try:
        aya = request.form["aya"]
        filetype = ".txt"
        filename = aya + filetype
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        punc = '[\?\-!\?\*,"\(\):\\[\];_/~፣፡።፤፥፦]'
        newtext = ''.join(' ' if re.search(punc, c) else c for c in text)
        words = newtext.split()
        finalwords = [w for w in words if not re.search('[0-9፩-፱፲-፼]', w)]
        newwords = []
        for w in words:
            word = ''
            for c in w:
                if c != "'":
                    word += c
            newwords.append(word)

        QrtsBett = request.form["QrtsBett"]
        matches_found = []  # Collect matches here

        if QrtsBett == "1":
            qrts = request.form.get("qrts", "")
            qrts2 = list(qrts)
            mytup = tuple(qrts2)
            mestawat = list(mytup)
            teklu = list(mytup)
            tekakelu = list(mytup)
            godolo = request.form.get("godolo", "")
            godolow = list(godolo)
            bzat = request.form.get("bzat", "")
            bzatu = list(bzat)
            ayneke = request.form.get("ayneke", "")
            aynekew = list(ayneke)
            tenshuashi = ['ለ-ሏ', 'ሠ-ሧ', 'ሰ-ሷ|ሠ-ሧ', 'ተ-ቷ', 'ነ-ኗ', 'ዘ-ዟ', 'ደ-ዷ', 'ጠ-ጧ', 'ጸ-ጿ|ፀ-ፇ', 'ፀ-ፇ']
            guadshua = ['lle', 'sse', 'sss', 'tte', 'nne', 'zze', 'dde', 'ttt', 'tse', 'tze']
            bota = len(qrts2)
            shuashi = ['ለ-ሏ|የ-ዯ', 'ሠ-ሧ|ሸ-ሿ', 'ሰ-ሷ|ሠ-ሧ|ሸ-ሿ', 'ተ-ቷ|ቸ-ቿ', 'ነ-ኗ|ኘ-ኟ', 'ዘ-ዟ|ዠ-ዧ', 'ደ-ዷ|ጀ-ጇ', 'ጠ-ጧ|ጨ-ጯ', 'ጸ-ጿ|ፀ-ፇ', 'ፀ-ፇ']
            res = {guadshua[u]: tenshuashi[u] for u in range(len(guadshua))}
            z=0
            for z in range(len(qrts2)):

                mestawat[z]='1,1'
                
                z+=1
            #print(mestawat)        
##            print (len(qrts2))
            for v in range(len(mestawat)) :
                if qrts2[v] in str(bzatu):
                    mestawat[v] = '1,2'
                elif qrts2[v] in str(godolow):
                    mestawat[v] = '0,1'
                else:
                    mestawat[v]='1,1'
            y=0
            for y in range(len(qrts2)):

                teklu[y]='49'
                
                y+=1
            #print(mestawat)        
            for k in range(len(teklu)) :
                if qrts2[k] in str(aynekew):
                    teklu[k] = '50'
                
                else:
                    teklu[k]='49'
##            #print(mestawat)
##            #print(mestawat[0])
##            #print(str(bzatu))
##            print(teklu)
##            print(teklu[0])
            
            for i in range(len(qrts2)):
             #for i in range(len(qrts2)):
                if qrts2[i] in 'ሀሁሂሃሄህሆሇ':
                    qrts2[i] = 'ሀ-ሇ|ሐ-ሗ|ኀ-ኍ|ኹ-ዅ'
            ##        qrts2[i] = 'ሇሏሗሟሧሯሷሿቋቇቛቧቯቷቿኋኇኗኟኧኯኳዃዏዟዧዯዷዿጇጓጏጟጧጯጷጿፇፏፗሆሎሖሞሦሮሶሾቆቖቦቮቶቾኆኖኞኦኮኾዎዖዞዦዮዶዾጆጎጞጦጮጶጾፆፎፖህልሕምሥርስሽቅቍቕቝብቭትችኅኍንኝእክኵኽዅውዕዝዥይድዽጅግጕጝጥጭጵጽፅፍፕሄሌሔሜሤሬሴሼቄቌቔቜቤቬቴቼኄኌኔኜኤኬኴኼዄዌዔዜዤዬዴዼጄጌጔጜጤጬጴጼፄፌፔሃላሓማሣራሳሻቃቓባቫታቻኃናኛኣካኻዋዓዛዣያዳዻጃጋጛጣጫጳጻፃፋፓሀለሐመሠረሰሸቀቈቐቘበቨተቸኀኈነኘአከኰኸዀወዐዘዠየደዸጀገጐጘጠጨጰጸፀፈፐሁሉሑሙሡሩሱሹቁቑቡቩቱቹኁኑኙኡኩኹዉዑዙዡዩዱዹጁጉጙጡጩጱጹፁፉፑሂሊሒሚሢሪሲሺቂቊቒቚቢቪቲቺኂኊኒኚኢኪኲኺዂዊዒዚዢዪዲዺጂጊጒጚጢጪጲጺፂፊፒፚፘፙ'
                elif qrts2[i] in 'ለሉሊላሌልሎሏ':
                    qrts2[i] = 'ለ-ሏ'
                elif qrts2[i] in 'ሐሑሒሓሔሕሖሗ':
                    qrts2[i] = 'ሐ-ሗ'
                elif qrts2[i] in 'መሙሚማሜምሞሟፙ':
                    qrts2[i] = 'መ-ሟ|ፙ'
                elif qrts2[i] in 'ሠሡሢሣሤሥሦሧ':
                    qrts2[i] = 'ሠ-ሧ'
                elif qrts2[i] in 'ረሩሪራሬርሮሯፘ':
                    qrts2[i] = 'ረ-ሯ|ፘ'
                elif qrts2[i] in 'ሰሱሲሳሴስሶሷ':
                    qrts2[i] = 'ሰ-ሷ|ሠ-ሧ'
                elif qrts2[i] in 'ሸሹሺሻሼሽሾሿ':
                    qrts2[i] = 'ሸ-ሿ'
                elif qrts2[i] in 'ቀቁቂቃቄቅቆቇቈቊቋቌቍ':   # እነ ቐቑቒቓቔቕቖቘቚቛቜቝ አልገቡም
                    qrts2[i] = 'ቀ-ቝ'
                elif qrts2[i] in 'በቡቢባቤብቦቧ':
                    qrts2[i] = 'በ-ቧ'
                elif qrts2[i] in 'ተቱቲታቴትቶቷ':
                    qrts2[i] = 'ተ-ቷ'
                elif qrts2[i] in 'ቸቹቺቻቼችቾቿ':
                    qrts2[i] = 'ቸ-ቿ'
                elif qrts2[i] in 'ኀኁኂኃኄኅኆኇኈኊኋኌኍ':
                    qrts2[i] = 'ኀ-ኍ'
                elif qrts2[i] in 'ነኑኒናኔንኖኗ':
                    qrts2[i] = 'ነ-ኗ'
                elif qrts2[i] in 'ኘኙኚኛኜኝኞኟ':
                    qrts2[i] = 'ኘ-ኟ'
                elif qrts2[i] in 'አኡኢኣኤእኦኧ':
                    qrts2[i] = 'አ-ኧ|ዐ-ዖ'
                elif qrts2[i] in 'ከኩኪካኬክኮኯኰኲኳኴኵ':
                    qrts2[i] = 'ከ-ኵ'
                elif qrts2[i] in 'ኸኹኺኻኼኽኾዀዂዃዄዅ':
                    qrts2[i] = 'ኸ-ዅ'
                elif qrts2[i] in 'ወዉዊዋዌውዎዏ':
                    qrts2[i] = 'ወ-ዏ'
                elif qrts2[i] in 'ዐዑዒዓዔዕዖ':
                    qrts2[i] = 'ዐ-ዖ' 
                elif qrts2[i] in 'ዘዙዚዛዜዝዞዟ':
                    qrts2[i] = 'ዘ-ዟ'
                elif qrts2[i] in 'ዠዡዢዣዤዥዦዧ':
                    qrts2[i] = 'ዠ-ዧ'
                elif qrts2[i] in 'የዩዪያዬይዮዯ':
                    qrts2[i] = 'የ-ዯ'
                elif qrts2[i] in 'ደዱዲዳዴድዶዷ':    #እነ ዸዹዺዻዼዽዾዿ አልገቡም
                    qrts2[i] = 'ደ-ዷ'
                elif qrts2[i] in 'ጀጁጂጃጄጅጆጇ':
                    qrts2[i] = 'ጀ-ጇ'
                elif qrts2[i] in 'ገጉጊጋጌግጎጏጐጒጓጔጕ':   #እነ ጘጙጚጛጜጝጞጟ አልገቡም
                    qrts2[i] = 'ገ-ጕ'
                elif qrts2[i] in 'ጠጡጢጣጤጥጦጧ':
                    qrts2[i] = 'ጠ-ጧ'
                elif qrts2[i] in 'ጨጩጪጫጬጭጮጯ':
                    qrts2[i] = 'ጨ-ጯ'
                elif qrts2[i] in 'ጰጱጲጳጴጵጶጷ':
                    qrts2[i] = 'ጰ-ጷ'
                elif qrts2[i] in 'ጸጹጺጻጼጽጾጿ':
                    qrts2[i] = 'ጸ-ጿ|ፀ-ፇ'
                elif qrts2[i] in 'ፀፁፂፃፄፅፆፇ':
                    qrts2[i] = 'ፀ-ፇ'
                elif qrts2[i] in 'ፈፉፊፋፌፍፎፏፚ':
                    qrts2[i] = 'ፈ-ፏ|ፚ'
                elif qrts2[i] in 'ፐፑፒፓፔፕፖፗ':
                    qrts2[i] = 'ፐ-ፗ'
                elif qrts2[i] in 'ቨቩቪቫቬቭቮቯ':
                    qrts2[i] = 'ቨ-ቯ'
                elif qrts2[i] == '0':
                    qrts2[i] = 'ሀ-ፚ'
                else :
                    qrts2[i] = qrts2[i]
            for k in range(len(qrts2)):
                if teklu[k]=='50':
                    qrts2[k]=tekakelu[k]
            print()
            qrts3=""
          
            yezore= len(qrts2)-1
            
            elmo=[]
            jaja=[]
            yaz=''
            oka=''
            for j in range(len(tenshuashi)) :
                for elem in range(yezore,-1,-1):
                    if qrts2[elem] == tenshuashi[j]:
                        yinshuashua = request.form.get(f"yinshuashua_{tenshuashi[j]}", "2")  # Default to '2' (No replacement)
                        if yinshuashua == '1':
##                        print(tenshuashi[j])
                            hoho=tenshuashi.index(str(tenshuashi[j]))
                            jaja.append(hoho)
##                        index_of_papa= papa.index(str(tenshuashi[j]))
##                        abo=int(index_of_papa)
##                        botawa=int(len(qrts2)-1-abo)                               
                            elmo.append(elem)
                            yaz=elmo[0] 
                            oka=jaja[0]
                    break
##            print(jaja)
     
            for w in range(len(qrts2)):
                if w==yaz:
                    qrts2[w]=shuashi[oka]
                else:
                    qrts2[w] = qrts2[w]
                                    
            for w in range(len(qrts2)):
               
                qrts3+='[' + str(qrts2[w])+']'+'{'+str(mestawat[w])+'}'     
                
##            print(qrts3)### ከፕሪንት መውጣት የሚችል
            Mircha = request.form.get("Mircha", "1")  # Default to '1'
            mircha = str(Mircha)
            for mircha in Mircha :
        
                if mircha == '1':
                    pattern = re.compile(('\\b')+(qrts3)+('\\b'))
                elif mircha == '2':
                    pattern = re.compile("(r'\\n|\s|\w*)"+(qrts3)+('\\b'))
                elif mircha == '3':
                    pattern = re.compile(('\\b')+(qrts3)+('\w*\s*'))    
                elif mircha == '4':
                    pattern = re.compile(("(r'\\n|\s|\w*)")+(qrts3)+('\w*\s*'))
                else:
                    print (repr(e))
                #print (pattern)
            print ('\n')
            for w in finalwords:
                matches = pattern.finditer(w)
                for match in matches :
                    matches_found.append(match.group())
        elif QrtsBett == "2":
            qrts = request.form.get("qrts2", "143")
            qrts2 = list(qrts)
            for i in range(len(qrts2)):
                if qrts2[i] == '0':
            ##        qrts2[i] = '\w*?'
                    qrts2[i] = 'ሇሏሗሟሧሯሷሿቋቇቛቧቯቷቿኋኇኗኟኧኯኳዃዏዟዧዯዷዿጇጓጏጟጧጯጷጿፇፏፗሆሎሖሞሦሮሶሾቆቖቦቮቶቾኆኖኞኦኮኾዎዖዞዦዮዶዾጆጎጞጦጮጶጾፆፎፖህልሕምሥርስሽቅቍቕቝብቭትችኅኍንኝእክኵኽዅውዕዝዥይድዽጅግጕጝጥጭጵጽፅፍፕሄሌሔሜሤሬሴሼቄቌቔቜቤቬቴቼኄኌኔኜኤኬኴኼዄዌዔዜዤዬዴዼጄጌጔጜጤጬጴጼፄፌፔሃላሓማሣራሳሻቃቓባቫታቻኃናኛኣካኻዋዓዛዣያዳዻጃጋጛጣጫጳጻፃፋፓሀለሐመሠረሰሸቀቈቐቘበቨተቸኀኈነኘአከኰኸዀወዐዘዠየደዸጀገጐጘጠጨጰጸፀፈፐሁሉሑሙሡሩሱሹቁቑቡቩቱቹኁኑኙኡኩኹዉዑዙዡዩዱዹጁጉጙጡጩጱጹፁፉፑሂሊሒሚሢሪሲሺቂቊቒቚቢቪቲቺኂኊኒኚኢኪኲኺዂዊዒዚዢዪዲዺጂጊጒጚጢጪጲጺፂፊፒፚፘፙ'
                elif qrts2[i] == '1':
                    qrts2[i] = 'ሀለሐመሠረሰሸቀቈቐቘበቨተቸኀኈነኘአከኰኸዀወዐዘዠየደዸጀገጐጘጠጨጰጸፀፈፐ'
                elif qrts2[i] == '2':
                    qrts2[i] = 'ሁሉሑሙሡሩሱሹቁቑቡቩቱቹኁኑኙኡኩኹዉዑዙዡዩዱዹጁጉጙጡጩጱጹፁፉፑ'
                elif qrts2[i] == '3':
                    qrts2[i] = 'ሂሊሒሚሢሪሲሺቂቊቒቚቢቪቲቺኂኊኒኚኢኪኲኺዂዊዒዚዢዪዲዺጂጊጒጚጢጪጲጺፂፊፒፚፘፙ'
                elif qrts2[i] == '4':
                    qrts2[i] = 'ሃላሓማሣራሳሻቃቓባቫታቻኃናኛኣካኻዋዓዛዣያዳዻጃጋጛጣጫጳጻፃፋፓ'
                elif qrts2[i] == '5':
                    qrts2[i] = 'ሄሌሔሜሤሬሴሼቄቌቔቜቤቬቴቼኄኌኔኜኤኬኴኼዄዌዔዜዤዬዴዼጄጌጔጜጤጬጴጼፄፌፔ'
                elif qrts2[i] == '6':
                    qrts2[i] = 'ህልሕምሥርስሽቅቍቕቝብቭትችኅኍንኝእክኵኽዅውዕዝዥይድዽጅግጕጝጥጭጵጽፅፍፕ'
                elif qrts2[i] == '7':
                    qrts2[i] = 'ሆሎሖሞሦሮሶሾቆቖቦቮቶቾኆኖኞኦኮኾዎዖዞዦዮዶዾጆጎጞጦጮጶጾፆፎፖ'
                elif qrts2[i] == '8':
                    qrts2[i] = 'ሇሏሗሟሧሯሷሿቋቇቛቧቯቷቿኋኇኗኟኧኯኳዃዏዟዧዯዷዿጇጓጏጟጧጯጷጿፇፏፗ'
                else :
                    qrts2[i] = qrts2[i]
            #print(qrts2)
            qrts3=""
            for w in qrts2:
                qrts3+='[' + str(w)+']'
            #print(qrts3)### ከፕሪንት መውጣት የሚችል
            Mircha = request.form.get("Mircha2", "1")  # Default to '1'
            mircha = str(Mircha)
            for mircha in Mircha :
        
                if mircha == '1':
                    pattern = re.compile(('\\b')+(qrts3)+('\\b'))
                elif mircha == '2':
                    pattern = re.compile("(r'\\n|\s|\w*)"+(qrts3)+('\\b'))
                elif mircha == '3':
                    pattern = re.compile(('\\b')+(qrts3)+('\w*\s*'))    
                elif mircha == '4':
                    pattern = re.compile(("(r'\\n|\s|\w*)")+(qrts3)+('\w*\s*'))
                else:
                    print (repr(e))
                #print (pattern)### ከፕሪንት መውጣት የሚችል
    #በቅርጽ ለማሰስ የተዘጋጀ
            print ('\n')
            for w in finalwords:
                matches = pattern.finditer(w)
                for match in matches :
                    matches_found.append(match.group())
        elif QrtsBett == "3":
            qrts3="(((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ን)(ደኛ|ዱ|ዲ|ዳ|ዴ|ዶ|ዷ))|((ሁ|ሑ|ኁ|ኹ)(ለ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሦ|ሶ)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ራ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ም)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ስ|ሥ)(ድ)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሰ|ሠ)(ባ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ስ|ሥ)(ም)(ን)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ዘ)(ጠ)(ኙ|ነኛ|ኜ|ኟ|ኖች|ኞ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ስ|ሥ)(ረኛ|ሩ|ሬ|ር|ሮ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ስ|ሥ)(ራ|ሯ))|((ሀ|ሃ|ሐ|ሓ|ኀ|ኃ|ሓ|ኻ)(ያ))|((ሰ|ሠ)(ላ)(ሳ|ሣ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ር)(ባ))|((ሀ|ሃ|ሐ|ሓ|ኀ|ኃ|ሓ|ኻ|አ|ኣ|ዐ|ዓ|ካ|ባ|ላ|ያ|ታ)(ም)(ሣ|ሳ|ሶቹ))|((ስ|ሥ)(ድ|ል)(ሣ|ሳ))|((ሰ|ሠ)(ባ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሰ|ሠ)(ማ)(ን|ኖቹ)(ያ))|((ዘ)(ጠ)(ና|ኖቹ))|((መ)(ቶ))|((ሺ|ሽ)(ህ|ሕ|ኅ|ኽ))|((ሚ|ም)(ል|ሊ|ለ)(የ|ዮ)(ን))|((እ|ዕ)(ል)(ፍ))|((አ|ኣ|ዐ|ዓ)(ዕ|እ)(ላ)(ፍ|ፋ)))"
            Mircha = request.form.get("Mircha3", "1")
            mircha = str(Mircha)
            print("Mircha: " + Mircha + " mircha: " + mircha)
            if mircha == '1':
                pattern = re.compile(("(r'\\n|\s|\w*)")+('[0-9፩-፱፲-፼]{1,}')+('\w*\s*'))
            elif mircha == '2':
                pattern = re.compile(("(r'\\n|\s|\w*)")+(qrts3)+('\w*\s*')) #አዲስ የተጨመረ የላይኞቹ ኮሜንት ስለተደረጉ 
            else:
                print (repr(e))

            for w in newwords: # new words ተባለ final words ነበረ
                matches = pattern.finditer(w)
                for match in matches :
                    matches_found.append(match.group())
        else:
            result = "Invalid option selected"

        matches_html = "".join(f"<li>{m}</li>" for m in matches_found)
        return f"""
            <h1>Processing Complete</h1>
            <h2>Matches Found:</h2>
            <ul>{matches_html}</ul>
        """
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(debug=True)
