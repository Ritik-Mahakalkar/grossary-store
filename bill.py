from tkinter import*
from tkinter import messagebox
import random,os,tempfile

#function

billnumber=random.randint(500,10000)
def clear():
    bath_soap_entry.delete(0,END)
    face_cream_entry.delete(0,END)
    face_wash_entry.delete(0,END)
    hair_removal_cream_entry.delete(0,END)
    hair_wash_entry.delete(0,END)
    hair_oil_entry.delete(0,END)
    face_powder_entry.delete(0,END)
    face_bleaching_entry.delete(0,END)
    eye_liner_entry.delete(0,END)
    face_pack_entry.delete(0,END)
    face_maker_entry.delete(0,END)
    rice_entry.delete(0,END)
    wheat_entry.delete(0,END)
    corn_entry.delete(0,END)
    Toor_dal_entry.delete(0,END)
    urad_dal_entry.delete(0,END)
    yellow_mong_entry.delete(0,END)
    chana_dal_entry.delete(0,END)
    split_urad_dal_entry.delete(0,END)
    rajma_entry.delete(0,END)
    peanut_entry.delete(0,END)
    gram_entry.delete(0,END)
    sugar_entry.delete(0,END)
    green_tea_entry.delete(0,END)
    salt_entry.delete(0,END)
    poha_entry.delete(0,END)
    rava_entry.delete(0,END)
    detargent_entry.delete(0,END)
    wash_bar_entry.delete(0,END)
    turmaric_entry.delete(0,END) 
    chili_powder_entry.delete(0,END)
    coriender_powder_entry.delete(0,END)
    sago_entry.delete(0,END)
    maza_entry.delete(0,END)
    fruti_entry.delete(0,END)
    sting_entry.delete(0,END)
    duo_entry.delete(0,END)
    red_bull_entry.delete(0,END)
    pepsi_entry.delete(0,END)
    mirinda_entry.delete(0,END)
    water_bottol_entry.delete(0,END)
    lassi_entry.delete(0,END)
    sprite_entry.delete(0,END)
    antome_entry.delete(0,END)
    pedha_entry.delete(0,END)
    kaju_katali_entry.delete(0,END)
    son_papadi_entry.delete(0,END)
    shrikhanda_entry.delete(0,END)
    amrakhanda_entry.delete(0,END)
    Rasgulla_entry.delete(0,END)
    basondi_entry.delete(0,END)
    gulab_jamun_entry.delete(0,END)
    sweet_curd_entry.delete(0,END)
    jalebi_entry.delete(0,END)
    ladu_entry.delete(0,END)
    biscuit_entry.delete(0,END)
    chips_entry.delete(0,END)
    maggi_entry.delete(0,END)
    bread_entry.delete(0,END)
    butter_entry.delete(0,END)
    jam_entry.delete(0,END)
    ketchup_entry.delete(0,END)
    soya_sause_entry.delete(0,END)
    cooking_oil_entry.delete(0,END)
    tomato_sause_entry.delete(0,END)
    chilli_sause_entry.delete(0,END)
    
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    email_entry.delete(0,END)
    bill_no_entry.delete(0,END)
    
    cosmatic_price_entry.delete(0,END)
    grossary_price_entry.delete(0,END)
    cold_price_entry.delete(0,END)
    sweet_price_entry.delete(0,END)
    fast_food_price_entry.delete(0,END)
    total_price_entry.delete(0,END)
    cosmatic_tax_entry.delete(0,END)
    grossary_tax_entry.delete(0,END)
    cold_tax_entry.delete(0,END)
    sweet_tax_entry.delete(0,END)
    fast_food_tax_entry.delete(0,END)
    total_tax_entry.delete(0,END)
    
    text_area.delete(1.0,END)
    
    
    
    

def bill_print():
    if text_area.get(1.0,END)=='\n':
        messagebox.showerror('error','Bill is not created')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(text_area.get(1.0,END))
        os.startfile(file,'print')
        
        
def serch_bill_no():
    for i in os.listdir('bills/'):
        
       if i.split('.')[0]==bill_no_entry.get():
            f=open(f'bills/{i}','r')
            text_area.delete(1.0,END)
            for data in f:
                text_area.insert(END,data)
            f.close()
            break
    else:
             messagebox.showerror('error','Bill not found')
            
            
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
   
    result=messagebox.askyesno('confirm',"do you want to save bill ?")
    if result:
        
        bill_saving_cont=text_area.get(1.0,END)
        file=open(f'bills/{billnumber}.txt',W)
        file.write(bill_saving_cont)
        file.close()
        messagebox.showinfo('success',f'{billnumber} save successfully')
        
