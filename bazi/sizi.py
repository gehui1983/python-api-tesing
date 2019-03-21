#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# 鸣谢 https://github.com/yuangu/sxtwl_cpp/tree/master/python
# CreateDate: 2019-2-21

summarys = {
    '甲日甲子': '''
    甲日甲子时,虽甲败在子,暗有癸水生气印绶,兼有官(海中金)生其印,若己土破印,通月气,贵。
    否则,秀而不实。  -- 如果有己土化比肩为佳。
    ''',

       '甲日乙丑': '''
    劫财羊刃不宜有；柱中逢火带辛金，制伏和平贵亦久。
    乙克丑中的财；乙丑为海中金，若年日时合成火局，制伏金，主德性纯和而贵；无火凶狠；如合水局凶恶损家。


    贵人天乙被乙劫财伤害。火局南方运贵，金神制伏相当。木枯水盛且平常，背祖离乡晚旺。
    ''',  

       '甲日丙寅': '''
    甲木寅上健旺，丙为食神, 且通火气, 寿星在位  
    通火木月气者贵，忌见官星及申冲禄。
    甲丙相邀入虎乡，福星坐禄显文章；运逢四柱无伤害，早晚陛迁至宪堂。
    若逢辰戌，两三妻，禄主朝元富贵。丁午庚申减福，无官惹绊为奇。
    生来贵显有人提，此命先难后易。
    ''',

       '甲日丁卯': '''
    伤官羊刃真当恼；纵然月气有扶持，未免为人性不好。
    乙木克己财，为人凶狠。若柱透辛，伤官见官，刑害百端，运气凶险，不得善终；
    柱有七煞合刃，行财官印绶，大贵。
    甲逢丁火化为灰，父母兄弟难倚。祖业田财聚散，妻儿总有刑亏。运行官煞始为奇，性格或嗔或喜。
    ''',     

       '甲日戊辰': '''
    天财坐库会滋身；富商巨贾田园盛，月带辛金名利成。时上偏财，遇龙守库。主为商贾发财，田园广盛。
    八月带禄，财官俱有，富贵双全。忌比肩、羊刃夺财。
    时上偏财不用多，干枝内外细搜罗；运通财旺官生至，运拙身衰恐受磨。甲日戊辰时遇，柱中要戌相扶。
    辛庚透干贵显，壬癸滋助不枯。只怕比劫弟兄多，岁运逢之有祸。
    ''',       

       '甲日己巳': '''
    病中财物实难任；月通火气方为贵，若是身衰亦不禁。
    食旺身衰，甲木巳上病，虽有暗戊为财，丙为食，不通月气，难任其福。
    甲己为平头煞，生逢春月，身旺财衰，主骨肉参商，平生作事，弄巧成拙。
    己巳金神有火制伏，巳酉丑合局，行南方运，名重禄高。柱不见火，残害化气，主凶恶暴亡。

    甲己中央作土神，时逢辰已脱埃尘；局中岁运趋炎火，显远功名富贵人。
    甲日时逢己巳，火临土厚无光。旱苗得雨叶枝强，火局金神旺相。
    进士有名无实，常人改祖番庄。为人性格不寻常，运至晚年气象。
    ''',          

       '甲日庚午': '''
    死地逢鬼，甲木死于午，午头见庚为鬼，不通月气，无救助者，带疾寿促。
    月逢丙寅，身旺庚绝则吉，亦主有始无终。若通木气，主方面，通水气，行东方运，止郎官。

    午时庚申是偏官，制伏相宜不等闲；身弱煞强无食见，平生谋望主艰难。
    甲日时逢庚午，柱中喜见寅申。身强煞浅转精神，父母雁行不顺。
    妻子早年刑害，晚年出众超群。平生反复好翻腾，先破后成之命。
    ''',   

       '甲日辛未': '''
    甲日辛未时，时贵逢官，甲见辛为官，未有天乙贵；己为财，未中己土得气，若通木气月，
    有寄托者富；通土气月者，富贵双全。

    甲逢辛未是财官，平步青云路不难；不比退毛鸡化凤，得时飞上彩云路。
    甲日时逢辛未，财官守库相扶。贵人财禄是良图，初苦未终荣富。君子迁官进职，常人丰厚充腴。
    刑冲破害柱中无，定得青云之路。
    ''',       

       '甲日壬申': '''
    六甲生时遇壬申，明伤暗鬼坐其身；柱无丙戊秋冬旺，坎坷飘流无定人。
    甲日壬申时，甲木绝在申，申土壬水长生，庚金建禄，明袅暗鬼，甲旺化鬼为官，犹不免凶暴。
    若生秋庚旺，生冬壬旺，柱无丙戊制伏，漂流之象。若巳午月，大吉。强横透庚，作煞论，运行北方，贵。

    甲日时逢喜遇申，偏官偏印怕刑冲；欲求名利终难定，有救须教运气通。
    甲日时逢壬申，倒食暗鬼相侵。生逢身旺主昌荣，身弱性情不定。
    雁侣六亲少力，谋为自立自成。运行吉地显声名，运弱平常之命。
    ''',      

       '甲日癸酉': '''
    暗官明印未希奇；柱中有火无刑破，元命胎生贵可知。
    甲日癸酉时，胎生元命，甲木酉上受胎，为甲生气，明癸为印，暗辛为官，有己土破印，不贵。
    酉为金神，若柱有寅戌，通火气者，德性纯厚而贵。无火见水，凶暴残疾。
    甲日交通癸酉时，金神火局两相宜；运行南地无刑破，富贵荣华事事奇。
    甲日时逢癸酉，为人富贵双全。三奇发福屡升迁，上下相和贵显。
    君子寒门将相，常人置立田园。无伤无破是英贤，此命定居台宪。
    ''',     

       '甲日甲戌': '''
    六甲日生时甲戌，木遭火局气不舒；好善福平常，父母并伤。
    -- 甲木在 山头火。
    甲日甲戌时，甲用丙为食，辛为官，戌上食神入火局，辛有余气，身被火焚，为人好善，平常衣禄。
    -- 甲木克戌中戊，为克父
    甲以戊为父，癸为母，戌上旺甲伤戊，内有暗戊伤癸，戊癸受克，难为二亲。

    时逢甲戌比肩逢，库有天禄火气冲；鸡鸭同鸣皆聚散，到头心志不相同。
    甲日时通甲戌，比肩带禄相逢。天孤仓库隐其中，酉丑辰支取用。
    无钥冲刑开破，立身多学少成。柱金木火旺火生，先暗后明之命。
    ''',   

       '甲日乙亥': '''
    六甲日生时乙亥，羊刃反伤为祸害；财官辛戊不相逢，只恐功名不亨泰。
    甲日乙亥时，甲木亥上长生有旺，乙为刃，制克学堂，壬为倒食，亥上建禄。
    甲以金为官，戊己为财，辛金沐浴，戊己衰绝，不能作福。
    生巳酉丑月及见辛，柱有戊字，贵。余虽聪明，功名不遂，艺术人也。

    甲日时逢乙亥强，有官有印不寻常；时来自有高人荐，运至财乡大显扬。
    甲日时逢乙亥，就中壬水相生。时临帝座紫微宫，子嗣螟蛉得用。父母雁行少力，花开结子。
    ''',    

       '乙日丙子': '''
    六乙日生时丙子，伤官坐贵福不全；柱中不见官刑破，方是平生贵禄缘。
    乙日丙子时，六乙鼠贵。乙用庚为官，死于子；见丙为伤，丙暗邀辛化煞为权，柱中不见庚辛，
    无丑绊午冲，方成格，贵。若有上忌及不通月气，无救助者，暴恶贫下，有疾寿促。

    六乙贵格丙子时，如无冲破始为奇；不遇庚申巳酉丑，定乘轩冕拜丹墀。
    乙日时临丙子，伤官伤尽荣昌。亥卯未月不寻常，运至身健旺相。辛庚不见发福，午冲丑绊平常。如逢刑克空一场。
    此命或衰或旺。
    ''',     
       '乙日丁丑': '''
    六乙日生时丁丑，食神相助遇财官；月通金气化为福，不是寻常下贱看。
    乙日丁丑时，食会财官，丁为食，庚为官，己为财，丑中有辛金合局，己土得位，如有倚托者，贵。
    通金气月化者，富厚尊重；不通月气，平常。

    仓库时开乙见丁，食神坐库禄财亲。无匙不作朝中客，也是清闲有福人。
    乙日时逢丁丑，寿星发达无疑，身居磨蝎莫嫌迟，库内钱财积聚。
    年时月合发达，空刑妻子难为。双亲雁侣有盈亏，运至牢藏金柜。
    ''',      
       '乙日戊寅': '''
    六乙日生时戊寅，败财背禄实伤身；有心无力多成败，止是平常衣禄人。
    六乙日戊寅时，败财背禄，乙用庚为官，寅中有丙，伤官背禄：
    用戊己为财，寅中甲旺财败，为人作事成败平常。通土气者吉。

    乙日寅时仔细推，为人招是又招非；运衰更遇空刑克，劳力劳心无定期。
    乙日戊寅时遇，就是暗损伤财。伤官背禄柱中排，富贵妻儿刑害。
    运旺财官发福，运行比煞兴灾。六亲骨肉少和谐，自立自成自在。
    ''',    
       '乙日己卯': '''
    六乙日生逢己卯，时居日禄财临好；旺通木气贵无疑，金重亦可恼。
    乙日己卯时，禄入庙堂，乙木逢卯建禄，为人秀丽，通木火者贵。见庚辛为伤禄破命，患目疾。
    若生巳酉丑月，平常衣禄。辰戌未，吉。申月亦吉。

    日禄居时格不同，食神则马要相逢；伤官印运皆为吉，官不逢兮禄自丰。
    乙日时临己卯，偏财时禄归迎。辛金酉字不相刑，虎榜定标名姓。
    父母六亲难靠，雁行各自飞腾，文章光耀有才能，无破无冲贵命。
    ''',  

       '乙日庚辰': '''
    六乙日生时庚辰，水白金清化象真；
    壬从辛酉通官贵，却防目疾减精神。
    乙日庚辰时，妻贤子贵。乙合庚化金，若通申巳酉丑月，
    为人秀丽，主贵，却防目疾。如不见化，以壬为印，庚为官，
    辰土癸水合局，乙木有托，行东南运，贵显平和。

    乙庚相会贵无疑，阴木阳金正合时；
    运吉身强无冲破，升迁自有贵人提。
    乙日庚辰时正，天官守库乾元，青年虎榜姓名传，禀性温良恭俭。士庶妻贤子贵。
    财人禄位升迁。南离戊癸火相连。富贵之中当险。
    ''',     

       '乙日辛巳': '''
    六乙日生时辛巳，金木交争主不仁；有化月中身旺贵，不通无化恐伤人。
    乙日辛巳时，暗金交争，是非日有，若通身旺月，有倚托，化鬼为官，行身旺运，贵。
    通木气月，行金旺运，大贵。通金气月，行身旺运，亦贵。

    乙巳相伤逢金木，求名求利常反复；
    六亲骨肉有如无，印绶运乡能发福。
    乙日时逢辛巳，柱中鬼旺身衰。六亲难靠不和谐，谋望有成有败。
    几度遇凶则吉，信知苦尽甘来。运行身旺印绶怀，富贵时人喝采。
    ''',        

       '乙日壬午': '''
    六乙日生时壬午，印绶生身财食聚；
    月通水木禄丰盈，不通月气平常数。
    乙日壬午时，印绶学堂，乙木长生在午，见壬为印，用丁为食，己为财，午上丁己建旺，
    若通水月气者，文章秀丽；不通月气，平常衣禄，通运亦好。

    乙日生逢壬午时，月通水木贵人钦；运行官旺无冲破，家业丰隆事称心。
    乙日时逢壬午，食神印绶同宫。无冲无破不相刑，信是声名响应。
    词馆清秀高士，文章出众超群，贵人喜见小人憎，中末峥嵘之命。
    ''',           

       '乙日癸未': '''
    六乙日生时癸未，入墓之中遇倒伤；马劣财微食见克，一生衣禄主平常。
    倒食食神，己土偏财，破癸癸倒未中丁火之食，平常衣禄。
    通土气月则吉。

    乙日相逢时癸未，算来离祖不成家；有刑克害多成败，运吉如添锦上花。
    乙日相逢癸未，生逢木墓夭孤。雁行兄弟有如无，心性不常喜怒。
    自立自成事业，六亲骨肉亲疏，贵人得合两相扶，此命先贫后富。
    ''',        

       '乙日甲申': '''
    六乙日生时甲申，官星得印位生成；月中通气无冲破，必定荣华仕路人。
    乙日甲申时，官印生身，乙用庚为官，壬为印，申上庚旺
    壬生，身有寄托，通金水月运者贵；不通，身弱官重，虽贵不永。

    乙日相逢时遇甲，长生驿马内相亲；贵人天乙来相助，释却褐衣入紫宸。
    乙日申时逢贵，其间高人见喜。小人称美有奇希，克破冲刑减力。
    身旺运逢吉地，信知两旺财官。有鞍有马有衣冠，定主门庭改换。
    ''',          

       '乙日乙酉': '''
    六乙日生时乙酉，得逢金局火为奇；用神遇木重重见，鬼绝寿伤反无依。
    乙日乙酉时，身绝鬼旺，乙以辛为鬼，酉上辛旺乙绝。
    若通巳酉丑月，化金局者贵。如用神坐木，身旺不化，又见于酉，不夭必贫。

    日干是乙时临酉，假煞为权身旺奇；身弱遇官徒费力，功名须待运通时。
    乙日时临乙酉，诞辰乙木无忧。其中权贵任求谋，无破功名定有。
    妻子早年克害，财源雨散云收。迁宗移祖免忧愁。中末家资成就。
    ''',    

       '乙日丙戌': '''
    六乙日生时丙戌，鬼败临身有损伤；若不气通身旺月，孤贫劳碌苦难当。
    鬼败临身，戌中有辛余气、丙丁库，食神制煞，若柱透庚，伤官见官，为祸百端；
    年月有寅午(三会)，丙火合局，即一木叠逢火位，主人傲物气高，衣禄平常，残疾，不然寿促。
    通身旺月气者，吉。

    乙日丙戌时火库，藏辛遇丑乃吉昌；若也运逢凶克害，算来此命且如常。
    乙日相逢丙戌，伤官库木枝枯。不临辛丑钥匙无。难倚六亲父母，雁侣分飞不睦，于人心悲成疏。
    要知发福改门闾，此命后甜先苦
    ''',   


       '乙日丁亥': '''
    六乙日生丁亥时，食神印绶亦奇哉；月气水土无财贵，切忌伤妻与子灾。
    乙日丁亥时，死处逢生，乙木死，亥却气壬水为生气印绶，
    乙用丁为食，亥中丁坐无气，喜甲木生，助丁食为福。如遇金局，行水运者，防目疾。
    四柱见财，或行财运、贪财坏印，主破财。戊为财为妻，庚为官为子，亥上庚绝土病，妻衰子少。

    时上生逢亥与丁，食神乙木遇长生；月气相扶为最贵，身衰无倚是常人。
    乙日时逢丁亥，食神印绶相扶。长生得意好无伤，荣显清名贵遇。
    喜逢丁壬化气，运临冠带迁除。无机妙法实难窥，丙己寅申减贵。
    ''',    

       '丙日戊子': '''
    六丙日生时戊子，财官生旺遇食神；月气相扶为最贵，身衰夫倚是常人。
    丙日戊子时，官旺财生，丙用辛为财，癸为官，丙合辛，戊合癸，子中癸旺辛生，丙火无气。
    若通火气，月有倚托者贵；不通贫下。通木气亦吉。

    活计生涯四季隆，丙逢戊子食官同；无伤晚岁皆成就，吉处遭凶险处通。
    丙子时逢戊子，官星食福同排。午丁未遇且沉埋，交通中年大快。
    父母妻子喜合。胸中隐匿文才。若逢好运一时来，富贵清闲自在。
    ''',     

       '丙日己丑': '''
    六丙日生时己丑，官鬼相生禄不成；若见申庚并乙旺，不求财禄过平生。
    丙日己丑时，伤官背禄，傲物志高。丙用癸为官，丑中有癸余气，被明暗土伤，柱透癸为祸。
    若见庚辛，伤官生财，却为福庆。

    丙日财官库里藏，戌辰未字显文章；身衰若也无匙钥，求名求利总平常。
    丙日时逢己丑，伤官财库暗藏。运交未戌不寻常。破出财官必旺。
    近贵谋夺劫财，算来虽有害。六亲真假少和谐，直断依时莫怪。
    ''',         

       '丙日庚寅': '''
    六丙日生时庚寅，学堂生气助其身；运中有合通金局，必是荣华富贵人。
    丙日庚寅时，生气学堂，丙寅上长生，文章秀气；丙以庚辛为财，寅上庚绝丙旺。
    若通月气金局者财旺，富贵双全，喜西方运；不通局者财薄。

    丙庚相合遇寅时，险难消除福自随；运至寒门名将相，时来平步上云梯。
    丙日庚寅时准，双亲衰旺离乡。妻儿早害晚荣昌，白虎归山正旺。
    木有成林松柏，生涯广聚财粮。堆金积玉满高堂，共羡人言上样。
    ''',  

       '丁日壬寅': '''
    六丁日生时壬寅，身去从官化木神；水木月通成局象，尊荣安富贵无伦。
    丁日壬寅时，身去从官，丁壬化木，寅上健旺，若水局之月，大贵；通木月亦贵。
    如丁未月，行东方运，好。

    丁亥日壬寅时，日贵格，配合壬寅，官印俱全，文章显达。子月，大贵，化气凶。

    丁壬合化入金乡，狗禄蝇名空自忙；节概衰残无足取，眼前骨肉亦参商。
    丁日壬寅时合，化局木旺之乡。月支申酉不相逢，得意高人荐用。
    父母雁行少力，外人喜笑春风，运逢水木没金踪，贵显荣达之命。
    ''',         

       '戊日己未':'''
    六戊日生时己未，羊刃偏官不怕冲；但是为人多性狠，平生衣禄亦无凶。
    戊日己未时，羊刃偏官，戊以己为羊刃，甲为偏官，时上明暗二己为刃，甲木未中合局，若见刑冲破害，刃煞有制，主贵。
    通月旺者平常衣禄，二十年，父母俱失；若不通月气，得寅申者贵。

    未中戊己土成堆，刑害冲来事亦谐；先暗后明凶变吉，贵人提携出尘埋。
    戊日时临己未，六亲骨肉成疏。喜逢火印暗中扶，甲乙寅卯为主。
    重谢花开结果，双亲雁行夭孤。自为自立自图谋，赖有贵人扶助。
    ''', 
       
    '辛日戊子':'''
    六辛日生时戊子，印绶学堂坐食神；不见丙丁同午破，必是荣华贵显人。
    辛日戊子时，六阴朝阳。辛金子上长生学堂。辛以戊为印。癸为食，时上明戊暗癸，
    柱中不见丙丁午字，冲开；通身旺月，大贵；犯者不贵。不通月气，通运，亦贵。
    
    
    天元六辛子时生，春天花开灿烂明。丙已午丁如破坏，功名难望晚方成。
    辛日时逢戊子，六阴会合朝阳。金神印绶显威光，相助一身荣旺。已午逢之减福，丙离雁侣尊堂。
    妻子勤助旺家庄、无破寒门将相。
   ''',            
       
    '辛日己丑':'''
    六辛日生时己丑，金土持争势不安；年月财官相救助，免交贫困受饥寒。
    辛日己丑时，金土相争。辛以己为倒食，丑上有明己暗辛。岁月无财官救助者，贫困；得财官运，亦吉。

    己丑时逢辛日险，财官埋没未为奇；六亲骨肉多刑害，年月冲开富贵推。辛日时临己丑，总由倒食淹留。
    就中金柜紧监收，午未戌开成就。甲丙卯寅发福，癸壬亥子漂流。少年谋望事难周，中未前程自有。
   ''',           

    '辛日庚寅':'''
    六辛日生时庚寅，财旺生官遇贵神；金木局中通月气，必为荣贵富豪人。
    辛日庚寅时，贵人财官。辛以寅为天乙贵，丙火为官，甲木为财，寅上丙、甲旺，若通金木月气或通运，主富贵显达。

    六辛之日遇寅时，财旺生官互换推；运拙利名应蹇滞，若行财禄更无虞。
    辛日庚寅时遇，弟兄骨肉生疏。双亲祖业靠难成，鸳侣中年违镜。
    亥癸坎壬减福，丙丁巳午驰名。春生冬产贵人钦，中末荣华之命。
   ''',           
       
    '辛日辛卯':'''
    六辛日生时辛卯，妻子难为遇比肩；秋产冬生贫下格，丙临寅马却当权。
    辛日辛卯时，比肩分财。辛以乙为财，卯上乙旺，遇比分夺，损伤妻子。
    生秋冬，财官无气，平常。寅巳午月，干透丙火，丙合辛生，官贵显达。辛卯，悬针煞，柱多不吉。

    辛日时逢辛卯，二辛分夺妻财。雁行鸳侣少合谐，独立自成无碍。
    年月财星生旺，忻然禄自天来。运行比劫事沉埋，木火运中通泰。
   ''',          
    
    '辛日壬辰':'''
    六辛日生时壬辰，伤官伤尽倍精神；四柱火虚防克害，九流技艺卜医人。
    辛日壬辰时，暗金沉水底。辛用丙为官，壬为伤官，辰水库，丙辛无气，壬水合局。
    若年月透丙，是伤官见官，刑祸百端，为人气高夸大，秀而不实。不通月气、无倚托者，为人反
    复成败，为医卜艺术。柱有木火身旺，行东南运、贵。

    六辛日干时壬辰，锁闭财官事未能；不通钥匙兼压伏，自古难发少年人。辛日壬辰时遇，伤官伤尽为奇。
    祖业父母早难为，雁行分飞无意。春夏财官生旺，东南方运施为。自谋自立作家资，不得亲人之力。
   ''',        
       
    '辛日癸巳':'''
    六辛日生时癸巳，贵气无伤官印强；月气有通兼倚托，早年荣贵姓名香。
    辛日癸巳时，官印扶身。辛以丙为官，戊为印，癸为食神。
    巳上丙戊健旺，癸合化火，赤白文章。若有倚托、通月气者，显达；若月不通，运通，亦贵。

    癸巳时逢辛日干，柱中独喜显财官；运行禄马无刑地，金榜题名步御銮。
    辛日时临癸巳，春生财旺 基。丙丁午年最为奇，破克刑冲不利。
    壬癸庚申无破，功名富贵为的。妻贤子孝两相宜，刑破巳时不利。
   ''', 
         
    '辛日甲午':'''
   六辛日逢甲午时，暗鬼枭神真可畏；若无倚托反劳生，莫道六辛逢马贵。
   辛日甲午时，鬼旺身衰。辛用丁为鬼，己为倒食，甲为财。甲午木死则神无气，丁己健旺，虽见午为天乙贵，平生反复；
   纵通旺气，亦贵不永。若生火土月，西方运，贵。

   六辛日干时甲午，财神无气不相当；春生木旺财官运，一路滔滔姓字香。
   辛日时临甲午，妻财无气身衰。干强火旺为鬼胎，火重金柔炼坏。
   最忌用神伤损，金沉海底生灾。无刑无破称心怀，贵重光明广大。
   ''',         
       
    '辛日乙未':'''
   六辛日生时乙未，火木相成金不畏；月通金气与春荣，财旺生官身自贵。
   辛日乙未时，天财入库。辛以乙为财，未上入库；己为倒食，丁为正鬼；
   未上有暗丁，己被明乙制伏，不能为害。若通巳酉丑月者，贵，通火，行西运；通金，行南运，俱贵。

   未时辛日库门开，卓立家成自发财；金木运中身旺吉，几经险遇福重来。
   辛日时逢乙未，库中透出偏财。运行木金忌身衰，丑戌之运通泰。
   经历初年发福，鸳帏抵敌无灾。荣华富贵命中排，无破为官清泰。
   ''',            
       
    '辛日丙申':'''
   辛日生时遇丙申，月通金火转精神；化成金水逢金地，聚福能为富贵人。
   辛日丙申时，丙辛化水，申上长生。若月通巳酉丑金气者，精神秀丽，文章聚福。
   通火气旺、有倚托者，贵。辛酉、辛未最妙，不成化象。申上官星无气，平常衣禄。

   辛日良时遇丙申，天元化合得其真；冬生若也无刑破。贵显当登要路津。
   辛日丙申时遇，长生禄马希奇。天元化合显光辉，职重名高威势。
   君子文章上立，常人荣旺家基。生时真定却无亏，运喜西南东地。
   ''',                  
       
    '辛日丁酉':'''
   六辛日生时丁酉，鬼破禄无祸百端；倚托身强方断吉，月通制伏是偏官。
   辛日丁酉时，火金持争。辛金酉上健旺，见丁为正鬼；酉上丁长生，破禄，不成其福，反复成败。
   身强通月气有制伏者，作偏官论；更行身旺运，贵。通金气无丁，身强，行南运，大贵。

   酉时辛日等同论，出户相迎喜事新；不遇刑冲空克破，何愁富贵不加身。
   辛日时临丁酉，偏官合局相投。丙、丁重见主淹留，嗣息女多男少。
   祖业残花秋暮，游人皎月云收。身强官旺福优游，运至财官大有。
   ''',           
       
    '辛日戊戌':'''
   六辛日生时戊戌，印绶生身坐禄堂；有托福人难靠祖，不通月气是平常。
   辛日戊戌时，禄同印堂同居。辛以戌为禄堂，戌上有明戊为印绶；
   以丙、丁为官，戌上戊土正位，丙、丁火局。若有倚托通月气者，难为祖业。不通，平常。

   辛日戌时财库闭，如开须待丑辰来；月中甲丙天干透，富贵荣华不用猜。
   辛日时临戊戌，五行财禄荣昌。柱中辰、戌两相当，名曰钥匙开藏。
   火水光辉发达，空亡锁闭如常。运行财地并官乡，无破天然福相。
   ''',           
       
    '辛日己亥':'''
   六辛日生时己亥，背禄剥官反破伤；如作飞天禄马贵，失时无合空忙忙。
   辛日己亥时，飞禄合局。辛以丙为官，亥上有旺壬伤，故官无气；如再得亥月或亥日，以亥冲出巳中丙火为官星。
   若是辛西、辛丑合局，贵；其余辛无合。不通月气，无倚托，贫下；有倚托，吉。

   辛日天干己亥时，枭神背禄主灾虞；无冲发福亦不重，禄马飞天贵自殊。
   辛日时临己亥，枭神背禄同宫。好如缺月被云龙。壬巳甲寅无用。
   父母完全不睦，残花结果防风。若无克破与刑冲，飞天禄马福重。
   ''',         
       

    '壬日庚子':'''
   六壬日生时庚子，子上明庚暗损伤；火土月中仍主吉，不通凶狠只平常。
   壬日庚子时，刃旺身强。壬以庚为倒食，癸为羊刃，时上明庚癸旺，若通火土月气，制伏庚癸，大贵；
   不通，凶狠平常。通运亦贵。

   天干壬日时庚子，枭日由来遇劫财；运弱妻儿防克害，运强财禄自天来。
   壬日时逢庚子，劫财倒食流连，运行比劫事忧煎，财禄不能通显。
   雁侣双亲失意，妻儿迟则团圆，财官运步福滔然，祖业从新改变。
   ''',      


    '壬日辛丑':'''
   六壬日生时辛丑，下有官星上印绶；如通月气运西南，官印扶身人清秀。
   壬日辛丑时，官印得位。壬以己为官，辛为印，丑上金局，
   暗已得位，若通月气，为人清秀，禄贵安稳；不通，主性僻诡谲。

   六壬日干辛丑时，官印相生事事奇；午月更通金土旺，为官清贵定无移。
   壬日时临辛丑，财官印绶其中，要知开库钥匙通，戊己相逢火重。癸卯乙字减福，
   有遇龙虎相冲，只争迟早改门风，富贵承恩拜宠。
   ''',         

    '壬日壬寅':'''
   六壬日生时壬寅，水火相逢既济论；水木月通财禄贵，不通无救是常人。
   壬日壬寅时，水火既济。壬用丙为财，甲为食，寅上丙生甲旺，壬水无气，若通水局，有倚托，皆贵，不通无救，福薄。
   壬寅日健旺，主大富，如不通月气，亦贵。

   六壬逢虎是浮沤，富贵功名莫强求；有印有官为上格，骤然财禄免忧愁。
   壬日壬寅时遇，比肩相遇食神，弟兄雁侣少同群，此是生时定分。
   坐局运行官地，身强禄位超伦，身衰刑害祸相侵，衣禄平常之命。
   ''',   


    '壬日癸卯':'''
   六壬日生时癸卯，引归死地势难安；劫财煞刃见伤鬼，倚托若无常命看。
   壬日癸卯时，身死刃生。壬以癸为刃，卯为暗乙，而伤官鬼。
   卯上癸生乙旺壬死，不通身旺月气，无救助及倚托者，夭贱。
   巳酉丑月，印旺无化者，性僻孤高虚诈，通身旺，见金气，行才运，贵。伤官伤尽，行南运，亦贵。

   壬癸相逢见卯贵，刑冲破害不周全。月逢二德兼身旺，改祸为祥乐自然。
   壬日时临癸卯，败财背禄相逐，平生反复事疑迟，水到东方失位。
   须有贵人救助，自身文福难齐，祖财骨肉有盈亏，命主晚成先废。
   ''',   
      

    '壬日甲辰':'''
    六壬日生时甲辰，壬骑龙背坐食神；柱中有托无刑害，必是荣华富贵人。
    壬日甲辰时，亦为壬骑龙背。壬以甲为食神，辰上壬水合局，甲有生气，食神旺相，通月气者富贵福厚。
    冬月，行卯运，不利。
    
    时遇甲辰壬日干，喜神重叠福多端；时来早晚功名就，运至申辰作显官。
    壬日甲辰时好，青龙入庙为高，犹如兰蕙出蓬蒿，水木滋生荣茂。
    时日冲开库旺，自然成就窝巢，运行吉地逞英豪，贵显亲人难靠。
    ''',      
       
    '壬日乙巳':'''
    六壬日生时乙巳，身绝有财不聚财；进神暗鬼来相克，透己相刑是祸胎。
    壬日乙巳时，财旺身绝。壬用丙为财，戊为鬼，庚为倒食。
    巳上有乙木为伤官，丙戌健旺，庚金长生，壬水气绝，柱有己官，祸患百端，傲物夸高。
    若不通身旺月无救助者，贫；有倚托，通旺，或行身旺运，皆吉。
    
    壬日时逢乙巳临，谋为未遇且沈吟：贵人举荐财官旺，子嗣鸳帏不一心。
    壬日时临乙巳，伤官背禄无取，虽然天乙贵人扶，贵显遇而不遇。
    谋望云为反覆，生平实事成虚，时来发达改门闾，犹似旱苗得雨。
    ''',           
      

    '壬日丙午':'''
    六壬日生时丙午，聚财之地坐胞胎；月逢金水须富贵，弃命从来是就财。
    壬日丙午时，禄马三奇。壬以己为官，丙丁为财，午上丁己是禄马，壬水受胎，
    有倚托，通金水月气，就财生旺，主富贵，通火气，亦贵。

    丙午时生壬日强，时中禄马不寻常；运行吉地无冲破，早晚升迁到省堂。
    壬日时逢丙午，亦名禄马同乡，就中既济见文章，志气宽洪海量。
    不过刑冲破害，自然财禄盈箱。运行财旺及官乡，定是朝中宰相。
    ''',     
       
    '壬日丁未':'''
    六壬日生时丁未，夫化妻从格局奇；若是局中通水木，发财发福两相宜。
    壬日丁未时，夫从妻化，壬合丁，未上同木局，贵。若月通木局，有倚托者发财，不通，但有资助，因妻致富。
    
    壬日时逢丁未临，木化成林忌见金；年月若还无破害，必教富贵福弥深。
    壬日时临丁来，就中暗合妻财，好来丑戌钥匙开，收积钱财广大。年月克冲不犯，天然衣禄安排，
    鸳帏子息早年乖，中末依然享泰。
    ''',       
       
    '壬日戊申':'''
    六壬日生时戊申，长生之地鬼伤身；身强制伏为高命，反此定知贫薄人。
    壬日戊申时，水土混浊。壬以戊为鬼，庚为印，申上庚金健旺，壬水长生，戊土偏官，身鬼俱强，
    为人勇暴，若通旺月，行身旺运，有甲木制伏者贵；不通，聪明不贵，再行鬼旺运，难以显达。
    
    申时壬戌合天元，运去财官福自然；鬼旺身衰无救助，平生劳碌不周全。
    壬日戊申时显，支干煞旺双全，喜逢辰子两相连，正合衣锦局面。
    被害刑冲克战，就中文福艰难，运行吉地紫泥宣，富贵妻多子健。
    ''',        
       
    '壬日己酉':'''
    六壬日生时己酉，明官暗印有扶持；月通身旺人清贵，犹恐恋花贪酒色。
    壬日己酉时，败处逢生。壬水酉上沐浴，辛为生气印绶，酉上辛金旺，用己为官，酉上有明己
    ，若通月气有倚托，行财官运，贵，反是，平常。但犯桃花坐命，风流人物，恋花贪酒。
    
    天干壬日酉时真，改祸为祥遇贵人；若不为官封品级，晚年享福旺家门。
    壬日时逢己酉，正官印绶无偏，荣枯贵贱是因缘，人自生成便见。乙癸卯冲破克，驳杂财官减半，
    遭富贵不双全，差了生时难辩。
    ''',     
       
    '壬日己酉':'''
    六壬日生时己酉，明官暗印有扶持；月通身旺人清贵，犹恐恋花贪酒色。
    壬日己酉时，败处逢生。壬水酉上沐浴，辛为生气印绶，酉上辛金旺，用己为官，酉上有明己
    ，若通月气有倚托，行财官运，贵，反是，平常。但犯桃花坐命，风流人物，恋花贪酒。
    
    天干壬日酉时真，改祸为祥遇贵人；若不为官封品级，晚年享福旺家门。
    壬日时逢己酉，正官印绶无偏，荣枯贵贱是因缘，人自生成便见。乙癸卯冲破克，驳杂财官减半，
    遭富贵不双全，差了生时难辩。
    ''',           
       
    '壬日庚戌':'''
    六壬日生时庚戌，身临财库却为鬼；明庚暗戌相刑克，财禄生平聚散多。
    壬日庚戌时，枭临财库，壬以丙丁为财，库于戌，庚为倒食，戊偏官，
    若通火木月气，有倚托者，贵；不通，财帛聚散。
    
    壬庚相逢戌时生，库有财官锁闭门；究竟无头多反覆，功名到底似浮云。
    壬日时逢庚戌，支干倒食难容。财官印绶库内封，无钥不能取用。丑酉辰逢作福，更逢丁己成名
    ，但怕克害过刑冲，驳杂如常之命。
    ''',     
       
    '壬日辛亥':'''
    六壬日逢辛亥时，印禄相随最是奇；财官不见无冲破，得路青云报尔知。
    壬日辛亥时，日禄居时，无克破，有倚托，柱中不见财官，富贵显达；行东运，大贵；
    若通气，减福；南方运，不贵巨富。
    
    壬辛会遇亥时推，白玉休嫌出见迟；长生禄马无刑破，抛却麻衣挂紫衣。
    壬日时临禄马，又为印绶同乡，水从金木自然强，此命极高为上。
    癸乙暗合咸福，无冲破显文章，积玉堆金满屋堂，荫子封妻之象。
    ''',           


    '癸日壬子':'''
    六癸日生时壬子，青云得路最为奇；若无己土冲克破，自有功名显达时。
    癸日壬子时，日禄归时，癸水子上建禄，
    若年月干支无戊己午未字刑冲破害，三元有倚托，通月气者，文章秀丽，官职显达；
    若通木气月，亦贵。如柱透己，有甲合，亦贵。否则，反覆。

    日禄归时局中得，食神喜遇怕刑冲；伤官莫道伤财运，官不加兮财不丰。
    癸日时临壬子，名为归禄格同，家门白屋也峥嵘，玄武当权禄重。
    水清宝瓶益盛，文章博览多通，荣迁来历紫薇封，甲午寅亥破动。

    ''',

       '癸日癸丑':'''
    六癸日生时癸丑，支中暗鬼有刑伤；月通身旺防妻损，丑巳遥合贵异常。
    癸以丁为妻，丑中丁火无气，若通身旺比肩之月，防损妻财。
    柱丑寅多，以寅刑巳，丑合巳，刑出巳中，丙戊为财官，须干
    头无戊己字，大贵。忌巳未卯破格。

    阴水重重时库收，少年难发莫强求；筹来受过中年后，安坐高堂任白头。
    癸日时逢癸丑，水流金局盈冲，库逢戌未禄财丰，不过空乏难动。
    无匙少年不显，有匙禄马和同，运来何用苦劳心，发达门庭大庆。

    ''',     

       '癸日甲寅':'''
    六癸日生时甲寅，刃复官禄减精神；柱中无有庚申字，刑合财官是贵人。
    癸日甲寅时，刑合财官，癸以丙为财，戊为官，寅刑出巳中丙戊为财官，
    若柱无官煞及刑冲破害损格，贵；有庚申戊己字，无制伏，不贵。

    甲寅癸日戊丙开，少年未遇且沉埋；若还四柱无冲破，平步登云到省台。
    癸日寅时克应，支干相合光荣，若无壬己戊庚申，必然财禄丰润。
    运至皇州显达，文章虎榜标名，但逢一字稍空冲，克子伤食剥俸。
    ''',    

       '癸日乙卯':'''
    六癸日生乙卯时，长生之地遇食神；众无午酉兼辛巳，福寿双全禄位人。
    癸日乙卯时，食神干旺。癸以乙为学堂食神，卯上癸水长生，乙坐禄，柱中无己破辛夺，
    午酉刑冲，通月气，有倚托，主聪明有寿，居官食禄；若有己土，不贵。春月生，北运，显达。

    乙癸相逢旺食支，天工造物本无私；运行自有高人荐，手攀丹桂上云逵。
    癸日时逢乙卯，贵人食禄之乡，玉堂乙卯位侯王，便是金门将相。
    君子文章播发，常人财禄盈箱，甲寅辛酉颇安常，富贵荣华大享。
    ''',   

       '癸日丙辰':'''
    六癸日生时丙辰，偏官无气未为贫；若无木气通其局，定是清高福禄人。
    癸日丙辰时，身坐官库，癸用戊己为官，辰上土墓为官库，
    见丙为财，辰为水局，丙火无气，癸水合局，柱无甲破官损库，主贵。

    癸日丙辰官库闭，财星虽透却无气；官要匙开财要兴，柱逢卯戊方为贵。
    癸日丙辰时遇，库中锁闭财官，要逢卯戊钥匙开，守祖六亲阻碍。暗有食神相助，空乏虚度资财，
    先贫后富命中排，改祖重兴渐快。
    ''',    

       '癸日丁巳':'''
    六癸日生时丁巳，贵地逢财遇暗官；有托就看财禄盛，无依必定福偏残。
    癸日丁巳时，癸合财官，癸用丙为财，戊为官，庚为印，巳为天乙贵人。
    巳上庚金长生，丙戊建禄，癸水受胎，若有倚托，通水气月，贵，不通水气。平常。
    时逢三奇，大抵发于晚年。

    巳时禄马同争先，造化无私产大贤；刑冲减半无空克，运至声名扬九天。
    癸日时临丁巳，贵人禄马同乡，三重蛇马正朝纲，玉殿金阶来往。壬亥申寅减半，只愁运落空亡，
    果无冲克无刑伤，舞拜凤凰池上。
    ''',   

       '癸日戊午':'''
    六癸日生时戊午，化火临时帝旺乡；运喜东南木火地，为官清正禄荣昌。
    癸日戊午时，化气成火局，癸合戊化火，午上帝旺，合局而贵，身旺不化癸水，地方之气引到南方，
    癸水无气，贵而寿促，东方运吉。

    将星扶禄命高低，见爱于人是与非；得志退毛鸡化凤，虎卧平坡被兔欺。
    癸日时逢戊午，天元既济之方，化为真火显威光，灾难消除福长。
    壬会甲寅减半，是非成败难防，六亲不睦暗刑伤，难得资财富旺。
    ''',      

       '癸日己未':'''
    六癸日生时癸未，鬼旺身衰福不齐；月气不通无救助，平常衣禄有相亏。

    偏官暗鬼库中埋，险难惊忧不聚财；丑戌相逢钥匙吉，旺中癸福定无灾。
    癸日时临己未，库中耗鬼身衰，不逢卯戌钥匙开，锁闭不能通泰。
    花落重荣结子，双亲雁侣难谐，纵然先贫后富来，弃旧迎新无碍。
    ''',      

       '癸日庚申':'''
    六癸日生时庚申，官星印旺在其支；柱中无己丙寅巳，自有荣华富贵时。
    癸日庚申时，作专印合禄。癸以戊为正官，庚为正印，申上庚旺戊生，以申合巳中戊丙，
    癸日得财官，若有倚托，柱中无财及破害刑冲官印，主贵；柱中有财，行财运，反复进退，少贵。

    癸日庚申仔细推，禹门深处见龙飞；文章得助雄威力，柱合财官世所希。
    癸日庚申时正，印绶齐合官星，亥寅申丙巳刑冲，离合立之身不定。
    无破黄甲显姓，常人财禄安宁，果无刑害与灾星，便是锦鸡化凤。
    ''',      

       '癸日壬戌':'''
    六癸日生日壬戌，支内正官生财库；月兼有救贵多成，倚托若无终不富。
    癸日壬戌时，水火既济，癸用丙丁为财，戊土为官，戊与癸合旺，为人智谋，通月气有倚托者贵；
    不通，平常；通火土月气，富贵双全；运气通，亦吉。

    天乙壬癸戌时排，库内财官等钥开；不遇刑冲空锁闭，少年难发更生灾。
    癸日时逢壬戌，就中仓库盈余，将星天德两相扶，辰戌钥匙开助。
    土旺长流水局，六亲恩处成疏，不遇空亡有增余，中末荣华享福。
    ''',          


       '癸日癸亥':'''
    六癸日生时癸亥，禄马飞天临旺神；不见官星兼惹绊，必为贵格异常人。
    癸日癸亥时，禄马飞天格，癸水亥健旺，癸用戊为官，丙为财，亥中丙戊俱绝，
    癸无财官，却亥去冲出巳中丙戊，飞来就癸为财官，柱无戊己惹绊及官星破禄，若见庚辛，
    清白而秀，为人智慧，贵为方面。

    阴水重重透海波，少年未遇且蹉跎；困龙得志方能化，不遇时来虎卧坡。
    癸日时逢癸亥，败财带禄亨通。喜宜秋夏忌春冬，戊丙庚木富盛。
    巳亥甲丙反复，六亲大不和同。一身不定好翻腾，先败后成之命。
    ''',          

}