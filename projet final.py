from tkinter import*
from pygame import mixer


"""fonctions"""
def Victoire():
    global Y_mort,A_mort,A_image,A_app,A_sprites,A_app,Y_app,A_app_aux,Stage_app,Y_sprites,Y_image,Y_app
    if Y_mort==1:
        A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_victoire[A_sprites]}")
        can.itemconfigure(A_app,image=A_image)
        can.coords(A_app,950,500)
        A_sprites=A_sprites+1

    else:
        Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_victoire[Y_sprites]}")
        can.itemconfigure(Y_app,image=Y_image)
        can.coords(Y_app,950,500)
        Y_sprites=Y_sprites+1

    if Y_sprites<25 and A_sprites<25:
        fen.after(60,Victoire)
    else:
        can.delete(Y_app,A_app,A_app_aux,Stage_app)
        Menu()


def Stage_menu():
    global Selec_stage, background_anim, indice_stage,image, Menu_image,imagebg,indice_background,indice_stage,Selec_image,image_stage_selec,Menu_image,imagemen,x_stage

    verif_select=1
    selection_pos_y=480


    indice_background=1
    indice_stage=1
    x_stage = 335

    deplmen=0


    bg_anim=PhotoImage(file= f"Interface/{background_animation[indice_background]}")
    imagebg=can.create_image(950,500, image = bg_anim)
    Selec_image=PhotoImage(file=f"Interface/{Selec_stage[indice_stage]}")
    image_stage_selec=can.create_image(x_stage,410, image=Selec_image)
    Menu_image=PhotoImage(file="Interface/3_stage_image.png")
    imagemen=can.create_image(950,500, image = Menu_image)
    background_anim()
    Selec_stage_anim()

    fen.bind('<q>', Stage_gauche)
    fen.bind('<d>', Stage_droite)
    fen.bind('<k>',JEU)




def background_anim():
    global background_anim,bg_anim,imagebg,indice_background,Menu_image,imagemen,verif_select


    bg_anim=PhotoImage(file=f"Interface/{background_animation[indice_background]}")
    can.itemconfigure(imagebg, image = bg_anim)
    indice_background= (indice_background + 1)%4
    Menu_image=PhotoImage(file="Interface/3_stage_image.png")
    can.itemconfigure(imagemen,image=Menu_image)



def Selec_stage_anim():
    global Selec_stage, x_stage,indice_stage,Selec_image,image_stage_selec,verif_select
    Selec_image=PhotoImage(file=f"Interface/{Selec_stage[indice_stage]}")
    can.itemconfigure(image_stage_selec, image = Selec_image)
    can.coords(image_stage_selec,x_stage,405)


    indice_stage= (indice_stage+1)%6
    if verif_select==1:
        fen.after(80, Selec_stage_anim)



def Stage_gauche(m):
    global x_stage,indice_stage
    indice_stage=0
    if x_stage == 335:
        x_stage = 1571
    else :
        x_stage = x_stage - 618


def Stage_droite(m):
    global x_stage,indice_stage
    indice_stage=0
    if x_stage == 1571:
        x_stage = 335
    else :
        x_stage = x_stage + 618

def Vie_et_placement():
    global Y_sortie,Y_mort,A_mort,A_subit_air,Y_subit_air,A_mort,Y_mort,COLLISIONS,A_sortie,Y_sortie,A_fort_air,A_roulade,Y_roulade,position_stage,Stage_image,Stage_app,le_stage,AM_image,YM_image,AM_app,YM_app,AM_sprites,YM_sprites,A_garde_air,Y_garde_air,A_garde,Y_garde,A_leger_air,A_fort_air,Y_coup_bas,deplacements,A_image_aux,S_sprites,A_app_aux,A_subit,Aaux_posx,Aaux_posy,A_dispo_garde,Y_subit,A_dispo_soulevement,Y_up,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air,Y_fort_air,Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut,Y_hurtbox,A_vie,A_degat,Y_vie,Y_degat,A_hpp,Y_hpp,A_hp,Y_hp,COMBAT,A_hp,Y_hp,A_stance,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHI2x2,AHI2y1,AHI2y2,AHI3x1,AHI3x2,AHI3y1,AHI3y2,AHISx1,AHISx2,AHISy1,AHISy2,AHUx1,AHUx2,AHUy1,AHUx2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHI2x1,YHI2x2,YHI2y1,YHI2y2,YHI3x1,YHI3x2,YHI3y1,YHI3y2,YHISx1,YHISx2,YHISy1,YHISy2,YHUx1,YHUx2,YHUy1,YHUx2,YHUy2,agencement,Y_posx,Y_posy,Y_sprites,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,Y_stance,Y_dir_saut,Y_image,Y_sprites,Y_app,A_fort_air,A_leger_air,A_up,A_compteur_fort,A_compteur_faible,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo,agencement,A_posx,A_posy,A_sprites,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,A_stance,A_dir_saut,A_sprites,A_image,A_posx,Y_posx,A_app,A_hurtbox,AHUx1,AHUx2,AHUy1,AHUy2,A_hitbox_1,AHI1x1,AHI1x2,AHI1y1,AHI1y2
    if agencement==1:
        if A_DPL_D==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_G==1:

            Y_garde=1

        else:
            Y_garde=0
    elif agencement==2:

        if A_DPL_G==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_D==1:

            Y_garde=1

        else:
            Y_garde=0

     #######################################################################################     BARRES DE VIE     #######################################################################################
    if Y_hp<Y_hpp:
        Y_hpp=Y_hpp-5
    if A_hp>A_hpp:
        A_hpp=A_hpp+5
    if Y_hp<179 and A_posy==700 and Y_posy==700:



        Y_hp=179
        A_sortie=1

        Y_mort=1

        COLLISIONS=0


    if A_hp>1721 and A_posy==700 and Y_posy==700:
        A_hp=1721
        A_mort=1
        Y_sortie=1
        COLLISIONS=0

    can.coords(A_vie,A_hp,57,1721,82)
    can.coords(A_degat,A_hpp,57,1721,82)
    can.coords(Y_vie,179,57,Y_hp,82)
    can.coords(Y_degat,179,57,Y_hpp,82)







    if agencement==1:


        if Y_posx<150  and A_posx<1750 and position_stage<=2750 or A_posx<150 and position_stage<=2750:


            if Y_subit==3 or Y_stance==54 or  A_stance==54 and A_posx<200:
                position_stage=position_stage+100
                A_posx=A_posx+100
                Y_posx=Y_posx+100

            elif Y_subit==1:
                position_stage=position_stage+4
                A_posx=A_posx+4
                Y_posx=Y_posx+4
            elif Y_subit==2:
                position_stage=position_stage+8
                A_posx=A_posx+8
                Y_posx=Y_posx+8
            elif Y_subit==4:
                position_stage=position_stage+8
                A_posx=A_posx+25
                Y_posx=Y_posx+25



            elif Y_stance==4 or Y_stance==8 and Y_dir_saut==4 or A_stance==8 and A_dir_saut==4 and A_posx<150 or A_stance==4 and A_posx<Y_posx+150 :
                position_stage=position_stage+35
                A_posx=A_posx+35
                Y_posx=Y_posx+35




            elif Y_stance==55 and Y_roulade==4 or A_stance==55 and A_posx<100 and A_roulade==4:
                position_stage=position_stage+45
                A_posx=A_posx+45
                Y_posx=Y_posx+45







            can.coords(Stage_app,position_stage,500)


        elif A_posx>1750 and Y_posx>150 and position_stage>=(-850) or A_posx>1750 and Y_posx>150 and position_stage>= (-850):
            if A_subit==3 or A_stance==56 or Y_stance==56 and Y_posx>1700:
                position_stage=position_stage-100
                Y_posx=Y_posx-100

            elif A_subit==1:
                position_stage=position_stage-4
                A_posx=A_posx-4
                Y_posx=Y_posx-4
            elif A_subit==2:
                position_stage=position_stage-8
                A_posx=A_posx-8
                Y_posx=Y_posx-8

            elif A_subit==4:
                position_stage=position_stage-8
                A_posx=A_posx-8
                Y_posx=Y_posx-8

            elif A_stance==6 or A_stance==8 and A_dir_saut==6 or Y_stance==8 and Y_dir_saut==6 and Y_posx>1750 or Y_stance==6 and Y_posx>A_posx-150:
                position_stage=position_stage-35
                Y_posx=Y_posx-35

            elif A_stance==55 and A_roulade==6 or Y_stance==55 and Y_roulade==6 and Y_posx>1750:
                position_stage=position_stage+45
                A_posx=A_posx+45
                Y_posx=Y_posx+45

            can.coords(Stage_app,position_stage,500)




        if position_stage>=2750 and Y_posx<=150 and A_posx<= (Y_posx+150) :
            A_posx=Y_posx+150
        elif position_stage<=(-850) and A_posx>=1750 and Y_posx>=(A_posx-150):
            Y_posx=A_posx-150
        if Y_posy==A_posy and Y_posx>A_posx-150 and A_stance==4 and Y_DPL_D==0 or Y_posy==A_posy and Y_posx>A_posx-150 and A_stance==54 and Y_DPL_D==0:
            Y_posx=A_posx-150

        elif Y_posy==A_posy and Y_posx>A_posx-150 and A_DPL_G==0 and Y_stance==6 or Y_posy==A_posy and Y_posx>A_posx-150 and A_DPL_G==0 and Y_stance==56 :
            A_posx=Y_posx+150


        elif Y_posy==A_posy and Y_posx>A_posx-150 and A_stance==4 and Y_stance==6 or Y_posy==A_posy and Y_posx>A_posx-150 and A_stance==54 and Y_stance==56 :
            A_posx=A_posx+75
            Y_posx=Y_posx-75

    elif agencement==2:


        if A_posx<150  and Y_posx<1750 and position_stage<=2750 or Y_posx<150 and position_stage<=2750:


            if A_subit==3 or A_stance==54 or  Y_stance==54 and Y_posx<200:
                position_stage=position_stage+100
                A_posx=A_posx+100
                Y_posx=Y_posx+100

            elif A_subit==1:
                position_stage=position_stage+4
                A_posx=A_posx+4
                Y_posx=Y_posx+4
            elif A_subit==2:
                position_stage=position_stage+8
                A_posx=A_posx+8
                Y_posx=Y_posx+8
            elif A_subit==4:
                position_stage=position_stage+8
                A_posx=A_posx+25
                Y_posx=Y_posx+25



            elif A_stance==4 or A_stance==8 and A_dir_saut==4 or Y_stance==8 and Y_dir_saut==4 and Y_posx<150 or Y_stance==4 and Y_posx<A_posx+150 :
                position_stage=position_stage+35
                A_posx=A_posx+35
                Y_posx=Y_posx+35




            elif A_stance==55 and A_roulade==4 or Y_stance==55 and Y_posx<100 and Y_roulade==4:
                position_stage=position_stage+45
                A_posx=A_posx+45
                Y_posx=Y_posx+45







            can.coords(Stage_app,position_stage,500)


        elif Y_posx>1750 and A_posx>150 and position_stage>=(-850) or Y_posx>1750 and A_posx>150 and position_stage>= (-850):
            if Y_subit==3 or Y_stance==56 or A_stance==56 and A_posx>1700:
                position_stage=position_stage-100
                A_posx=A_posx-100

            elif Y_subit==1:
                position_stage=position_stage-4
                A_posx=A_posx-4
                Y_posx=Y_posx-4
            elif Y_subit==2:
                position_stage=position_stage-8
                A_posx=A_posx-8
                Y_posx=Y_posx-8

            elif Y_subit==4:
                position_stage=position_stage-8
                A_posx=A_posx-8
                Y_posx=Y_posx-8

            elif Y_stance==6 or Y_stance==8 and Y_dir_saut==6 or A_stance==8 and A_dir_saut==6 and A_posx>1750 or A_stance==6 and A_posx>Y_posx-150:
                position_stage=position_stage-35
                A_posx=A_posx-35

            elif Y_stance==55 and Y_roulade==6 or A_stance==55 and A_roulade==6 and A_posx>1750:
                position_stage=position_stage+45
                A_posx=A_posx+45
                Y_posx=Y_posx+45

            can.coords(Stage_app,position_stage,500)




        if position_stage>=2750 and A_posx<=150 and Y_posx<= (A_posx+150) :
            Y_posx=A_posx+150
        elif position_stage<=(-850) and Y_posx>=1750 and A_posx>=(Y_posx-150):
            A_posx=Y_posx-150
        if A_posy==Y_posy and A_posx>Y_posx-150 and Y_stance==4 and A_DPL_D==0 or A_posy==Y_posy and A_posx>Y_posx-150 and Y_stance==54 and A_DPL_D==0:
            A_posx=Y_posx-150

        elif A_posy==Y_posy and A_posx>Y_posx-150 and Y_DPL_G==0 and A_stance==6 or A_posy==Y_posy and A_posx>Y_posx-150 and Y_DPL_G==0 and A_stance==56 :
            Y_posx=A_posx+150


        elif A_posy==Y_posy and A_posx>Y_posx-150 and Y_stance==4 and A_stance==6 or A_posy==Y_posy and A_posx>Y_posx-150 and Y_stance==54 and A_stance==56 :
            A_posx=A_posx-75
            Y_posx=Y_posx+75


    if Y_posx<100:
        Y_posx=100
    elif Y_posx>1800:
        Y_posx=1800
    if A_posx<100:
        A_posx=100
    elif A_posx>1800:
        A_posx=1800

    if AM_sprites>30:
        AM_sprites=31
    if YM_sprites>30:
        YM_sprites=31
    YM_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_special_meter[YM_sprites]}")
    can.itemconfigure(YM_app,image=YM_image)



    AM_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_special_meter[AM_sprites]}")
    can.itemconfigure(AM_app,image=AM_image)
     #######################################################################################     POSITIONNEMENT     #######################################################################################
    if A_posx>Y_posx :
        agencement=1
    elif A_posx<Y_posx:
        agencement=2

    if COLLISIONS==1:
        fen.after(60,Vie_et_placement)


def collisions_Yani():
    global A_subit_air,Y_subit_air,A_mort,Y_mort,COLLISIONS,A_sortie,Y_sortie,A_fort_air,A_roulade,Y_roulade,position_stage,Stage_image,Stage_app,le_stage,AM_image,YM_image,AM_app,YM_app,AM_sprites,YM_sprites,A_garde_air,Y_garde_air,A_garde,Y_garde,A_leger_air,A_fort_air,Y_coup_bas,deplacements,A_image_aux,S_sprites,A_app_aux,A_subit,Aaux_posx,Aaux_posy,A_dispo_garde,Y_subit,A_dispo_soulevement,Y_up,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air,Y_fort_air,Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut,Y_hurtbox,A_vie,A_degat,Y_vie,Y_degat,A_hpp,Y_hpp,A_hp,Y_hp,COMBAT,A_hp,Y_hp,A_stance,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHI2x2,AHI2y1,AHI2y2,AHI3x1,AHI3x2,AHI3y1,AHI3y2,AHISx1,AHISx2,AHISy1,AHISy2,AHUx1,AHUx2,AHUy1,AHUx2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHI2x1,YHI2x2,YHI2y1,YHI2y2,YHI3x1,YHI3x2,YHI3y1,YHI3y2,YHISx1,YHISx2,YHISy1,YHISy2,YHUx1,YHUx2,YHUy1,YHUx2,YHUy2,agencement,Y_posx,Y_posy,Y_sprites,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,Y_stance,Y_dir_saut,Y_image,Y_sprites,Y_app,A_fort_air,A_leger_air,A_up,A_compteur_fort,A_compteur_faible,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo,agencement,A_posx,A_posy,A_sprites,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,A_stance,A_dir_saut,A_sprites,A_image,A_posx,Y_posx,A_app,A_hurtbox,AHUx1,AHUx2,AHUy1,AHUy2,A_hitbox_1,AHI1x1,AHI1x2,AHI1y1,AHI1y2

    if agencement==1:
        if A_DPL_D==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_G==1:

            Y_garde=1

        else:
            Y_garde=0
    elif agencement==2:

        if A_DPL_G==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_D==1:

            Y_garde=1

        else:
            Y_garde=0
    #"""yani hitbox 1"""
    if YHI1x1>= AHUx1>=YHI1x2 and AHUy1<=YHI1y1<=AHUy2 or AHUx1<= YHI1x1<=AHUx2 and AHUy1<=YHI1y1<=AHUy2 or AHUx1<=YHI1x2<=AHUx2 and AHUy1 <= YHI1y1<= AHUy2   or AHUx1<=YHI1x1<=AHUx2  and  AHUy1<= YHI1y2<= AHUy2    or AHUx1<=YHI1x2 <= AHUx2  and  AHUy1<=YHI1y2<=AHUy2 or YHI1x1<=AHUx1<=YHI1x2 and YHI1y1<=AHUy1<=YHI1y2 or YHI1x1<=AHUx2<=YHI1x2 and YHI1y1<=AHUy2<=YHI1y2 or YHI1x1<=AHUx1<=YHI1x2 and AHUy1<=YHI1y1<=AHUy2 or AHUx1<=YHI1x1<=AHUx2 and YHI1y1<AHUy1<YHI1y2:
####################ULTIME#################################
        if Y_stance==99 and A_garde==0 and Y_sprites<10 or Y_stance==99 and A_subit==2 and Y_sprites<10 :
            A_sprites=1
            A_hp=A_hp+60
            A_subit=3


        elif Y_stance==99 and A_garde==0 and Y_sprites>10 or Y_stance==99 and A_subit==3 and Y_sprites>10:
            A_hp=A_hp+120
            A_sprites=1
            A_subit=2




####################degats faibles#################################


        elif Y_stance==11 and A_garde==0 or Y_stance==13 and A_garde==1 and A_DPL_B!=1 or Y_stance==12 and A_garde==0 or Y_stance==13 and A_garde==0 or Y_stance==112 and A_garde==0 or Y_stance==112 and A_garde==1 and A_DPL_B!=1 or Y_leger_air==1 and A_garde==0 or Y_leger_air==1 and A_garde==1 and A_stance==2:
            if A_posy!=700:
                A_subit_air=1
            else:

                A_subit=1
            A_sprites=1

            A_hp=A_hp+15
            if Y_stance!=99:
                AM_sprites=AM_sprites+1



####################degats moyen############################
        elif Y_stance==14 and A_garde==0 or Y_stance==15 and A_garde==0   or Y_fort_air==1 and A_garde==0 or Y_fort_air==1 and A_garde==1 and A_stance==2 :
            A_sprites=1
            if A_posy!=700:
                A_subit_air=1
            else:
                A_subit=2

            A_hp=A_hp+75
            YM_sprites=YM_sprites+3
            AM_sprites=AM_sprites+2



#################ejection#################


        elif  Y_stance==16 and A_garde==0 or Y_stance==16 and A_subit!=0:
            if A_posy!=700:
                A_subit_air=1
            else:
                A_subit=3
            A_hp=A_hp+60
            A_sprites=1
            YM_sprites=YM_sprites+3
            AM_sprites=AM_sprites+2