def bill_area():
    text_area.delete(1.0,END)
    if name_entry.get()==""or phone_entry.get()==" " or email_entry=="":
        messagebox.showerror('Error' ,' Please enter customer detail')
    elif cosmatic_price_entry.get()==""and grossary_price_entry.get==" "and cold_price_entry.get()=="" and sweet_price_entry.get()==""and fast_food_price_entry.get()=="":
        messagebox.showerror('Error' ,' No product are selected')
    elif cosmatic_price_entry.get()=="0 RS"and grossary_price_entry.get=="0 RS"and cold_price_entry.get()=="o RS" and sweet_price_entry.get()=="0 RS" and fast_food_price_entry.get()=="0 RS":
        messagebox.showerror('Error' ,' No product are selected')
    else:
       text_area.insert(END,'** Mahakalkar Grossary  store , nagpur**\n')
       text_area.insert(END,f'\nBill NO:{ billnumber}')
       text_area.insert(END,f'\nName:{name_entry.get()}')
       text_area.insert(END,f'\nPhone NO:{ phone_entry.get()}')
       text_area.insert(END,f'\nEmail:{ email_entry.get()}\n')
       text_area.insert(END,'\n********************************************\n')
       text_area.insert(END,'Product\t\tQuantity\t\tPrice')
       text_area.insert(END,'\n********************************************\n')
       if bath_soap_entry.get()!='0':
           text_area.insert(END,f'Bath soap\t\t{ bath_soap_entry.get()}\t\t{soap_price}RS\n')
       if face_cream_entry.get()!='0':
           text_area.insert(END,f'Face cream\t\t{ face_cream_entry.get()}\t\t{face_cream_price}RS\n') 
       if face_wash_entry.get()!='0':
           text_area.insert(END,f'Face wash\t\t{ face_wash_entry.get()}\t\t{face_wash_price}RS\n')   
       if face_powder_entry.get() !='0':
           text_area.insert(END,f'Face powder\t\t{ face_powder_entry.get()}\t\t{face_powder_price}RS\n') 
       if face_bleaching_entry.get() !='0':
           text_area.insert(END,f'Face bleaching \t\t{ face_bleaching_entry.get()}\t\t{face_bleaching_price} Rs\n') 
       if hair_removal_cream_entry.get()!='0':
           text_area.insert(END,f'Hair removal \t\t{ hair_removal_cream_entry.get()}\t\t{hair_removal_cream_price}RS\n')
       if hair_wash_entry.get() !='0':
           text_area.insert(END,f'Hair wash\t\t{ hair_wash_entry.get()}\t\t{hair_wash_price}RS\n')  
       if hair_oil_entry.get()!='0':
           text_area.insert(END,f'Hair oil\t\t{ hair_oil_entry.get()}\t\t{hair_oil_price}RS\n')
       if rice_entry.get()!='0':
           text_area.insert(END,f'Rice\t\t{ rice_entry.get()}\t\t{rice_price}RS\n')
       if wheat_entry.get()!='0':
           text_area.insert(END,f'Wheat\t\t{ wheat_entry.get()}\t\t{wheat_price}RS\n')
       if corn_entry.get()!='0':
           text_area.insert(END,f'Corn\t\t{ corn_entry.get()}\t\t{corn_price}RS\n')
       if rajma_entry.get()!='0':
           text_area.insert(END,f'Rajma\t\t{ rajma_entry.get()}\t\t{rajma_price}RS\n')
       if Toor_dal_entry.get()!='0':
           text_area.insert(END,f'Toor dal\t\t{ Toor_dal_entry.get()}\t\t{Toor_dal_price}RS\n')
       if urad_dal_entry.get()!='0':
           text_area.insert(END,f'Urad dal\t\t{ urad_dal_entry.get()}\t\t{urad_dal_price}RS\n')
       if yellow_mong_entry.get()!='0':
           text_area.insert(END,f'Yellow mong\t\t{ yellow_mong_entry.get()}\t\t{yellow_mong_price}RS\n')
       if chana_dal_entry.get()!='0':
           text_area.insert(END,f'Chana dal\t\t{ chana_dal_entry.get()}\t\t{chana_dal_price}RS\n')
       if split_urad_dal_entry.get()!='0':
           text_area.insert(END,f'Split urad dal\t\t{ split_urad_dal_entry.get()}\t\t{split_urad_dal_price}RS\n')
       if peanut_entry.get()!='0':
           text_area.insert(END,f'Peanut \t\t{ peanut_entry.get()}\t\t{peanut_price}RS\n')
       if gram_entry.get()!='0':
           text_area.insert(END,f'Gram\t\t{ gram_entry.get()}\t\t{gram_price}RS\n')
       if sugar_entry.get()!='0':
           text_area.insert(END,f'sugar\t\t{ sugar_entry.get()}\t\t{sugar_price}RS\n')
       if green_tea_entry.get()!='0':
           text_area.insert(END,f'Green tea\t\t{ green_tea_entry.get()}\t\t{green_tea_price}RS\n')
       if salt_entry.get()!='0':
           text_area.insert(END,f'salt\t\t{ salt_entry.get()}\t\t{salt_price}RS\n')
       if salt_entry.get()!='0':
           text_area.insert(END,f'salt\t\t{ salt_entry.get()}\t\t{salt_price}RS\n')
        
       if poha_entry.get()!='0':
           text_area.insert(END,f'poha\t\t{ poha_entry.get()}\t\t{poha_price}RS\n')
       if rava_entry.get()!='0':
           text_area.insert(END,f'Rava\t\t{ rava_entry.get()}\t\t{rava_price}RS\n')
       if detargent_entry.get()!='0':
           text_area.insert(END,f'Detargent\t\t{ detargent_entry.get()}\t\t{detargent_price}RS\n')
       if wash_bar_entry.get()!='0':
           text_area.insert(END,f'Wash Bar\t\t{ wash_bar.get()}\t\t{wash_bar_price}RS\n')
       if turmaric_entry.get()!='0':
           text_area.insert(END,f'Turmaric\t\t{ turmaric_entry.get()}\t\t{turmaric_price}RS\n')
       if chili_powder_entry.get()!='0':
           text_area.insert(END,f'Chilli powder\t\t{ chili_powder_entry.get()}\t\t{chili_powder_price}RS\n')
       if coriender_powder_entry.get()!='0':
           text_area.insert(END,f'Coriender powder\t\t{ coriender_powder_entry.get()}\t\t{coriender_powder_price}RS\n')
       if sago_entry.get()!='0':
           text_area.insert(END,f'Sago\t\t{ sago_entry.get()}\t\t{sago_price}RS\n')
       if maza_entry.get()!='0':
           text_area.insert(END,f'Maza\t\t{ maza_entry.get()}\t\t{maza_price}RS\n')
       if  fruti_entry.get()!='0':
           text_area.insert(END,f'Fruti\t\t{ fruti_entry.get()}\t\t{fruti_price}RS\n')
       if sting_entry.get()!='0':
           text_area.insert(END,f'Sting\t\t{ sting_entry.get()}\t\t{sting_price}RS\n')
       if duo_entry.get()!='0':
           text_area.insert(END,f'Mountain duo\t\t{ duo_entry.get()}\t\t{duo_price}RS\n') 
       if red_bull_entry.get()!='0':
           text_area.insert(END,f'Red bull\t\t{ red_bull_entry.get()}\t\t{red_bull_price}RS\n')
       if pepsi_entry.get()!='0':
           text_area.insert(END,f'Pepsi\t\t{ pepsi_entry.get()}\t\t{pepsi_price}RS\n')
       if mirinda_entry.get()!='0':
           text_area.insert(END,f'Mirinda\t\t{ mirinda_entry.get()}\t\t{mirinda_price}RS\n')
       if water_bottol_entry.get()!='0':
           text_area.insert(END,f'Water bottle\t\t{ water_bottol_entry.get()}\t\t{water_bottol_price}RS\n')
       if lassi_entry.get()!='0':
           text_area.insert(END,f'Lassi\t\t{ lassi_entry.get()}\t\t{lassi_price}RS\n')
       if sprite_entry.get()!='0':
           text_area.insert(END,f'Sprite\t\t{ sprite_entry.get()}\t\t{sprite_price}RS\n')
       if antome_entry.get()!='0':
           text_area.insert(END,f'Antome\t\t{ antome_entry.get()}\t\t{antome_price}RS\n')
       if pedha_entry.get()!='0':
           text_area.insert(END,f'Pedha\t\t{ pedha_entry.get()}\t\t{pedha_price}RS\n')
       if kaju_katali_entry.get()!='0':
           text_area.insert(END,f'Kaju katali\t\t{ kaju_katali_entry.get()}\t\t{kaju_katali_price}RS\n')
       if son_papadi_entry.get()!='0':
           text_area.insert(END,f'Son papadi\t\t{ son_papadi_entry.get()}\t\t{son_papadi_price}RS\n')
       if shrikhanda_entry.get()!='0':
           text_area.insert(END,f'Shrikhanda\t\t{ shrikhanda_entry.get()}\t\t{shrikhanda_price}RS\n')
       if amrakhanda_entry.get()!='0':
           text_area.insert(END,f'Amrakhanda\t\t{ amrakhanda_entry.get()}\t\t{amrakhanda_price}RS\n')
       if Rasgulla_entry.get()!='0':
           text_area.insert(END,f'Rasgulla\t\t{ Rasgulla_entry.get()}\t\t{rasgulla_price}RS\n')
       if basondi_entry.get()!='0':
           text_area.insert(END,f'Basondi\t\t{ basondi_entry.get()}\t\t{basondi_price}RS\n')
       if gulab_jamun_entry.get()!='0':
           text_area.insert(END,f'Gulab jamun\t\t{ gulab_jamun_entry.get()}\t\t{gulab_jamun_price}RS\n')
       if sweet_curd_entry.get()!='0':
           text_area.insert(END,f'Sweet curd\t\t{ sweet_curd_entry.get()}\t\t{sweet_curd_price}RS\n')
       if jalebi_entry.get()!='0':
           text_area.insert(END,f'Jalebi\t\t{ jalebi_entry.get()}\t\t{jalebi_price}RS\n')
       if ladu_entry.get()!='0':
           text_area.insert(END,f'Ladu\t\t{ ladu_entry.get()}\t\t{ladu_price}RS\n')
       if biscuit_entry.get()!='0':
           text_area.insert(END,f'Biscuit\t\t{ biscuit_entry.get()}\t\t{biscuit_price}RS\n')
       if chips_entry.get()!='0':
           text_area.insert(END,f'Chips\t\t{ chips_entry.get()}\t\t{chips_price}RS\n')
       if maggi_entry.get()!='0':
           text_area.insert(END,f'Maggi\t\t{ maggi_entry.get()}\t\t{maggi_price}RS\n')
       if bread_entry.get()!='0':
           text_area.insert(END,f'Bread\t\t{ bread_entry.get()}\t\t{bread_price}RS\n')
       if butter_entry.get()!='0':
           text_area.insert(END,f'Butter\t\t{ butter_entry.get()}\t\t{butter_price}RS\n')
       if jam_entry.get()!='0':
           text_area.insert(END,f'Jam\t\t{ jam_entry.get()}\t\t{jam_price}RS\n')
       if ketchup_entry.get()!='0':
           text_area.insert(END,f'Ketchup\t\t{ ketchup_entry.get()}\t\t{ketchup_price}RS\n')
       if soya_sause_entry.get()!='0':
           text_area.insert(END,f'Soya sause\t\t{ soya_sause_entry.get()}\t\t{soya_sause_price}RS\n')
       if cooking_oil_entry.get()!='0':
           text_area.insert(END,f'Cooking oil\t\t{ cooking_oil_entry.get()}\t\t{cooking_oil_price}RS\n')
       if tomato_sause_entry.get()!='0':
           text_area.insert(END,f'Tomato sause\t\t{ tomato_sause_entry.get()}\t\t{tomato_sause_price}RS\n')
       if chilli_sause_entry.get()!='0':
           text_area.insert(END,f'Chilli sause\t\t{ chilli_sause_entry.get()}\t\t{chilli_sause_price}RS\n')
       text_area.insert(END,'\n********************************************\n')
       if cosmatic_tax_entry.get()!='0.0 RS':
           text_area.insert(END,f'Cosmatic tax :\t{cosmatix_tax_price} RS\n')
       if grossary_tax_entry.get()!='0.0 RS':
           text_area.insert(END,f'Grossary tax :\t{total_grossary_tax_price} RS\n')
        
       if cold_tax_entry.get()!='0.0 RS':
           text_area.insert(END,f'Cold tax:\t{total_cold_tax_price} RS\n')
       if sweet_tax_entry.get()!='0.0 RS':
           text_area.insert(END,f'Sweet tax:\t{total_sweet_tax_price} RS\n')
       if fast_food_tax_entry.get()!='0.0 RS':
           text_area.insert(END,f'Fast food tax :\t{total_fast_food_tax_price} RS\n')
       text_area.insert(END,'\n********************************************\n')  
       text_area.insert(END,f'Total Product Price:{ total_price_value}\n')
       text_area.insert(END,f'Total Tax Price:\t{ total_tax_value} RS\n')
       text_area.insert(END,'\n********************************************\n')
       text_area.insert(END,f'\nTotal Bill Amount:\t{ total_bill_amount} RS\n')
       text_area.insert(END,'\n********************************************\n')
       messagebox.showinfo('info',f'Total Bill Amount:\t{ total_bill_amount} RS')
       
       save_bill()  
       
       
         
    
        
           

