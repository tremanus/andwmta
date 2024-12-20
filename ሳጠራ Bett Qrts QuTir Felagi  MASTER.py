def main ():
    import time
    start=time.time()
    import re
    x = int(input ('የሚቆረጠውን የመግቢያ ፊደላት እርዝመት አስገባ ቁጥር አስገባ : ' ))+1
    aya = input ('የሰነድ ስም :')
    filetype = '.txt'
    filename = aya + filetype
    print (filename)
    f = open(filename,'r', encoding="utf-8") #read in Alice
    text = f.read()
    f.close()
    text = text[0:] #strip header
    #convert to lower case
    ##lowertext = text.lower() ለአማርኛ አያስፈልግም
    #punctuation to convert
    #punc = '[\.\?\-!\?\*,"\(\):\`\[\];_/~]'
    punc = '[\?\-!\?\*,"\(\):\`\[\];_/~፣፡።፤፥፦]'
    #convert punctuation to space
    newtext = ''
    for c in text:
        if re.search(punc,c):
            newtext += ' '
        else:
            newtext += c
    words = newtext.split() #split into words
    #eliminate single quotes
    newwords = []
    for w in words:
        word = ''
        for c in w:
            if c != "'":
                word += c
        newwords.append(word)
    #eliminate words with numbers

    finalwords = []
    for w in newwords:
        if re.search('[0-9፩-፱፲-፼]',w):
            continue
        else:
            finalwords.append(w)

    lengthedword = []
    
    QrtsBett = input('\n ቃላቶች በምን መልክ እንዲታሠሡልህ ትፈልጋለህ? \n @@@@@@ በቤት እንዲታሠሡ 1 አስገባ \n @@@@@@ በቅርጽ እንዲታሠሡ 2 አስገባ \n @@@@@@ ቁጥሮች እንዲታሠሡ 3 አስገባ \n ')
    qb = str(QrtsBett)
    for qb in QrtsBett:
        if qb == '1' :
            qrts = input('\n የምትፈልጋቸውን ፊደል ቤቶች በፈለከው ቤት ግን በቅደም ተከተል አስገባ ለማንኛውም ፊደል ቤት 0 ቁጥርን ተጠቀም')
            qrts2 = list(qrts)
            mytup=tuple(qrts2)
            mestawat=list(mytup)
            teklu=list(mytup)
            tekakelu=list(mytup)
            godolo = input('\n ከላይ ቢጎድልም ቅር የማይልህ የፊደል ቤት ካለ አስገባው')
            godolow = list(godolo)
            bzat = input('\n ከላይ እንዲደገም የምትፈልገው የፊደል ቤት ካለ አስገባ')
            bzatu = list(bzat)
            ayneke = input('\n ከላይ ካስገባሃሸው ፊደላት ራሱ ሳይቀያየር እንዲቆይ የምትፈልገውን ፊደል አስገባ')
            aynekew = list(ayneke)
            tenshuashi=['ለ-ሏ','ሠ-ሧ','ሰ-ሷ|ሠ-ሧ','ተ-ቷ','ነ-ኗ','ዘ-ዟ','ደ-ዷ','ጠ-ጧ','ጸ-ጿ|ፀ-ፇ','ፀ-ፇ']
            guadshua=['lle','sse','sss','tte','nne','zze','dde','ttt','tse','tze']
            bota=len(qrts2)
            shuashi=['ለ-ሏ|የ-ዯ','ሠ-ሧ|ሸ-ሿ','ሰ-ሷ|ሠ-ሧ|ሸ-ሿ','ተ-ቷ|ቸ-ቿ','ነ-ኗ|ኘ-ኟ','ዘ-ዟ|ዠ-ዧ','ደ-ዷ|ጀ-ጇ','ጠ-ጧ|ጨ-ጯ','ጸ-ጿ|ፀ-ፇ','ፀ-ፇ']
            res = {guadshua[u]: tenshuashi[u] for u in range(len(guadshua))}
            #res2={guadshua[u]: shuashi[u] for u in range(len(guadshua))}
            #print(qrts2)### ከፕሪንት መውጣት የሚችል
##            myfreqdict={"p":"1,1","q":"0,1","r":"1,2"}
##            p=1,1
##            q=0,1
##            r=1,2
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
            #papa=list(yezore)
            #hani=tuple(papa)
            #gogo=list(hani)
            
            elmo=[]
            jaja=[]
            yaz=''
            oka=''
            for j in range(len(tenshuashi)) :
                for elem in range(yezore,-1,-1):
                    if qrts2[elem] == tenshuashi[j]:
                        yinshuashua=input('\n የ  "'+tenshuashi[j] +'"  ቤት ይንሿሿልህ ወይ? \n @@@@@ ለአዎ 1 አስገባ \n @@@@@ ለአይ 2 አስገባ?')
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
##            print(elmo)
             
##            print(yaz)
##            print(oka)
##            
            for w in range(len(qrts2)):
                if w==yaz:
                    qrts2[w]=shuashi[oka]
                else:
                    qrts2[w] = qrts2[w]
                                    
            for w in range(len(qrts2)):
               
                qrts3+='[' + str(qrts2[w])+']'+'{'+str(mestawat[w])+'}'     
                
