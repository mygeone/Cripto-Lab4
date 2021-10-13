import time, hashlib

from hashes import hashPassword


def hashOwn(password):
    return hashPassword(password,False,'q')

def hashSHA1(password):
    return hashlib.sha1(password.encode())

def hashSHA256(password):
    return hashlib.sha256(password.encode())

def hashMD5(password):
    return hashlib.md5(password.encode())

def test(passwordLists):
    startTimeOwn = time.time()
    for password in passwordLists:
        hashOwn(password)
    endTimeOwn = time.time() - startTimeOwn

    startTimeSHA1 = time.time()
    for password in passwordLists:
        hashSHA1(password)
    endTimeSHA1 = time.time() - startTimeSHA1

    startTimeSHA256 = time.time()
    for password in passwordLists:
        hashSHA256(password)
    endTimeSHA256 = time.time() - startTimeSHA256

    startTimeMD5 = time.time()
    for password in passwordLists:
        hashMD5(password)
    endTimeMD5 = time.time() - startTimeMD5

    print("El tiempo en hashear",len(passwordLists),"con el algoritmo propio fue de  :",endTimeOwn,"    segundos")
    print("El tiempo en hashear",len(passwordLists),"con el algoritmo SHA-1 fue de   :",endTimeSHA1,"   segundos")
    print("El tiempo en hashear",len(passwordLists),"con el algoritmo SHA-256 fue de :",endTimeSHA256,"   segundos")
    print("El tiempo en hashear",len(passwordLists),"con el algoritmo MD5 fue de     :",endTimeMD5,"    segundos")

pass1 = ['"+""!gBv>2Iw0RdT..|KA"']

pass10 = ["9A/nb$8vqtb|@qQ_omdrB2N,;2,","UXdMQw9}:BicAOZtoxTf+Kd'cmE"
">YMDs4o","-kM9$N^ig:?'<gQ+@|=)","eGW/sn7U0^0_68z@~OnnA","u,*lluAM9hy{<zNz}vH","7j+QIBJ-7o5eiib+g$1U5Y"
"q~e|GzfP4U<vHCAuUu!GqJ+>Vmj/","s iwcpAav8hHk","Daa:gHBf.Mtkum`1;h8)","&X0>{T","xvT{31^"]

pass20 = [">m k:!SMRpLxekZn0zve>&`-","f^.'=rBQp8NC=(r0YX","*!ut5i q","Yq|GEboy+"
"lOy9Ddr@j>p{Z&Sg$Vc}uZ+a2vP(","s``sp|f&O|yERlc&*?Bh.n&Ymxle","~'`GaU2/S`","51(PTF*a&T+lf?1{r8GVx#cnc8uX","&L<|~)/?b8U.^Opp1R-/w?Y-xPa@U-iwtadSG"
"Mi`9Gl&CSv<tQmwlqVxlyz<'_SK(cR","3E,V( Y7~0@A#Rw</iS0l8Bj5c2klfZ4we","FMdIJ$yzU!Hg<DH:PCphiW8`l-.3 ynu/bm aOl","Hk=K:dC}m1.J-Eg{Boz''","!f@/"
"$6!KB|Gkc+*x69wBBun2K}Pg0lP>d!qX 2","4hhldcgf>IQv{/v3By/:grDH","*k","^?jdT$NifcG4Z>4IFbIhkx(be1I6^;>x","QCYP1g$M=(;.3(BG;Y&THg/XhJ-M;hFn"
" dKoTJE7Z~+--&If`6va","?`pl","&$w84","5Hk =u2 _e!Y","N<k$F<SKBQ|*IY>dOp&b~&Wkk{||z)kUxr4<$?d"]