def total():
    global total_cold_tax_price,total_grossary_tax_price,cosmatix_tax_price,total_fast_food_tax_price,total_sweet_tax_price,total_bill_amount
    
    global soap_price
    global face_cream_price
    global face_wash_price
    global hair_removal_cream_price
    global  hair_wash_price
    global hair_oil_price
    global face_powder_price
    global face_bleaching_price
    global cosmatic_price
    
    soap_price=int(bath_soap_entry.get())*32
    face_cream_price=int(face_cream_entry.get())*40
    face_wash_price=int(face_wash_entry.get())*20
    hair_removal_cream_price=int(hair_removal_cream_entry.get())*100
    hair_wash_price=int(hair_wash_entry.get())*160
    hair_oil_price=int(hair_oil_entry.get())*40
    face_powder_price=int(face_powder_entry.get())*50
    face_bleaching_price=int(face_bleaching_entry.get())*60
    total_cosmatic_price=soap_price + face_cream_price +face_wash_price +hair_removal_cream_price +hair_wash_price+hair_oil_price+face_powder_price+face_bleaching_price
    cosmatic_price_entry.delete(0,END)
    cosmatic_price_entry.insert(0,f'{total_cosmatic_price} RS')
    cosmatix_tax_price=total_cosmatic_price*0.08
    cosmatic_tax_entry.delete(0,END)
    cosmatic_tax_entry.insert(0,f'{cosmatix_tax_price} RS')
    
    global rice_price,wheat_price,corn_price,Toor_dal_price,urad_dal_price,yellow_mong_price,chana_dal_price,split_urad_dal_price,rajma_price, peanut_price,gram_price
    rice_price=int(rice_entry.get())*140
    wheat_price=int(wheat_entry.get())*48
    corn_price=int(corn_entry.get())*30
    Toor_dal_price=int(Toor_dal_entry.get())*140
    urad_dal_price=int(urad_dal_entry.get())*140
    yellow_mong_price=int(yellow_mong_entry.get())*160
    chana_dal_price=int(chana_dal_entry.get())*80
    split_urad_dal_price=int(split_urad_dal_entry.get())*160
    rajma_price=int(rajma_entry.get())*200
    peanut_price=int(peanut_entry.get())*140
    gram_price=int(gram_entry.get())*90
    
    global sugar_price,green_tea_price,salt_price,poha_price,rava_price,detargent_price,wash_bar_price,turmaric_price,chili_powder_price,coriender_powder_price,sago_price
    sugar_price=int(sugar_entry.get())*42
    green_tea_price=int(green_tea_entry.get())*350
    salt_price=int(salt_entry.get())*30
    poha_price=int(poha_entry.get())*55
    rava_price=int(rava_entry.get())*40
    detargent_price=int(detargent_entry.get())*150
    wash_bar_price=int(wash_bar_entry.get())*10
    turmaric_price=int(turmaric_entry.get())*200
    chili_powder_price=int(chili_powder_entry.get())*300
    coriender_powder_price=int(coriender_powder_entry.get())*400
    sago_price=int(sago_entry.get())*100
    
    total_grossary1_price=rice_price+wheat_price+corn_price+Toor_dal_price+urad_dal_price+yellow_mong_price+chana_dal_price+split_urad_dal_price+rajma_price+peanut_price+gram_price
    total_grossary2_price=sugar_price+green_tea_price+salt_price+poha_price+rava_price+detargent_price+wash_bar_price+turmaric_price+chili_powder_price+coriender_powder_price+sago_price
    total_grossay_price=total_grossary1_price+total_grossary2_price
    grossary_price_entry.delete(0,END)
    grossary_price_entry.insert(0,f'{total_grossay_price} RS')
    total_grossary_tax_price=total_grossay_price*0.007
    grossary_tax_entry.delete(0,END)
    grossary_tax_entry.insert(0,f'{total_grossary_tax_price} RS')
    
    global maza_price,fruti_price,sting_price,duo_price,red_bull_price,pepsi_price,mirinda_price,water_bottol_price,lassi_price,sprite_price,antome_price
    maza_price=int(maza_entry.get())*30
    fruti_price=int(fruti_entry.get())*20
    sting_price=int(sting_entry.get())*22
    duo_price=int(duo_entry.get())*28
    red_bull_price=int(red_bull_entry.get())*40
    pepsi_price=int(pepsi_entry.get())*40
    mirinda_price=int(mirinda_entry.get())*40
    water_bottol_price=int(water_bottol_entry.get())*10
    lassi_price=int(lassi_entry.get())*25
    sprite_price=int(sprite_entry.get())*28
    antome_price=int(antome_entry.get())*15
    
    total_cold_price=maza_price+fruti_price+sting_price+duo_price+red_bull_price+pepsi_price+mirinda_price+water_bottol_price+lassi_price+sprite_price+antome_price
    cold_price_entry.delete(0,END)
    cold_price_entry.insert(0,f'{total_cold_price} RS')
    total_cold_tax_price=total_cold_price*0.081
    cold_tax_entry.delete(0,END)
    cold_tax_entry.insert(0,f'{total_cold_tax_price} RS')
   
    
    global pedha_price,kaju_katali_price,son_papadi_price,shrikhanda_price,amrakhanda_price,rasgulla_price,basondi_price,gulab_jamun_price,sweet_curd_price,jalebi_price,ladu_price
    pedha_price=int(pedha_entry.get())*320
    kaju_katali_price=int(kaju_katali_entry.get())*440
    son_papadi_price=int(son_papadi_entry.get())*200
    shrikhanda_price=int(shrikhanda_entry.get())*400
    amrakhanda_price=int(amrakhanda_entry.get())*400
    rasgulla_price=int(Rasgulla_entry.get())*5
    basondi_price=int(basondi_entry.get())*80
    gulab_jamun_price=int(gulab_jamun_entry.get())*8
    sweet_curd_price=int(sweet_curd_entry.get())*40
    jalebi_price=int(jalebi_entry.get())*240
    ladu_price=int(ladu_entry.get())*400
    total_sweet_price=pedha_price+kaju_katali_price+son_papadi_price+shrikhanda_price+amrakhanda_price+rasgulla_price+basondi_price+gulab_jamun_price+sweet_curd_price+jalebi_price+ladu_price
    sweet_price_entry.delete(0,END)
    sweet_price_entry.insert(0,f'{total_sweet_price} RS')
    total_sweet_tax_price=total_sweet_price*0.009
    sweet_tax_entry.delete(0,END)
    sweet_tax_entry.insert(0,f'{total_sweet_tax_price} RS')
    
    
    global biscuit_price,chips_price,maggi_price,bread_price,butter_price,jam_price,ketchup_price,soya_sause_price,cooking_oil_price,tomato_sause_price,chilli_sause_price
    biscuit_price=int(biscuit_entry.get())*10
    chips_price=int(chips_entry.get())*5
    maggi_price=int(maggi_entry.get())*12
    bread_price=int(bread_entry.get())*10
    butter_price=int(butter_entry.get())*400
    jam_price=int(jam_entry.get())*120
    ketchup_price=int(ketchup_entry.get())*250
    soya_sause_price=int(soya_sause_entry.get())*160
    cooking_oil_price=int(cooking_oil_entry.get())*180
    tomato_sause_price=int(tomato_sause_entry.get())*15
    chilli_sause_price=int(chilli_sause_entry.get())*15
    total_fast_food_price=biscuit_price+chips_price+maggi_price+bread_price+butter_price+jam_price+ketchup_price+soya_sause_price+cooking_oil_price+tomato_sause_price+chilli_sause_price
    fast_food_price_entry.delete(0,END)
    fast_food_price_entry.insert(0,f'{total_fast_food_price} RS')
    total_fast_food_tax_price=total_fast_food_price*0.04
    fast_food_tax_entry.delete(0,END)
    fast_food_tax_entry.insert(0,f'{total_fast_food_tax_price} RS')
    
    global total_price_value
    global total_tax_value
    
    total_price_value=total_cosmatic_price+total_cold_price+total_grossay_price+total_fast_food_price+total_sweet_price
    total_price_entry.delete(0,END)
    total_price_entry.insert(0,f'{total_price_value} RS')
    
    total_tax_value=total_cold_tax_price+total_fast_food_tax_price+total_grossary_tax_price+total_sweet_tax_price+cosmatix_tax_price
    total_tax_entry.delete(0,END)
    total_tax_entry.insert(0,f'{total_tax_value} RS')
    
    total_bill_amount=total_tax_value+total_price_value

    
    