##            print(qrts3)### ከፕሪንት መውጣት የሚችል
            Mircha = input('\n የመረጥካቸው ቤቶች ቅደም ትከተል\n @@@ ዕቅጩን እንዲታሰስ 1 አስገባ \n @@@ ከፊት ብቻ  ቅጥያም እንዲጨመር 2 አስገባ\n @@@ ከኋላ ብቻ ቅጥያም እንዲጨመር 3 አስገባ\n @@@ ከፊት እና ከኋላ ቅጥያም እንዲጨመር 4 አስገባ')
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
                    print(match.group())
        elif qb == '2' :
            qrts = input('\n የምትፈልገውን ቅርጽ በቁጥር መልክ አስገባ ለማንኛውም ቅርጽ መደብ 0 ቁጥርን ተጠቀም')
            qrts2 = list(qrts)
            #print(qrts2)
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
            Mircha = input('\n የመረጥካቸው ቤቶች ቅደም ትከተል\n @@@ ዕቅጩን እንዲታሰስ 1 አስገባ \n @@@ ከፊት ብቻ  ቅጥያም እንዲጨመር 2 አስገባ\n @@@ ከኋላ ብቻ ቅጥያም እንዲጨመር 3 አስገባ\n @@@ ከፊት እና ከኋላ ቅጥያም እንዲጨመር 4 አስገባ')
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
                    print(match.group())
        elif qb == '3':
            qrts3="(((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ን)(ደኛ|ዱ|ዲ|ዳ|ዴ|ዶ|ዷ))|((ሁ|ሑ|ኁ|ኹ)(ለ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሦ|ሶ)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ራ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ም)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ስ|ሥ)(ድ)(ስ|ሥ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሰ|ሠ)(ባ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ስ|ሥ)(ም)(ን)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ዘ)(ጠ)(ኙ|ነኛ|ኜ|ኟ|ኖች|ኞ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ስ|ሥ)(ረኛ|ሩ|ሬ|ር|ሮ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ስ|ሥ)(ራ|ሯ))|((ሀ|ሃ|ሐ|ሓ|ኀ|ኃ|ሓ|ኻ)(ያ))|((ሰ|ሠ)(ላ)(ሳ|ሣ))|((አ|ኣ|ዐ|ዓ|ካ|ባ|ያ|ላ|ታ)(ር)(ባ))|((ሀ|ሃ|ሐ|ሓ|ኀ|ኃ|ሓ|ኻ|አ|ኣ|ዐ|ዓ|ካ|ባ|ላ|ያ|ታ)(ም)(ሣ|ሳ|ሶቹ))|((ስ|ሥ)(ድ|ል)(ሣ|ሳ))|((ሰ|ሠ)(ባ)(ተኛ|ቱ|ታ|ቴ|ት|ቶ|ቷ))|((ሰ|ሠ)(ማ)(ን|ኖቹ)(ያ))|((ዘ)(ጠ)(ና|ኖቹ))|((መ)(ቶ))|((ሺ|ሽ)(ህ|ሕ|ኅ|ኽ))|((ሚ|ም)(ል|ሊ|ለ)(የ|ዮ)(ን))|((እ|ዕ)(ል)(ፍ))|((አ|ኣ|ዐ|ዓ)(ዕ|እ)(ላ)(ፍ|ፋ)))"
            Mircha = input('\n የቁጥሮችን ፍለጋ ለማድረግ \n @@@ በአሃዝ ያሉትን ለማሰስ 1 አስገባ \n @@@ በፊደል ያሉትን ለማሰስ 2 አስገባ \n')
            mircha = str(Mircha)
            for mircha in Mircha :
        
                if mircha == '1':
                    pattern = re.compile(("(r'\\n|\s|\w*)")+('[0-9፩-፱፲-፼]{1,}')+('\w*\s*'))
                elif mircha == '2':
                    pattern = re.compile(("(r'\\n|\s|\w*)")+(qrts3)+('\w*\s*')) #አዲስ የተጨመረ የላይኞቹ ኮሜንት ስለተደረጉ 
                else:
                    print (repr(e))
            #print (pattern)
     #

    #በቅርጽ ለማሰስ የተዘጋጀ
    # በቅላት ባውንደሪ \b ከፊትና ኋላ በመለየት በቅርጽ ልክ ወይም ባነሰ የቅርጽ ቅደም ተከተል ለማሰስ መዘጋጀት ያለበት
    #\b adrgo keza [any][][][][any][][0]
            print ('\n')
            for w in newwords: # new words ተባለ final words ነበረ
                matches = pattern.finditer(w)
                for match in matches :
                    print(match.group()) 
        else:
            print (repr(e))
            
     ### ከፕሪንት መውጣት የሚችል

    TiyaQe = input('\n ዐረፍተ ነገሮቹ ይለቀሙልህ ወይ?\n @@@ ለአዎ 1 አስገባ\n @@@ ይቅር ለማለት 2 አስገባ @@@@@@')
    mels = str(TiyaQe)
    for mels in TiyaQe:
        if mels == '1' :
            def getsentences(t):
                splitters = '።?!' #characters to split on
                ss = [] #put sentences here
                i = 0
                        #go character by character
                while i < len(t):
                    s = '' #reset current sentence
                    #read to end of text or
                    #end of a sentence
                    while i < len(t) and \
                        t[i] not in splitters:
                            s += t[i]
                            i += 1
                        #if text isn't over, current character
                        #is splitter and should be appended
                    if i < len(t):
                        s += t[i]
                    i += 1 #go on to next character
                    ss.append(s) #add sentence to list
                return ss
            s = getsentences(text)

            print ('\n')
            for z in range(len(s)):
                mematch=re.finditer(pattern,s[z])
                for matcha in mematch:
                    print(matcha,s[z])
                  
        elif mels == '2' :
            pass
        else:
            print (repr(e))

        

    print()
    end=time.time()
    print(f"Runtime of the program is {end-start}")
    
if __name__ =="__main__": main ()