pass50 = ["E!q EO124u^(LFS1Mp4.MhKM A^,","wcGUo1edR&'sMFD","GG1Lak`7AFCzugfw;</6i-~|","^/IQBi;YWvOj?E CuQne(1/_`ysiJxe<","Z|JeP^omfeS*rHfmJ4Bp5(Td#l"
"RBjCF8#V47c+Y","5,m=;^cXwT`6VK5LCVw@Pa_ v8irf'Ql^rQ7 5","y:cUjbj.ku7^f;kVXt:EF^naf!XW","B/B#+nlirOEz@:xQR4@;*C>Hk|^V<|+","L9PL/=Chcp2MM+FOh7xV5`8NeA0cP9"
"gCTnh7 _(bQ,uq5D#JI4:bj;4<0+,>:eAyl6","G7aiyiS5|#6tYNk_p.|>O u@HtCyBl","A/Dy^^rnqQ8vT/rJ^ 8?pdHkV;aS","b2)3paUW2|*`f_r^bzIqx!8&-1`NE","(|R@ud'.h(k0X3yu1 4Y"
".","`-MW#:ADw>w=Jnnew~kXTW7L5","=9ZQoN<M1O","7~ROp9W0?dovchk^Du","2E"
")x","8#X`b-aP 1cog=s3N=1s)ISeA~$jSaC/HUa","r`'|g","YFsZ_W7y|lhf>ZqJyjFO*P$CCOq ^H","12Ghz-h+ &mcT$pJy"
"/3YuTr8!Wyk#()vR","9/p:<6;CzKwV=pLjqMru,eK#bo","Q9,Cf&h `cK45=+ZPjPRPx","d97pEo6x0!XkMdZA& ;TrOa`ZJg","n?"
"4uM#+=aq","j; #o8GM*B",";H8e`jAoZHZ>Y9NI","sH&?'x1.,,:fY3E,ajP|o/-Hj=","YjRwNLoL5p 5u.nlT4P;$vS;'sD*E=GD"
"Lcw<(b!$YAso8GsO:74eW.Nfm","1C^*~ZMeZqhG5~eifMqV~:h4f*SX!e(,","R^Rw:xyASF,+UWZiS#(?","c>c?DnI$>h.bMZ0ypr/>xnN*t=U20`ThbwY<xtt","oox 6 _8.>h=h(V !(ywgS`KoRkl2ma=#-k::g"
"xigEoxe-7oF6-gyFbw@MW3>92 z5*sz<=e7/J2","Wf.DGzv',/*V$N","<&kreXk>?|","yp;IAWR&XDUPc_E,|)<E^Q","u&0;J70gBtN^"
"dj_3B@,g~52;h@*`MjSS~;Cc4","LiJ1","?dM5RSX/lu>x!Y82R(bLygRVS;j-gf$--$WWzM","|#.6yU~>F/UAPo)iSCEMx_P-79(?YHG","~J71k@z<q**fdarD"
"23!(5Nt?O9X'ZJ","5y0AONo,@hiB@gkiVlZ'Kfy2mK<(pAXI~Eo","K-x<'dPb`9Tp_fYqf(;","4kgPhJj!#3xt13fstX:.R9c+Wun,ankC","I/dx7@*XR)Xg&yNMR7GWh'X(:V|AP#yZ","@P5MVgYGKZBgmm8","J>LWT*!2Z","os5rG.","_X=Dx8h'OJ37gQ#lKJ73)d`qIk,G'D:90ij(odKE","!_M2';v"
"NJfU6EzT)k,$^7G#DfCnc:j"]