# gui part
root = Tk()
root.geometry("1350x700+0+0")
root.title("billing softweare")

root.iconbitmap('egal1.png')
heading=Label(root,text='Grossary billing systam',font=('times new roman',30,'bold')
              ,bg='gray20' ,foreground='gold' )
heading.pack(fill=X)

custmor_detail_frame=LabelFrame(root,text='customer detail',font=('times new roman',15,'bold'),foreground='red',background='gray20')
custmor_detail_frame.pack(fill=X) 

name_label=Label(custmor_detail_frame,text='name',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
name_label.grid(row=0,column=0,padx=20,pady=10)
name_entry =Entry(custmor_detail_frame,font=('arial',15),width=18)
name_entry.grid(row=0,column=1,padx=8,pady=10)

phone=Label(custmor_detail_frame,text='phone no',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
phone.grid(row=0,column=2,padx=20,pady=2)
phone_entry =Entry(custmor_detail_frame,font=('arial',15),width=18)
phone_entry.grid(row=0,column=3,padx=10)

email=Label(custmor_detail_frame,text='Email',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
email.grid(row=0,column=4,padx=20,pady=2)
email_entry =Entry(custmor_detail_frame,font=('arial',15),width=18)
email_entry.grid(row=0,column=5,padx=8)

bill_no=Label(custmor_detail_frame,text='Bill NO',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
bill_no.grid(row=0,column=6,padx=20,pady=2)
bill_no_entry =Entry(custmor_detail_frame,font=('arial',15),width=18)
bill_no_entry.grid(row=0,column=7,padx=8)

btn=Button(custmor_detail_frame,text='serch', font=('arial',10,'bold'),width=12, command=serch_bill_no)
btn.grid(row=0,column=8,padx=8)

product_frame=Frame(root )
product_frame.pack()

cosmatics=LabelFrame(product_frame,text='cosmatics',font=('times new roman',15,'bold'),foreground='red',background='gray20')
cosmatics.grid(row=0,column=0)

bath_soap=Label(cosmatics,text='bath soap',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
bath_soap.grid(row=0,column=0,pady=6,padx=6)
bath_soap_entry=Entry(cosmatics,font=('arial',10),width=8)
bath_soap_entry.grid(row=0,column=1,pady=6,padx=6)
bath_soap_entry.insert(0,0)

face_cream=Label(cosmatics,text='face cream',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_cream.grid(row=1,column=0,pady=6,padx=6)
face_cream_entry=Entry(cosmatics,font=('arial',10),width=8)
face_cream_entry.grid(row=1,column=1,pady=6,padx=6)
face_cream_entry.insert(0,0)

face_wash=Label(cosmatics,text='face wash',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_wash.grid(row=2,column=0,pady=6,padx=6)
face_wash_entry=Entry(cosmatics,font=('arial',10),width=8)
face_wash_entry.grid(row=2,column=1,pady=6,padx=6)
face_wash_entry.insert(0,0)

hair_removal_cream=Label(cosmatics,text='hair removal',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
hair_removal_cream.grid(row=3,column=0,pady=6,padx=6)
hair_removal_cream_entry=Entry(cosmatics,font=('arial',10),width=8)
hair_removal_cream_entry.grid(row=3,column=1,pady=6,padx=6)
hair_removal_cream_entry.insert(0,0)

hair_wash=Label(cosmatics,text='hair wash',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
hair_wash.grid(row=4,column=0,pady=6,padx=6)
hair_wash_entry=Entry(cosmatics,font=('arial',10),width=8)
hair_wash_entry.grid(row=4,column=1,pady=6,padx=6)
hair_wash_entry.insert(0,0)

hair_oil=Label(cosmatics,text='hair oil',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
hair_oil.grid(row=5,column=0,pady=6,padx=6)
hair_oil_entry=Entry(cosmatics,font=('arial',10),width=8)
hair_oil_entry.grid(row=5,column=1,pady=6,padx=6)
hair_oil_entry.insert(0,0)

face_powder=Label(cosmatics,text='face powder',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_powder.grid(row=6,column=0,pady=6,padx=6)
face_powder_entry=Entry(cosmatics,font=('arial',10),width=8)
face_powder_entry.grid(row=6,column=1,pady=6,padx=6)
face_powder_entry.insert(0,0)

face_bleaching=Label(cosmatics,text='face powder',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_bleaching.grid(row=7,column=0,pady=6,padx=6)
face_bleaching_entry=Entry(cosmatics,font=('arial',10),width=8)
face_bleaching_entry.grid(row=7,column=1,pady=6,padx=6)
face_bleaching_entry.insert(0,0)

eye_liner=Label(cosmatics,text='eye liner',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
eye_liner.grid(row=8,column=0,pady=6,padx=6)
eye_liner_entry=Entry(cosmatics,font=('arial',10),width=8)
eye_liner_entry.grid(row=8,column=1,pady=6,padx=6)
eye_liner_entry.insert(0,0)

face_pack=Label(cosmatics,text='face pack',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_pack.grid(row=9,column=0,pady=6,padx=6)
face_pack_entry=Entry(cosmatics,font=('arial',10),width=8)
face_pack_entry.grid(row=9,column=1,pady=6,padx=6)
face_pack_entry.insert(0,0)

face_maker=Label(cosmatics,text='face maker',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
face_maker.grid(row=10,column=0,pady=6,padx=6)
face_maker_entry=Entry(cosmatics,font=('arial',10),width=8)
face_maker_entry.grid(row=10,column=1,pady=6,padx=6)
face_maker_entry.insert(0,0)





grossary=LabelFrame(product_frame,text='grossary',font=('times new roman',15,'bold'),foreground='red',background='gray20')
grossary.grid(row=0,column=1)

rice=Label(grossary,text='rice',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
rice.grid(row=0,column=0,pady=6 ,padx=6)
rice_entry=Entry(grossary,font=('arial',10),width=8)
rice_entry.grid(row=0,column=1,pady=6,padx=6)
rice_entry.insert(0,0)

wheat=Label(grossary,text='wheat',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
wheat.grid(row=1,column=0,pady=6,padx=6)
wheat_entry=Entry(grossary,font=('arial',10),width=8)
wheat_entry.grid(row=1,column=1,pady=6,padx=6)
wheat_entry.insert(0,0)

corn=Label(grossary,text='corn flour',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
corn.grid(row=2,column=0,pady=6,padx=6)
corn_entry=Entry(grossary,font=('arial',10),width=8)
corn_entry.grid(row=2,column=1,pady=6,padx=6)
corn_entry.insert(0,0)

Toor_dal=Label(grossary,text='Toor dal',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
Toor_dal.grid(row=3,column=0,pady=6,padx=6)
Toor_dal_entry=Entry(grossary,font=('arial',10),width=8)
Toor_dal_entry.grid(row=3,column=1,pady=6,padx=6)
Toor_dal_entry.insert(0,0)

urad_dal=Label(grossary,text='Urad dal',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
urad_dal.grid(row=4,column=0,pady=6)
urad_dal_entry=Entry(grossary,font=('arial',10),width=8)
urad_dal_entry.grid(row=4,column=1,pady=6,padx=6)
urad_dal_entry.insert(0,0)

yellow_mong=Label(grossary,text='yellow mong',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
yellow_mong.grid(row=5,column=0,pady=6,padx=6)
yellow_mong_entry=Entry(grossary,font=('arial',10),width=8)
yellow_mong_entry.grid(row=5,column=1,pady=6,padx=6)
yellow_mong_entry.insert(0,0)

chana_dal=Label(grossary,text='chana dal',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
chana_dal.grid(row=6,column=0,pady=6,padx=6)
chana_dal_entry=Entry(grossary,font=('arial',10),width=8)
chana_dal_entry.grid(row=6,column=1,pady=6,padx=6)
chana_dal_entry.insert(0,0)

split_urad_dal=Label(grossary,text='Split urad dal',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
split_urad_dal.grid(row=7,column=0,pady=6,padx=6)
split_urad_dal_entry=Entry(grossary,font=('arial',10),width=8)
split_urad_dal_entry.grid(row=7,column=1,pady=6,padx=6)
split_urad_dal_entry.insert(0,0)

rajma=Label(grossary,text='Rajma',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
rajma.grid(row=8,column=0,pady=6,padx=6)
rajma_entry=Entry(grossary,font=('arial',10),width=8)
rajma_entry.grid(row=8,column=1,pady=6,padx=6)
rajma_entry.insert(0,0)

peanut=Label(grossary,text='Peanut',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
peanut.grid(row=9,column=0,pady=6,padx=6)
peanut_entry=Entry(grossary,font=('arial',10),width=8)
peanut_entry.grid(row=9,column=1,pady=6,padx=6)
peanut_entry.insert(0,0)

gram=Label(grossary,text='Gram',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
gram.grid(row=10,column=0,pady=6,padx=6)
gram_entry=Entry(grossary,font=('arial',10),width=8)
gram_entry.grid(row=10,column=1,pady=6,padx=6)
gram_entry.insert(0,0)




daily=LabelFrame(product_frame,text='grossary',font=('times new roman',15,'bold'),foreground='red',background='gray20')
daily.grid(row=0,column=2)

sugar=Label(daily,text='Sugar',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sugar.grid(row=0,column=0,pady=6 ,padx=6)
sugar_entry=Entry(daily,font=('arial',10),width=8)
sugar_entry.grid(row=0,column=1,pady=6,padx=6)
sugar_entry.insert(0,0)

green_tea=Label(daily,text='Green tea',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
green_tea.grid(row=1,column=0,pady=6,padx=6)
green_tea_entry=Entry(daily,font=('arial',10),width=8)
green_tea_entry.grid(row=1,column=1,pady=6,padx=6)
green_tea_entry.insert(0,0)

salt=Label(daily,text='Salt',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
salt.grid(row=2,column=0,pady=6,padx=6)
salt_entry=Entry(daily,font=('arial',10),width=8)
salt_entry.grid(row=2,column=1,pady=6,padx=6)
salt_entry.insert(0,0)

poha=Label(daily,text='Poha',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
poha.grid(row=3,column=0,pady=6,padx=6)
poha_entry=Entry(daily,font=('arial',10),width=8)
poha_entry.grid(row=3,column=1,pady=6,padx=6)
poha_entry.insert(0,0)

rava=Label(daily,text='Rava',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
rava.grid(row=4,column=0,pady=6)
rava_entry=Entry(daily,font=('arial',10),width=8)
rava_entry.grid(row=4,column=1,pady=6,padx=6)
rava_entry.insert(0,0)

detargent=Label(daily,text='Washing powder',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
detargent.grid(row=5,column=0,pady=6,padx=6)
detargent_entry=Entry(daily,font=('arial',10),width=8)
detargent_entry.grid(row=5,column=1,pady=6,padx=6)
detargent_entry.insert(0,0)

wash_bar=Label(daily,text='wash soap',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
wash_bar.grid(row=6,column=0,pady=6,padx=6)
wash_bar_entry=Entry(daily,font=('arial',10),width=8)
wash_bar_entry.grid(row=6,column=1,pady=6,padx=6)
wash_bar_entry.insert(0,0)

turmaric=Label(daily,text='Turmaric',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
turmaric.grid(row=7,column=0,pady=6,padx=6)
turmaric_entry=Entry(daily,font=('arial',10),width=8)
turmaric_entry.grid(row=7,column=1,pady=6,padx=6)  
turmaric_entry.insert(0,0) 

chili_powder=Label(daily,text='Chilli powder',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
chili_powder.grid(row=8,column=0,pady=6,padx=6)
chili_powder_entry=Entry(daily,font=('arial',10),width=8)
chili_powder_entry.grid(row=8,column=1,pady=6,padx=6)
chili_powder_entry.insert(0,0)

coriender_powder=Label(daily,text='Coriender powder',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
coriender_powder.grid(row=9,column=0,pady=6,padx=6)
coriender_powder_entry=Entry(daily,font=('arial',10),width=8)
coriender_powder_entry.grid(row=9,column=1,pady=6,padx=6)
coriender_powder_entry.insert(0,0)

sago=Label(daily,text='face maker',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sago.grid(row=10,column=0,pady=6,padx=6)
sago_entry=Entry(daily,font=('arial',10),width=8)
sago_entry.grid(row=10,column=1,pady=6,padx=6)
sago_entry.insert(0,0)





cold=LabelFrame(product_frame,text='cold',font=('times new roman',15,'bold'),foreground='red',background='gray20')
cold.grid(row=0,column=3)

maza=Label(cold,text='Maza',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
maza.grid(row=0,column=0,pady=6 ,padx=6)
maza_entry=Entry(cold,font=('arial',10),width=8)
maza_entry.grid(row=0,column=1,pady=6,padx=6)
maza_entry.insert(0,0)

fruti=Label(cold,text='Fruti',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
fruti.grid(row=1,column=0,pady=6,padx=6)
fruti_entry=Entry(cold,font=('arial',10),width=8)
fruti_entry.grid(row=1,column=1,pady=6,padx=6)
fruti_entry.insert(0,0)

sting=Label(cold,text='Sting',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sting.grid(row=2,column=0,pady=6,padx=6)
sting_entry=Entry(cold,font=('arial',10),width=8)
sting_entry.grid(row=2,column=1,pady=6,padx=6)
sting_entry.insert(0,0)

duo=Label(cold,text='Mountain duo',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
duo.grid(row=3,column=0,pady=6,padx=6)
duo_entry=Entry(cold,font=('arial',10),width=8)
duo_entry.grid(row=3,column=1,pady=6,padx=6)
duo_entry.insert(0,0)

red_bull=Label(cold,text='Red bull',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
red_bull.grid(row=4,column=0,pady=6)
red_bull_entry=Entry(cold,font=('arial',10),width=8)
red_bull_entry.grid(row=4,column=1,pady=6,padx=6)
red_bull_entry.insert(0,0)

pepsi=Label(cold,text='Pepsi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
pepsi.grid(row=5,column=0,pady=6,padx=6)
pepsi_entry=Entry(cold,font=('arial',10),width=8)
pepsi_entry.grid(row=5,column=1,pady=6,padx=6)
pepsi_entry.insert(0,0)

mirinda=Label(cold,text='Mirinda',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
mirinda.grid(row=6,column=0,pady=6,padx=6)
mirinda_entry=Entry(cold,font=('arial',10),width=8)
mirinda_entry.grid(row=6,column=1,pady=6,padx=6)
mirinda_entry.insert(0,0)

water_bottol=Label(cold,text='Water bottle',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
water_bottol.grid(row=7,column=0,pady=6,padx=6)
water_bottol_entry=Entry(cold,font=('arial',10),width=8)
water_bottol_entry.grid(row=7,column=1,pady=6,padx=6)
water_bottol_entry.insert(0,0)

lassi=Label(cold,text='Lassi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
lassi.grid(row=8,column=0,pady=6,padx=6)
lassi_entry=Entry(cold,font=('arial',10),width=8)
lassi_entry.grid(row=8,column=1,pady=6,padx=6)
lassi_entry.insert(0,0)

sprite=Label(cold,text='Sprite',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sprite.grid(row=9,column=0,pady=6,padx=6)
sprite_entry=Entry(cold,font=('arial',10),width=8)
sprite_entry.grid(row=9,column=1,pady=6,padx=6)
sprite_entry.insert(0,0)

antome=Label(cold,text='Antome',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
antome.grid(row=10,column=0,pady=6,padx=6)
antome_entry=Entry(cold,font=('arial',10),width=8)
antome_entry.grid(row=10,column=1,pady=6,padx=6)
antome_entry.insert(0,0)







sweet=LabelFrame(product_frame,text='sweet',font=('times new roman',15,'bold'),foreground='red',background='gray20')
sweet.grid(row=0,column=4)

pedha=Label(sweet,text='Pedha',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
pedha.grid(row=0,column=0,pady=6 ,padx=6)
pedha_entry=Entry(sweet,font=('arial',10),width=8)
pedha_entry.grid(row=0,column=1,pady=6,padx=6)
pedha_entry.insert(0,0)

kaju_katali=Label(sweet,text='Kaju katali',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
kaju_katali.grid(row=1,column=0,pady=6,padx=6)
kaju_katali_entry=Entry(sweet,font=('arial',10),width=8)
kaju_katali_entry.grid(row=1,column=1,pady=6,padx=6)
kaju_katali_entry.insert(0,0)

son_papadi=Label(sweet,text='Son papadi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
son_papadi.grid(row=2,column=0,pady=6,padx=6)
son_papadi_entry=Entry(sweet,font=('arial',10),width=8)
son_papadi_entry.grid(row=2,column=1,pady=6,padx=6)
son_papadi_entry.insert(0,0)

shrikhanda=Label(sweet,text='Shrikhanda',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
shrikhanda.grid(row=3,column=0,pady=6,padx=6)
shrikhanda_entry=Entry(sweet,font=('arial',10),width=8)
shrikhanda_entry.grid(row=3,column=1,pady=6,padx=6)
shrikhanda_entry.insert(0,0)

amrakhanda=Label(sweet,text='Amrakhanda',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
amrakhanda.grid(row=4,column=0,pady=6)
amrakhanda_entry=Entry(sweet,font=('arial',10),width=8)
amrakhanda_entry.grid(row=4,column=1,pady=6,padx=6)
amrakhanda_entry.insert(0,0)

Rasgulla=Label(sweet,text='Rasgulla',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
Rasgulla.grid(row=5,column=0,pady=6,padx=6)
Rasgulla_entry=Entry(sweet,font=('arial',10),width=8)
Rasgulla_entry.grid(row=5,column=1,pady=6,padx=6)
Rasgulla_entry.insert(0,0)

basondi=Label(sweet,text='Basondi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
basondi.grid(row=6,column=0,pady=6,padx=6)
basondi_entry=Entry(sweet,font=('arial',10),width=8)
basondi_entry.grid(row=6,column=1,pady=6,padx=6)
basondi_entry.insert(0,0)

gulab_jamun=Label(sweet,text='Gulab jamun',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
gulab_jamun.grid(row=7,column=0,pady=6,padx=6)
gulab_jamun_entry=Entry(sweet,font=('arial',10),width=8)
gulab_jamun_entry.grid(row=7,column=1,pady=6,padx=6)
gulab_jamun_entry.insert(0,0)

sweet_curd=Label(sweet,text='Sweet curd',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sweet_curd.grid(row=8,column=0,pady=6,padx=6)
sweet_curd_entry=Entry(sweet,font=('arial',10),width=8)
sweet_curd_entry.grid(row=8,column=1,pady=6,padx=6)
sweet_curd_entry.insert(0,0)

jalebi=Label(sweet,text='Jalebi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
jalebi.grid(row=9,column=0,pady=6,padx=6)
jalebi_entry=Entry(sweet,font=('arial',10),width=8)
jalebi_entry.grid(row=9,column=1,pady=6,padx=6)
jalebi_entry.insert(0,0)

ladu=Label(sweet,text='Ladu',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
ladu.grid(row=10,column=0,pady=6,padx=6)
ladu_entry=Entry(sweet,font=('arial',10),width=8)
ladu_entry.grid(row=10,column=1,pady=6,padx=6)
ladu_entry.insert(0,0)







fast_food=LabelFrame(product_frame,text='fast food',font=('times new roman',15,'bold'),foreground='red',background='gray20')
fast_food.grid(row=0,column=5)

biscuit=Label(fast_food,text='Biscuit',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
biscuit.grid(row=0,column=0,pady=6 ,padx=6)
biscuit_entry=Entry(fast_food,font=('arial',10),width=8)
biscuit_entry.grid(row=0,column=1,pady=6,padx=6)
biscuit_entry.insert(0,0)

chips=Label(fast_food,text='Chips',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
chips.grid(row=1,column=0,pady=6,padx=6)
chips_entry=Entry(fast_food,font=('arial',10),width=8)
chips_entry.grid(row=1,column=1,pady=6,padx=6)
chips_entry.insert(0,0)

maggi=Label(fast_food,text='Maggi',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
maggi.grid(row=2,column=0,pady=6,padx=6)
maggi_entry=Entry(fast_food,font=('arial',10),width=8)
maggi_entry.grid(row=2,column=1,pady=6,padx=6)
maggi_entry.insert(0,0)

bread=Label(fast_food,text='Bread',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
bread.grid(row=3,column=0,pady=6,padx=6)
bread_entry=Entry(fast_food,font=('arial',10),width=8)
bread_entry.grid(row=3,column=1,pady=6,padx=6)
bread_entry.insert(0,0)

butter=Label(fast_food,text='Butter',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
butter.grid(row=4,column=0,pady=6)
butter_entry=Entry(fast_food,font=('arial',10),width=8)
butter_entry.grid(row=4,column=1,pady=6,padx=6)
butter_entry.insert(0,0)

jam=Label(fast_food,text='jam',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
jam.grid(row=5,column=0,pady=6,padx=6)
jam_entry=Entry(fast_food,font=('arial',10),width=8)
jam_entry.grid(row=5,column=1,pady=6,padx=6)
jam_entry.insert(0,0)

ketchup=Label(fast_food,text='Ketchup',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
ketchup.grid(row=6,column=0,pady=6,padx=6)
ketchup_entry=Entry(fast_food,font=('arial',10),width=8)
ketchup_entry.grid(row=6,column=1,pady=6,padx=6)
ketchup_entry.insert(0,0)

soya_sause=Label(fast_food,text='Soya sause',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
soya_sause.grid(row=7,column=0,pady=6,padx=6)
soya_sause_entry=Entry(fast_food,font=('arial',10),width=8)
soya_sause_entry.grid(row=7,column=1,pady=6,padx=6)
soya_sause_entry.insert(0,0)

cooking_oil=Label(fast_food,text='Cooing oil',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
cooking_oil.grid(row=8,column=0,pady=6,padx=6)
cooking_oil_entry=Entry(fast_food,font=('arial',10),width=8)
cooking_oil_entry.grid(row=8,column=1,pady=6,padx=6)
cooking_oil_entry.insert(0,0)

tomato_sause=Label(fast_food,text='Tomato sause',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
tomato_sause.grid(row=9,column=0,pady=6,padx=6)
tomato_sause_entry=Entry(fast_food,font=('arial',10),width=8)
tomato_sause_entry.grid(row=9,column=1,pady=6,padx=6)
tomato_sause_entry.insert(0,0)

chilli_sause=Label(fast_food,text='Chilli sause',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
chilli_sause.grid(row=10,column=0,pady=6,padx=6)
chilli_sause_entry=Entry(fast_food,font=('arial',10),width=8)
chilli_sause_entry.grid(row=10,column=1,pady=6,padx=6)
chilli_sause_entry.insert(0,0)










bill =Frame(product_frame)
bill.grid(row=0,column=6)

billarea=Label(bill,text='Bill area',font=('times new roman',15,'bold'))
billarea.pack(fill=X)
scrollbar=Scrollbar(bill,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
text_area=Text(bill,height=22,width=44 ,yscrollcommand=Scrollbar.set)
text_area.pack()
scrollbar.config(command=text_area.yview)






billmenu=LabelFrame(root,text='bill menu',font=('times new roman',15,'bold'),foreground='red',background='gray20')
billmenu.pack()

cosmatic_price=Label(billmenu,text='cosmatic price',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
cosmatic_price.grid(row=0,column=0,pady=6,padx=6)
cosmatic_price_entry=Entry(billmenu,font=('arial',10),width=10)
cosmatic_price_entry.grid(row=0,column=1,pady=6,padx=6)



grossary_price=Label(billmenu,text='grossary price',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
grossary_price.grid(row=1,column=0,pady=6,padx=6)
grossary_price_entry=Entry(billmenu,font=('arial',10),width=10)
grossary_price_entry.grid(row=1,column=1,pady=6,padx=6)

cold_price=Label(billmenu,text='cold price',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
cold_price.grid(row=2,column=0,pady=6,padx=6)
cold_price_entry=Entry(billmenu,font=('arial',10),width=10)
cold_price_entry.grid(row=2,column=1,pady=6,padx=6)

sweet_price=Label(billmenu,text='sweet price',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sweet_price.grid(row=0,column=2,pady=6,padx=6)
sweet_price_entry=Entry(billmenu,font=('arial',10),width=10)
sweet_price_entry.grid(row=0,column=3,pady=6,padx=6)

fast_food_price=Label(billmenu,text='Fast food price',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
fast_food_price.grid(row=1,column=2,pady=6,padx=6)
fast_food_price_entry=Entry(billmenu,font=('arial',10),width=10)
fast_food_price_entry.grid(row=1,column=3,pady=6,padx=6)

total_price=Label(billmenu,text='Total price',font=('times new roman',10,'bold'),foreground='green',background='gray20')
total_price.grid(row=2,column=2,pady=6,padx=6)
total_price_entry=Entry(billmenu,font=('arial',10),width=10)
total_price_entry.grid(row=2,column=3,pady=6,padx=6)



cosmatic_tax=Label(billmenu,text='Cosmatic tax',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
cosmatic_tax.grid(row=0,column=4,pady=6,padx=6)
cosmatic_tax_entry=Entry(billmenu,font=('arial',10),width=10)
cosmatic_tax_entry.grid(row=0,column=5,pady=6,padx=6)

grossary_tax=Label(billmenu,text='Grossary tax',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
grossary_tax.grid(row=1,column=4,pady=6,padx=6)
grossary_tax_entry=Entry(billmenu,font=('arial',10),width=10)
grossary_tax_entry.grid(row=1,column=5,pady=6,padx=6)

cold_tax=Label(billmenu,text='Cold tax',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
cold_tax.grid(row=2,column=4,pady=6,padx=6)
cold_tax_entry=Entry(billmenu,font=('arial',10),width=10)
cold_tax_entry.grid(row=2,column=5,pady=6,padx=6)

sweet_tax=Label(billmenu,text='Sweet tax',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
sweet_tax.grid(row=0,column=6,pady=6,padx=6)
sweet_tax_entry=Entry(billmenu,font=('arial',10),width=10)
sweet_tax_entry.grid(row=0,column=7,pady=6,padx=6)

fast_food_tax=Label(billmenu,text='Fast food tax',font=('times new roman',10,'bold'),foreground='blue',background='gray20')
fast_food_tax.grid(row=1,column=6,pady=6,padx=6)
fast_food_tax_entry=Entry(billmenu,font=('arial',10),width=10)
fast_food_tax_entry.grid(row=1,column=7,pady=6,padx=6)

total_tax=Label(billmenu,text='Total tax',font=('times new roman',10,'bold'),foreground='green',background='gray20')
total_tax.grid(row=2,column=6,pady=6,padx=6)
total_tax_entry=Entry(billmenu,font=('arial',10),width=10)
total_tax_entry.grid(row=2,column=7,pady=6,padx=6)





btnframe=Frame(billmenu)
btnframe.grid(row=1,column=8)

totalbtn=Button(btnframe,text='total',font=('arial',16,'bold'),bg='gray20',fg='white',pady=10,width=10,bd=5,command=total)
totalbtn.grid(row=1,column=8,pady=4,padx=6)

billbtn=Button(btnframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',pady=10,width=10,bd=5, command=bill_area)
billbtn.grid(row=1,column=9,pady=4,padx=6)


printbtn=Button(btnframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',pady=10,width=10,bd=5,command=bill_print)
printbtn.grid(row=1,column=10,pady=4,padx=6)

clearbtn=Button(btnframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',pady=10,width=10,bd=5,command=clear)
clearbtn.grid(row=1,column=11,pady=4,padx=6)


root.mainloop()