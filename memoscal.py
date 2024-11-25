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
        #st.write(f"el tipo de norma es: {tipo_norma_sismo}")
        tipo_norma_viento=st.selectbox("Tipo de norma (Viento)", ["NTC","CFE", "Otra"])



        with st.form(key="form1"):
            #Datos generales
            proyecto=st.text_input("Nombre del proyecto")
            fecha=st.date_input("Fecha")
            autor=st.text_input("Autor")
            inicialesautor=st.text_input("Iniciales del autor")
            revisor=st.text_input("Revisor")
            inicialesrevisor=st.text_input("Iniciales del revisor")
            direccion=st.text_input("Dirección del proyecto")
            st.markdown("###### Coordenadas")
            latitud=st.text_input("Latitud")
            longitud=st.text_input("Longitud")
            #Descripciones
            st.markdown("##### Descripciones")
            descripcionarq=st.text_area("Descripción arquitectónica")
            st.markdown("###### Descripción de la estructura")
            descripciongrav=st.text_area("Descripción del sistema gravitacional")
            descripsistemlat=st.text_area("Descripción del sistema lateral")
            descripsistemcim=st.text_area("Descripción de la cimentación")
            #Mecanica de suelos
            st.markdown("##### Mecánica de suelos")
            autormecsuelos=st.text_input("Despacho que realizó estudio de mecánica de suelos")
            docmecsuelos=st.text_input("Nombre del informe de macánica de suelos")
            #Informacion sismica
            st.markdown("##### Información sísmica")
            #st.markdown("###### Tipo de norma")
            #boton_NTC=st.form_submit_button("NTC")
            #boton_CFE=st.form_submit_button("CFE")
            #boton_otranorma=st.form_submit_button("Otra norma")
            
            #tipo_norma_sismo=st.selectbox("Tipo de norma", ["NTC","CFE", "Otra"])



            #st.write(f"el tipo de norma es: {tipo_norma_sismo}")
            regionsismo = None
            nivelzonificacion = None
            
            if tipo_norma_sismo=="CFE":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["CFE-MDOCS-2015", "CFE-MDOCS-2008"])
                #st.write(f"La norma es: {normasismo}")
                regionsismoselect=st.selectbox("Región sismica",["A","B","C","D"])
                regionsismo=f"la región {regionsismoselect}"
                nivelzonificacion="la República Mexicana"
                #st.write(f"tu regionsismo es: {regionsismo}")
                #st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")
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
                #st.write(f"la norma es: {normasismo}")
                #st.write(f"tu regionsismo es: {regionsismo}")
                #st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")
                gruposismo=st.text_input("Indicar Grupo")
                


            elif tipo_norma_sismo=="NTC":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["NTC-Sismo-2004", "NTC-Sismo-2017", "NTC-Sismo-2020", "NTC-Sismo-2023"])
                regionsismoselect=st.selectbox("Zona sismica",["I","II","III"])
                regionsismo=f"la zona {regionsismoselect}"
                nivelzonificacion="la Ciudad de México"
                #st.write(f"la norma es: {normasismo}")
                #st.write(f"tu regionsismo es: {regionsismo}")
                #st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")
                programasismo="SASID"

            else:
                normasismo = None
                st.warning("No se ha indicado norma aplicable")
            
            metodosismo=st.text_area("Descripción del método sismico aplicado")

   

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


