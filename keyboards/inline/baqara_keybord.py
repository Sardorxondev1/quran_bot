from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import baqara_callback_data
baqara_keybord1 = InlineKeyboardMarkup(row_width=4)

buttons1 = {
    '1':'1',    '2':'2',
    '3':'3',    '4':'4',
    '5':'5',    '6':'6',
    '7':'7',    "8":"8",
    '9':'9',    '10':'10',
    '11':'11',  '12':'12',
    '13':'13',  '14':'14',
    '15':'15',  '16':'16'
}

for key,value in buttons1.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord1.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back1'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next1'))
baqara_keybord1.insert(back_button)
baqara_keybord1.insert(next_button)

baqara_keybord2 = InlineKeyboardMarkup(row_width=4)
buttons2 = {
    '17':'17',    '18':'18',
    '19':'19',    '20':'20',
    '21':'21',    '22':'22',
    '23':'23',    '24':'24',
    '25':'25',    '26':'26',
    '27':'27',    '28':'28',
    '29':'29',    '30':'30',
    '31':'31',    '32':'32'
}

for key,value in buttons2.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord2.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back2'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next2'))
baqara_keybord2.insert(back_button)
baqara_keybord2.insert(next_button)

baqara_keybord3 = InlineKeyboardMarkup(row_width=4)
buttons3 = {
    '33':'33',    '34':'34',
    '35':'35',    '36':'36',
    '37':'37',    '38':'38',
    '39':'39',    '40':'40',
    '41':'41',    '42':'42',
    '43':'43',    '44':'44',
    '45':'45',    '46':'46',
    '47':'47',    '48':'48'
}

for key,value in buttons3.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord3.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back3'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next3'))
baqara_keybord3.insert(back_button)
baqara_keybord3.insert(next_button)

baqara_keybord4 = InlineKeyboardMarkup(row_width=4)
buttons4 = {
    '49':'49',    '50':'50',
    '51':'51',    '52':'52',
    '53':'53',    '54':'54',
    '55':'55',    '56':'56',
    '57':'57',    '58':'58',
    '59':'59',    '60':'60',
    '61':'61',    '62':'62',
    '63':'63',    '64':'64'
}

for key,value in buttons4.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord4.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back4'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next4'))
baqara_keybord4.insert(back_button)
baqara_keybord4.insert(next_button)

baqara_keybord5 = InlineKeyboardMarkup(row_width=4)
buttons5 = {
    '65':'65',
    '66':'66',    '67':'67',
    '68':'68',    '69':'69',
    '70':'70',    '71':'71',
    '72':'72',    '73':'73',
    '74':'74',    '75':'75',
    '76':'76',    '77':'77',
    '78':'78',    '79':'79', '80':'80'

}

for key,value in buttons5.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord5.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back5'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next5'))
baqara_keybord5.insert(back_button)
baqara_keybord5.insert(next_button)

baqara_keybord6 = InlineKeyboardMarkup(row_width=4)
buttons6 = {
    '81':'81',
    '82':'82',    '83':'83',
    '84':'84',    '85':'85',
    '86':'86',    '87':'87',
    '88':'88',    '89':'89',
    '90':'90',    '91':'91',
    '92':'92',    '93':'93',
    '94':'94',    '95':'95', '96':'96'

}

for key,value in buttons6.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord6.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back6'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next6'))
baqara_keybord6.insert(back_button)
baqara_keybord6.insert(next_button)

baqara_keybord7 = InlineKeyboardMarkup(row_width=4)
buttons7 = {
    '97':'97',
    '98':'98',    '99':'99',
    '100':'100',    '101':'101',
    '102':'102',    '103':'103',
    '104':'104',    '105':'105',
    '106':'106',    '107':'107',
    '108':'108',    '109':'109',
    '110':'110',    '111':'111', '112':'112'

}

for key,value in buttons7.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord7.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back7'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next7'))
baqara_keybord7.insert(back_button)
baqara_keybord7.insert(next_button)