################soulevement###############
        elif Y_stance==142 and A_garde==0 or Y_stance==142 and A_garde==1 and A_DPL_B!=1 or Y_stance==142 and A_subit!=0:
            A_subit=4
            A_hp=A_hp+60
            A_sprites=1
            YM_sprites=YM_sprites+3
            AM_sprites=AM_sprites+2




####################garde accroupie#####################
        elif  Y_stance==99 and A_garde==1 and A_DPL_B==1 or Y_stance==142 and A_garde==1 and A_DPL_B==1 or Y_stance==16 and A_garde==1 and A_DPL_B==1 or Y_stance==14 and A_garde==1 and A_DPL_B==1 or Y_stance==15 and A_garde==1 and A_DPL_B==1  or Y_stance==11 and A_garde==1 and A_DPL_B==1 or Y_stance==12 and A_garde==1 and A_DPL_B==1 or Y_stance==13 and A_garde==1 and A_DPL_B==1 or Y_stance==112 and A_garde==1 and A_DPL_B==1 or Y_stance==112 and A_garde==1 and A_DPL_B :

            A_sprites=0
            A_stance=91
            A_dispo=0
            A_dispo_frappe=0
            A_dispo_saut=0
            AM_sprites=AM_sprites+1
            if Y_stance!=11 or Y_stance!=12 or Y_stance!=13 or Y_stance!=112 or Y_leger_air!=1:
                YM_sprites=YM_sprites+3

#################garde aerienne###################

        elif  Y_stance==99 and A_garde==1 and A_posy<700 or Y_stance==11 and A_posy<700 and A_garde==1 or Y_stance==12 and A_posy<700 and A_garde==1 or Y_stance== 13 and A_posy<700 and A_garde==1 or Y_stance==14 and A_posy<700 and A_garde==1 or Y_stance==15  and A_posy<700 and A_garde==1 or Y_stance==16 and A_posy<700 and A_garde==1 or Y_leger_air==1 and A_posy<700 and A_garde==1 or Y_fort_air==1 and A_posy<700 and A_garde==1:
            A_sprites=0
            A_garde_air=1
            A_dispo=0
            A_dispo_frappe=0
            A_dispo_saut=0
            AM_sprites=AM_sprites+1
            if Y_stance!=11 or Y_stance!=12 or Y_stance!=13 or Y_stance!=112 or Y_leger_air!=1:
                YM_sprites=YM_sprites+3


#########################garde debout##########################
        elif  Y_stance==99 and A_garde==1 or Y_stance==16 and A_garde==1 or Y_stance==14 and A_garde==1 or Y_stance==15 and A_garde==1 or Y_fort_air==1 and A_garde==1 and A_DPL_B!=1 or Y_stance==11 and A_garde==1 or Y_stance==12 and A_garde==1 or Y_stance==13 and A_garde==1 or Y_stance==112 and A_garde==1 and A_stance==2  or Y_leger_air==1 and A_garde==1 and A_stance!=2:

            A_sprites=0
            A_stance=90
            A_dispo=0
            A_dispo_frappe=0
            A_dispo_saut=0
            AM_sprites=AM_sprites+1
            if Y_stance!=11 or Y_stance!=12 or Y_stance!=13 or Y_stance!=112 or Y_leger_air!=1:
                YM_sprites=YM_sprites+3
#####################grab#######################
        elif A_subit!=4 and Y_stance==666 and A_subit!=6 and A_subit!=3 and A_stance!=8 and A_posy==700:

            YM_sprites=YM_sprites+3
            AM_sprites=AM_sprites+2
            A_subit=6
            Y_sprites=1
            YHI1x1=-100
            YHI1x2=-100
            YHI1y1=-100
            YHI1y2=-100
            can.coords(Y_hitbox_1,YHI1x1,YHI1y1,YHI1x2,YHI1y2)



        AHI1x1=-100
        AHI1x2=-100
        AHI1y1=-100
        AHI1y2=-100
    if COLLISIONS==1:
        fen.after(60,collisions_Yani)

def collisions_Alexandre():
    global A_subit_air,Y_subit_air,A_mort,Y_mort,COLLISIONS,A_sortie,Y_sortie,A_fort_air,A_roulade,Y_roulade,position_stage,Stage_image,Stage_app,le_stage,AM_image,YM_image,AM_app,YM_app,AM_sprites,YM_sprites,A_garde_air,Y_garde_air,A_garde,Y_garde,A_leger_air,A_fort_air,Y_coup_bas,deplacements,A_image_aux,S_sprites,A_app_aux,A_subit,Aaux_posx,Aaux_posy,A_dispo_garde,Y_subit,A_dispo_soulevement,Y_up,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air,Y_fort_air,Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut,Y_hurtbox,A_vie,A_degat,Y_vie,Y_degat,A_hpp,Y_hpp,A_hp,Y_hp,COMBAT,A_hp,Y_hp,A_stance,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHI2x2,AHI2y1,AHI2y2,AHI3x1,AHI3x2,AHI3y1,AHI3y2,AHISx1,AHISx2,AHISy1,AHISy2,AHUx1,AHUx2,AHUy1,AHUx2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHI2x1,YHI2x2,YHI2y1,YHI2y2,YHI3x1,YHI3x2,YHI3y1,YHI3y2,YHISx1,YHISx2,YHISy1,YHISy2,YHUx1,YHUx2,YHUy1,YHUx2,YHUy2,agencement,Y_posx,Y_posy,Y_sprites,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,Y_stance,Y_dir_saut,Y_image,Y_sprites,Y_app,A_fort_air,A_leger_air,A_up,A_compteur_fort,A_compteur_faible,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo,agencement,A_posx,A_posy,A_sprites,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,A_stance,A_dir_saut,A_sprites,A_image,A_posx,Y_posx,A_app,A_hurtbox,AHUx1,AHUx2,AHUy1,AHUy2,A_hitbox_1,AHI1x1,AHI1x2,AHI1y1,AHI1y2

    if agencement==1:
        if A_DPL_D==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_G==1:

            Y_garde=1

        else:
            Y_garde=0
    elif agencement==2:

        if A_DPL_G==1:

            A_garde=1

        else:
            A_garde=0

        if Y_DPL_D==1:

            Y_garde=1

        else:
            Y_garde=0
     #######################################################################################     GESTION DES COLLISIONS     #######################################################################################
    #alexandre hitbox 1
    if YHUx1<= AHI1x1<=YHUx2 and YHUy1<=AHI1y1<=YHUy2 or YHUx1<=AHI1x2<=YHUx2 and YHUy1 <= AHI1y1<= YHUy2   or YHUx1<=AHI1x1<=YHUx2  and  YHUy1<= AHI1y2<= YHUy2    or YHUx1<=AHI1x2 <= YHUx2  and  YHUy1<= AHI1y2<=YHUy2 or AHI1x1<=YHUx1<=AHI1x2 and AHI1y1<=YHUy1<=AHI1y2 or AHI1x1<=YHUx2<=AHI1x2 and AHI1y1<=YHUy2<=AHI1y2 or AHI1x1<=YHUx1<=AHI1x2 and YHUy1<=AHI1y1<=YHUy2 or YHUx1<=AHI1x1<=YHUx2 and AHI1y1<YHUy1<AHI1y2:

####################degats faibles#################################
        if A_stance==99 and Y_garde==0 or A_stance==99 and Y_subit==1 or A_stance==99 and Y_subit==2 or  A_stance==11 and Y_garde==0 or A_stance==12 and Y_garde==0 or A_stance==13 and Y_garde==0 or A_stance==112 and Y_garde==0 or A_stance==112 and Y_garde==1 and Y_DPL_B!=1 or A_leger_air==1 and Y_garde==0 or A_leger_air==1 and Y_garde==1 and Y_stance==2:

            if Y_posy!=700:
                Y_subit_air=1
            else:
                Y_subit=1
            if Y_subit!=4:
                Y_sprites=1

            Y_hp=Y_hp-5
            if A_stance!=99:
                YM_sprites=YM_sprites+1



####################degats moyen############################
        elif A_stance==14 and Y_garde==0 or A_stance==15 and Y_garde==0   or A_fort_air==1 and Y_garde==0 or A_fort_air==1 and Y_garde==1 and Y_stance==2 or A_stance==14 and Y_subit!=0 or  A_stance==15 and Y_subit!=0:
            if Y_posy!=700:
                Y_subit_air=1

            else:

                Y_subit=2
            if Y_subit!=4:
                Y_sprites=1

            Y_hp=Y_hp-45
            AM_sprites=AM_sprites+3
            YM_sprites=YM_sprites+2



#################ejection#################


        elif  A_stance==16 and Y_garde==0 or A_stance==16 and Y_subit!=0:
            if Y_posy!=700:
                Y_subit_air=1
            else:
                Y_subit=3
            Y_hp=Y_hp-60
            if Y_subit!=4:
                Y_sprites=1
            AM_sprites=AM_sprites+3
            YM_sprites=YM_sprites+2
################soulevement###############
        elif A_stance==142 and Y_garde==0 or A_stance==142 and Y_garde==1 and Y_DPL_B!=1 or A_stance==142 and Y_subit!=0:
            Y_subit=4
            Y_hp=Y_hp-60
            Y_sprites=1
            AM_sprites=AM_sprites+3
            YM_sprites=YM_sprites+2




####################garde accroupie#####################
        elif A_stance==99 and Y_garde==1 and Y_DPL_B==1 or A_stance==142 and Y_garde==1 and Y_DPL_B==1 or A_stance==16 and Y_garde==1 and Y_DPL_B==1 or A_stance==14 and Y_garde==1 and Y_DPL_B==1 or A_stance==15 and Y_garde==1 and Y_DPL_B==1  or A_stance==11 and Y_garde==1 and Y_DPL_B==1 or A_stance==12 and Y_garde==1 and Y_DPL_B==1 or A_stance==13 and Y_garde==1 and Y_DPL_B==1 or A_stance==112 and Y_garde==1 and Y_DPL_B==1 or A_stance==112 and Y_garde==1 and Y_DPL_B==1 :

            Y_sprites=0
            Y_stance=91
            Y_dispo=0
            Y_dispo_frappe=0
            Y_dispo_saut=0
            YM_sprites=YM_sprites+1
            if A_stance!=11 or A_stance!=12 or A_stance!=13 or A_stance!=112 or A_leger_air!=1:
                AM_sprites=AM_sprites+3

#################garde aerienne###################

        elif A_stance==11 and Y_posy<700 and Y_garde==1 or A_stance==12 and Y_posy<700 and Y_garde==1 or A_stance== 13 and Y_posy<700 and Y_garde==1 or A_stance==14 and Y_posy<700 and Y_garde==1 or A_stance==15  and Y_posy<700 and Y_garde==1 or A_stance==16 and Y_posy<700 and Y_garde==1 or A_leger_air==1 and Y_posy<700 and Y_garde==1 or A_fort_air==1 and Y_posy<700 and Y_garde==1:
            Y_sprites=0
            Y_garde_air=1
            Y_dispo=0
            Y_dispo_frappe=0
            Y_dispo_saut=0
            YM_sprites=YM_sprites+1
            if A_stance!=11 or A_stance!=12 or A_stance!=13 or A_stance!=112 or A_leger_air!=1:
                AM_sprites=AM_sprites+3

#########################garde debout##########################
        elif  A_stance==99 and Y_garde==1 and Y_DPL_B==0 or A_stance==16 and Y_garde==1 or A_stance==14 and Y_garde==1 or A_stance==15 and Y_garde==1 or A_fort_air==1 and Y_garde==1 and Y_DPL_B!=1 or A_stance==11 and Y_garde==1 or A_stance==12 and Y_garde==1 or A_stance==13 and Y_garde==1 or A_stance==112 and Y_garde==1 and Y_DPL_B==1  or A_leger_air==1 and Y_garde==1 and Y_DPL_B!=1:

            Y_sprites=0
            Y_stance=90
            Y_dispo=0
            Y_dispo_frappe=0
            Y_dispo_saut=0
            YM_sprites=YM_sprites+1
            if A_stance!=11 or A_stance!=12 or A_stance!=13 or A_stance!=112 or A_leger_air!=1:
                AM_sprites=AM_sprites+3

#####################grab#######################
        elif Y_subit!=4 and A_stance==666 and Y_subit!=6 and Y_subit!=3 and Y_stance!=8 and Y_posy==700:

            AM_sprites=AM_sprites+3
            YM_sprites=YM_sprites+2
            Y_subit=6
            A_sprites=1
            AHI1x1=-100
            AHI1x2=-100
            AHI1y1=-100
            AHI1y2=-100
            can.coords(A_hitbox_1,AHI1x1,AHI1y1,AHI1x2,AHI1y2)

###################ultime#########################
        if Y_subit!=4 and A_stance==99 and Y_subit!=6 and Y_subit!=3 and Y_posy==700 and A_sprites==24 and Y_garde==0 or Y_subit!=4 and A_stance==99 and Y_subit!=6 and Y_subit!=3 and Y_posy==700 and A_sprites==24 and Y_subit!=0:

            YM_sprites=YM_sprites+3
            Y_subit=99
            A_sprites=1
            S_sprites=1
            AHI1x1=-100
            AHI1x2=-100
            AHI1y1=-100
            AHI1y2=-100
            can.coords(A_hitbox_1,AHI1x1,AHI1y1,AHI1x2,AHI1y2)

        YHI1x1=-100
        YHI1x2=-100
        YHI1y1=-100
        YHI1y2=-100










    if COLLISIONS==1:
        fen.after(60,collisions_Alexandre)


