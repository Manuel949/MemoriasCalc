import streamlit as st
import pandas as pd
from docx import Document
# from docx.shared import Inches
# import matplotlib.pyplot as plt
import io





def main():
    st.title("GENERADOR DE MEMORIAS DE CÁLCULO")
    st.write("Introducir la información requerida para la generación de la memoria.")


    #Introduccion de plantilla
    template_file = st.file_uploader("Cargar plantilla de memoria", type="docx")

    if template_file:
        st.success("Plantilla cargada correctamente")
        #Introducción de datos
        st.subheader("Datos de la memoria")

        tipo_norma_sismo=st.selectbox("Tipo de norma (Sismo)", ["NTC","CFE", "Otra"])
        tipo_norma_viento=st.selectbox("Tipo de norma (Viento)", ["CFE", "Otra"])



        with st.form(key="form1"):
            #STEP 1
            #DATOS GENERALES
            proyecto=st.text_input("Nombre del proyecto")
            fecha=st.date_input("Fecha")
            autor,inicialesautor=st.columns([0.7,0.3])
            autor.text_input("Autor")
            inicialesautor.text_input("Iniciales del autor")
            revisor,inicialesrevisor=st.columns([0.7,0.3])
            revisor.text_input("Revisor")
            inicialesrevisor.text_input("Iniciales del revisor")
            direccion=st.text_input("Dirección del proyecto")
            st.markdown("###### Coordenadas")
            latitud,longitud=st.columns(2)
            latitud.text_input("Latitud")
            longitud.text_input("Longitud")
            #STEP 2
            #DESCRIPCIONES
            st.markdown("##### Descripciones")
            descripcionarq=st.text_area("Descripción arquitectónica")
            st.markdown("###### Descripción de la estructura")
            descripciongrav=st.text_area("Descripción del sistema gravitacional")
            descripsistemlat=st.text_area("Descripción del sistema lateral")
            descripsistemcim=st.text_area("Descripción de la cimentación")
            #STEP 3
            #MECANICA DE SUELOS
            st.markdown("##### Mecánica de suelos")
            autormecsuelos=st.text_input("Despacho que realizó estudio de mecánica de suelos")
            docmecsuelos=st.text_input("Nombre del informe de macánica de suelos")
            #STEP 4
            #INFORMACION SISMICA
            st.markdown("##### Información sísmica")
            
            regionsismo = None
            nivelzonificacion = None
            
            if tipo_norma_sismo=="CFE":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["CFE-MDOCS-2015", "CFE-MDOCS-2008"])
                regionsismoselect=st.selectbox("Región sismica",["A","B","C","D"])
                regionsismo=f"la región {regionsismoselect}"
                nivelzonificacion="la República Mexicana"
                gruposismoselect=st.selectbox("Grupo (Sismo)",["A+","A","B"])
                gruposismo=f"Grupo {gruposismoselect}"
                if gruposismoselect=="A+":
                    descripgruposismo="Estructuras en las que se requiere un grado de seguridad extrema, ya que su falla causaría cientos o miles de víctimas, y/o graves pérdidas y daños económicos, culturales, ecológicos o sociales"
                elif gruposismoselect=="A":
                    descripgruposismo="Estructuras en que se requiere un grado de seguridad alto. Construcciones cuya falla estructural causaría la pérdida de un número elevado de vidas o pérdidas económicas, daños ecológicos o culturales, científicos o tecnológicos de magnitud intensa o excepcionalmente alta, o que constituyan un peligro significativo por contener sustancias tóxicas o inflamables, así como construcciones cuyo funcionamiento sea esencial después de un sismo"
                else:
                    descripgruposismo="Estructuras en las que se requiere un grado de seguridad convencional. Construcciones cuya falla estructural ocasionaría la pérdida de un número reducido de vidas, pérdidas económicas moderadas o pondría en peligro otras construcciones de este grupo y/o daños a las del Grupo A+ y A moderados"
                programasismo="PRODISIS"
            


            elif tipo_norma_sismo=="Otra":
                normasismo=st.text_input("Indicar norma")
                regionsismoselect=st.text_input("Región sismica")
                regionsismo=f"la región {regionsismoselect}"
                nivelzonificacion=st.text_input("Entidad (ciudad y/o pais)")
                gruposismo=st.text_input("Indicar Grupo")
                


            elif tipo_norma_sismo=="NTC":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["NTC-Sismo-2004", "NTC-Sismo-2017", "NTC-Sismo-2020", "NTC-Sismo-2023"])
                regionsismoselect=st.selectbox("Zona sismica",["I","II","III"])
                regionsismo=f"la zona {regionsismoselect}"
                nivelzonificacion="la Ciudad de México"
                gruposismoselect=st.selectbox("Grupo (Sismo)",["A","B"])
                gruposismo=f"Grupo {gruposismoselect}"
                if gruposismoselect=="A":
                    descripgruposismo="Edificaciones cuya falla estructural podría tener consecuencias particularmente graves"
                else:
                    descripgruposismo="Edificaciones comunes destinadas a viviendas, oficinas y locales comerciales, hoteles y construcciones comerciales e industriales no incluidas en el Grupo A"
                programasismo="SASID"

            else:
                normasismo = None
                st.warning("No se ha indicado norma aplicable")
            
            metodosismo=st.text_area("Descripción del método sismico aplicado")
            ductilidad=st.selectbox("Ductilidad",["Q=1", "Q=1.25", "Q=2","Q=3","Q=4"])
            driftpclim=st.text_input("Distorsión límite para prevención de colapso")
            driftservlim=st.text_input("Distorsión límite para servicio")

            #STEP 5
            #INFORMACION VIENTO
            st.markdown("##### Información de viento")

            if tipo_norma_viento=="CFE":
                normaviento=st.selectbox("Norma aplicable para análisis por viento", ["CFE-MDOCV-2020", "CFE-MDOCV-2008"])
                grupovientoselect=st.selectbox("Grupo (Viento)",["A","B","C"])
                grupoviento=f"Grupo {grupovientoselect}"
                tipoviento=st.selectbox("Clasificación de la estructura ante la acción de viento", ["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"])
                categoriarug=st.selectbox("Categoría de rugosidad", ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4"])
                if categoriarug=="Categoría 1":
                    alturagrad="245"
                    exponenteviento="0.099"
                elif categoriarug=="Cateroría 2":
                    alturagrad="315"
                    exponenteviento="0.128"
                elif categoriarug=="Catrgoría 3":
                    alturagrad="390"
                    exponenteviento="0.156"
                else:
                    alturagrad="455"
                    exponenteviento="0.170"

                facttopoviento=st.text_input("Factor de topografía")
                tipotopoviento=st.selectbox("Tipo de terreno", ["Valles cerrados", "Terreno plano", "Promontorios", "Terraplenes"])
            else:
                normaviento=st.text_input("Norma aplicable para análisis por viento")
                grupoviento=st.text_input("Indicar grupo")
                tipoviento=st.text_input("Clasificación de la estructura ante la acción de viento")
                categoriarug=st.text_input("Categoría de rugosidad")
                alturagrad=None
                exponenteviento=None
                facttopoviento=st.text_input("Factor de topografía")
                tipotopoviento=st.text_input("Tipo de terreno")


            #STEP 6
            #SOFTWARE UTILIZADO
            st.markdown("##### Software utilizado")

            softwares=st.multiselect("Selecciona los software utilizados", ["ETABS", "SAP2000", "ROBOT", "SAFE", "EXCEL", "RAM Connection", "IDEA Statica Connection"])
            software1=softwares[0] if len(softwares)>0 else None
            software2=softwares[1] if len(softwares)>1 else None
            software3=softwares[2] if len(softwares)>2 else None
            software4=softwares[3] if len(softwares)>3 else None
            software5=softwares[4] if len(softwares)>4 else None
            software6=softwares[5] if len(softwares)>5 else None
            software7=softwares[6] if len(softwares)>6 else None
            
            ###1
            if software1=="SAFE":
                descripsoft1="Análisis y diseño de sistema de piso"
            elif software1=="EXCEL":
                descripsoft1="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software1=="RAM Connection" or software1=="IDEA Statica Connection":
                descripsoft1="Diseño de conexiones"
            elif software1=="ETABS" or software1=="SAP2000" or software1=="ROBOT":
                descripsoft1="Análisis y diseño estructural"
            else:
                descripsoft1=None
            ###2
            if software2=="SAFE":
                descripsoft2="Análisis y diseño de sistema de piso"
            elif software2=="EXCEL":
                descripsoft2="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software2=="RAM Connection" or software2=="IDEA Statica Connection":
                descripsoft2="Diseño de conexiones"
            elif software2=="ETABS" or software2=="SAP2000" or software2=="ROBOT":
                descripsoft2="Análisis y diseño estructural"
            else:
                descripsoft2=None
            ###3
            if software3=="SAFE":
                descripsoft3="Análisis y diseño de sistema de piso"
            elif software3=="EXCEL":
                descripsoft3="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software3=="RAM Connection" or software3=="IDEA Statica Connection":
                descripsoft3="Diseño de conexiones"
            elif software3=="ETABS" or software3=="SAP2000" or software3=="ROBOT":
                descripsoft3="Análisis y diseño estructural"
            else:
                descripsoft3=None
            ###4
            if software4=="SAFE":
                descripsoft4="Análisis y diseño de sistema de piso"
            elif software4=="EXCEL":
                descripsoft4="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software4=="RAM Connection" or software4=="IDEA Statica Connection":
                descripsoft4="Diseño de conexiones"
            elif software4=="ETABS" or software4=="SAP2000" or software4=="ROBOT":
                descripsoft4="Análisis y diseño estructural"
            else:
                descripsoft4=None
            ###5
            if software5=="SAFE":
                descripsoft5="Análisis y diseño de sistema de piso"
            elif software5=="EXCEL":
                descripsoft5="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software5=="RAM Connection" or software5=="IDEA Statica Connection":
                descripsoft5="Diseño de conexiones"
            elif software5=="ETABS" or software5=="SAP2000" or software5=="ROBOT":
                descripsoft5="Análisis y diseño estructural"
            else:
                descripsoft5=None
            ###6
            if software6=="SAFE":
                descripsoft6="Análisis y diseño de sistema de piso"
            elif software6=="EXCEL":
                descripsoft6="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software6=="RAM Connection" or software6=="IDEA Statica Connection":
                descripsoft6="Diseño de conexiones"
            elif software6=="ETABS" or software6=="SAP2000" or software6=="ROBOT":
                descripsoft6="Análisis y diseño estructural"
            else:
                descripsoft6=None
            ###7
            if software7=="SAFE":
                descripsoft7="Análisis y diseño de sistema de piso"
            elif software7=="EXCEL":
                descripsoft7="Diseño de elementos estructurales, conexiones, cálculo de acciones, etc."
            elif software7=="RAM Connection" or software7=="IDEA Statica Connection":
                descripsoft7="Diseño de conexiones"
            elif software7=="ETABS" or software7=="SAP2000" or software7=="ROBOT":
                descripsoft7="Análisis y diseño estructural"
            else:
                descripsoft7=None
            
            #st.write(f"Software 1: {software1} {descripsoft1}")
            #st.write(f"Software 2: {software2} {descripsoft2}")
            #st.write(f"Software 3: {software3} {descripsoft3}")
            #st.write(f"Software 4: {software4} {descripsoft4}")
            #st.write(f"Software 5: {software5} {descripsoft5}")
            #st.write(f"Software 6: {software6} {descripsoft6}")
            #st.write(f"Software 7: {software7} {descripsoft7}")

            #STEP 7
            #CONFIGURACION MODELADO
            st.markdown("##### Otras consideraciones de Modelado")
            tipolosa=st.selectbox("Sistema de piso modelado como:", ["membrana", "shell"])
            diafragma=st.selectbox("Tipo de driafragma", ["rígido","semirrígido"])
           
            crackcolumn=st.slider("Factor de agrietamiento en columnas",min_value=0.0,max_value=1.0,value=0.7,step=0.05)
            crackbeam=st.slider("Factor de agrietamiento en trabes",min_value=0.0,max_value=1.0,value=0.5,step=0.05)
            crackwall1=st.slider("Factor de agrietamiento en muros (en el plano)",min_value=0.0,max_value=1.0,value=0.5,step=0.05)
            crackwall2=st.slider("Factor de agrietamiento en muros (fuera del plano)",min_value=0.0,max_value=1.0,value=0.25,step=0.05)
            crackcoupbeam=st.slider("Factor de agrietamiento en trabes de acople",min_value=0.0,max_value=1.0,value=0.3,step=0.05)
            crackslab=st.slider("Factor de agrietamiento en losas",min_value=0.0,max_value=1.0,value=0.25,step=0.05)
            
            rigidpanel=st.slider("Rigidez efectiva del panel (%)",min_value=0,max_value=100,value=50,step=10)

            amortiguamiento=st.slider("Amortiguamiento (%)",min_value=0,max_value=50,value=5,step=1)

            #STEP 8
            #CORTANTE BASAL
            st.markdown("##### Cortante Basal")
            askrevcortantebasal=st.selectbox("¿Fue necesario incrementar fuerzas sísmicas para cumplir con cortante basal mínimo?", ["No", "Si"])
            if askrevcortantebasal=="Si":
                revcortantebasal="De acuerdo con el cálculo realizado, es necesario afectar las ordenadas espectrales para alcanzar el cortante basal mínimo. Cabe aclarar que dichos factores fueron tomados en cuenta para reportar los desplazamientos mostrados en la sección anterior"
            else:
                revcortantebasal=None
            
            #FIN DE FORMULARIO



            submit_button=st.form_submit_button("Aplicar")
            if submit_button:
                st.write(proyecto)
                st.write(fecha)
                st.write(autor)
                st.write(inicialesautor)
                st.write(revisor)
                st.write(inicialesrevisor)
                st.write(direccion)
                st.write(latitud)
                st.write(longitud)
                st.write(descripcionarq)
                st.write(descripciongrav)
                st.write(descripsistemlat)
                st.write(descripsistemcim)
                st.write(autormecsuelos)
                st.write(docmecsuelos)
                st.write(normasismo)
                st.write(regionsismo)
                st.write(nivelzonificacion)
                st.write(gruposismo)
                st.write(descripgruposismo)
                st.write(metodosismo)
                st.write(programasismo)
            else:
                st.info("Aun no se ejecuta")
                


    else: 
        st.warning("No se ha cargado plantilla")

main()