baqara_keybord8 = InlineKeyboardMarkup(row_width=4)
buttons8 = {
    '113':'113',
    '114':'114',    '115':'115',
    '116':'116',    '117':'117',
    '118':'118',    '119':'119',
    '120':'120',    '121':'121',
    '122':'122',    '123':'123',
    '124':'124',    '125':'125',
    '126':'126',    '127':'127', '128':'128'

}

for key,value in buttons8.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord8.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back8'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next8'))
baqara_keybord8.insert(back_button)
baqara_keybord8.insert(next_button)

baqara_keybord9 = InlineKeyboardMarkup(row_width=4)
buttons9 = {
    '129':'129',
    '130':'130',    '131':'131',
    '132':'132',    '133':'133',
    '134':'134',    '135':'135',
    '136':'136',    '137':'137',
    '138':'138',    '139':'139',
    '140':'140',    '141':'141',
    '142':'142',    '143':'143', '144':'144'

}

for key,value in buttons9.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord9.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='back9'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='next9'))
baqara_keybord9.insert(back_button)
baqara_keybord9.insert(next_button)

baqara_keybord10 = InlineKeyboardMarkup(row_width=4)
buttons10 = {
    '145':'145',
    '146':'146',    '147':'147',
    '148':'148',    '149':'149',
    '150':'150',    '151':'151',
    '152':'152',    '153':'153',
    '154':'154',    '155':'155',
    '156':'156',    '157':'157',
    '158':'158',    '159':'159', '160':'160'

}

for key,value in buttons10.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord10.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backten'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextten'))
baqara_keybord10.insert(back_button)
baqara_keybord10.insert(next_button)

baqara_keybord11 = InlineKeyboardMarkup(row_width=4)
buttons11 = {
    '161':'161',
    '162':'162',    '163':'163',
    '164':'164',    '165':'165',
    '166':'166',    '167':'167',
    '168':'168',    '169':'169',
    '170':'170',    '171':'171',
    '172':'172',    '173':'173',
    '174':'174',    '175':'175', '176':'176'

}

for key,value in buttons11.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord11.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backeleven'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nexteleven'))
baqara_keybord11.insert(back_button)
baqara_keybord11.insert(next_button)

baqara_keybord12 = InlineKeyboardMarkup(row_width=4)
buttons12 = {
    '177':'177',
    '178':'178',    '179':'179',
    '180':'180',    '181':'181',
    '182':'182',    '183':'183',
    '184':'184',    '185':'185',
    '186':'186',    '187':'187',
    '188':'188',    '189':'189',
    '190':'190',    '191':'191', '192':'192'

}

for key,value in buttons12.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord12.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backtwele'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nexttwele'))
baqara_keybord12.insert(back_button)
baqara_keybord12.insert(next_button)

baqara_keybord13 = InlineKeyboardMarkup(row_width=4)
buttons13 = {
    '193':'193',
    '194':'194',    '195':'195',
    '196':'196',    '197':'197',
    '198':'198',    '199':'199',
    '200':'200',    '201':'201',
    '202':'202',    '203':'203',
    '204':'204',    '205':'205',
    '206':'206',    '207':'207', '208':'208'

}

for key,value in buttons13.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord13.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backthirteen'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextthirteen'))
baqara_keybord13.insert(back_button)
baqara_keybord13.insert(next_button)

baqara_keybord14 = InlineKeyboardMarkup(row_width=4)
buttons14 = {
    '209':'209',
    '210':'210',    '211':'211',
    '212':'212',    '213':'213',
    '214':'214',    '215':'215',
    '216':'216',    '217':'217',
    '218':'218',    '219':'219',
    '220':'220',    '221':'221',
    '222':'222',    '223':'223', '224':'224'

}

for key,value in buttons14.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord14.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backfourteen'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextfourteen'))
baqara_keybord14.insert(back_button)
baqara_keybord14.insert(next_button)