def JEU(a):
    global Y_app_aux,Y_image_aux,Yaux_posx,Yaux_posy,Y_sortie,A_mort,Y_mort,A_subit_air,Y_subit_air,COLLISIONS,verif_select,A_sprites,Y_sprites,A_posx,A_posy,Y_posx,Y_posy,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHUx1,AHUx2,AHUy1,AHUy2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHUx1,YHUx2,YHUy1,YHUy2,agencement,A_up,A_leger_air,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort,A_fort_air,A_DPL_B,A_DPL_G,A_DPL_D,A_dispo,A_stance,A_dir_saut,A_garde,A_dispo_garde,AM_sprites,A_subit,A_hp,A_hpp,A_dispo_soulevement,Aaux_posx,Aaux_posy,A_dispo_dash,A_roulade,A_dispo_roulade,A_compteur_roulade,A_sortie,Y_up,Y_leger_air,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,deplacements,Y_fort_air,Y_DPL_B,Y_DPL_G,Y_DPL_D,Y_dispo,Y_stance,Y_dir_saut,Y_garde,Y_dispo_garde,YM_sprites,Y_subit,Y_hp,Y_hpp,Y_dispo_soulevement,Yaux_posx,Yaux_posy,Y_dispo_dash,Y_roulade,Y_dispo_roulade,Y_compteur_roulade,position_stage,COLLISIONS,depart,COMBAT,S_sprites,x_stage,le_stage,Stage_image,x_stage,le_stage,Stage_image,x_stage,le_stage,Stage_image,Stage_app,A_hurtbox,Y_hurtbox,A_hitbox_1,Y_hitbox_1,Y_outline,A_outline,Y_degat,A_degat,Y_vie,A_vie,YM_image,YM_app,AM_image,AM_app,Y_image,Y_app,A_image_aux,A_app_aux,A_image,A_app




    can.delete(image,imagemen,image_stage_selec,imagebg)


    """""""""""""""""""""""""""""""""""""""""""""""""""""""""DEFINITION DES VARIABLES"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    A_mort=0
    Y_mort=0
    verif_select=0
    COLLISIONS=1
    A_sprites=1
    Y_sprites=1
    A_subit_air=0
    Y_subit_air=0
    A_posx=1500
    A_posy=0

    Y_posx=300
    Y_posy=700
    Y_sortie=0




    """coordonnées des variables"""
    """x=coordx ; y=coordsy ; HI=Hitbox ; HU=Hurtbox ; A=Alexandre ; Y=Yani ; S=soulevement"""
    """ordre nomenclature == 1: prénom ; 2: hit/hurt 3:num de la box ; 4: coords"""

    AHI1x1=-100 ; AHI1x2=-100 ; AHI1y1=-100 ; AHI1y2=-100 ; AHUx1=0 ; AHUx2=0 ; AHUy1=0 ; AHUy2=0
    YHI1x1=-100 ; YHI1x2=-100 ; YHI1y1=-100 ; YHI1y2=-100 ; YHUx1=0 ; YHUx2=0 ; YHUy1=0 ; YHUy2=0



    """statuts"""
    """4=vers la gauche 5=rien 6=vers la droite 8=air 2=accroupi"""


    """agencement :  1 : Alexandre a gauche et Yani a droite ; 2 : Yani a gauche et Alexandre a droite"""
    agencement=1


    A_up=1
    A_leger_air=0
    A_dispo_frappe=1
    A_dispo_saut=1
    A_compteur_faible=1
    A_compteur_fort=1

    A_fort_air=0
    A_DPL_B=0
    A_DPL_G=0
    A_DPL_D=0
    A_dispo=1
    A_stance=5
    A_dir_saut=5

    A_garde=0
    A_dispo_garde=1

    """subit : 0:rien  1 : coup faible  2 : coup moyen  3 : coup fort  4 : soulevement"""

    AM_sprites=1
    A_subit=0

    A_hp=1008

    A_hpp=A_hp

    A_dispo_soulevement=1

    Yaux_posx=-100
    Yaux_posy=-100
    Aaux_posx=-100
    Aaux_posy=-100
    A_dispo_dash=1
    A_roulade=0
    A_dispo_roulade=1
    A_compteur_roulade=1
    A_sortie=0


    Y_up=1
    Y_leger_air=0
    Y_dispo_frappe=1
    Y_dispo_saut=1
    Y_compteur_faible=1
    Y_compteur_fort=1
    deplacements=0
    Y_fort_air=0
    Y_DPL_B=0
    Y_DPL_G=0
    Y_DPL_D=0
    Y_dispo=1
    Y_stance=5
    Y_dir_saut=5

    Y_garde=0
    Y_dispo_garde=1

    """subit : 0:rien  1 : coup faible  2 : coup moyen  3 : coup fort  4 : soulevement"""

    YM_sprites=1
    Y_subit=0

    Y_hp=892

    Y_hpp=Y_hp

    Y_dispo_soulevement=1


    Yaux_posx=-100
    Yaux_posy=-100
    Y_dispo_dash=1
    Y_roulade=0
    Y_dispo_roulade=1
    Y_compteur_roulade=1




    position_stage=950

    depart=1
    COMBAT=1

    S_sprites=0


    fen.unbind('<z>')
    fen.unbind('<q>')
    fen.unbind('<s>')
    fen.unbind('<d>')
    fen.unbind('<k>')



#####################attribution des touches##########################

    A_Deplacements()


    Y_Deplacements()



    """creation des sprites"""

    A_hurtbox=can.create_rectangle(-300,-300,-300,-300,fill="blue")


    Y_hurtbox=can.create_rectangle(500,500,600,1000,fill="blue")

    A_hitbox_1=can.create_rectangle(-100,-100,-100,-100,fill="green")
    Y_hitbox_1=can.create_rectangle(-200,-200,-200,-200,fill="red")



    if x_stage==335:
        le_stage=1

        Stage_image=PhotoImage(file="Stages/Backgrounds/cathedral.png")
        mixer.music.load("Stages/Musics/CATHEDRAL.ogg")


    elif x_stage==953:
        le_stage=2
        Stage_image=PhotoImage(file="Stages/Backgrounds/alucard_castle.png")
        mixer.music.load("Stages/Musics/CASTLE.ogg")

    elif x_stage==1571:
        le_stage=3
        Stage_image=PhotoImage(file="Stages/Backgrounds/temple.png")
        mixer.music.load("Stages/Musics/TEMPLE.ogg")
    Stage_app=can.create_image(position_stage,500, image = Stage_image)




    Y_outline=can.create_rectangle(167,45,904,92,fill='grey')
    A_outline=can.create_rectangle(996,45,1733,92,fill='grey')
    Y_degat=can.create_rectangle(179,57,Y_hpp,82,fill='red')
    A_degat=can.create_rectangle(A_hpp,57,1721,82,fill='red')
    Y_vie=can.create_rectangle(179,57,Y_hp,82,fill='blue')
    A_vie=can.create_rectangle(A_hp,57,1721,82,fill='blue')



    YM_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_special_meter[YM_sprites]}")
    YM_app=can.create_image(83,72,image=YM_image)

    AM_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_special_meter[AM_sprites]}")
    AM_app=can.create_image(1817,72,image=AM_image)

    Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_debout[Y_sprites]}")
    Y_app=can.create_image(Y_posx,Y_posy,image=Y_image)

    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand[A_sprites]}")
    A_app_aux=can.create_image(Aaux_posx,Aaux_posy,image=A_image_aux)

    A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_debout[A_sprites]}")
    A_app=can.create_image(A_posx,A_posy,image=A_image)

    Y_image_aux=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ultime_explosion[13]}")
    Y_app_aux=can.create_image(Yaux_posx,Yaux_posy,image=Y_image_aux)



    Vie_et_placement()
    Animation_Alexandre()
    collisions_Alexandre()
    Animation_Yani()

    collisions_Yani()
    mixer.music.play()

############################COMMANDES########################################

####################################ALEXANDRE####################################
def A_dash(a):
    global A_compteur_roulade,A_dispo_roulade,A_roulade,agencement,A_dispo_dash,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort,A_up,AHI1x1,AHI1x2,AHI1y1,AHI1y2,A_subit
    if A_DPL_D==0 and A_DPL_G==0 and A_stance!=8 and A_posy==700 and A_dispo_roulade==1 and A_subit==0 or A_DPL_D==1 and A_DPL_G==1 and A_stance!=8 and A_dispo_roulade==1 and A_posy==700 and A_subit==0:
        AHI1x1=-100
        AHI1x2=-100
        AHI1y1=-100
        AHI1y2=-100
        A_stance=55
        A_compteur_faible=1
        A_compteur_fort=1
        A_sprites=1
        A_dispo=0
        A_compteur_roulade=1
        A_dispo_roulade=0

        A_dispo_frappe=0
        A_dispo_saut=0
        if agencement==1:
            A_roulade=4
        elif agencement==2:
            A_roulade=6
    elif A_DPL_D==1 and A_dispo==1 and A_subit==0 or A_DPL_D and A_stance==8 and A_dispo_dash==1 and A_subit==0:
        A_stance=56
        A_sprites=1
        A_dispo_dash=0
        AHI1x1=-100
        AHI1x2=-100
        AHI1y1=-100
        AHI1y2=-100

        A_dispo=0
    elif A_DPL_G==1 and A_dispo==1 and A_subit==0 or A_DPL_G and A_stance==8 and A_dispo_dash==1 and A_subit==0:
        A_stance=54
        A_sprites=1
        A_dispo_dash=0
        AHI1x1=-100
        AHI1x2=-100
        AHI1y1=-100
        AHI1y2=-100

        A_dispo=0

def A_ulti(a):
    global A_stance,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort,A_dispo,AM_sprites
    if A_posy==700 and A_dispo_frappe==1:
        if AM_sprites==31:

            A_dispo=0
            A_stance=99
            A_sprites=1
            A_compteur_faible=1
            A_compteur_fort=1
            A_dispo_frappe=0
            A_dispo_saut=0


def A_grab(a):
    global A_stance,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort,A_dispo
    if A_posy==700 and A_dispo_frappe==1 and A_dispo==1 and A_subit==0 and Y_subit==0:

        A_dispo=0
        A_stance=666
        A_sprites=1
        A_compteur_faible=1
        A_compteur_fort=1
        A_dispo_frappe=0
        A_dispo_saut=0
def A_projectile(a):
    global A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort
    if A_DPL_B==0 and A_dispo_frappe==1 and A_dispo_saut==1 and A_subit==0:
        A_compteur_fort=1
        A_sprites=1
        A_dispo_frappe=0
        A_dispo=0
        A_stance=18
        A_dispo_saut=0
        A_compteur_faible=1



def A_frappe_faible(a):
    global A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_faible,A_compteur_fort,A_leger_air
    if A_DPL_B==1 and A_dispo_frappe==1 and A_posy==700 and A_compteur_faible!=3 and A_subit==0 and A_compteur_fort==1:
        A_compteur_fort=1
        A_sprites=1
        A_dispo_frappe=0
        A_dispo=0
        A_stance=112
        A_dispo_saut=0
        A_compteur_faible=A_compteur_faible+1
    elif A_DPL_B==0 and A_posy==700 and A_dispo_frappe==1 and A_subit==0:
        A_compteur_fort=1
        if A_compteur_faible==1:
            A_stance=11
            A_sprites=1
            A_compteur_faible=A_compteur_faible+1
        elif A_compteur_faible==2 and A_subit==0:
            A_stance=12
            A_sprites=1
            A_compteur_faible=A_compteur_faible+1
        elif A_compteur_faible==3 and A_subit==0:
            A_stance=13
            A_sprites=1
            A_compteur_faible=0


        A_dispo_frappe=0
        A_dispo=0

        A_dispo_saut=0
    elif A_stance==8 and A_dispo_frappe==1 or A_stance==54 and A_dispo_frappe==1 and A_posy<700 or A_stance==56 and A_dispo_frappe==1 and A_posy<700 :
        A_leger_air=1
        A_dispo_frappe=0
        A_sprites=1



def A_frappe_forte(a):
    global A_dispo_soulevement,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_sprites,A_dispo_frappe,A_dispo_saut,A_compteur_fort,A_compteur_faible,A_fort_air

    if A_DPL_B==1 and A_dispo_frappe==1 and A_posy==700 and A_dispo_soulevement==1:

        A_sprites=1
        A_dispo_frappe=0
        A_dispo=0
        A_stance=142
        A_dispo_saut=0
        A_compteur_faible=1
        A_dispo_soulevement=0
    elif A_DPL_B==0 and A_posy==700 and A_dispo_frappe==1:
        A_compteur_faible=0
        if A_compteur_fort==1:
            A_stance=14
            A_sprites=1
            A_compteur_fort=A_compteur_fort+1
        elif A_compteur_fort==2:
            A_stance=15
            A_sprites=1
            A_compteur_fort=A_compteur_fort+1
        elif A_compteur_fort==3:
            A_stance=16
            A_sprites=1
            A_compteur_fort=0


        A_dispo_frappe=0
        A_dispo=0

        A_dispo_saut=0
    elif A_stance==8 and A_dispo_frappe==1 or A_stance==54 and A_dispo_frappe==1 and A_posy<700 or A_stance==56 and A_dispo_frappe==1 and A_posy<700 :
        A_fort_air=1
        A_dispo_frappe=0
        A_sprites=1






def A_saut(a):
    global A_dispo,A_stance,A_sprites,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_dir_saut
    if A_dispo_saut==1:
        if A_DPL_D==1:
            A_dir_saut=6
        elif A_DPL_G==1:
            A_dir_saut=4
        A_stance=8
        A_dispo_saut=0
        A_dispo=0
        A_dispo_frappe=1

        A_sprites=1
def A_gauche_lance(a):
    global A_DPL_G
    A_DPL_G=1

def A_arret_gauche(a):
    global A_DPL_G
    A_DPL_G=0
def A_droite_lance(a):
    global A_DPL_D
    A_DPL_D=1
def A_arret_droite(a):
    global A_DPL_D
    A_DPL_D=0
def A_bas_lance(a):
    global A_DPL_B
    A_DPL_B=1
def A_arret_bas(a):
    global A_DPL_B,A_sprites,A_dispo
    A_DPL_B=0

def A_Deplacements():
    global A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo_saut,COMBAT
    if A_dispo==1:
        if A_DPL_B==1 and A_DPL_G==0 and A_DPL_D==0 :
            A_stance=2
            A_dir_saut=5
        elif A_DPL_B==1 and A_DPL_G==1 and A_DPL_D==0 :
            A_stance=2
            A_dir_saut=4
        elif A_DPL_B==1 and A_DPL_G==0 and A_DPL_D==1 :
            A_stance=2
            A_dir_saut=6
        elif A_DPL_B==0 and A_DPL_G==1 and A_DPL_D==0 :
            A_stance=4
            A_dir_saut=4
        elif A_DPL_B==0 and A_DPL_G==0 and A_DPL_D==1 :
            A_stance=6
            A_dir_saut=6
        elif A_DPL_B==0 and A_DPL_G==0 and A_DPL_D==0:
            A_stance=5
            A_dir_saut=5





    if COMBAT==1:
        fen.after(60,A_Deplacements)
####################################YANI####################################


def Y_dash(y):
    global Y_compteur_roulade,Y_dispo_roulade,Y_roulade,agencement,Y_dispo_dash,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_up,Y_subit
    if Y_DPL_D==0 and Y_DPL_G==0 and Y_stance!=8 and Y_posy==700 and Y_dispo_roulade==1 and Y_subit==0 or Y_DPL_D==1 and Y_DPL_G==1 and Y_stance!=8 and Y_dispo_roulade==1 and Y_posy==700 and Y_subit==0:
        Y_stance=55
        Y_sprites=1
        Y_dispo=0
        Y_compteur_roulade=1
        Y_dispo_roulade=0

        Y_dispo_frappe=0
        Y_dispo_saut=0
        if agencement==1:
            Y_roulade=6
        elif agencement==2:
            Y_roulade=4
    elif Y_DPL_D==1 and Y_dispo==1 and Y_subit==0 or Y_DPL_D and Y_stance==8 and Y_dispo_dash==1 and Y_subit==0:
        Y_stance=56
        Y_sprites=1
        Y_dispo_dash=0

        Y_dispo=0
    elif Y_DPL_G==1 and Y_dispo==1 and Y_subit==0 or Y_DPL_G and Y_stance==8 and Y_dispo_dash==1 and Y_subit==0:
        Y_stance=54
        Y_sprites=1
        Y_dispo_dash=0

        Y_dispo=0

def Y_ulti(y):
    global Y_stance,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_dispo,YM_sprites
    if Y_posy==700 and Y_dispo_frappe==1:
        if YM_sprites==31:

            Y_dispo=0
            Y_stance=99
            Y_sprites=1
            Y_compteur_faible=1
            Y_compteur_fort=1
            Y_dispo_frappe=0
            Y_dispo_saut=0


def Y_grab(y):
    global Y_stance,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_dispo
    print("hoho")
    if Y_posy==700 and Y_dispo_frappe==1 and Y_dispo==1 and A_subit==0:
        print("fdp")
        Y_sprites=1
        Y_dispo=0
        Y_stance=666

        Y_compteur_faible=1
        Y_compteur_fort=1
        Y_dispo_frappe=0
        Y_dispo_saut=0
def Y_projectile(y):
    global Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort
    if Y_DPL_B==0 and Y_dispo_frappe==1 and Y_posy==700:
        Y_compteur_fort=1
        Y_sprites=1
        Y_dispo_frappe=0
        Y_dispo=0
        Y_stance=18
        Y_dispo_saut=0
        Y_compteur_faible=1



def Y_frappe_faible(y):
    global Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air
    if Y_DPL_B==1 and Y_dispo_frappe==1 and Y_posy==700 and Y_compteur_faible!=3 and Y_compteur_fort==1 :
        Y_compteur_fort=1
        Y_sprites=1
        Y_dispo_frappe=0
        Y_dispo=0
        Y_stance=112
        Y_dispo_saut=0
        Y_compteur_faible=Y_compteur_faible+1
    elif Y_DPL_B==0 and Y_posy==700 and Y_dispo_frappe==1:
        Y_compteur_fort=1
        if Y_compteur_faible==1:
            Y_stance=11
            Y_sprites=1
            Y_compteur_faible=Y_compteur_faible+1
        elif Y_compteur_faible==2:
            Y_stance=12
            Y_sprites=1
            Y_compteur_faible=Y_compteur_faible+1
        elif Y_compteur_faible==3:
            Y_stance=13
            Y_sprites=1
            Y_compteur_faible=0


        Y_dispo_frappe=0
        Y_dispo=0

        Y_dispo_saut=0
    elif Y_stance==8 and Y_dispo_frappe==1 or Y_stance==54 and Y_dispo_frappe==1 and Y_posy<700 or Y_stance==56 and Y_dispo_frappe==1 and Y_posy<700 :
        Y_leger_air=1
        Y_dispo_frappe=0
        Y_sprites=1



def Y_frappe_forte(y):
    global Y_dispo_soulevement,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_fort,Y_compteur_faible,Y_fort_air

    if Y_DPL_B==1 and Y_dispo_frappe==1 and Y_posy==700 and Y_dispo_soulevement==1:

        Y_sprites=1
        Y_dispo_frappe=0
        Y_dispo=0
        Y_stance=142
        Y_dispo_saut=0
        Y_compteur_faible=1
        Y_dispo_soulevement=0
    elif Y_DPL_B==0 and Y_posy==700 and Y_dispo_frappe==1:
        Y_compteur_faible=0
        if Y_compteur_fort==1:
            Y_stance=14
            Y_sprites=1
            Y_compteur_fort=Y_compteur_fort+1
        elif Y_compteur_fort==2:
            Y_stance=15
            Y_sprites=1

            Y_compteur_fort=0



        Y_dispo_frappe=0
        Y_dispo=0

        Y_dispo_saut=0
    elif Y_stance==8 and Y_dispo_frappe==1 or Y_stance==54 and Y_dispo_frappe==1 and Y_posy<700 or Y_stance==56 and Y_dispo_frappe==1 and Y_posy<700 :
        Y_fort_air=1
        Y_dispo_frappe=0
        Y_sprites=1






def Y_saut(y):
    global Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut
    if Y_dispo_saut==1:
        if Y_DPL_D==1:
            A_dir_saut=6
        elif Y_DPL_G==1:
            Y_dir_saut=4
        Y_stance=8
        Y_dispo_saut=0
        Y_dispo=0
        Y_dispo_frappe=1

        Y_sprites=1
def Y_gauche_lance(y):
    global Y_DPL_G
    Y_DPL_G=1

def Y_arret_gauche(y):
    global Y_DPL_G
    Y_DPL_G=0
def Y_droite_lance(y):
    global Y_DPL_D
    Y_DPL_D=1
def Y_arret_droite(y):
    global Y_DPL_D
    Y_DPL_D=0
def Y_bas_lance(y):
    global Y_DPL_B
    Y_DPL_B=1
def Y_arret_bas(y):
    global Y_DPL_B,Y_sprites,Y_dispo
    Y_DPL_B=0

def Y_Deplacements():
    global Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_dispo_saut,COMBAT
    if Y_dispo==1:
        if Y_DPL_B==1 and Y_DPL_G==0 and Y_DPL_D==0 :
            Y_stance=2
            Y_dir_saut=5
        elif Y_DPL_B==1 and Y_DPL_G==1 and Y_DPL_D==0 :
            Y_stance=2
            Y_dir_saut=4
        elif Y_DPL_B==1 and Y_DPL_G==0 and Y_DPL_D==1 :
            Y_stance=2
            Y_dir_saut=6
        elif Y_DPL_B==0 and Y_DPL_G==1 and Y_DPL_D==0 :
            Y_stance=4
            Y_dir_saut=4
        elif Y_DPL_B==0 and Y_DPL_G==0 and Y_DPL_D==1 :
            Y_stance=6
            Y_dir_saut=6
        elif Y_DPL_B==0 and Y_DPL_G==0 and Y_DPL_D==0:
            Y_stance=5
            Y_dir_saut=5





    if COMBAT==1:
        fen.after(60,Y_Deplacements)


##############################################################################ANIMATION COMBAT##########################################
def Animation_Alexandre():
    global  AM_sprites,YM_sprites,A_bruitages,Y_mort,A_mort,A_subit_air,COMBAT,A_sortie,AHUy2,depart,COMBAT,A_compteur_roulade,A_dispo_roulade,A_roulade,A_dispo_dash,A_garde_air,deplacements,A_image_aux,S_sprites,A_app_aux,A_subit,Aaux_posx,Aaux_posy,A_dispo_garde,Y_subit,A_dispo_soulevement,Y_up,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air,Y_fort_air,Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut,Y_hurtbox,A_vie,A_degat,Y_vie,Y_degat,A_hpp,Y_hpp,A_hp,Y_hp,COMBAT,A_hp,Y_hp,A_stance,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHI2x2,AHI2y1,AHI2y2,AHI3x1,AHI3x2,AHI3y1,AHI3y2,AHISx1,AHISx2,AHISy1,AHISy2,AHUx1,AHUx2,AHUy1,AHUx2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHI2x1,YHI2x2,YHI2y1,YHI2y2,YHI3x1,YHI3x2,YHI3y1,YHI3y2,YHISx1,YHISx2,YHISy1,YHISy2,YHUx1,YHUx2,YHUy1,YHUx2,YHUy2,agencement,Y_posx,Y_posy,Y_sprites,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,Y_stance,Y_dir_saut,Y_image,Y_sprites,Y_app,A_fort_air,A_leger_air,A_up,A_compteur_fort,A_compteur_faible,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo,agencement,A_posx,A_posy,A_sprites,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,A_stance,A_dir_saut,A_sprites,A_image,A_posx,Y_posx,A_app,A_hurtbox,AHUx1,AHUx2,AHUy1,AHUy2,A_hitbox_1,AHI1x1,AHI1x2,AHI1y1,AHI1y2





     #######################################################################################     ALEXANDRE     #######################################################################################

    if A_posx>2300:
        COMBAT=0
     #######################################################################################     POSITION 1     #######################################################################################
    if agencement==1:
        if A_mort==1:

            if A_sprites>3:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_mort[4]}")
            else:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_mort[A_sprites]}")








     #######################################################################################     DEGATS SUBIS     #######################################################################################
        elif depart==1:

            if A_sprites<11:
                A_posy=A_posy+70
            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_entrée[A_sprites]}")

            if A_sprites==29:
                fen.bind('<KeyPress-q>',A_gauche_lance)
                fen.bind('<KeyRelease-q>',A_arret_gauche)
                fen.bind('<KeyPress-d>',A_droite_lance)
                fen.bind('<KeyRelease-d>',A_arret_droite)
                fen.bind('<KeyPress-s>',A_bas_lance)
                fen.bind('<KeyRelease-s>',A_arret_bas)
                fen.bind('u',A_dash)
                fen.bind('z',A_saut)
                fen.bind('<g>',A_frappe_faible)
                fen.bind('<y>',A_frappe_forte)
                fen.bind('<j>',A_projectile)
                fen.bind('<k>',A_grab)
                fen.bind('<space>',A_ulti)


        elif A_sortie==1 and A_dispo==1:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Avictoire.ogg")
                A_bruitages.play()

            if A_sprites>11:
                A_sprites=0



            fen.unbind('<KeyPress-q>')
            fen.unbind('<KeyRelease-q>')
            fen.unbind('<KeyPress-d>')
            fen.unbind('<KeyRelease-d>')
            fen.unbind('<KeyPress-s>')
            fen.unbind('<KeyRelease-s>')
            fen.unbind('i')
            fen.unbind('z')
            fen.unbind('<g>')
            fen.unbind('<y>')
            fen.unbind('<u>')
            fen.unbind('<h>')
            fen.unbind('<b>')



            A_posx=A_posx+50
            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_sortie[A_sprites]}")







        elif A_subit==1:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit1.ogg")
                    A_bruitages.play()
            A_posx=A_posx+4


            if A_sprites<5:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_faible[0]}")
                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250



            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1

        elif A_subit==2:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()
            A_posx=A_posx+8


            if A_sprites<10:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant[0]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0

                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1
        elif A_subit==3:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()


            if A_sprites<10:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale[0]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250

                A_posx=A_posx+100

            elif Y_stance==666:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale[0]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250


                A_sprites=1


            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1


        elif A_subit==4:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()


            if A_sprites<8:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant[0]}")
                A_posy=A_posy-70


                A_posx=A_posx+25
            elif A_posy<700:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale[0]}")
                A_posy=A_posy+70
                A_posx=A_posx+25





            else:
                A_posy=700
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1




            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250



        elif A_subit==6:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit1.ogg")
                    A_bruitages.play()





            if Y_sprites<11:

                A_posx=Y_posx+250
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_faible[0]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            else:

                A_subit=3



     #######################################################################################     DEBOUT     #######################################################################################
        elif A_stance==5:
            if A_sprites>7:
                A_sprites=1

            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_debout[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250



     #######################################################################################     DASH     #######################################################################################
        elif A_stance==55:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adash.ogg")
                A_bruitages.play()

            if A_roulade==4:
                A_posx=A_posx-45
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_roulade[0]}")
            elif A_roulade==6:
                A_posx=A_posx+45
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_roulade_R[0]}")

            if A_sprites==6:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250

            AHUx1=0
            AHUx2=0
            AHUy1=0
            AHUy2=0




        elif A_stance==54 or A_stance==56:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adash.ogg")
                A_bruitages.play()

            if A_sprites==4:
                if A_posy<700:
                    A_stance=8
                    A_up=0

                else:

                    A_leger_air=0
                    A_dispo_dash=1
                    A_sprites=1
                    A_up=1
                    A_leger_air=0
                    A_fort_air=0
                    A_compteur_faible=1
                    A_compteur_fort=1




                    if A_DPL_D==1:
                        A_dir_saut=6
                    elif A_DPL_G==1:
                        A_dir_saut=4
                    else:
                        A_dir_saut=5


                    AHUx1=A_posx-70
                    AHUx2=A_posx+60
                    AHUy1=A_posy-150
                    AHUy2=A_posy+250


                    A_stance=5
                    A_dispo=1
                    A_dispo_saut=1
                    A_dispo_frappe=1


            if A_stance==54:
                A_posx=A_posx-100

                A_dir_saut=4


            elif A_stance==56:
                A_posx=A_posx+100
                A_dir_saut=6




            if A_fort_air==0 and A_leger_air==0 and A_stance==54:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_dash_avant[0]}")
            elif A_fort_air==0 and A_leger_air==0 and A_stance==56:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_dash_arriere[0]}")
            elif A_leger_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_air[A_sprites]}")
                if A_sprites==2:
                    AHI1x1=A_posx-225
                    AHI1x2=A_posx-70
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+50

                elif A_sprites==3:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_leger_air=0
                    A_stance=8
                    A_up=0
            elif A_fort_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_air[A_sprites]}")
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adunk.ogg")
                    A_bruitages.play()
                if A_sprites==3:
                    AHI1x1=A_posx-425
                    AHI1x2=A_posx-170
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+300

                elif A_sprites==4:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_fort_air=0
                    A_stance=8
                    A_up=0






            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250









     #######################################################################################     MARCHE AVANT     #######################################################################################
        elif A_stance==4:
            if A_sprites>6:
                A_sprites=1


            A_posx=A_posx-35


            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_marche_avant[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250





     #######################################################################################     MARCHE ARRIERE     #######################################################################################
        elif A_stance==6:
            if A_sprites>8:
                A_sprites=1


            A_posx=A_posx+35


            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_marche_arriere[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




     #######################################################################################     ACCROUPI     #######################################################################################
        elif A_stance==2:
            if A_sprites>11:
                A_sprites=1



            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_accroupi[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-10
            AHUy2=A_posy+250



     #######################################################################################     SAUT ET COUPS AERIENS     #######################################################################################

        elif A_stance==8:




            if A_dir_saut==4:
                A_posx=A_posx-35
            elif A_dir_saut==6:
                A_posx=A_posx+35


            if A_posy>400 and A_up==1:



                A_posy=A_posy-100

            elif A_posy==400 and A_up==1:




                A_posy=A_posy-50

            elif A_posy==350 and A_up==1:


                A_posy=A_posy-25
                A_up=0

            elif A_posy==325 and A_up==0:



                A_posy=A_posy+25

            elif A_posy==350 and A_up==0:


                A_posy=A_posy+50

            elif A_posy<600 and A_up==0:

               A_posy=A_posy+100

            elif A_posy>=600 and A_up==0:


                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100






                A_posy=A_posy+100
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_saut[A_sprites]}")

                if A_DPL_D==1:
                    A_dir_saut=6
                elif A_DPL_G==1:
                    A_dir_saut=4
                else:
                    A_dir_saut=5


                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250
                A_subit_air=0

                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1

                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1
            if A_subit_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant[0]}")


                if A_sprites==3:


                    A_subit_air=0

            elif A_leger_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_air[A_sprites]}")
                if A_sprites==2:
                    AHI1x1=A_posx-225
                    AHI1x2=A_posx-70
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+50

                elif A_sprites==3:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_leger_air=0
            elif A_fort_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_air[A_sprites]}")
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adunk.ogg")
                    A_bruitages.play()
                if A_sprites==3:
                    AHI1x1=A_posx-425
                    AHI1x2=A_posx-170
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+300

                elif A_sprites==4:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_fort_air=0
            elif A_leger_air==0 and A_fort_air==0:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_saut[A_sprites]}")


            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250

     #######################################################################################     COUPS FAIBLES DEBOUT     #######################################################################################
        elif A_stance==11:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afaible1.ogg")
                A_bruitages.play()
            if A_sprites==2:
                AHI1x1=A_posx-125
                AHI1x2=A_posx-30
                AHI1y1=A_posy-60
                AHI1y2=A_posy+10

            elif A_sprites==3:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==6:
                if Y_subit!=4:
                    Y_subit=0
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_1[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==12:
            if A_sprites==1:
                AHI1x1=A_posx-200
                AHI1x2=A_posx-30
                AHI1y1=A_posy-120
                AHI1y2=A_posy+105

            elif A_sprites==2:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==5:
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_2[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==13:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afaible2.ogg")
                A_bruitages.play()
                AHI1x1=A_posx-250
                AHI1x2=A_posx-30
                AHI1y1=A_posy-75
                AHI1y2=A_posy+100

            elif A_sprites==2:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==5:
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1
                A_dispo_frappe=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_3[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250



     #######################################################################################     COUPS PUISSANTS DEBOUT     #######################################################################################
        elif A_stance==14:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort1.ogg")
                A_bruitages.play()
            if A_sprites==3:
                AHI1x1=A_posx-275
                AHI1x2=A_posx-30
                AHI1y1=A_posy-150
                AHI1y2=A_posy+30

            elif A_sprites==4:


                A_dispo_frappe=1

                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_compteur_faible=1
                A_dispo_saut=1
                A_dispo_frappe=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_1[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==15:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort2.ogg")
                A_bruitages.play()
            if A_sprites==3:
                AHI1x1=A_posx-300
                AHI1x2=A_posx-30
                AHI1y1=A_posy-150
                AHI1y2=A_posy+50

            elif A_sprites==4:


                A_dispo_frappe=1

                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_dispo_saut=1
                A_dispo_frappe=1
                A_compteur_faible=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_2[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==16:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort3.ogg")
                A_bruitages.play()


            if A_sprites==3:
                AHI1x1=A_posx-360
                AHI1x2=A_posx-30
                AHI1y1=A_posy-150
                AHI1y2=A_posy+70

            elif A_sprites==4:


                A_dispo_frappe=1

                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_dispo_saut=1
                A_dispo_frappe=1
                A_compteur_faible=1
                if Y_subit!=4:
                    Y_subit=0







            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_3[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250





     #######################################################################################     PROJECTILE DEBOUT     #######################################################################################

        elif A_stance==18:
            if A_sprites==6:
                AHI1x1=A_posx-1250
                AHI1x2=A_posx-70
                AHI1y1=A_posy-20
                AHI1y2=A_posy+250

            elif A_sprites==7:

                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==11:
                A_dispo=1






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_projectile[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+100
            AHUy1=A_posy-100
            AHUy2=A_posy+250





     #######################################################################################     COUP FAIBLE ACCROUPI     #######################################################################################
        elif A_stance==112:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Atir.ogg")
                A_bruitages.play()
            if A_sprites==2:
                AHI1x1=A_posx-200
                AHI1x2=A_posx-70
                AHI1y1=A_posy+100
                AHI1y2=A_posy+250

            elif A_sprites==3:

                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==7:
                if Y_subit!=4:
                    Y_subit=0
                A_dispo=1
                A_compteur_faible=1






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_accroupi[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+80
            AHUy1=A_posy-10
            AHUy2=A_posy+250




     #######################################################################################     COUP PUISSANT ACCROUPI     #######################################################################################
        elif A_stance==142:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asouleve.ogg")
                A_bruitages.play()
            A_compteur_faible=1
            A_compteur_fort=1
            if Y_subit!=4 and A_sprites==4:
                A_dispo_soulevement=1
            if A_sprites==4:
                AHI1x1=A_posx-350
                AHI1x2=A_posx-150
                AHI1y1=A_posy+-200
                AHI1y2=A_posy+250

            elif A_sprites==5:



                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==7:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1







            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_accroupi[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-10
            AHUy2=A_posy+250




     #######################################################################################     PROJECTILE ACCROUPI     #######################################################################################

     #######################################################################################     LE GRAB     #######################################################################################

        elif A_stance==666:

            if Y_subit!=6 and A_sprites<11:
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Agrab.ogg")
                    A_bruitages.play()



                if A_sprites==2:
                    AHI1x1=A_posx-200
                    AHI1x2=A_posx-30
                    AHI1y1=A_posy-100
                    AHI1y2=A_posy-60

                elif A_sprites==4:


                    A_dispo_frappe=1
                    A_dispo_saut=1
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100


                elif A_sprites==6:

                    A_dispo=1



                    A_dispo_frappe=1
                    A_dispo_saut=1









                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_grab[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            elif Y_subit==6 or Y_subit==3 and A_stance==666:
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/AgrabR.ogg")
                    A_bruitages.play()








                if A_sprites==11:
                    Y_subit=3
                    Y_hp=Y_hp-45
                elif A_sprites==13:
                    A_dispo=1

                    A_sprites=1


                    A_dispo_frappe=1
                    A_dispo_saut=1
                    A_stance=5

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_grab_reussi[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250






     #######################################################################################     L'ULTIME     #######################################################################################

        elif A_stance==99:




            if Y_subit!=99 :
                if A_sprites==1:

                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Astandrush.ogg")
                    A_bruitages.play()




                if 26>A_sprites>5:
                    AHI1x1=Aaux_posx-150
                    AHI1x2=Aaux_posx+150
                    AHI1y1=Aaux_posy-150
                    AHI1y2=Aaux_posy+100

                if A_sprites>5:

                    if Aaux_posx>(Y_posx+50):
                        Aaux_posx=Aaux_posx-26
                    else:
                        Aaux_posx=(Y_posx+50)

                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand[S_sprites]}")



                if A_sprites==5:


                    AHI1x1=Aaux_posx-200
                    AHI1x2=Aaux_posx-30
                    AHI1y1=Aaux_posy-100
                    AHI1y2=Aaux_posy-60

                    S_sprites=1
                    Aaux_posx=A_posx-250
                    Aaux_posy=A_posy
                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand[S_sprites]}")





                elif A_sprites==26:



                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100


                elif A_sprites==28:

                    A_dispo=1
                    AM_sprites=1
                    YM_sprites=15



                    A_dispo_frappe=1
                    A_dispo_saut=1
                    Aaux_posy=-200










                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250



                S_sprites=(S_sprites+1)


            elif Y_subit==99 :
                if A_sprites==6:
                    A_bruitages= mixer.Sound("AultimeR.ogg")
                    A_bruitages.play()







                if A_sprites<10:

                    Deplacements=(A_posx-(Aaux_posx))/10

                    A_posx=A_posx-Deplacements




                if A_sprites<21:
                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand_reussi[S_sprites]}")




                if A_sprites==17:
                    Y_hp=Y_hp-150


                elif A_sprites==22:
                    Aaux_posy=-200






                elif A_sprites==29:
                    A_dispo=1
                    AM_sprites=1
                    YM_sprites=15





                    A_dispo_frappe=1
                    A_dispo_saut=1
                    A_stance=5
                    Y_subit=0

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_reussi[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250



                S_sprites=(S_sprites+1)


     #######################################################################################     DEFENSE     #######################################################################################
        elif A_stance==90:
            if A_sprites!=5:
                A_posx=A_posx+5


                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_garde_debout[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250





            else:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1

        elif A_stance==91:
            if A_sprites!=5:
                A_posx=A_posx+5


                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_garde_accroupi[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250





            else:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1











     #######################################################################################     POSITION 2     #######################################################################################









    elif agencement==2:
        if A_mort==1:

            if A_sprites>3:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_mort_R[4]}")
            else:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_mort_R[A_sprites]}")


        elif A_sortie==1 and A_dispo==1:

            if A_sprites>11:
                A_sprites=0


            fen.unbind('<KeyPress-q>')
            fen.unbind('<KeyRelease-q>')
            fen.unbind('<KeyPress-d>')
            fen.unbind('<KeyRelease-d>')
            fen.unbind('<KeyPress-s>')
            fen.unbind('<KeyRelease-s>')
            fen.unbind('i')
            fen.unbind('z')
            fen.unbind('<g>')
            fen.unbind('<y>')
            fen.unbind('<u>')
            fen.unbind('<h>')
            fen.unbind('<b>')



            A_posx=A_posx+50
            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_sortie[A_sprites]}")
     #######################################################################################     DEGATS SUBIS     #######################################################################################
        elif A_subit==1:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit1.ogg")
                    A_bruitages.play()
            A_posx=A_posx-4


            if A_sprites<5:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_faible_R[0]}")

                AHUx1=A_posx-60
                AHUx2=A_posx+70
                AHUy1=A_posy-150
                AHUy2=A_posy+250



            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1
        elif A_subit==2:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()
            A_posx=A_posx-8


            if A_sprites<10:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant_R[0]}")

                AHUx1=A_posx-60
                AHUx2=A_posx+70
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1
        elif A_subit==3:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()


            if A_sprites<10:
                print(A_sprites)

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale_R[0]}")

                AHUx1=A_posx-60
                AHUx2=A_posx+70
                AHUy1=A_posy-150
                AHUy2=A_posy+250

                A_posx=A_posx-100


            elif Y_stance==666:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale_R[0]}")

                AHUx1=A_posx-60
                AHUx2=A_posx+70
                AHUy1=A_posy-150
                AHUy2=A_posy+250


                A_sprites=1


            else:
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1


        elif A_subit==4:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit2.ogg")
                    A_bruitages.play()


            if A_sprites<8:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant_R[0]}")


                A_posy=A_posy-70


                A_posx=A_posx-25
            elif A_posy<700:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ejection_horizontale_R[0]}")
                A_posy=A_posy+70
                A_posx=A_posx-25





            else:
                A_posy=700
                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1
                A_subit=0
                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1



            AHUx1=A_posx-60
            AHUx2=A_posx+70
            AHUy1=A_posy-150
            AHUy2=A_posy+250



        elif A_subit==6:
            if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asubit1.ogg")
                    A_bruitages.play()





            if Y_sprites<11:

                A_posx=Y_posx-250
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_faible_R[0]}")

                AHUx1=A_posx-60
                AHUx2=A_posx+70
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            else:

                A_subit=3

     #######################################################################################     DEBOUT     #######################################################################################
        elif A_stance==5:
            if A_sprites>7:
                A_sprites=1

            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_debout_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250


     #######################################################################################     DASH     #######################################################################################
        elif A_stance==55:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adash.ogg")
                A_bruitages.play()

            if A_roulade==4:
                A_posx=A_posx-45
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_roulade[0]}")
            elif A_roulade==6:
                A_posx=A_posx+45
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_roulade_R[0]}")

            if A_sprites==6:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250

            AHUx1=0
            AHUx2=0
            AHUy1=0
            AHUy2=0




        elif A_stance==54 or A_stance==56:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adash.ogg")
                A_bruitages.play()

            if A_sprites==4:
                if A_posy<700:
                    A_stance=8
                    A_up=0

                else:

                    A_leger_air=0
                    A_dispo_dash=1
                    A_sprites=1
                    A_up=1
                    A_leger_air=0
                    A_fort_air=0
                    A_compteur_faible=1
                    A_compteur_fort=1




                    if A_DPL_D==1:
                        A_dir_saut=6
                    elif A_DPL_G==1:
                        A_dir_saut=4
                    else:
                        A_dir_saut=5


                    AHUx1=A_posx-70
                    AHUx2=A_posx+60
                    AHUy1=A_posy-150
                    AHUy2=A_posy+250


                    A_stance=5
                    A_dispo=1
                    A_dispo_saut=1
                    A_dispo_frappe=1


            if A_stance==54:
                A_posx=A_posx-100

                A_dir_saut=4


            elif A_stance==56:
                A_posx=A_posx+100
                A_dir_saut=6




            if A_fort_air==0 and A_leger_air==0 and A_stance==54:

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_dash_arriere_R[0]}")
            elif A_fort_air==0 and A_leger_air==0 and A_stance==56:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_dash_avant_R[0]}")
            elif A_leger_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_air_R[A_sprites]}")
                if A_sprites==2:
                    AHI1x1=A_posx+70
                    AHI1x2=A_posx+225
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+50

                elif A_sprites==3:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_leger_air=0
                    A_stance=8
                    A_up=0
            elif A_fort_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_air_R[A_sprites]}")
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adunk.ogg")
                    A_bruitages.play()
                if A_sprites==3:
                    AHI1x1=A_posx+170
                    AHI1x2=A_posx+425
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+300

                elif A_sprites==4:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_fort_air=0
                    A_stance=8
                    A_up=0






            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250





     #######################################################################################     MARCHE AVANT     #######################################################################################
        elif A_stance==4:
            if A_sprites>8:
                A_sprites=1


            A_posx=A_posx-35


            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_marche_avant_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250





     #######################################################################################     MARCHE ARRIERE     #######################################################################################
        elif A_stance==6:
            if A_sprites>6:
                A_sprites=1


            A_posx=A_posx+35


            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_marche_arriere_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




     #######################################################################################     ACCROUPI     #######################################################################################
        elif A_stance==2:
            if A_sprites>11:
                A_sprites=1



            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_accroupi_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-10
            AHUy2=A_posy+250



     #######################################################################################     SAUT ET COUPS AERIENS     #######################################################################################

        elif A_stance==8:




            if A_dir_saut==4:
                A_posx=A_posx-35
            elif A_dir_saut==6:
                A_posx=A_posx+35


            if A_posy>400 and A_up==1:



                A_posy=A_posy-100

            elif A_posy==400 and A_up==1:




                A_posy=A_posy-50

            elif A_posy==350 and A_up==1:


                A_posy=A_posy-25
                A_up=0

            elif A_posy==325 and A_up==0:



                A_posy=A_posy+25

            elif A_posy==350 and A_up==0:


                A_posy=A_posy+50

            elif A_posy<600 and A_up==0:

               A_posy=A_posy+100

            elif A_posy>=600 and A_up==0:


                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100




                A_leger_air=0
                A_dispo_dash=1
                A_sprites=1
                A_up=1
                A_leger_air=0
                A_fort_air=0
                A_compteur_faible=1
                A_compteur_fort=1

                A_posy=A_posy+100
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_saut_R[A_sprites]}")

                if A_DPL_D==1:
                    A_dir_saut=6
                elif A_DPL_G==1:
                    A_dir_saut=4
                else:
                    A_dir_saut=5


                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250


                A_stance=5
                A_dispo=1
                A_dispo_saut=1
                A_dispo_frappe=1

            if A_subit_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_hit_debout_puissant_R[0]}")


                if A_sprites==3:


                    A_subit_air=0

            elif A_leger_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_air_R[A_sprites]}")
                if A_sprites==2:
                    AHI1x1=A_posx+70
                    AHI1x2=A_posx+225
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+50

                elif A_sprites==3:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_leger_air=0
            elif A_fort_air==1:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_air_R[A_sprites]}")
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Adunk.ogg")
                    A_bruitages.play()
                if A_sprites==3:
                    AHI1x1=A_posx+170
                    AHI1x2=A_posx+425
                    AHI1y1=A_posy-150
                    AHI1y2=A_posy+300

                elif A_sprites==4:
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100

                    A_dispo_frappe=1
                    A_fort_air=0
            elif A_leger_air==0 and A_fort_air==0:
                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_saut_R[A_sprites]}")


            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250

     #######################################################################################     COUPS FAIBLES DEBOUT     #######################################################################################
        elif A_stance==11:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afaible1.ogg")
                A_bruitages.play()
            if A_sprites==2:
                AHI1x1=A_posx+30
                AHI1x2=A_posx+125
                AHI1y1=A_posy-60
                AHI1y2=A_posy+10



            elif A_sprites==3:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==6:
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_1_R[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==12:
            if A_sprites==1:
                AHI1x1=A_posx+30
                AHI1x2=A_posx+200
                AHI1y1=A_posy-120
                AHI1y2=A_posy+105

            elif A_sprites==2:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==5:
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_2_R[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==13:

            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afaible2.ogg")
                A_bruitages.play()
                AHI1x1=A_posx+30
                AHI1x2=A_posx+250
                AHI1y1=A_posy-75
                AHI1y2=A_posy+100

            elif A_sprites==2:


                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==5:
                A_dispo=1
                A_compteur_faible=1
                A_dispo_saut=1
                A_dispo_frappe=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_3_R[A_sprites]}")

            AHUx1=A_posx-75
            AHUx2=A_posx+60
            AHUy1=A_posy-150
            AHUy2=A_posy+250



     #######################################################################################     COUPS PUISSANTS DEBOUT     #######################################################################################
        elif A_stance==14:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort1.ogg")
                A_bruitages.play()
            if A_sprites==3:
                AHI1x1=A_posx+30
                AHI1x2=A_posx+275
                AHI1y1=A_posy-150
                AHI1y2=A_posy+30

            elif A_sprites==4:


                A_dispo_frappe=1

                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_compteur_faible=1
                A_dispo_saut=1
                A_dispo_frappe=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_1_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==15:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort2.ogg")
                A_bruitages.play()
            if A_sprites==3:
                AHI1x1=A_posx+30
                AHI1x2=A_posx+300
                AHI1y1=A_posy-150
                AHI1y2=A_posy+50

            elif A_sprites==4:


                A_dispo_frappe=1

                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_dispo_saut=1
                A_dispo_frappe=1
                A_compteur_faible=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_2_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250




        elif A_stance==16:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Afort3.ogg")
                A_bruitages.play()


            if A_sprites==3:
                AHI1x1=A_posx+30
                AHI1x2=A_posx+360
                AHI1y1=A_posy-150
                AHI1y2=A_posy+70

            elif A_sprites==4:




                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==8:
                A_dispo=1
                A_compteur_fort=1
                A_dispo_saut=1
                A_dispo_frappe=1
                A_compteur_faible=1
                if Y_subit!=4:
                    Y_subit=0







            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_3_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+110
            AHUy1=A_posy-150
            AHUy2=A_posy+250





     #######################################################################################     PROJECTILE DEBOUT     #######################################################################################

        elif A_stance==18:
            if A_sprites==6:
                AHI1x1=A_posx+70
                AHI1x2=A_posx+1250
                AHI1y1=A_posy-20
                AHI1y2=A_posy+250

            elif A_sprites==7:

                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==11:
                A_dispo=1






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_projectile_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+100
            AHUy1=A_posy-100
            AHUy2=A_posy+250





     #######################################################################################     COUP FAIBLE ACCROUPI     #######################################################################################
        elif A_stance==112:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Atir.ogg")
                A_bruitages.play()
            if A_sprites==2:
                AHI1x1=A_posx+70
                AHI1x2=A_posx+200
                AHI1y1=A_posy+100
                AHI1y2=A_posy+250

            elif A_sprites==3:

                A_dispo_frappe=1
                A_dispo_saut=1
                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==7:
                A_dispo=1
                A_compteur_faible=1
                if Y_subit!=4:
                    Y_subit=0






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_faible_accroupi_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+80
            AHUy1=A_posy-10
            AHUy2=A_posy+250




     #######################################################################################     COUP PUISSANT ACCROUPI     #######################################################################################
        elif A_stance==142:
            if A_sprites==1:
                A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Asouleve.ogg")
                A_bruitages.play()
            A_compteur_faible=1
            A_compteur_fort=1
            if Y_subit!=4 and A_sprites==4:
                A_dispo_soulevement=1
            if A_sprites==4:
                AHI1x1=A_posx+150
                AHI1x2=A_posx+350
                AHI1y1=A_posy+-200
                AHI1y2=A_posy+250

            elif A_sprites==5:



                AHI1x1=-100
                AHI1x2=-100
                AHI1y1=-100
                AHI1y2=-100



            elif A_sprites==7:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1






            A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_coup_puissant_accroupi_R[A_sprites]}")

            AHUx1=A_posx-70
            AHUx2=A_posx+60
            AHUy1=A_posy-10
            AHUy2=A_posy+250




     #######################################################################################     PROJECTILE ACCROUPI     #######################################################################################

     #######################################################################################     LE GRAB     #######################################################################################

        elif A_stance==666:

            if Y_subit!=6 and A_sprites<11:
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Agrab.ogg")
                    A_bruitages.play()


                if A_sprites==2:
                    AHI1x1=A_posx+30
                    AHI1x2=A_posx+200
                    AHI1y1=A_posy-100
                    AHI1y2=A_posy-60

                elif A_sprites==4:


                    A_dispo_frappe=1
                    A_dispo_saut=1
                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100


                elif A_sprites==6:

                    A_dispo=1



                    A_dispo_frappe=1
                    A_dispo_saut=1









                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_grab_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250




            elif Y_subit==6 or Y_subit==3 and A_stance==666:
                if A_sprites==1:
                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/AgrabR.ogg")
                    A_bruitages.play()







                if A_sprites==11:
                    Y_subit=3
                    Y_hp=Y_hp-45

                elif A_sprites==13:
                    A_dispo=1

                    A_sprites=1


                    A_dispo_frappe=1
                    A_dispo_saut=1
                    A_stance=5

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_grab_reussi_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250






     #######################################################################################     L'ULTIME     #######################################################################################

        elif A_stance==99:



            if Y_subit!=99 :




                if 26>A_sprites>5:
                    AHI1x1=Aaux_posx-150
                    AHI1x2=Aaux_posx+150
                    AHI1y1=Aaux_posy-150
                    AHI1y2=Aaux_posy+100

                if A_sprites>5:

                    if Aaux_posx<(Y_posx-50):
                        Aaux_posx=Aaux_posx+26
                    else:
                        Aaux_posx=(Y_posx-50)

                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand_R[S_sprites]}")



                if A_sprites==5:

                    A_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Astandrush.ogg")
                    A_bruitages.play()
                    AHI1x1=Aaux_posx+30
                    AHI1x2=Aaux_posx+200
                    AHI1y1=Aaux_posy-100
                    AHI1y2=Aaux_posy-60

                    S_sprites=1
                    Aaux_posx=A_posx+250
                    Aaux_posy=A_posy
                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand_R[S_sprites]}")





                elif A_sprites==26:



                    AHI1x1=-100
                    AHI1x2=-100
                    AHI1y1=-100
                    AHI1y2=-100


                elif A_sprites==28:

                    A_dispo=1
                    AM_sprites=1
                    YM_sprites=15



                    A_dispo_frappe=1
                    A_dispo_saut=1
                    Aaux_posy=-200










                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250



                S_sprites=(S_sprites+1)


            elif Y_subit==99 :
                if A_sprites==6:
                    A_bruitages= mixer.Sound("AultimeR.ogg")
                    A_bruitages.play()







                if A_sprites<10:

                    Deplacements=(A_posx-(Aaux_posx))/10

                    A_posx=A_posx-Deplacements




                if A_sprites<21:
                    A_image_aux=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_stand_reussi_R[S_sprites]}")




                if A_sprites==17:
                    Y_hp=Y_hp-300


                elif A_sprites==22:
                    Aaux_posy=-200






                elif A_sprites==29:
                    A_dispo=1
                    AM_sprites=1
                    YM_sprites=15
                    Y_stance=5





                    A_dispo_frappe=1
                    A_dispo_saut=1
                    A_stance=5
                    if Y_subit!=4:
                        Y_subit=0

                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_ultime_reussi_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+110
                AHUy1=A_posy-150
                AHUy2=A_posy+250



                S_sprites=(S_sprites+1)


     #######################################################################################     DEFENSE     #######################################################################################
        elif A_stance==90:
            if A_sprites!=5:
                A_posx=A_posx-5


                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_garde_debout_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250





            else:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1

        elif A_stance==91:
            if A_sprites!=5:
                A_posx=A_posx-5


                A_image=PhotoImage(file=f"Characters/Alexandre/Sprites/{sprite_A_garde_accroupi_R[A_sprites]}")

                AHUx1=A_posx-70
                AHUx2=A_posx+60
                AHUy1=A_posy-150
                AHUy2=A_posy+250





            else:
                A_dispo=1
                A_dispo_frappe=1
                A_dispo_saut=1







    if A_compteur_roulade>9:
        A_dispo_roulade=1
    A_compteur_roulade=A_compteur_roulade+1
    A_sprites=A_sprites+1
    can.coords(A_app,A_posx,A_posy)
    can.coords(A_hurtbox,AHUx1,AHUy1,AHUx2,AHUy2)
    can.coords(A_hitbox_1,AHI1x1,AHI1y1,AHI1x2,AHI1y2)
    can.coords(A_app_aux,Aaux_posx,Aaux_posy)
    can.itemconfigure(A_app,image=A_image)
    can.itemconfigure(A_app_aux,image=A_image_aux)
    if COMBAT==1:
        fen.after(60,Animation_Alexandre)
    elif COMBAT==0 and Y_mort==1:

        A_sprites=0
        Y_sprites=0

        can.delete(Y_hurtbox, A_hurtbox,A_hitbox_1,Y_hitbox_1,Y_outline,A_outline,Y_degat,A_degat,Y_vie,A_vie,YM_app,AM_app)
        Victoire()















def Animation_Yani():
    global  Y_bruitages,AM_sprites,YM_sprites,A_dispo_soulevement,Y_bruitages,Y_app_aux,Y_image_aux,Yaux_posx,Yaux_posy,Y_stance,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_dispo,A_mort,Y_sortie,depart,Y_subit_air,COMBAT,Y_compteur_roulade,Y_dispo_roulade,Y_roulade,Y_dispo_dash,Y_garde_air,deplacements,Y_image_aux,S_sprites,Y_app_aux,Y_subit,Yaux_posx,Yaux_posy,Y_dispo_garde,A_subit,Y_dispo_soulevement,Y_up,Y_DPL_D,Y_DPL_G,Y_DPL_B,Y_stance,Y_dir_saut,Y_dispo,Y_sprites,Y_dispo_frappe,Y_dispo_saut,Y_compteur_faible,Y_compteur_fort,Y_leger_air,Y_fort_air,Y_dispo,Y_stance,Y_sprites,Y_dispo_saut,Y_dispo_frappe,Y_DPL_D,Y_DPL_G,Y_dir_saut,Y_hurtbox,A_vie,A_degat,Y_vie,Y_degat,A_hpp,Y_hpp,A_hp,Y_hp,COMBAT,A_hp,Y_hp,A_stance,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,AHI1x1,AHI1x2,AHI1y1,AHI1y2,AHI2x1,AHI2x2,AHI2y1,AHI2y2,AHI3x1,AHI3x2,AHI3y1,AHI3y2,AHISx1,AHISx2,AHISy1,AHISy2,AHUx1,AHUx2,AHUy1,AHUx2,YHI1x1,YHI1x2,YHI1y1,YHI1y2,YHI2x1,YHI2x2,YHI2y1,YHI2y2,YHI3x1,YHI3x2,YHI3y1,YHI3y2,YHISx1,YHISx2,YHISy1,YHISy2,YHUx1,YHUx2,YHUy1,YHUx2,YHUy2,agencement,Y_posx,Y_posy,Y_sprites,Y_subit_faible,Y_subit_moyen,Y_subit_fort,Y_subit_soulevement,Y_subit_ulti,Y_stance,Y_dir_saut,Y_image,Y_sprites,Y_app,A_fort_air,A_leger_air,A_up,A_compteur_fort,A_compteur_faible,A_dispo_saut,A_dispo_frappe,A_DPL_D,A_DPL_G,A_DPL_B,A_stance,A_dir_saut,A_dispo,A_dispo,agencement,A_posx,A_posy,A_sprites,A_subit_faible,A_subit_moyen,A_subit_fort,A_subit_soulevement,A_subit_ulti,A_stance,A_dir_saut,A_sprites,A_image,A_posx,Y_posx,A_app,A_hurtbox,AHUx1,AHUx2,AHUy1,AHUy2,A_hitbox_1,AHI1x1,AHI1x2,AHI1y1,AHI1y2


    if Y_posy<-400:
        COMBAT=0


     #######################################################################################     YANI    #######################################################################################


     #######################################################################################     POSITION 1     #######################################################################################
    if agencement==2:

        if Y_mort==1:

            if Y_sprites>8:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort_R[9]}")
            else:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort_R[Y_sprites]}")


        elif Y_sortie==1 and Y_dispo==1 and A_sprites>20:
            if A_sprites==21:

                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Yvictoire.ogg")
                Y_bruitages.play()


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_sortie[3]}")
            Y_posx=Y_posx+100
            Y_posy=Y_posy-100







     #######################################################################################     DEGATS SUBIS     #######################################################################################


        elif Y_subit==1:
            Y_posx=Y_posx+4
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitfaible.ogg")
                Y_bruitages.play()


            if Y_sprites<5:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible_R[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250



            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
        elif Y_subit==2:
            Y_posx=Y_posx+8
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitlourd.ogg")
                Y_bruitages.play()


            if Y_sprites<10:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant_R[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
        elif Y_subit==3:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("ejecte.ogg")
                Y_bruitages.play()


            if Y_sprites<10:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale_R[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250

                Y_posx=Y_posx+100


            elif A_stance==666:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale_R[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250


                Y_sprites=1


            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1


        elif Y_subit==4:
            A_dispo_soulevement=0
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitlourd.ogg")
                Y_bruitages.play()


            if Y_sprites<8:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant_R[0]}")


                Y_posy=Y_posy-70


                Y_posx=Y_posx+25
            elif Y_posy<700:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale_R[0]}")
                Y_posy=Y_posy+70
                Y_posx=Y_posx+25





            else:
                Y_posy=700
                A_dispo_soulevement=1
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1




            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



        elif Y_subit==6:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitfaible.ogg")
                Y_bruitages.play()





            if A_sprites<11:

                Y_posx=A_posx+250
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible_R[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            else:

                Y_subit=3

        elif Y_subit==99:

            if A_sprites<6:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible_R[0]}")
            else:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort_R[1]}")






     #######################################################################################     DEBOUT     #######################################################################################
        elif Y_stance==5:
            if Y_sprites>7:
                Y_sprites=1

            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_debout_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



     #######################################################################################     DASH     #######################################################################################
        elif Y_stance==55:

            if Y_roulade==4:
                Y_posx=Y_posx-45
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_roulade_R[0]}")
            elif Y_roulade==6:
                Y_posx=Y_posx+45
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_roulade[0]}")

            if Y_sprites==6:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250

            YHUx1=-100
            YHUx2=-100
            YHUy1=-100
            YHUy2=-100




        elif Y_stance==54 or Y_stance==56:

            if Y_sprites==4:
                if Y_posy<700:
                    Y_stance=8
                    Y_up=0

                else:

                    Y_leger_air=0
                    Y_dispo_dash=1
                    Y_sprites=1
                    Y_up=1
                    Y_leger_air=0
                    Y_fort_air=0
                    Y_compteur_faible=1
                    Y_compteur_fort=1




                    if Y_DPL_D==1:
                        Y_dir_saut=6
                    elif Y_DPL_G==1:
                        Y_dir_saut=4
                    else:
                        Y_dir_saut=5


                    YHUx1=Y_posx-70
                    YHUx2=Y_posx+60
                    YHUy1=Y_posy-150
                    YHUy2=Y_posy+250


                    Y_stance=5
                    Y_dispo=1
                    Y_dispo_saut=1
                    Y_dispo_frappe=1


            if Y_stance==54:
                Y_posx=Y_posx-100

                Y_dir_saut=4


            elif Y_stance==56:
                Y_posx=Y_posx+100
                Y_dir_saut=6




            if Y_fort_air==0 and Y_leger_air==0 and Y_stance==54:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_dash_avant_R[0]}")
            elif Y_fort_air==0 and Y_leger_air==0 and Y_stance==56:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_dash_arriere_R[0]}")
            elif Y_leger_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_air_R[Y_sprites]}")
                if Y_sprites==2:
                    YHI1x1=Y_posx-150
                    YHI1x2=Y_posx-50
                    YHI1y1=Y_posy-70
                    YHI1y2=Y_posy+40

                elif Y_sprites==3:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_leger_air=0
                    Y_stance=8
                    Y_up=0
            elif Y_fort_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_air_R[Y_sprites]}")
                if Y_sprites==3:
                    YHI1x1=Y_posx-250
                    YHI1x2=Y_posx-10
                    YHI1y1=Y_posy+50
                    YHI1y2=Y_posy+200

                elif Y_sprites==4:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_fort_air=0
                    Y_stance=8
                    Y_up=0






            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250










     #######################################################################################     MARCHE AVANT     #######################################################################################
        elif Y_stance==4:
            if Y_sprites>6:
                Y_sprites=1


            Y_posx=Y_posx-35


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_marche_avant_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250





     #######################################################################################     MARCHE ARRIERE     #######################################################################################
        elif Y_stance==6:
            if Y_sprites>8:
                Y_sprites=1


            Y_posx=Y_posx+35


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_marche_arriere_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




     #######################################################################################     ACCROUPI     #######################################################################################
        elif Y_stance==2:
            if Y_sprites>7:
                Y_sprites=1



            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_accroupi_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250



     #######################################################################################     SAUT ET COUPS AERIENS     #######################################################################################

        elif Y_stance==8:





            if Y_dir_saut==4:
                Y_posx=Y_posx-35
            elif Y_dir_saut==6:
                Y_posx=Y_posx+35


            if Y_posy>400 and Y_up==1:


                Y_posy=Y_posy-100

            elif Y_posy==400 and Y_up==1:

                Y_posy=Y_posy-50

            elif Y_posy==350 and Y_up==1:

                Y_posy=Y_posy-25
                Y_up=0

            elif Y_posy==325 and Y_up==0:


                Y_posy=Y_posy+25

            elif Y_posy==350 and Y_up==0:


                Y_posy=Y_posy+50

            elif Y_posy<600 and Y_up==0:


               Y_posy=Y_posy+100

            elif Y_posy>=600 and Y_up==0:


                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100




                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1

                Y_posy=Y_posy+100
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_saut_R[Y_sprites]}")

                if Y_DPL_D==1:
                    Y_dir_saut=6
                elif Y_DPL_G==1:
                    Y_dir_saut=4
                else:
                    Y_dir_saut=5


                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250


                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1

            if Y_subit_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant_R[0]}")


                if Y_sprites==3:


                    Y_subit_air=0

            elif Y_leger_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_air_R[Y_sprites]}")
                if Y_sprites==2:
                    YHI1x1=Y_posx-150
                    YHI1x2=Y_posx-50
                    YHI1y1=Y_posy-70
                    YHI1y2=Y_posy+40

                elif Y_sprites==3:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_leger_air=0
            elif Y_fort_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_air_R[Y_sprites]}")
                if Y_sprites==3:
                    YHI1x1=Y_posx-250
                    YHI1x2=Y_posx-10
                    YHI1y1=Y_posy+50
                    YHI1y2=Y_posy+200

                elif Y_sprites==4:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_fort_air=0
            elif Y_leger_air==0 and Y_fort_air==0:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_saut_R[Y_sprites]}")


            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250


     #######################################################################################     COUPS FYIBLES DEBOUT     #######################################################################################
        elif Y_stance==11:
            if Y_sprites==2:

                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ycoupfaible1.ogg")
                Y_bruitages.play()
                YHI1x1=Y_posx-160
                YHI1x2=Y_posx-65
                YHI1y1=Y_posy-60
                YHI1y2=Y_posy+10

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==6:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_1_R[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==12:
            if Y_sprites==2:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ycoupdepiedausol.ogg")
                Y_bruitages.play()
                YHI1x1=Y_posx-250
                YHI1x2=Y_posx-30
                YHI1y1=Y_posy-10
                YHI1y2=Y_posy+105

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==5:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_2_R[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==13:
            if Y_sprites==2:
                YHI1x1=Y_posx-600
                YHI1x2=Y_posx+0
                YHI1y1=Y_posy+150
                YHI1y2=Y_posy+200

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==5:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1
                Y_dispo_frappe=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_3_R[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



     #######################################################################################     COUPS PUISSANTS DEBOUT     #######################################################################################
        elif Y_stance==14:
            if Y_sprites==3:
                YHI1x1=Y_posx-200
                YHI1x2=Y_posx-30
                YHI1y1=Y_posy-120
                YHI1y2=Y_posy-0

            elif Y_sprites==4:


                Y_dispo_frappe=1

                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==8:
                Y_dispo=1
                Y_compteur_fort=1
                Y_compteur_faible=1
                Y_dispo_saut=1
                Y_dispo_frappe=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_1_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+110
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==15:
            if Y_sprites==4:

                YHI1x1=Y_posx-220
                YHI1x2=Y_posx-30
                YHI1y1=Y_posy-220
                YHI1y2=Y_posy-0
            elif Y_sprites==5:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100

            elif Y_sprites==6:
                YHI1x1=Y_posx-240
                YHI1x2=Y_posx-30
                YHI1y1=Y_posy-220
                YHI1y2=Y_posy+120
            elif Y_sprites==7:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100

                Y_dispo_frappe=1

            elif Y_sprites==8:



                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100




                Y_dispo=1
                Y_compteur_fort=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
                Y_compteur_faible=1





            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_2_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+110
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250








     #######################################################################################     PROJECTILE DEBOUT     #######################################################################################

        elif Y_stance==18:
            if Y_sprites==6:
                YHI1x1=Y_posx-1250
                YHI1x2=Y_posx-70
                YHI1y1=Y_posy-20
                YHI1y2=Y_posy+250

            elif Y_sprites==7:

                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==11:
                Y_dispo=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_projectile_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+100
            YHUy1=Y_posy-100
            YHUy2=Y_posy+250





     #######################################################################################     COUP FAIBLE ACCROUPI     #######################################################################################
        elif Y_stance==112:
            if Y_sprites==2:
                YHI1x1=Y_posx-150
                YHI1x2=Y_posx+0
                YHI1y1=Y_posy+0
                YHI1y2=Y_posy+100

            elif Y_sprites==3:

                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==7:
                Y_dispo=1
                Y_compteur_faible=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_accroupi_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+80
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250




     #######################################################################################     COUP PUISSYNT YCCROUPI     #######################################################################################
        elif Y_stance==142:
            Y_compteur_faible=1
            Y_compteur_fort=1
            if A_subit!=4 and Y_sprites==4:
                Y_dispo_soulevement=1
            if Y_sprites==4:
                YHI1x1=Y_posx-350
                YHI1x2=Y_posx-150
                YHI1y1=Y_posy+-200
                YHI1y2=Y_posy+250

            elif Y_sprites==5:



                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==7:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_accroupi_R[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250




     #######################################################################################     PROJECTILE ACCROUPI     #######################################################################################

     #######################################################################################     LE GRAB     #######################################################################################

        elif Y_stance==666:

            if A_subit!=6 and Y_sprites<11:


                if Y_sprites==2:
                    YHI1x1=Y_posx-200
                    YHI1x2=Y_posx-30
                    YHI1y1=Y_posy-100
                    YHI1y2=Y_posy-60

                elif Y_sprites==4:


                    Y_dispo_frappe=1
                    Y_dispo_saut=1
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100


                elif Y_sprites==6:

                    Y_dispo=1



                    Y_dispo_frappe=1
                    Y_dispo_saut=1









                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_grab_R[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+110
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            elif A_subit==6 or A_subit==3 and Y_stance==666:







                if Y_sprites==3:
                    A_subit=3
                    A_hp=A_hp+45

                elif Y_sprites==7:
                    Y_dispo=1

                    Y_sprites=1


                    Y_dispo_frappe=1
                    Y_dispo_saut=1
                    Y_stance=5

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_grab_reussi_R[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+110
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250







     #######################################################################################     ULTIME     #######################################################################################

        elif Y_stance==99:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Yepekaye.ogg")
                Y_bruitages.play()
            Y_image_aux=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ultime_explosion[Y_sprites]}")
            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ultime_R[Y_sprites]}")

            if Y_sprites==8:
                YHI1x1=Y_posx-400
                YHI1x2=Y_posx-30
                YHI1y1=Y_posy-200
                YHI1y2=Y_posy+200

            elif Y_sprites==9:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100
            elif Y_sprites==13:
                Yaux_posx=A_posx
                Yaux_posy=A_posy
                YHI1x1=Yaux_posx-100
                YHI1x2=Yaux_posx+100
                YHI1y1=Yaux_posy-100
                YHI1y2=Yaux_posy+100


            elif Y_sprites==16:
                Yaux_posx=-500
                Yaux_posy=-500

                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100
                AM_sprites=15
                YM_sprites=1
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

            can.itemconfigure(Y_app_aux,image=Y_image_aux)
            can.coords(Y_app_aux,Yaux_posx,Yaux_posy)







     #######################################################################################     DEFENSE     #######################################################################################
        elif Y_stance==90:
            if Y_sprites!=5:
                Y_posx=Y_posx+5


                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_garde_debout_R[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250





            else:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

        elif Y_stance==91:
            if Y_sprites!=5:
                Y_posx=Y_posx+5


                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_garde_accroupi_R[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250





            else:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1



     #######################################################################################     POSITION 2     #######################################################################################



    elif agencement==1:

        if Y_mort==1:

            if Y_sprites>8:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort[9]}")
            else:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort[Y_sprites]}")

     #######################################################################################     DEGATS SUBIS     #######################################################################################
        elif depart==1:


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_entrée[Y_sprites]}")

            if Y_sprites==29:

                fen.bind('<KeyPress-Left>',Y_gauche_lance)
                fen.bind('<KeyRelease-Left>',Y_arret_gauche)
                fen.bind('<KeyPress-Right>',Y_droite_lance)
                fen.bind('<KeyRelease-Right>',Y_arret_droite)
                fen.bind('<KeyPress-Down>',Y_bas_lance)
                fen.bind('<KeyRelease-Down>',Y_arret_bas)
                fen.bind('9',Y_dash)
                fen.bind('<Up>',Y_saut)
                fen.bind('<7>',Y_frappe_faible)
                fen.bind('<8>',Y_frappe_forte)

                fen.bind('4',Y_grab)
                fen.bind('<0>',Y_ulti)


                depart=0

        elif Y_sortie==1 and Y_dispo==1 and A_sprites>20:
            if A_sprites==21:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Yvictoire.ogg")
                Y_bruitages.play()


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_sortie[3]}")
            Y_posx=Y_posx+100
            Y_posy=Y_posy-100

        elif Y_subit==1:
            Y_posx=Y_posx-4
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitfaible.ogg")
                Y_bruitages.play()


            if Y_sprites<5:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible[0]}")

                YHUx1=Y_posx-60
                YHUx2=Y_posx+70
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250



            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
        elif Y_subit==2:

            Y_posx=Y_posx-8
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitlourd.ogg")
                Y_bruitages.play()

            if Y_sprites<10:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant[0]}")

                YHUx1=Y_posx-60
                YHUx2=Y_posx+70
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
        elif Y_subit==3:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Yejecte.ogg")
                Y_bruitages.play()


            if Y_sprites<10:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250

                Y_posx=Y_posx-100


            elif A_stance==666:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250


                Y_sprites=1


            else:
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1


        elif Y_subit==4:
            A_dispo_soulevement=0
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitlourd.ogg")
                Y_bruitages.play()


            if Y_sprites<8:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant[0]}")


                Y_posy=Y_posy-70


                Y_posx=Y_posx-25
            elif Y_posy<700:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ejection_horizontale[0]}")
                Y_posy=Y_posy+70
                Y_posx=Y_posx-25





            else:
                A_dispo_soulevement=1
                Y_posy=700
                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1
                Y_subit=0
                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1




            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



        elif Y_subit==6:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ysubitfaible.ogg")
                Y_bruitages.play()





            if A_sprites<11:

                Y_posx=A_posx-250
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible[0]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            else:

                Y_subit=3


        elif Y_subit==99:
            if A_sprites<6:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_faible[0]}")
            elif A_sprites==6:
                Y_posx=Y_posx-50
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort[1]}")
            else:

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_mort[1]}")



     #######################################################################################     DEBOUT     #######################################################################################
        elif Y_stance==5:
            if Y_sprites>7:
                Y_sprites=1

            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_debout[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



     #######################################################################################     DASH     #######################################################################################
        elif Y_stance==55:

            if Y_roulade==4:
                Y_posx=Y_posx-45
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_roulade_R[0]}")
            elif Y_roulade==6:
                Y_posx=Y_posx+45
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_roulade[0]}")

            if Y_sprites==6:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250

            YHUx1=0
            YHUx2=0
            YHUy1=0
            YHUy2=0



        elif Y_stance==54 or Y_stance==56:

            if Y_sprites==4:
                if Y_posy<700:
                    Y_stance=8
                    Y_up=0

                else:

                    Y_leger_air=0
                    Y_dispo_dash=1
                    Y_sprites=1
                    Y_up=1
                    Y_leger_air=0
                    Y_fort_air=0
                    Y_compteur_faible=1
                    Y_compteur_fort=1




                    if Y_DPL_D==1:
                        Y_dir_saut=6
                    elif Y_DPL_G==1:
                        Y_dir_saut=4
                    else:
                        Y_dir_saut=5


                    YHUx1=Y_posx-70
                    YHUx2=Y_posx+60
                    YHUy1=Y_posy-150
                    YHUy2=Y_posy+250


                    Y_stance=5
                    Y_dispo=1
                    Y_dispo_saut=1
                    Y_dispo_frappe=1


            if Y_stance==54:
                Y_posx=Y_posx-100
                Y_dir_saut=4

            elif Y_stance==56:
                Y_posx=Y_posx+100
                Y_dir_saut=6



            if Y_fort_air==0 and Y_leger_air==0 and Y_stance==54:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_dash_arriere[0]}")

            elif Y_fort_air==0 and Y_leger_air==0 and Y_stance==56:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_dash_avant[0]}")

            elif Y_leger_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_air[Y_sprites]}")
                if Y_sprites==2:

                    YHI1x1=Y_posx+50
                    YHI1x2=Y_posx+150
                    YHI1y1=Y_posy-70
                    YHI1y2=Y_posy+40

                elif Y_sprites==3:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_leger_air=0
                    Y_stance=8
                    Y_up=0

            elif Y_fort_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_air[Y_sprites]}")
                if Y_sprites==3:
                    YHI1x1=Y_posx+10
                    YHI1x2=Y_posx+250
                    YHI1y1=Y_posy+50
                    YHI1y2=Y_posy+200

                elif Y_sprites==4:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_fort_air=0
                    Y_stance=8
                    Y_up=0






            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250










     #######################################################################################     MARCHE AVANT     #######################################################################################
        elif Y_stance==4:
            if Y_sprites>6:
                Y_sprites=1


            Y_posx=Y_posx-35


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_marche_arriere[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250





     #######################################################################################     MARCHE ARRIERE     #######################################################################################
        elif Y_stance==6:
            if Y_sprites>8:
                Y_sprites=1


            Y_posx=Y_posx+35


            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_marche_avant[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




     #######################################################################################     ACCROUPI     #######################################################################################
        elif Y_stance==2:
            if Y_sprites>7:
                Y_sprites=0



            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_accroupi[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250



     #######################################################################################     SAUT ET COUPS AERIENS     #######################################################################################

        elif Y_stance==8:




            if Y_dir_saut==4:
                Y_posx=Y_posx-35
            elif Y_dir_saut==6:
                Y_posx=Y_posx+35


            if Y_posy>400 and Y_up==1:


                Y_posy=Y_posy-100

            elif Y_posy==400 and Y_up==1:

                Y_posy=Y_posy-50

            elif Y_posy==350 and Y_up==1:

                Y_posy=Y_posy-25
                Y_up=0

            elif Y_posy==325 and Y_up==0:


                Y_posy=Y_posy+25

            elif Y_posy==350 and Y_up==0:


                Y_posy=Y_posy+50

            elif Y_posy<600 and Y_up==0:


               Y_posy=Y_posy+100

            elif Y_posy>=600 and Y_up==0:


                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100




                Y_leger_air=0
                Y_dispo_dash=1
                Y_sprites=1
                Y_up=1
                Y_leger_air=0
                Y_fort_air=0
                Y_compteur_faible=1
                Y_compteur_fort=1

                Y_posy=Y_posy+100
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_saut[Y_sprites]}")

                if Y_DPL_D==1:
                    Y_dir_saut=6
                elif Y_DPL_G==1:
                    Y_dir_saut=4
                else:
                    Y_dir_saut=5


                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250


                Y_stance=5
                Y_dispo=1
                Y_dispo_saut=1
                Y_dispo_frappe=1

            if Y_subit_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_hit_debout_puissant[0]}")

                if Y_sprites==3:

                    Y_subit_air=0

            elif Y_leger_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_air[Y_sprites]}")
                if Y_sprites==2:
                    YHI1x1=Y_posx+50
                    YHI1x2=Y_posx+150
                    YHI1y1=Y_posy-70
                    YHI1y2=Y_posy+40

                elif Y_sprites==3:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_leger_air=0
            elif Y_fort_air==1:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_air[Y_sprites]}")
                if Y_sprites==3:
                    YHI1x1=Y_posx+10
                    YHI1x2=Y_posx+250
                    YHI1y1=Y_posy+50
                    YHI1y2=Y_posy+200

                elif Y_sprites==4:
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100

                    Y_dispo_frappe=1
                    Y_fort_air=0
            elif Y_leger_air==0 and Y_fort_air==0:
                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_saut[Y_sprites]}")


            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250


     #######################################################################################     COUPS FYIBLES DEBOUT     #######################################################################################
        elif Y_stance==11:
            if Y_sprites==2:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ycoupfaible1.ogg")
                Y_bruitages.play()
                YHI1x1=Y_posx+65
                YHI1x2=Y_posx+160
                YHI1y1=Y_posy-60
                YHI1y2=Y_posy+10

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==6:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1




            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_1[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==12:
            if Y_sprites==2:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Ycoupdepiedausol.ogg")
                Y_bruitages.play()

                YHI1x1=Y_posx+30
                YHI1x2=Y_posx+250
                YHI1y1=Y_posy-10
                YHI1y2=Y_posy+105

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==5:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_2[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==13:
            if Y_sprites==2:
                YHI1x1=Y_posx+0
                YHI1x2=Y_posx+600
                YHI1y1=Y_posy+150
                YHI1y2=Y_posy+200

            elif Y_sprites==3:


                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==6:
                Y_dispo=1
                Y_compteur_faible=1
                Y_dispo_saut=1
                Y_dispo_frappe=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_3[Y_sprites]}")

            YHUx1=Y_posx-75
            YHUx2=Y_posx+60
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250



     #######################################################################################     COUPS PUISSANTS DEBOUT     #######################################################################################
        elif Y_stance==14:
            if Y_sprites==4:
                YHI1x1=Y_posx+30
                YHI1x2=Y_posx+200
                YHI1y1=Y_posy-120
                YHI1y2=Y_posy-0

            elif Y_sprites==5:


                Y_dispo_frappe=1

                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==8:
                Y_dispo=1
                Y_compteur_fort=1

                Y_compteur_faible=1
                Y_dispo_saut=1
                Y_dispo_frappe=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_1[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+110
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250




        elif Y_stance==15:
            if Y_sprites==4:

                YHI1x1=Y_posx+30
                YHI1x2=Y_posx+220
                YHI1y1=Y_posy-220
                YHI1y2=Y_posy-0
            elif Y_sprites==5:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100

            elif Y_sprites==6:
                YHI1x1=Y_posx+30
                YHI1x2=Y_posx+240
                YHI1y1=Y_posy-220
                YHI1y2=Y_posy+120
            elif Y_sprites==7:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100
                Y_dispo_frappe=1

            elif Y_sprites==8:



                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100




                Y_dispo=1
                Y_compteur_fort=1
                Y_dispo_saut=1
                Y_dispo_frappe=1
                Y_compteur_faible=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_2[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+110
            YHUy1=Y_posy-150
            YHUy2=Y_posy+250





     #######################################################################################     PROJECTILE DEBOUT     #######################################################################################

        elif Y_stance==18:
            if Y_sprites==6:
                YHI1x1=Y_posx+70
                YHI1x2=Y_posx+1250
                YHI1y1=Y_posy-20
                YHI1y2=Y_posy+250

            elif Y_sprites==7:

                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==11:
                Y_dispo=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_projectile[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+100
            YHUy1=Y_posy-100
            YHUy2=Y_posy+250





     #######################################################################################     COUP FAIBLE ACCROUPI     #######################################################################################
        elif Y_stance==112:
            if Y_sprites==2:
                YHI1x1=Y_posx+0
                YHI1x2=Y_posx+150
                YHI1y1=Y_posy+0
                YHI1y2=Y_posy+100

            elif Y_sprites==3:

                Y_dispo_frappe=1
                Y_dispo_saut=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==7:
                Y_dispo=1
                Y_compteur_faible=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_faible_accroupi[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+80
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250




     #######################################################################################     COUP PUISSYNT YCCROUPI     #######################################################################################
        elif Y_stance==142:
            Y_compteur_faible=1
            Y_compteur_fort=1
            if A_subit!=4 and Y_sprites==4:
                Y_dispo_soulevement=1
            if Y_sprites==4:
                YHI1x1=Y_posx+150
                YHI1x2=Y_posx+350
                YHI1y1=Y_posy+-200
                YHI1y2=Y_posy+250

            elif Y_sprites==5:



                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100



            elif Y_sprites==7:
                Y_dispo_saut=1
                Y_dispo=1
                Y_dispo_frappe=1






            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_coup_puissant_accroupi[Y_sprites]}")

            YHUx1=Y_posx-70
            YHUx2=Y_posx+60
            YHUy1=Y_posy-10
            YHUy2=Y_posy+250




     #######################################################################################     PROJECTILE ACCROUPI     #######################################################################################

     #######################################################################################     LE GRAB     #######################################################################################

        elif Y_stance==666:
            print("pute")

            if A_subit!=6 and Y_sprites<11:


                if Y_sprites==2:
                    YHI1x1=Y_posx+30
                    YHI1x2=Y_posx+200
                    YHI1y1=Y_posy-100
                    YHI1y2=Y_posy-60

                elif Y_sprites==4:


                    Y_dispo_frappe=1
                    Y_dispo_saut=1
                    YHI1x1=-100
                    YHI1x2=-100
                    YHI1y1=-100
                    YHI1y2=-100


                elif Y_sprites==6:

                    Y_dispo=1



                    Y_dispo_frappe=1
                    Y_dispo_saut=1









                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_grab[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+110
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250




            elif A_subit==6 or A_subit==3 and Y_stance==666:







                if Y_sprites==3:
                    A_subit=3
                    A_hp=A_hp+45

                if Y_sprites==7:
                    Y_dispo=1

                    Y_sprites=1


                    Y_dispo_frappe=1
                    Y_dispo_saut=1
                    Y_stance=5

                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_grab_reussi[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+110
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250



     #######################################################################################     ULTIME     #######################################################################################

        elif Y_stance==99:
            if Y_sprites==1:
                Y_bruitages= mixer.Sound("Characters/Yani/Sounds/Yepekaye.ogg")
                Y_bruitages.play()
            Y_image_aux=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ultime_explosion[Y_sprites]}")
            Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_ultime[Y_sprites]}")

            if Y_sprites==8:
                YHI1x1=Y_posx+30
                YHI1x2=Y_posx+400
                YHI1y1=Y_posy-200
                YHI1y2=Y_posy+200

            elif Y_sprites==9:
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100
            elif Y_sprites==13:
                Yaux_posx=A_posx
                Yaux_posy=A_posy
                YHI1x1=Yaux_posx-100
                YHI1x2=Yaux_posx+100
                YHI1y1=Yaux_posy-100
                YHI1y2=Yaux_posy+100


            elif Y_sprites==16:
                Yaux_posx=-500
                Yaux_posy=-500
                AM_sprites=15
                YM_sprites=1
                YHI1x1=-100
                YHI1x2=-100
                YHI1y1=-100
                YHI1y2=-100
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

            can.itemconfigure(Y_app_aux,image=Y_image_aux)
            can.coords(Y_app_aux,Yaux_posx,Yaux_posy)






     #######################################################################################     DEFENSE     #######################################################################################
        elif Y_stance==90:
            if Y_sprites!=5:
                Y_posx=Y_posx-5


                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_garde_debout[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250





            else:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1

        elif Y_stance==91:
            if Y_sprites!=5:
                Y_posx=Y_posx-5


                Y_image=PhotoImage(file=f"Characters/Yani/Sprites/{sprite_Y_garde_accroupi[Y_sprites]}")

                YHUx1=Y_posx-70
                YHUx2=Y_posx+60
                YHUy1=Y_posy-150
                YHUy2=Y_posy+250





            else:
                Y_dispo=1
                Y_dispo_frappe=1
                Y_dispo_saut=1


    if Y_compteur_roulade>9:
        Y_dispo_roulade=1
    Y_compteur_roulade=Y_compteur_roulade+1
    Y_sprites=Y_sprites+1

    can.coords(Y_app,Y_posx,Y_posy-50)
    can.coords(Y_hitbox_1,YHI1x1,YHI1y1,YHI1x2,YHI1y2)
    can.coords(Y_hurtbox,YHUx1,YHUy1,YHUx2,YHUy2)
    can.itemconfigure(Y_app,image=Y_image)
    if COMBAT==1:
        fen.after(60,Animation_Yani)
    elif COMBAT==0 and A_mort==1:
        A_sprites=0
        Y_sprites=0

        can.delete(Y_hurtbox, A_hurtbox,A_hitbox_1,Y_hitbox_1,Y_outline,A_outline,Y_degat,A_degat,Y_vie,A_vie,YM_app,AM_app)
        Victoire()



def Menu():
    global Selec_menu, indice_menu,deplmen,image, Menu_image,Menurun,sub_menu,verif_select
    indice_menu=0
    verif_select=0
    Menu_image = PhotoImage(file=f"Interface/{Selec_Menu[indice_menu]}")
    image=can.create_image(950,500, image=Menu_image)

    lance_menu(1)


def Menu_bas(m):
    global deplmen
    deplmen=2

def Menu_haut(m):
    global deplmen
    deplmen=1

def Menu_valider(m):
    global indice_menu,Menurun,verif_select,Menu_image,sub_menu
    fen.unbind('k')

    Menurun=0
    sub_menu=1





def Menu_anim():
    global deplmen,indice_menu, image, Menu_image,Menurun,verif_select, indice_transition



    if deplmen==1:
        if indice_menu!=11:
            indice_menu=indice_menu+1
        else:
            indice_menu=0

    elif deplmen==2:
        if indice_menu!=0:
            indice_menu=indice_menu-1
        else:
            indice_menu=11
    if indice_menu == 0 and deplmen!=0 or indice_menu == 3 and deplmen!=0 or indice_menu == 6 and deplmen!=0 or indice_menu == 9 and deplmen!=0 :
        deplmen=0


    Menu_image = PhotoImage(file=f"Interface/{Selec_Menu[indice_menu]}")
    can.itemconfigure(image,image=Menu_image)
    if Menurun==1:
        fen.after(1,Menu_anim)

    elif indice_menu==0:
        verif_select=1
        indice_transition=0
        Transition_menu()
        mixer.music.load("Interface/Sounds/STAGESELECT.ogg")
        mixer.music.play()
    elif indice_menu==3:
        mixer.music.stop()
        Quitter()
    elif indice_menu==6:
        Credits()
        mixer.music.load("Interface/Sounds/CREDITS.ogg")
        mixer.music.play()
    elif indice_menu==9:
        Commandes()
        mixer.music.load("Interface/Sounds/CREDITS.ogg")
        mixer.music.play()




def Transition_menu():
    global Menu_image, indice_transition, image

    if indice_transition == 10:
        Stage_menu()
    else:
        indice_transition = indice_transition+1
        Menu_image=PhotoImage(file=f"Interface/{Transition[indice_transition]}")
        can.itemconfigure(image,image=Menu_image)
        fen.after(60, Transition_menu)



def Credits():
    global image,text,sub_menu,Menu_image
    fen.unbind('k')

    Menu_image=PhotoImage(file="Interface/CREDITS.png")
    can.itemconfigure(image,image=Menu_image)
    fen.bind('k',lance_menu)


def lance_menu(y):
    global Selec_menu, indice_menu,deplmen,image, Menu_image,Menurun,sub_menu,image_stage_selec,imagemen,imagebg,verif_select

    if verif_select==1:

        can.delete(image_stage_selec,imagemen,imagebg)
        verif_select=0

    mixer.music.load("Interface/Sounds/MENU.ogg")
    mixer.music.play()

    fen.unbind('k')


    Menurun=1
    sub_menu=0

    deplmen=0
    Menu_image = PhotoImage(file=f"Interface/{Selec_Menu[indice_menu]}")

    fen.bind('<z>', Menu_haut)
    fen.bind('<s>', Menu_bas)
    fen.bind('<k>', Menu_valider)
    Menu_anim()



def Quitter_instant(a):
    global image
    mixer.music.stop()

    can.delete(image)
    can.create_text(950,500,text="Merci d'avoir""\n""        joué",font='Times 100 bold',fill="pink")
    fen.after(2000,fen.destroy)

def Quitter():
    global image


    can.delete(image)
    can.create_text(950,500,text="Merci d'avoir""\n""        joué",font='Times 100 bold',fill="pink")
    fen.after(2000,fen.destroy)

def Commandes():
    global Menu_image,image,sub_menu

    Menu_image=PhotoImage(file="Interface/COMMANDES.png")
    can.itemconfigure(image,image=Menu_image)
    fen.bind('k',lance_menu)




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""APPEL DES SPRITES"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#############Sprites Alexandre~###################

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""INDEPENDANT"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
sprite_A_special_meter=[]
for S in range(0,40):
    sprite_A_special_meter.append("Alexandrespecial ("+str(S)+").png")

sprite_A_entrée=[]
for S in range(1,40):
    sprite_A_entrée.append("Alexandreentrée ("+str(S)+").png")

sprite_A_sortie=[]
for S in range(1,40):
    sprite_A_sortie.append("Alexandresortie ("+str(S)+").png")

sprite_A_victoire=[]
for S in range(1,40):
    sprite_A_victoire.append("Alexandrevictoire ("+str(S)+").png")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""BASE"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
sprite_A_debout=[]
for S in range(1,9):
    sprite_A_debout.append("Alexandredebout ("+str(S)+").png")

sprite_A_accroupi=[]
for S in range(1,15):
    sprite_A_accroupi.append("Alexandreaccroupi ("+str(S)+").png")

sprite_A_marche_avant=[]
for S in range(1,10):
    sprite_A_marche_avant.append("Alexandremarcheavant ("+str(S)+").png")

sprite_A_marche_arriere=[]
for S in range(1,10):
    sprite_A_marche_arriere.append("Alexandremarchearriere ("+str(S)+").png")

sprite_A_dash_avant=[]
for S in range(1,11):
    sprite_A_dash_avant.append("Alexandredashavant ("+str(S)+").png")

sprite_A_dash_arriere=[]
for S in range(1,11):
    sprite_A_dash_arriere.append("Alexandredasharriere ("+str(S)+").png")
sprite_A_roulade=[]
for S in range(1,11):
    sprite_A_roulade.append("Alexandreroulade ("+str(S)+").png")

sprite_A_saut=[]
for S in range(1,18):
    sprite_A_saut.append("Alexandreair ("+str(S)+").png")

sprite_A_sol=[]
for S in range(1,11):
    sprite_A_sol.append("Alexandresol ("+str(S)+").png")
sprite_A_garde_air=[]
for S in range(1,11):
    sprite_A_garde_air.append("Alexandregardeair ("+str(S)+").png")

sprite_A_garde_debout=[]
for S in range(1,11):
    sprite_A_garde_debout.append("Alexandregardedebout ("+str(S)+").png")

sprite_A_garde_accroupi=[]
for S in range(1,11):
    sprite_A_garde_accroupi.append("Alexandregardeaccroupi ("+str(S)+").png")



sprite_A_coup_faible_1=[]
for S in range(0,8):
    sprite_A_coup_faible_1.append("Alexandrecoupfaible1 ("+str(S)+").png")

sprite_A_coup_faible_2=[]
for S in range(1,11):
    sprite_A_coup_faible_2.append("Alexandrecoupfaible2 ("+str(S)+").png")

sprite_A_coup_faible_3=[]
for S in range(1,11):
    sprite_A_coup_faible_3.append("Alexandrecoupfaible3 ("+str(S)+").png")



sprite_A_coup_puissant_1=[]
for S in range(1,11):
    sprite_A_coup_puissant_1.append("Alexandrecouppuissant1 ("+str(S)+").png")

sprite_A_coup_puissant_2=[]
for S in range(1,11):
    sprite_A_coup_puissant_2.append("Alexandrecouppuissant2 ("+str(S)+").png")

sprite_A_coup_puissant_3=[]
for S in range(1,11):
    sprite_A_coup_puissant_3.append("Alexandrecouppuissant3 ("+str(S)+").png")

sprite_A_projectile=[]
for S in range(1,13):
    sprite_A_projectile.append("Alexandreprojectile ("+str(S)+").png")


sprite_A_coup_faible_accroupi=[]
for S in range(1,11):
    sprite_A_coup_faible_accroupi.append("Alexandrecoupfaibleaccroupi ("+str(S)+").png")

sprite_A_coup_puissant_accroupi=[]
for S in range(1,11):
    sprite_A_coup_puissant_accroupi.append("Alexandrecouppuissantaccroupi ("+str(S)+").png")

sprite_A_projectile_accroupi=[]
for S in range(1,11):
    sprite_A_projectile_accroupi.append("Alexandreprojectileaccroupi ("+str(S)+").png")


sprite_A_coup_faible_air=[]
for S in range(1,11):
    sprite_A_coup_faible_air.append("Alexandrecoupfaibleair ("+str(S)+").png")

sprite_A_coup_puissant_air=[]
for S in range(1,11):
    sprite_A_coup_puissant_air.append("Alexandrecouppuissantair ("+str(S)+").png")

sprite_A_projectile_air=[]
for S in range(1,11):
    sprite_A_projectile_air.append("Alexandreprojectileair ("+str(S)+").png")

sprite_A_grab=[]
for S in range(1,11):
    sprite_A_grab.append("Alexandregrab ("+str(S)+").png")

sprite_A_grab_reussi=[]
for S in range(1,17):
    sprite_A_grab_reussi.append("Alexandregrabreussi ("+str(S)+").png")


sprite_A_hit_accroupi=[]
for S in range(1,11):
    sprite_A_hit_accroupi.append("Alexandrehitaccroupi ("+str(S)+").png")

sprite_A_hit_debout_faible=[]
for S in range(1,11):
    sprite_A_hit_debout_faible.append("Alexandrehitdeboutfaible ("+str(S)+").png")

sprite_A_hit_debout_puissant=[]
for S in range(1,11):
    sprite_A_hit_debout_puissant.append("Alexandrehitdeboutpuissant ("+str(S)+").png")

sprite_A_ejection_horizontale=[]
for S in range(1,11):
    sprite_A_ejection_horizontale.append("Alexandreejectionhorizontale ("+str(S)+").png")




sprite_A_ultime=[]
for S in range(0,40):
    sprite_A_ultime.append("Alexandreultime ("+str(S)+").png")

sprite_A_ultime_reussi=[]
for S in range(0,40):
    sprite_A_ultime_reussi.append("Alexandreultimereussi ("+str(S)+").png")

sprite_A_ultime_stand=[]
for S in range(0,40):
    sprite_A_ultime_stand.append("Alexandreultimestand ("+str(S)+").png")

sprite_A_ultime_stand_reussi=[]
for S in range(0,40):
    sprite_A_ultime_stand_reussi.append("Alexandreultimestandreussi ("+str(S)+").png")

sprite_A_mort=[]
for S in range(0,40):
    sprite_A_mort.append("Alexandremort ("+str(S)+").png")
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""REVERSE"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

sprite_A_debout_R=[]
for S in range(1,9):
    sprite_A_debout_R.append("AlexandredeboutR ("+str(S)+").png")

sprite_A_accroupi_R=[]
for S in range(1,15):
    sprite_A_accroupi_R.append("AlexandreaccroupiR ("+str(S)+").png")

sprite_A_marche_avant_R=[]
for S in range(1,10):
    sprite_A_marche_avant_R.append("AlexandremarcheavantR ("+str(S)+").png")

sprite_A_marche_arriere_R=[]
for S in range(1,10):
    sprite_A_marche_arriere_R.append("AlexandremarchearriereR ("+str(S)+").png")

sprite_A_dash_avant_R=[]
for S in range(1,11):
    sprite_A_dash_avant_R.append("AlexandredashavantR ("+str(S)+").png")

sprite_A_dash_arriere_R=[]
for S in range(1,11):
    sprite_A_dash_arriere_R.append("AlexandredasharriereR ("+str(S)+").png")
sprite_A_roulade_R=[]
for S in range(1,11):
    sprite_A_roulade_R.append("AlexandrerouladeR ("+str(S)+").png")

sprite_A_saut_R=[]
for S in range(1,18):
    sprite_A_saut_R.append("AlexandreairR ("+str(S)+").png")

sprite_A_sol_R=[]
for S in range(1,11):
    sprite_A_sol_R.append("AlexandresolR ("+str(S)+").png")
sprite_A_garde_air_R=[]
for S in range(1,11):
    sprite_A_garde_air_R.append("AlexandregardeairR ("+str(S)+").png")

sprite_A_garde_debout_R=[]
for S in range(1,11):
    sprite_A_garde_debout_R.append("AlexandregardedeboutR ("+str(S)+").png")

sprite_A_garde_accroupi_R=[]
for S in range(1,11):
    sprite_A_garde_accroupi_R.append("AlexandregardeaccroupiR ("+str(S)+").png")



sprite_A_coup_faible_1_R=[]
for S in range(0,8):
    sprite_A_coup_faible_1_R.append("Alexandrecoupfaible1R ("+str(S)+").png")

sprite_A_coup_faible_2_R=[]
for S in range(1,11):
    sprite_A_coup_faible_2_R.append("Alexandrecoupfaible2R ("+str(S)+").png")

sprite_A_coup_faible_3_R=[]
for S in range(1,11):
    sprite_A_coup_faible_3_R.append("Alexandrecoupfaible3R ("+str(S)+").png")



sprite_A_coup_puissant_1_R=[]
for S in range(1,11):
    sprite_A_coup_puissant_1_R.append("Alexandrecouppuissant1R ("+str(S)+").png")

sprite_A_coup_puissant_2_R=[]
for S in range(1,11):
    sprite_A_coup_puissant_2_R.append("Alexandrecouppuissant2R ("+str(S)+").png")

sprite_A_coup_puissant_3_R=[]
for S in range(1,11):
    sprite_A_coup_puissant_3_R.append("Alexandrecouppuissant3R ("+str(S)+").png")

sprite_A_projectile_R=[]
for S in range(1,13):
    sprite_A_projectile_R.append("AlexandreprojectileR ("+str(S)+").png")


sprite_A_coup_faible_accroupi_R=[]
for S in range(1,11):
    sprite_A_coup_faible_accroupi_R.append("AlexandrecoupfaibleaccroupiR ("+str(S)+").png")

sprite_A_coup_puissant_accroupi_R=[]
for S in range(1,11):
    sprite_A_coup_puissant_accroupi_R.append("AlexandrecouppuissantaccroupiR ("+str(S)+").png")

sprite_A_projectile_accroupi_R=[]
for S in range(1,11):
    sprite_A_projectile_accroupi_R.append("AlexandreprojectileaccroupiR ("+str(S)+").png")


sprite_A_coup_faible_air_R=[]
for S in range(1,11):
    sprite_A_coup_faible_air_R.append("AlexandrecoupfaibleairR ("+str(S)+").png")

sprite_A_coup_puissant_air_R=[]
for S in range(1,11):
    sprite_A_coup_puissant_air_R.append("AlexandrecouppuissantairR ("+str(S)+").png")

sprite_A_projectile_air_R=[]
for S in range(1,11):
    sprite_A_projectile_air_R.append("AlexandreprojectileairR ("+str(S)+").png")

sprite_A_grab_R=[]
for S in range(1,11):
    sprite_A_grab_R.append("AlexandregrabR ("+str(S)+").png")

sprite_A_grab_reussi_R=[]
for S in range(1,17):
    sprite_A_grab_reussi_R.append("AlexandregrabreussiR ("+str(S)+").png")


sprite_A_hit_accroupi_R=[]
for S in range(1,11):
    sprite_A_hit_accroupi_R.append("AlexandrehitaccroupiR ("+str(S)+").png")

sprite_A_hit_debout_faible_R=[]
for S in range(1,11):
    sprite_A_hit_debout_faible_R.append("AlexandrehitdeboutfaibleR ("+str(S)+").png")

sprite_A_hit_debout_puissant_R=[]
for S in range(1,11):
    sprite_A_hit_debout_puissant_R.append("AlexandrehitdeboutpuissantR ("+str(S)+").png")

sprite_A_ejection_horizontale_R=[]
for S in range(1,11):
    sprite_A_ejection_horizontale_R.append("AlexandreejectionhorizontaleR ("+str(S)+").png")




sprite_A_ultime_R=[]
for S in range(0,40):
    sprite_A_ultime_R.append("AlexandreultimeR ("+str(S)+").png")

sprite_A_ultime_reussi_R=[]
for S in range(0,40):
    sprite_A_ultime_reussi_R.append("AlexandreultimereussiR ("+str(S)+").png")

sprite_A_ultime_stand_R=[]
for S in range(0,40):
    sprite_A_ultime_stand_R.append("AlexandreultimestandR ("+str(S)+").png")

sprite_A_ultime_stand_reussi_R=[]
for S in range(0,40):
    sprite_A_ultime_stand_reussi_R.append("AlexandreultimestandreussiR ("+str(S)+").png")


sprite_A_mort_R=[]
for S in range(0,40):
    sprite_A_mort_R.append("AlexandremortR ("+str(S)+").png")
######################sprites YANNI#############################

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""INDEPENDANT"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
sprite_Y_special_meter=[]
for S in range(0,40):
    sprite_Y_special_meter.append("Yanispecial ("+str(S)+").png")

sprite_Y_entrée=[]
for S in range(1,40):
    sprite_Y_entrée.append("Yanientrée ("+str(S)+").png")

sprite_Y_sortie=[]
for S in range(1,40):
    sprite_Y_sortie.append("Yanisortie ("+str(S)+").png")

sprite_Y_victoire=[]
for S in range(1,40):
    sprite_Y_victoire.append("Yanivictoire ("+str(S)+").png")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""BASE"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
sprite_Y_debout=[]
for S in range(1,9):
    sprite_Y_debout.append("Yanidebout ("+str(S)+").png")

sprite_Y_accroupi=[]
for S in range(1,15):
    sprite_Y_accroupi.append("Yaniaccroupi ("+str(S)+").png")

sprite_Y_marche_avant=[]
for S in range(1,10):
    sprite_Y_marche_avant.append("Yanimarcheavant ("+str(S)+").png")

sprite_Y_marche_arriere=[]
for S in range(1,10):
    sprite_Y_marche_arriere.append("Yanimarchearriere ("+str(S)+").png")

sprite_Y_dash_avant=[]
for S in range(1,11):
    sprite_Y_dash_avant.append("Yanidashavant ("+str(S)+").png")

sprite_Y_dash_arriere=[]
for S in range(1,11):
    sprite_Y_dash_arriere.append("Yanidasharriere ("+str(S)+").png")
sprite_Y_roulade=[]
for S in range(1,11):
    sprite_Y_roulade.append("Yaniroulade ("+str(S)+").png")

sprite_Y_saut=[]
for S in range(1,18):
    sprite_Y_saut.append("Yaniair ("+str(S)+").png")

sprite_Y_sol=[]
for S in range(1,11):
    sprite_Y_sol.append("Yanisol ("+str(S)+").png")
sprite_Y_garde_air=[]
for S in range(1,11):
    sprite_Y_garde_air.append("Yanigardeair ("+str(S)+").png")

sprite_Y_garde_debout=[]
for S in range(1,11):
    sprite_Y_garde_debout.append("Yanigardedebout ("+str(S)+").png")

sprite_Y_garde_accroupi=[]
for S in range(1,11):
    sprite_Y_garde_accroupi.append("Yanigardeaccroupi ("+str(S)+").png")



sprite_Y_coup_faible_1=[]
for S in range(0,8):
    sprite_Y_coup_faible_1.append("Yanicoupfaible1 ("+str(S)+").png")

sprite_Y_coup_faible_2=[]
for S in range(1,11):
    sprite_Y_coup_faible_2.append("Yanicoupfaible2 ("+str(S)+").png")

sprite_Y_coup_faible_3=[]
for S in range(1,11):
    sprite_Y_coup_faible_3.append("Yanicoupfaible3 ("+str(S)+").png")



sprite_Y_coup_puissant_1=[]
for S in range(1,11):
    sprite_Y_coup_puissant_1.append("Yanicouppuissant1 ("+str(S)+").png")

sprite_Y_coup_puissant_2=[]
for S in range(1,11):
    sprite_Y_coup_puissant_2.append("Yanicouppuissant2 ("+str(S)+").png")

sprite_Y_coup_puissant_3=[]
for S in range(1,11):
    sprite_Y_coup_puissant_3.append("Yanicouppuissant3 ("+str(S)+").png")

sprite_Y_projectile=[]
for S in range(1,13):
    sprite_Y_projectile.append("Yaniprojectile ("+str(S)+").png")


sprite_Y_coup_faible_accroupi=[]
for S in range(1,11):
    sprite_Y_coup_faible_accroupi.append("Yanicoupfaibleaccroupi ("+str(S)+").png")

sprite_Y_coup_puissant_accroupi=[]
for S in range(1,11):
    sprite_Y_coup_puissant_accroupi.append("Yanicouppuissantaccroupi ("+str(S)+").png")

sprite_Y_projectile_accroupi=[]
for S in range(1,11):
    sprite_Y_projectile_accroupi.append("Yaniprojectileaccroupi ("+str(S)+").png")


sprite_Y_coup_faible_air=[]
for S in range(1,11):
    sprite_Y_coup_faible_air.append("Yanicoupfaibleair ("+str(S)+").png")

sprite_Y_coup_puissant_air=[]
for S in range(1,11):
    sprite_Y_coup_puissant_air.append("Yanicouppuissantair ("+str(S)+").png")

sprite_Y_projectile_air=[]
for S in range(1,11):
    sprite_Y_projectile_air.append("Yaniprojectileair ("+str(S)+").png")

sprite_Y_grab=[]
for S in range(1,11):
    sprite_Y_grab.append("Yanigrab ("+str(S)+").png")

sprite_Y_grab_reussi=[]
for S in range(1,17):
    sprite_Y_grab_reussi.append("Yanigrabreussi ("+str(S)+").png")


sprite_Y_hit_accroupi=[]
for S in range(1,11):
    sprite_Y_hit_accroupi.append("Yanihitaccroupi ("+str(S)+").png")

sprite_Y_hit_debout_faible=[]
for S in range(1,11):
    sprite_Y_hit_debout_faible.append("Yanihitdeboutfaible ("+str(S)+").png")

sprite_Y_hit_debout_puissant=[]
for S in range(1,11):
    sprite_Y_hit_debout_puissant.append("Yanihitdeboutpuissant ("+str(S)+").png")

sprite_Y_ejection_horizontale=[]
for S in range(1,11):
    sprite_Y_ejection_horizontale.append("Yaniejectionhorizontale ("+str(S)+").png")




sprite_Y_ultime=[]
for S in range(0,40):
    sprite_Y_ultime.append("Yaniultime ("+str(S)+").png")



sprite_Y_ultime_explosion=[]
for S in range(0,40):
    sprite_Y_ultime_explosion.append("Yaniultimeexplosion ("+str(S)+").png")


sprite_Y_mort=[]
for S in range(0,40):
    sprite_Y_mort.append("Yanimort ("+str(S)+").png")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""REVERSE"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

sprite_Y_debout_R=[]
for S in range(1,9):
    sprite_Y_debout_R.append("YanideboutR ("+str(S)+").png")

sprite_Y_accroupi_R=[]
for S in range(1,15):
    sprite_Y_accroupi_R.append("YaniaccroupiR ("+str(S)+").png")

sprite_Y_marche_avant_R=[]
for S in range(1,10):
    sprite_Y_marche_avant_R.append("YanimarcheavantR ("+str(S)+").png")

sprite_Y_marche_arriere_R=[]
for S in range(1,10):
    sprite_Y_marche_arriere_R.append("YanimarchearriereR ("+str(S)+").png")

sprite_Y_dash_avant_R=[]
for S in range(1,11):
    sprite_Y_dash_avant_R.append("YanidashavantR ("+str(S)+").png")

sprite_Y_dash_arriere_R=[]
for S in range(1,11):
    sprite_Y_dash_arriere_R.append("YanidasharriereR ("+str(S)+").png")
sprite_Y_roulade_R=[]
for S in range(1,11):
    sprite_Y_roulade_R.append("YanirouladeR ("+str(S)+").png")

sprite_Y_saut_R=[]
for S in range(1,18):
    sprite_Y_saut_R.append("YaniairR ("+str(S)+").png")

sprite_Y_sol_R=[]
for S in range(1,11):
    sprite_Y_sol_R.append("YanisolR ("+str(S)+").png")
sprite_Y_garde_air_R=[]
for S in range(1,11):
    sprite_Y_garde_air_R.append("YanigardeairR ("+str(S)+").png")

sprite_Y_garde_debout_R=[]
for S in range(1,11):
    sprite_Y_garde_debout_R.append("YanigardedeboutR ("+str(S)+").png")

sprite_Y_garde_accroupi_R=[]
for S in range(1,11):
    sprite_Y_garde_accroupi_R.append("YanigardeaccroupiR ("+str(S)+").png")



sprite_Y_coup_faible_1_R=[]
for S in range(0,8):
    sprite_Y_coup_faible_1_R.append("Yanicoupfaible1R ("+str(S)+").png")

sprite_Y_coup_faible_2_R=[]
for S in range(1,11):
    sprite_Y_coup_faible_2_R.append("Yanicoupfaible2R ("+str(S)+").png")

sprite_Y_coup_faible_3_R=[]
for S in range(1,11):
    sprite_Y_coup_faible_3_R.append("Yanicoupfaible3R ("+str(S)+").png")



sprite_Y_coup_puissant_1_R=[]
for S in range(1,11):
    sprite_Y_coup_puissant_1_R.append("Yanicouppuissant1R ("+str(S)+").png")

sprite_Y_coup_puissant_2_R=[]
for S in range(1,11):
    sprite_Y_coup_puissant_2_R.append("Yanicouppuissant2R ("+str(S)+").png")

sprite_Y_coup_puissant_3_R=[]
for S in range(1,11):
    sprite_Y_coup_puissant_3_R.append("Yanicouppuissant3R ("+str(S)+").png")

sprite_Y_projectile_R=[]
for S in range(1,13):
    sprite_Y_projectile_R.append("YaniprojectileR ("+str(S)+").png")


sprite_Y_coup_faible_accroupi_R=[]
for S in range(1,11):
    sprite_Y_coup_faible_accroupi_R.append("YanicoupfaibleaccroupiR ("+str(S)+").png")

sprite_Y_coup_puissant_accroupi_R=[]
for S in range(1,11):
    sprite_Y_coup_puissant_accroupi_R.append("YanicouppuissantaccroupiR ("+str(S)+").png")

sprite_Y_projectile_accroupi_R=[]
for S in range(1,11):
    sprite_Y_projectile_accroupi_R.append("YaniprojectileaccroupiR ("+str(S)+").png")


sprite_Y_coup_faible_air_R=[]
for S in range(1,11):
    sprite_Y_coup_faible_air_R.append("YanicoupfaibleairR ("+str(S)+").png")

sprite_Y_coup_puissant_air_R=[]
for S in range(1,11):
    sprite_Y_coup_puissant_air_R.append("YanicouppuissantairR ("+str(S)+").png")

sprite_Y_projectile_air_R=[]
for S in range(1,11):
    sprite_Y_projectile_air_R.append("YaniprojectileairR ("+str(S)+").png")

sprite_Y_grab_R=[]
for S in range(1,11):
    sprite_Y_grab_R.append("YanigrabR ("+str(S)+").png")

sprite_Y_grab_reussi_R=[]
for S in range(1,17):
    sprite_Y_grab_reussi_R.append("YanigrabreussiR ("+str(S)+").png")


sprite_Y_hit_accroupi_R=[]
for S in range(1,11):
    sprite_Y_hit_accroupi_R.append("YanihitaccroupiR ("+str(S)+").png")

sprite_Y_hit_debout_faible_R=[]
for S in range(1,11):
    sprite_Y_hit_debout_faible_R.append("YanihitdeboutfaibleR ("+str(S)+").png")

sprite_Y_hit_debout_puissant_R=[]
for S in range(1,11):
    sprite_Y_hit_debout_puissant_R.append("YanihitdeboutpuissantR ("+str(S)+").png")

sprite_Y_ejection_horizontale_R=[]
for S in range(1,11):
    sprite_Y_ejection_horizontale_R.append("YaniejectionhorizontaleR ("+str(S)+").png")




sprite_Y_ultime_R=[]
for S in range(0,40):
    sprite_Y_ultime_R.append("YaniultimeR ("+str(S)+").png")








sprite_Y_mort_R=[]
for S in range(0,40):
    sprite_Y_mort_R.append("YanimortR ("+str(S)+").png")









"""MISC"""
Selec_Menu=[]
for S in range (1, 14):
    Selec_Menu.append("Selec_Menu ("+str(S)+").png")

Transition=[]
for S in range (1,12):
    Transition.append("Transition ("+str(S)+").png")

Selec_stage=[]

for S in range (1, 10):
    Selec_stage.append("Selec_stage ("+str(S)+").png")

background_animation=[]

for S in range (1, 5):
    background_animation.append("backg_anim ("+str(S)+").png")










"""creation de la fenetre"""

fen=Tk()
can=Canvas(fen,heigh=1000,width=1900,bg='black')

mixer.init()
Y_bruitages= mixer.Sound("Characters/Alexandre/Sounds/Agrab.ogg")

A_bruitages = mixer.Sound("Characters/Alexandre/Sounds/Agrab.ogg")
fen.bind('p',Quitter_instant)



Menu()
can.pack()
fen.mainloop()