pass100 = ["@P5MVgYGKZBgmm8","J>LWT*!2Z","os5rG.","_X=Dx8h'OJ37gQ#lKJ73)d`qIk,G'D:90ij(odKE","!_M2';v"
"NJfU6EzT)k,$^7G#DfCnc:j","PivOFH>Jl`<U~c)WaDR #Bj","KMBL Us~e+CEd<^$e8>!h-uCrdPo9wk!:4","65A,/hz$_&zLD6P&9D+9(:3a","H#6b-^(D6MRc:;S9=fXT4mGM`'X.$H5!qLwx'1"
"5>QrzsaT-TJlAnTZjzDE*u)","R^H-;;1mGRe=~0nc5;9t,sH?Kz","~IZO.74?","eLrN7XVbbkEERTqQOn4qg/a-,eSgF:U!wJ","v5!B+h6oRsxyJ O-&`A2k4x2bS6 QMqR?2P"
"P<~jq0ZePW4d1s/faX5M_r.gM5~uONfDXCpciH",";Sf 11o.,1o@","D1+j4","NZv#sz","Yy?8Lr+V.K6p,-QAX';SUE!i*dvZp&"
"5$9uZV+^=abKRbTspqX","eJaHM:hSwLfLL:OT!a~TS,*","<rZ->EMC","Q,yP>B@ly>r;x<G$O_TLu$","K25A~w/E8*R~wb"
"|ab)Ql&J<:A4gK!z$drW<&.FQLmu","@4?QQB9^In;vK/Uwi;Kh","4(","g<5Z8l$1N.Tv,j`1o=L$$-'`uyqH",",Jf|QmsfjxD(cySH!^by3:4DW*6n_*~7NBb4_uMY"
"","-657zm7I~$&+xu*PgmZ?bohI:dlAM?)^se","GH#.*u9^@;f8Po","54","S1`; 9.q#3!6mby&!c'"
"?zT|E&^k/,|n.H&HnL","|(37ibn6x(4sVmHaY:Pfj`2wl","9a","Z~W&Lp5aI3x'WS^a16p)av)3=BatS","AsiU~9d7!(Qm/r5PV|=gz_zDub|:Q_jQ>I"
"?g?2$","@X:Y$nHCQJuU2hPJp&qDA","aalFJQ># =6af@s4os2ZvLZ*Tm:5@Hgx","sdtry/IM!B|P?wf(/(oc-)fck6_kv","=-M_Vdg$N,vE$<3!p&-g1gt"
"HU0-X2K+z","Du","UveU($Y=^<;+`*4AAH(O*Unh$|>o,hk5",",@jc~6","f>Cd9_<*GJMPaFkdSvM"
"L3qnBmU(o e!xZ/~VJ G=J?J$7'h7g  #I?","js|STG'ADzB/?DbtXEqSVgM3EE3e.f6h_h/1xjN","iV,z<~BL~xblXTL(3^g$TL`wShxqgtN?gS","VWjeQ6Tr3*P",".ajB;"
"Wj~)4or^q_t$G^","j",">F7oMw5|hIj!CyhT@Sr<~wmI*oI~+","m1AQ$B:&X?1_HB!VQ","t4qsi?U#G;;p&j7kmn;qT!LTz"
"a32(?+&9VMIFk-_nC3`kP","(!e9xc;Wha9Rjnv:x4`NrkaX$?2u/R<IE*g",">v@4Z)cpuRo","","b^'5O? _$Q9x$27i:0Fy>B/xB<n"
"R9Qo$q57U 9Vj+W(@GWwCtTC2 R6top6>ES","& WHcU|+N#q!W,<@A^$Q*tdL(Iu.Oyd","A,","J3QeT","3VV-ab:"
" V4`4&WtYlxERfAyF-zWaACom#s|E5Kz!E1",":0Ldn'B?CN|#S^GG;|U6PoO$dsc","*p>hNLbxNdgEu5bGuG/=Z/_TX0i","NefqaVis0hLN","'@3A6&|j7S80>7"
"5q0$0'a31EF|sSEI&w&?XI6nd0Y U?g8G1>B","uHMDaXFL|Jeg3i!XX$zK:?6ulV^VplW4mo"," &K","m;Y8z|O/s_w9Z?SoSp0","yAO_N,83vLtK5I;.9Dyo+n.8b8g?Q.Pk/`>oD"
"*Ob|*(VycZ","M.ygU>M4OaqB)oFS2ys`u J6mX,=/W6n)Fe","a(HoNX8$9/L~sGl80 &Ac>^dntKO","K<)pa;mg>'J",";eH=1^|v#N!RBd_MeN?GhWubhUaO`&e/z+ior"
" 0Jq;J$RbgQOH11,<*=(UL_V4@@qybHLJhXqt`g","C,","tECA7Qi$5#8nn7fx~+:Tp","","(*;DF*7"
"ZK<Pr;uZuQK=*WoX$eal8pL0P.`J;IjlAf?9z(","zH8IB'EVn*Kwz-Y",">n+OrgQ.","+KV#o<0T6hi7cgXnr+0*+J>ptb>gCGCj$kQ47r","3xK?B8/|'~_7"
"Y^,:q4I&nlg=2Z'uKMq~s~tr","yVcQM","384M6Y7/Y0RA$HMBG","H9UHGui7DvPk0-Rv'","Fx_FT"
"~wSqLskN@8SS,^Di|C","JuYY|U5","HwOpYR+nnPoN92+WlYHS7","TI`):5&/jrP137n6J~C0|S4P<F,*Nrt'.^l~",""
"D.A+FUZob,)5d<Sa8YrL~+xgaSx|2g!3't!<L21","F=g+1j^R","AjQTwjT!mNyqLa,uu@d;wj?E",">6mM3=/bIn9s;V&Zj","x3^QsMbrw&Q0v~.>7NA"
"Vo?s7LfLjl|W6(AHU1(XS","My'9,+CDDr0+EV9.@","V j^5i|uoHM,B9<RP.Wi","h7ndORV'H=5F)i2t84PI+B&`c?bWd/N","4GX_HmBh>xliOjC=4/9FJZv!&0JdF6BG<Rud>=RJ"
"kS!z#9<","LX2'*GL.9f*br","8eV>FT+2LqVWt^?bu3-_IFPu~~ek4IL-i^oP*jN","eYJeM9v*KX","h(VCJZa4sL#$hF!a+o"
"jA-DHs~@Z;Ej 9^KG+1sa2<es Q#Uw e,+=*","aJ$LUd0LC#;9;bYvAWIw","dhRjqv@k`M2<wKpW","U#iVZRg(ZUKQ9y5&SX|a&~YG1M?r9 Tw D-gQ2,*"]

print("----------------------------------------------")
test(pass1)
print("----------------------------------------------")
test(pass10)
print("----------------------------------------------")
test(pass20)
print("----------------------------------------------")
test(pass50)
print("----------------------------------------------")
test(pass100)
print("----------------------------------------------")