baqara_keybord15 = InlineKeyboardMarkup(row_width=4)
buttons15 = {
    '225':'225',
    '226':'226',    '227':'227',
    '228':'228',    '229':'229',
    '230':'230',    '231':'231',
    '232':'232',    '233':'233',
    '234':'234',    '235':'235',
    '236':'236',    '237':'237',
    '238':'238',    '239':'239', '240':'240'

}

for key,value in buttons15.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord15.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backfifeteen'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextfifeteen'))
baqara_keybord15.insert(back_button)
baqara_keybord15.insert(next_button)

baqara_keybord16 = InlineKeyboardMarkup(row_width=4)
buttons16 = {
    '241':'241',
    '242':'242',    '243':'243',
    '244':'244',    '245':'245',
    '246':'246',    '247':'247',
    '248':'248',    '249':'249',
    '250':'250',    '251':'251',
    '252':'252',    '253':'253',
    '254':'254',    '255':'255', '256':'256'

}

for key,value in buttons16.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord16.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backsixteen'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextsixteen'))
baqara_keybord16.insert(back_button)
baqara_keybord16.insert(next_button)

baqara_keybord17 = InlineKeyboardMarkup(row_width=4)
buttons17 = {
    '257':'257',
    '258':'258',    '259':'259',
    '260':'260',    '261':'261',
    '262':'262',    '263':'263',
    '264':'264',    '265':'265',
    '266':'266',    '267':'267',
    '268':'268',    '269':'269',
    '270':'270',    '271':'271', '272':'272'
        }
for key,value in buttons17.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord17.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backseventeen'))
next_button = InlineKeyboardButton(text='keyingisi',callback_data=baqara_callback_data.new(items='nextseventeen'))
baqara_keybord17.insert(back_button)
baqara_keybord17.insert(next_button)

baqara_keybord18 = InlineKeyboardMarkup(row_width=4)
buttons18 = {
    '273':'273',
    '274':'274',    '275':'275',
    '276':'276',    '277':'277',
    '278':'278',    '279':'279',
    '280':'280',    '281':'281',
    '282':'282',    '283':'283',
    '284':'284',    '285':'285',
    '286':'286'
}

for key,value in buttons18.items():
    tugma = InlineKeyboardButton(text=key,callback_data=baqara_callback_data.new(items=value))
    baqara_keybord18.insert(tugma)

back_button = InlineKeyboardButton(text='ortga',callback_data=baqara_callback_data.new(items='backeighteen'))
baqara_keybord18.insert(back_button)

baqara_keybords = {
    'backeighteen':baqara_keybord17,
    'backseventeen':baqara_keybord16,
    'backsixteen':baqara_keybord15,
    'backfifeteen':baqara_keybord14,
    'backfourteen':baqara_keybord13,
    'backthirteen':baqara_keybord12,
    'backtwele':baqara_keybord11,
    'backeleven':baqara_keybord10,
    'backten':baqara_keybord9,
    'back9':baqara_keybord8,
    'back8':baqara_keybord7,
    'back7':baqara_keybord6,
    'back6':baqara_keybord5,
    'back5':baqara_keybord4,
    'back4':baqara_keybord3,
    'back3':baqara_keybord2,
    'back2':baqara_keybord1,
    'next1':baqara_keybord2,
    'next2':baqara_keybord3,
    'next3':baqara_keybord4,
    'next4':baqara_keybord5,
    'next5':baqara_keybord6,
    'next6':baqara_keybord7,
    'next7':baqara_keybord8,
    'next8':baqara_keybord9,
    'next9':baqara_keybord10,
    'nextten':baqara_keybord11,
    'nexteleven':baqara_keybord12,
    'nexttwele':baqara_keybord13,
    'nextthirteen':baqara_keybord14,
    'nextfourteen':baqara_keybord15,
    'nextfifeteen':baqara_keybord16,
    'nextsixteen':baqara_keybord17,
    'nextseventeen':baqara_keybord18
            }